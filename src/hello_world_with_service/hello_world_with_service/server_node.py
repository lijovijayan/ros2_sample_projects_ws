import rclpy
from rclpy.node import Node
from rclpy.service import Service
from hello_world_interfaces.srv import HelloWorld

class Server(Node):
    _service: Service
    def __init__(self):
        super().__init__("server")
        
        self.get_logger().info("Initializing server node")
        # init logic
        self._service = self.create_service(HelloWorld, 'sample_service', self.service_callback)
        self.get_logger().info("Initialized client node")
        self.get_logger().info("Service: 'sample_service'")
        
    def service_callback(self, request: HelloWorld.Request, response: HelloWorld.Response):
        reqMsg = request.req_msg
        response.res_msg = f"{reqMsg}!!!"
        return response

def main(args = None):
    rclpy.init(args=args)
    
    node = Server()
    
    rclpy.spin(node)
    
    rclpy.shutdown()

if __name__ == "__main__":
    main()
