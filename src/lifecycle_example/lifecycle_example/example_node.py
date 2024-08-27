import rclpy

from rclpy.lifecycle import LifecycleNode
from rclpy.lifecycle.node import TransitionCallbackReturn, LifecycleState

from rclpy.publisher import Publisher
from rclpy.timer import Timer

from example_interfaces.msg import Int64

class LifecycleExampleNode(LifecycleNode):
    _publisher: Publisher = None
    _timer: Timer = None
    _number: int = None
    _publisher_frequency: int = None
    
    def __init__(self):
        super().__init__("lifecycle_example_node")
        
        self.get_logger().info("In constructor")
        self._number = 0
        self._publisher_frequency = 1
        
    # Use the on_configure to initilize the ROS2 communications, connect to a Hardware 
    def on_configure(self, previous_state: LifecycleState):
        self.get_logger().info("In on_configure")
        self._publisher = self.create_lifecycle_publisher(Int64, 'lifecycle_example', 10)
        self._timer = self.create_timer(self._publisher_frequency, self.publish_number)
        self._timer.cancel()
        
        return TransitionCallbackReturn.SUCCESS
        # return super().on_configure(previous_state)
        
        # We can raise an Exception or return TransitionCallbackReturn.ERROR to trigger an error
        # raise Exception()
        # return TransitionCallbackReturn.ERROR
    
    # Active/Enabled HW
    def on_activate(self, previous_state: LifecycleState):
        self._timer.reset()
        self.get_logger().info("In on_activate")
        return super().on_activate(previous_state)
    
    # Disable/Deactiveate HW
    def on_deactivate(self, previous_state: LifecycleState):
        self._timer.cancel()
        self.get_logger().info("In on_deactivate")
        return super().on_deactivate(previous_state)
    
    # Use the on_cleanup to destroy the ROS2 communications, Hardware connections
    def on_cleanup(self, previous_state: LifecycleState):
        self.get_logger().info("In on_cleanup")
        self.destroy_lifecycle_publisher(self._publisher)
        self.destroy_timer(self._timer)
        self._number = 0
        
        return TransitionCallbackReturn.SUCCESS
        # return super().on_cleanup(previous_state)
        
    def on_shutdown(self, previous_state: LifecycleState):
        self.get_logger().info("In on_shutdown")
        self.destroy_lifecycle_publisher(self._publisher)
        self.destroy_timer(self._timer)
        
        return super().on_shutdown(previous_state)
    
    # return TransitionCallbackReturn.ERROR from other funtions to trigger the on_error
    # limitation of on_error: The on_error will not be able identify what was the reason for the error, and what caused it.
    # It's better to resove the error from it's source other than triggering an on_error
    def on_error(self, previous_state: LifecycleState):
        self.get_logger().info("In on_error")
        return super().on_error(previous_state)
        
    def publish_number(self):
        msg = Int64()
        msg.data = self._number
        self._publisher.publish(msg)
        self._number = self._number + 1


def main(args = None):
    rclpy.init(args=args)
    node = LifecycleExampleNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
