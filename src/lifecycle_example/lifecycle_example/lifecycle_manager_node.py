from functools import partial
import rclpy
from rclpy.node import Node
from lifecycle_msgs.srv import ChangeState
from lifecycle_msgs.msg import Transition
from concurrent.futures import Future

class LifecycleManagerNode(Node):
    def __init__(self):
        super().__init__("lifecycle_manager_node")
        self._service_client = self.create_client(ChangeState, "/lifecycle_example_node/change_state")
        
        msg = ChangeState.Request()
        
        transition = Transition()
        transition.id = Transition.TRANSITION_CONFIGURE
        transition.label = "configure"
        
        msg.transition = transition
        
        self.update_event(msg, False)
        
        msg = ChangeState.Request()
        transition = Transition()
        transition.id = Transition.TRANSITION_ACTIVATE
        transition.label = "activate"
        msg.transition = transition
        
        self._timer1 = self.create_timer(1, partial(self.update_event, event_msg=msg, destroy_timer=True))
        
    def update_event(self, event_msg: ChangeState.Request, destroy_timer: bool):
        self._service_client.wait_for_service()
        self._service_client.call_async(event_msg).add_done_callback(self. on_service_response)
        if destroy_timer is True:
            self.destroy_timer(self._timer1)
        
    def on_service_response(self, future_response: Future[ChangeState.Response]):
        response = future_response.result()
        self.get_logger().info(f"Lifecycle switch status: {response.success}")

def main(args = None):
    rclpy.init(args=args)
    node = LifecycleManagerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
