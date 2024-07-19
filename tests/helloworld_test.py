import unittest

import grpc_testing
import helloworld_pb2
from stub_grpc_py import greeter_server

# https://github.com/grpc/grpc/tree/master/src/python/grpcio_tests/tests/testing

class HelloWorldTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        target_service = helloworld_pb2.DESCRIPTOR.services_by_name['Greeter']
        servicer = greeter_server.Greeter()
        servicers = {target_service: servicer}

        self._target_service = target_service
        self._fake_server = grpc_testing.server_from_dictionary(servicers, grpc_testing.strict_real_time())

    def setUp(self):
        pass

    def test_successful_Square(self):
        expected = helloworld_pb2.HelloReply(message='Hello, TestUser!')
        
        request = helloworld_pb2.HelloRequest(name='TestUser')
        rpc = self._fake_server.invoke_unary_unary(
            method_descriptor=(self._target_service
                .methods_by_name['SayHello']),
            invocation_metadata={},
            request=request,
            timeout=1)
        # respose, metadata, code, details.
        actual, *_ = rpc.termination()
        self.assertEqual(expected, actual)
