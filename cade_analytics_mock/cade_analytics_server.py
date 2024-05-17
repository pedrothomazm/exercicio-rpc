from concurrent import futures
from datetime import datetime
import threading

import sys
import pandas as pd
sys.path.append("generated")

import grpc
import event_receiver_pb2
import event_receiver_pb2_grpc

Empty = event_receiver_pb2.google_dot_protobuf_dot_empty__pb2.Empty

# Initialize a DataFrame to store events
events_df = pd.DataFrame(columns = ["date", "user_id", "stimulus", "target"])
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
        new_events  = []

        # Append new events to the DataFrame
        for event in request.events:
            new_events.append({
                "date": datetime.fromtimestamp(event.date),
                "user_id": event.user_id,
                "stimulus": event.stimulus,
                "target": event.target
            })

        # Convert list of dictionaries to DataFrame and concatenate with the existing DataFrame
        new_events_df = pd.DataFrame(new_events)
        with df_lock:
            events_df = pd.concat([events_df, new_events_df], ignore_index=True)

        print("Received events: %s" % request)
        
        # Next, we perform some simple analyzes in order to, very briefly, test the following aspects of the code:
            # - Make sure the server is receiving, processing and analyzing data correctly.
            # - Measure the impact on server performance when performing these operations (processing time).
            # - Evaluate how server response time varies depending on the load (number of events and complexity of analyses).

        # count number of events per user
        user_event_counts = events_df["user_id"].value_counts()
        print("Number of events per user:\n", user_event_counts)

        # Count events per target component
        target_event_counts = events_df["target"].value_counts()
        print("Number of events per target component:\n", target_event_counts)

        # Count number of events per date
        date_event_counts = events_df["date"].value_counts()
        print("Number of events per date:\n", date_event_counts)

        return Empty()


def serve():
    """
    Starts the gRPC server and listens for client connections.

    This function sets up the server with a specified number of worker threads to handle incoming RPCs concurrently.
    The server binds to a specified port to listen for client requests and remains running until manually terminated.
    """

    # Create a gRPC server with a thread pool executor to handle concurrent calls
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Handlie RPC calls defined in the protobuf file
    event_receiver_pb2_grpc.add_EventReceiverServicer_to_server(
        EventReceiverServicer(), server
    )

    # Bind the server to a port on all interfaces
        ## listening on port 50051 on all available IPv4 and IPv6 addressess
    server.add_insecure_port("[::]:50051")

    # Non-blocking call => server runs in the background
    server.start()
    print("Server started")

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Server shutdown requested via KeyboardInterrupt")

    print("Server stopped")

    
if __name__ == "__main__":
    print("Starting server")
    serve()
    