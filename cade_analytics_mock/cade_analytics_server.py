from concurrent import futures
from datetime import datetime
import threading
import time

import sys
import pandas as pd

sys.path.append("generated")

import grpc
import event_receiver_pb2
import event_receiver_pb2_grpc

Empty = event_receiver_pb2.google_dot_protobuf_dot_empty__pb2.Empty

# Initialize a DataFrame to store events
events_df = pd.DataFrame(columns=["date", "user_id", "stimulus", "target"])
df_lock = threading.Lock()


# Classe que implementa o serviço gRPC
class EventReceiverServicer(event_receiver_pb2_grpc.EventReceiverServicer):
    def SendEvents(self, request, context):
        """
        Receives a list of events and processes them.

        Args:
            request: The EventList message containing one or more events.
            context: The gRPC context for the call.

        Returns:
            An Empty message indicating successful processing.
        """

        global events_df
        new_events = []

        # Append new events to the DataFrame
        for event in request.events:
            new_events.append(
                {
                    "date": datetime.fromtimestamp(event.date),
                    "user_id": event.user_id,
                    "stimulus": event_receiver_pb2.Stimulus.Name(event.stimulus),
                    "target": event_receiver_pb2.Target.Name(event.target),
                }
            )

        # Convert list of dictionaries to DataFrame and concatenate with the existing DataFrame
        new_events_df = pd.DataFrame(new_events)
        with df_lock:
            events_df = pd.concat([events_df, new_events_df], ignore_index=True)

        print(f"Received {len(request.events)} events")

        return Empty()


def serve(port):
    """
    Starts the gRPC server and listens for client connections.

    This function sets up the server with a specified number of worker threads to handle incoming RPCs concurrently.
    The server binds to a specified port to listen for client requests and remains running until manually terminated.
    
    Args:
        port (int): The port number on which the server listens for client connections.
    """

    # Create a gRPC server with a thread pool executor to handle concurrent calls
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Handlie RPC calls defined in the protobuf file
    event_receiver_pb2_grpc.add_EventReceiverServicer_to_server(
        EventReceiverServicer(), server
    )

    # Bind the server to a port on all interfaces
    ## listening on all available IPv4 and IPv6 addressess
    server.add_insecure_port(f"[::]:{port}")

    # Non-blocking call => server runs in the background
    server.start()
    print("Server started")

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Server shutdown requested via KeyboardInterrupt")

    print("Server stopped")


def continuous_analysis(interval=10):
    """
    Periodically performs analysis on the events DataFrame.

    Args:
        interval (int): Interval in seconds between each analysis.
    """

    while True:
        time.sleep(interval)

        with df_lock:
            copy = events_df.copy()

        # count number of events per user
        user_event_counts = copy["user_id"].value_counts()
        print("\n\nNumber of events per user:\n", user_event_counts)

        # Count events per target component
        target_event_counts = copy["target"].value_counts()
        print("\nNumber of events per target component:\n", target_event_counts)

        # Count number of events per day
        copy["date"] = pd.to_datetime(copy["date"]).dt.date
        daily_event_counts = copy["date"].value_counts()
        print("\nNumber of events per day:\n", daily_event_counts)


def main():
    print("What is the port number to start the gRPC server? ", end="")
    port = input()
    
    # Start the continuous analysis thread as a daemon, so
    # it stops when the main thread stops
    analysis_thread = threading.Thread(target=continuous_analysis, daemon=True)
    analysis_thread.start()

    # Start the gRPC server
    serve(port)


if __name__ == "__main__":
    main()
