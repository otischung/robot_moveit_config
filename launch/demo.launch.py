from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder(
        "robot_v4", package_name="robot_moveit_config").to_moveit_configs()

    moveit_joint_republisher = Node(
        package="moveit_postprocess",
        executable="moveit_joint_republisher",
        name="moveit_joint_republisher"
    )

    return LaunchDescription([
        generate_demo_launch(moveit_config),
        moveit_joint_republisher
    ])
