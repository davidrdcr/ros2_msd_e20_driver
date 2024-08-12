import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions

def generate_launch_description():
	publisher_node = launch_ros.actions.Node(
        package='dc_motor_controller',
        executable='publisher_node',
        name='publisher_node',
    )

    controller_node = launch_ros.actions.Node(
        package='dc_motor_controller',
        executable='controller_node',
        name='controller_node',
    )

    motor_state_node = launch_ros.actions.Node(
        package='dc_motor_controller',
        executable='motor_state_node',
        name='motor_state_node',
    )

    data_logger_node = launch_ros.actions.Node(
        package='dc_motor_controller',
        executable='data_logger_node',
        name='data_logger_node',
    )
    
    joy_node = launch_ros.actions.Node(
    package='joy',
    executable='joy_node',
    name='joy_node',
    )
    
    
    return launch.LaunchDescription([
        publisher_node,
        controller_node,
        motor_state_node,
        data_logger_node,
        joy_node,
    ])
