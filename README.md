# stub_grpc_py

https://grpc.io/docs/languages/python/quickstart/

## Run

All commands assume that you are in the top level project directory.


(Re-)Compile proto at the top project directory (iff proto is updated).

```shell
$ python -m grpc_tools.protoc -I ./src/stub_grpc_py/protos --python_out=. --pyi_out=. --grpc_python_out=. ./src/stub_grpc_py/protos/helloworld.proto
```

Run the server:

```shell
$ rye run python src/stub_grpc_py/greeter_server.py
```

Run the client.

```shell
$ rye run python src/stub_grpc_py/greeter_client.py
```
