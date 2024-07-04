from concurrent import futures
import grpc
from . import wallet_pb2, wallet_pb2_grpc
from sqlalchemy.orm import Session
from app import crud, database

class WalletService(wallet_pb2_grpc.WalletServiceServicer):
    def Topup(self, request, context):
        db = SessionLocal()
        wallet = crud.top_up_wallet(db, request.user_id, request.amount)
        db.close()
        if wallet:
            return wallet_pb2.WalletResponse(
                status=True,
                new_balance=wallet.balance,
                transaction_id="some_id"
            )
        return wallet_pb2.WalletResponse(status=False)

    def Deduct(self, request, context):
        db = SessionLocal()
        wallet = crud.deduct_wallet(db, request.user_id, request.amount)
        db.close()
        if wallet:
            return wallet_pb2.WalletResponse(
                status=True,
                new_balance=wallet.balance,
                transaction_id="some_id"
            )
        return wallet_pb2.WalletResponse(status=False)

    def GetBalance(self, request, context):
        db = SessionLocal()
        wallet = crud.get_wallet(db, request.user_id)
        db.close()
        if wallet:
            return wallet_pb2.WalletResponse(
                status=True,
                new_balance=wallet.balance,
                transaction_id="some_id"
            )
        return wallet_pb2.WalletResponse(status=False)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    wallet_pb2_grpc.add_WalletServiceServicer_to_server(WalletService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
