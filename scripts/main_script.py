#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Name: open_terminal_script.py
Description: Opens a terminal in a specified directory with optional customizations, including color settings (Windows only) and additional commands.
Author: Kyle
Date: 2025-01-12
Version: 1.0
"""

######################################
#              Imports              #
######################################
import os
import subprocess
import platform

#########################################
#          Helper Functions           #
#########################################
def setup_logging():
    """Set up logging configuration."""
    pass  # Placeholder if logging is required in the future

def open_terminal_with_customizations(directory, color=None, commands=None):
    """
    Opens a terminal in the specified directory with optional customizations.

    :param directory: Directory to open in the terminal.
    :param color: Terminal color (Windows only).
    :param commands: List of additional commands to execute after opening the terminal.
    """
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    os_name = platform.system()
    try:
        if os_name == "Windows":
            # Build the command string
            command_list = [f"cd /d {directory}"]
            if color:
                command_list.append(f"color {color}")
            if commands:
                command_list.extend(commands)
            command = " && ".join(command_list)
            # Open the terminal and keep it open
            subprocess.run(["cmd", "/K", command], shell=True)

        elif os_name == "Linux":
            # Build the Linux command
            command_list = [f"cd {directory}", "clear"]
            if commands:
                command_list.extend(commands)
            command = " && ".join(command_list)
            # Open gnome-terminal or bash
            subprocess.run(["gnome-terminal", "--", "bash", "-c", command])

        elif os_name == "Darwin":
            # macOS Terminal
            print("Customizations are limited on macOS Terminal.")
            command_list = [f"cd {directory}"]
            if commands:
                command_list.extend(commands)
            command = "; ".join(command_list)
            # Use AppleScript to send commands to Terminal
            subprocess.run([
                "osascript", "-e",
                f'tell application "Terminal" to do script "{command}"'
            ])
            subprocess.run(["open", "-a", "Terminal", directory])

        else:
            print(f"Unsupported OS: {os_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

#########################################
#           Main Function             #
#########################################
def main():
    """Main function to execute the script."""
    # Example Usage
    directory_to_open = "C:\\Projects\\main_coding\\Git_Projects" # Replace this with the filepath you want to open
    color_to_set = "3"  # Windows terminal color (e.g., 3 for aqua)
    custom_commands = [
        "cls",      # Clear the screen
        "dir"       # List directory contents
    ]

    open_terminal_with_customizations(directory_to_open, color=color_to_set, commands=custom_commands)

#########################################
#         Script Entry Point          #
#########################################
if __name__ == "__main__":
    main()
