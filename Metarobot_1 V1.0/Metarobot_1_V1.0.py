# pip install click==8.1.3

"""
Metarobot CLI
==============

Copyright (C) 2024, Sourceduty - All Rights Reserved.

Description:
------------
This is an interactive Command-Line Interface (CLI) program for managing, monitoring, 
and controlling robotic systems in the field of Computational Metarobotics. 
The program enables users to interact with individual robots or swarms, assign tasks, 
fetch data, and monitor system operations.

Key Features:
-------------
1. System Management:
   - Initialize the metarobotic system.
   - Check system status and connected robots.
2. Task Management:
   - Assign tasks to robots or swarms.
   - Stop robot operations.
3. Monitoring:
   - Fetch real-time status of robots.
   - Retrieve operation logs for debugging and analysis.
4. Utility:
   - Clear the terminal.
   - Exit the CLI gracefully.

Project Structure:
------------------
metarobot-cli/
├── metarobot_cli.py         # Main CLI entry point
├── commands/                # Command handler scripts
│   ├── __init__.py          # Marks this as a package
│   ├── system.py            # System management commands
│   ├── tasks.py             # Task-related commands
│   └── monitor.py           # Monitoring-related commands
├── utils/                   # Utility scripts
│   ├── __init__.py          # Marks this as a package
│   ├── logger.py            # Logging setup for diagnostics
│   └── config.py            # Configuration file handler (future use)
└── requirements.txt         # Python dependencies

Usage:
------
1. Run the CLI:
   $ python metarobot_cli.py

2. Available Commands:
   - `init`       : Initialize the robotic system.
   - `status`     : Display system status.
   - `assign`     : Assign tasks to robots or swarm.
   - `stop`       : Stop specific robot operations.
   - `monitor`    : Monitor robots or retrieve logs.
   - `clear`      : Clear the terminal screen.
   - `exit`       : Exit the CLI.

3. Example Commands:
   - Initialize the system:
       (metarobot) init
   - Assign a task to the swarm:
       (metarobot) assign survey
   - Stop a specific robot:
       (metarobot) stop 3
   - Retrieve operation logs:
       (metarobot) logs

Author:
-------
Developed for Computational Metarobotics research.

"""

import cmd
from commands import system, tasks, monitor
from utils.logger import setup_logger

# Initialize the logger
logger = setup_logger()


class MetarobotCLI(cmd.Cmd):
    intro = "Welcome to the Metarobot CLI. Type 'help' or '?' to list commands.\n"
    prompt = "metarobot >>> "

    # === SYSTEM COMMANDS ===
    def do_init(self, arg):
        """Initialize the Metarobot system."""
        system.init_system()
        logger.info("System initialized.")

    def do_status(self, arg):
        """Display the status of the robotic system."""
        status = system.get_status()
        print(status)

    # === TASK COMMANDS ===
    def do_assign(self, arg):
        """Assign a task to a robot or swarm. Usage: assign <task_name> [robot_id]"""
        args = arg.split()
        if len(args) == 0:
            print("Error: Task name is required. Usage: assign <task_name> [robot_id]")
            return
        task_name = args[0]
        robot_id = args[1] if len(args) > 1 else None
        tasks.assign_task(task_name, robot_id)

    def do_stop(self, arg):
        """Stop the operation of a specific robot. Usage: stop <robot_id>"""
        if not arg:
            print("Error: Robot ID is required. Usage: stop <robot_id>")
            return
        tasks.stop_robot(arg)

    # === MONITOR COMMANDS ===
    def do_monitor(self, arg):
        """Display robot monitoring information."""
        monitor_data = monitor.get_monitor_data()
        print(monitor_data)

    def do_logs(self, arg):
        """Retrieve logs of robotic operations."""
        logs = monitor.get_logs()
        print("Logs:")
        for log in logs:
            print(log)

    # === OTHER COMMANDS ===
    def do_exit(self, arg):
        """Exit the Metarobot CLI."""
        print("Exiting Metarobot CLI. Goodbye!")
        return True

    def do_clear(self, arg):
        """Clear the terminal screen."""
        print("\033[H\033[J", end="")  # ANSI escape sequence to clear the screen


if __name__ == "__main__":
    MetarobotCLI().cmdloop()
