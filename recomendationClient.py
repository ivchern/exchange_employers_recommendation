from protobufs import recommendations_pb2
from protobufs import recommendations_pb2_grpc
import grpc


def run():
    channel = grpc.secure_channel('127.0.0.1:50051', channel_credentials())
    try:
        stub = recommendations_pb2_grpc.recommendationSystemStub(channel)
        request = recommendations_pb2.CardRequest(
            id=2,
            skill=["skill1", "skill2"],
            matchedCard=[
                recommendations_pb2.CardList(id=1, skill=["skill1", "skill2"]),
                recommendations_pb2.CardList(id=2, skill=["skill2"])
            ]
        )
        response = stub.getRecommendation(request)
        print(response)
    finally:
        channel.close()


def channel_credentials():
    server_root_cert = 'keys/server.crt'
    channel_credentials = grpc.ssl_channel_credentials(root_certificates=open(server_root_cert, 'rb').read())
    return channel_credentials


if __name__ == "__main__":
    run()
