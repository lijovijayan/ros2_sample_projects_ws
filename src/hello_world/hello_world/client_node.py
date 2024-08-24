import rclpy
from rclpy.node import Node
from hello_world_interfaces.msg import HelloWorld

class Client(Node):
    def __init__(self):
        super().__init__('client')
        self.get_logger().info("Initialing the client node")
        self.create_subscription(HelloWorld, 'sample_topic', self.message_callback, 10)
        self.get_logger().info("Initialized client node")
        self.get_logger().info("Topic: 'sample_topic'")
        
    def message_callback(self, msg: HelloWorld):
        self.get_logger().info(f"Received message from server: {msg.message}")

def main(args = None):
    rclpy.init(args = args)
    
    client = Client()
    
    rclpy.spin(client)
    
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
