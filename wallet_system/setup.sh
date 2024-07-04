mkdir wallet_system
cd wallet_system
python3 -m venv env
source env/bin/activate
pip install fastapi[all] sqlalchemy psycopg2-binary grpcio grpcio-tools
python -m grpc_tools.protoc -I./proto --python_out=./app/grpc --grpc_python_out=./app/grpc ./proto/wallet.proto
docker-compose up --build
