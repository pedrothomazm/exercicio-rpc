import sys
sys.path.append('generated')

import grpc
import event_receiver_pb2
import event_receiver_pb2_grpc
from typing import List
import datetime
import random


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
        "BUTTON_CLICK", "FORM_SUMBISSION", "PAGE_LOAD", "DATA_ENTRY",
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

    # Lista de eventos no formato di protobuf, os empacotamos em EventList
    event_list = event_receiver_pb2.EventList(events=events)
    response = stub.SendEvents(event_list)

    print("Response: %s" % response)


def run_test():
    """
    Main function to run the gRPC client.
    """
    channel = grpc.insecure_channel("localhost:50051")
    stub = event_receiver_pb2_grpc.EventReceiverStub(channel)
    # Gerar eventos mockados e enviá-los
    mock_events = generate_mock_events(5)  # Gera 5 eventos (testando)
    convert_and_send_events(mock_events, stub)

if __name__ == "__main__":
    run_test()
