from concurrent import futures

import sys
sys.path.append("generated")

import grpc
import event_receiver_pb2
import event_receiver_pb2_grpc

Empty = event_receiver_pb2.google_dot_protobuf_dot_empty__pb2.Empty


# Classe que implementa o serviço gRPC
class EventReceiverServicer(event_receiver_pb2_grpc.EventReceiverServicer):
    def SendEvents(self, request, context):
        # TODO: Implementar a lógica de processamento dos eventos aqui
        # Imprime para confirmar que os eventos foram recebidos
        print("Received events: %s" % request)
        return Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    event_receiver_pb2_grpc.add_EventReceiverServicer_to_server(
        EventReceiverServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started")
    server.wait_for_termination()


if __name__ == "__main__":
    print("Starting server")
    serve()
