import rclpy
from rclpy.node import Node
from rclpy.node import Node
from rclpy.client import Client as ServiceClient
from hello_world_interfaces.srv import HelloWorld
from concurrent.futures import Future

class Client(Node):
    _client: ServiceClient
    def __init__(self):
        super().__init__('client')
        self.get_logger().info("Initialing the client node")
        # init logic
        self._client = self.create_client(HelloWorld, 'sample_service')
        self.get_logger().info("Initialized client node")
        self.get_logger().info("Service: 'sample_service'")
        
        self.create_timer(1, self.request_data)
        
        
        
    def request_data(self, message: str = 'Hello world'):
        while not self._client.wait_for_service():
            self.get_logger().warn("Waiting for server...")
        
        self.get_logger().info(f"Request message: '{message}'")
        request = HelloWorld.Request()
        request.req_msg = message
        self._client.call_async(request=request).add_done_callback(self.response_callback)
            
    def response_callback(self, response: Future[HelloWorld.Response]):
        result: HelloWorld.Response = response.result()
        self.get_logger().info(f"Response from the server: '{result.res_msg}'")

def main(args = None):
    rclpy.init(args = args)
    
    client = Client()
    
    rclpy.spin(client)
    
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
