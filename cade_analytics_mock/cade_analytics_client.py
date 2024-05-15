import sys
sys.path.append('generated')

import grpc
import event_receiver_pb2
import event_receiver_pb2_grpc


def run_test():
    channel = grpc.insecure_channel('localhost:50051')
    stub = event_receiver_pb2_grpc.EventReceiverStub(channel)
    # Envia um evento de clique de botão para teste
    response = stub.SendEvents(event_receiver_pb2.EventList(events=[
        event_receiver_pb2.Event(
            date=1234567890,
            user_id=123,
            stimulus=event_receiver_pb2.Stimulus.BUTTON_CLICK,
            target=event_receiver_pb2.Target.USER_INTERFACE
        )
    ]))
    print("Response: %s" % response)


if __name__ == '__main__':
    run_test()