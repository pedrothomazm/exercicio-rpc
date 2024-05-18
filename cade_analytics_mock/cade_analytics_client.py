import sys
sys.path.append('generated')

import grpc
import event_receiver_pb2
import event_receiver_pb2_grpc
from typing import List
import datetime
import random
import threading
import time


def generate_random_date(start: datetime.datetime = datetime.datetime(2020, 1, 1), end: datetime.datetime = datetime.datetime.now()) -> int:
    """
    Generate a random datetime between two datetime objects.

    Parameters:
    start (datetime): lower limit for date generation.
    end (datatime): upper limit for date generation.

    Returns:
        A timestamp object.
    """

    random_date = start + (end - start) * random.random()

    return int(random_date.timestamp())


def generate_mock_events(num_events: int) -> List[event_receiver_pb2.Event]:
    """
    Generate a list of mock events compatible with the gRPC event structure.

    Parameters:
        num_events (int): Number of events to generate.

    Returns:
        List of event_receiver_pb2.Event: List of gRPC-compatible event objects.
    """
    event_stimulus = [
        "BUTTON_CLICK", "FORM_SUBMISSION", "PAGE_LOAD", "DATA_ENTRY",
        "SYSTEM_BOOT", "FILE_UPLOAD", "DROPDOWN_SELECTION"
    ]
    event_targets = [
        "USER_INTERFACE", "DATABASE_CONNECTOR", "AUTHENTICATION_MODULE",
        "DATA_PROCESSING_UNIT", "NETWORK_ADAPTER", "STORAGE_MANAGER", "SECURITY_MODULE"
    ]
    
    events = []
    for _ in range(num_events):
        event = event_receiver_pb2.Event(
            date = generate_random_date(),
            user_id = random.randint(1, 1000),  # User' IDs range from 1 to 1000
            stimulus = event_receiver_pb2.Stimulus.Value(random.choice(event_stimulus)),
            target = event_receiver_pb2.Target.Value(random.choice(event_targets))
        )
        events.append(event)
    
    return events


def convert_and_send_events(events, stub):
    """
    Sends a list of events of the protobuf format to the gRPC server.

    Args:
        events (list of event_receiver_pb2.Event): List of events in gRPC format.
        stub: Stub of the gRPC service to send events.
    """

    # List of events in protobuf format, we package them in EventList
    event_list = event_receiver_pb2.EventList(events=events)
    stub.SendEvents(event_list)


def run_test(ip_address: str, port: str, num_threads: int) -> float:
    """
    Runs multiple gRPC client instances in parallel and measures response time.

    Args:
        ip_address (str): IP address of the gRPC server.
        port (str): Port of the gRPC server.
        num_threads (int): Number of threads to run in parallel.
    """
    def client_thread(results, index):
        channel = grpc.insecure_channel(f"{ip_address}:{port}")
        stub = event_receiver_pb2_grpc.EventReceiverStub(channel)

        # Start time
        start_time = time.time()

        mock_events = generate_mock_events(random.randint(1, 21))  # Generates a random number of events per thread
        convert_and_send_events(mock_events, stub)

        # Final time
        end_time = time.time()

        # Execution duration
        results[index] = end_time - start_time
        channel.close()

    # List to store the results
    results = [0] * num_threads  
    threads = []

    # Start threads
    for i in range(num_threads):
        thread = threading.Thread(target=client_thread, args=(results, i))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Calculate average response time
    average_time = sum(results) / num_threads
    return average_time

if __name__ == "__main__":
    print("What is the IP address of the gRPC server? ", end="")
    ip_address = input()
    print("What is the port of the gRPC server? ", end="")
    port = input()
    print("How many repetitions do you want to run? ", end="")
    repetitions = int(input())
    
    # Gradually increase the number of threads from 1 to 20
    for i in range(1, 21):  
        print(f"Testing with {i} threads...")
        total_time = 0
        for _ in range(repetitions):
            total_time += run_test(ip_address, port, i)
        average_time = total_time / repetitions
        print(f"Average response time: {average_time:.6f} seconds")

