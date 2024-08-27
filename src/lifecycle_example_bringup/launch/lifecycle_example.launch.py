from launch import LaunchDescription
from launch_ros.actions import LifecycleNode
from launch_ros.actions import Node

def generate_launch_description():
    launch_description = LaunchDescription()
    
    lifcycle_node = LifecycleNode(
        package="lifecycle_example",
        executable="lifecycle_example",
        name="lifecycle_example_node",
        namespace=""
    )
    
    lifcycle_manager_node = Node(
        package="lifecycle_example",
        executable="lifecycle_manager",
        name="lifecycle_manager_node",
        namespace=""
    )
    
    launch_description.add_action(lifcycle_node)
    launch_description.add_action(lifcycle_manager_node)
    
    return launch_description

