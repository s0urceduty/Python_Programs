def assign_task(task_name, robot_id=None):
    """Assign a task to a specific robot or the entire swarm."""
    if robot_id:
        print(f"Assigning task '{task_name}' to robot ID {robot_id}...")
    else:
        print(f"Assigning task '{task_name}' to the swarm...")
    # Mock success
    print("Task assigned successfully.")


def stop_robot(robot_id):
    """Stop a specific robot."""
    print(f"Stopping robot {robot_id}...")
    # Mock success
    print("Robot stopped successfully.")

