import os
from concurrent import futures

import grpc

import protobufs.recommendations_pb2 as recommendations_pb2
import protobufs.recommendations_pb2_grpc as recommendations_pb2_grpc
import service.recomendationService as recomendationService


class RecommendationSystemService(recommendations_pb2_grpc.recommendationSystemServicer):
    def recommendation(self, request, context):
        request_dict = {
            "id": request.id,
            "matchedCard": [
                {
                    "id": card.id,
                    "skill": card.skill
                }
                for card in request.matchedCard
            ]
        }

        selected_card_ids = recomendationService.get_recommendation(request_dict, 0.2)
        response = recommendations_pb2.CardResponse(selectedCardId=selected_card_ids)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_recommendationSystemServicer_to_server(
        RecommendationSystemService(), server)

    server.add_secure_port('localhost:50051', get_sert_keys())
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()


def get_sert_keys():
    with open('keys/server.key', 'rb') as f:
        private_key = f.read()
    with open('keys/server.crt', 'rb') as f:
        certificate_chain = f.read()

    server_creds = grpc.ssl_server_credentials(
        ((private_key, certificate_chain,),))
    return server_creds


if __name__ == '__main__':
    serve()
