# Wallet System

This project implements a simple wallet system that allows users to top up, deduct, and check their balance. The system is built using FastAPI for the HTTP API, gRPC for inter-service communication, and PostgreSQL as the database.

## Features

- Top up wallet
- Deduct from wallet
- Get wallet balance

## Technologies Used

- FastAPI
- gRPC
- PostgreSQL
- SQLAlchemy
- Docker

## Project Structure

wallet_system/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── crud.py
│ ├── schemas.py
│ ├── grpc/
│ │ ├── init.py
│ │ ├── wallet_pb2.py
│ │ ├── wallet_pb2_grpc.py
│ │ ├── server.py
│ └── tests/
│ ├── init.py
│ ├── test_main.py
├── proto/
│ ├── wallet.proto
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── setup.sh
