# Robot Moveit Config

This repository is made by the "moveit setup assistant".



## Changes

We have to make some changes to let the launch script works properly.

- `config/robot_v4.ros2_control.xacro`:

  - Modify the `load_yaml` to the `xacro.load_yaml`

    ```xml
    <xacro:property name="initial_positions" value="${xacro.load_yaml(initial_positions_file)['initial_positions']}"/>
    ```

- `config/joint_limits.yaml`:

  - Modify the integer number to double floating point number.
  - e.g., 100 -> 100.0, 0 -> 0.0