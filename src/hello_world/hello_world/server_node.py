import rclpy
from rclpy.node import Node
from rclpy.publisher import Publisher
from hello_world_interfaces.msg import HelloWorld

class Server(Node):
    _publisher: Publisher
    def __init__(self):
        super().__init__("server")
        
        self.get_logger().info("Initializing 'hello_world_server' node")
        self._publisher = self.create_publisher(HelloWorld, 'sample_topic', 10)
        self.get_logger().info("Initialized 'hello_world_server'")
        self.get_logger().info("Topic: 'sample_topic'")
        
        self.create_timer(1, self.publish_topic)

    def publish_topic(self):
        msg = HelloWorld()
        msg.message = 'Hello world!!!'
        self._publisher.publish(msg)
        self.get_logger().info(f"Published the message: {msg.message}")

def main(args = None):
    rclpy.init(args=args)
    
    node = Server()
    
    rclpy.spin(node)
    
    rclpy.shutdown()

if __name__ == "__main__":
    main()
