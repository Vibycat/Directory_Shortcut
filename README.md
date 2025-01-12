
# Open Terminal Script

## Overview
This project provides a Python script to open a terminal in a specified directory with optional customizations, such as color settings (Windows only) and additional commands. It is designed to enhance user productivity by allowing quick access to commonly used directories with specific terminal configurations.

## Features
- Opens a terminal in a given directory on Windows, Linux, or macOS.
- Allows optional customization of terminal color (Windows only).
- Executes additional commands upon terminal launch.
- Cross-platform compatibility with OS-specific implementations.

## Requirements
- Python 3.x
- Compatible with Windows, Linux, and macOS operating systems.

## Usage
### Example
```python
directory_to_open = "C:\\Projects\\main_coding\\Git_Projects"
color_to_set = "3"  # Windows terminal color (e.g., 3 for aqua)
custom_commands = [
    "cls",  # Clear the screen
    "dir"   # List directory contents
]

open_terminal_with_customizations(directory_to_open, color=color_to_set, commands=custom_commands)
```

## Functions
### `open_terminal_with_customizations(directory, color=None, commands=None)`
- **Description**: Opens a terminal in the specified directory with optional customizations.
- **Parameters**:
  - `directory`: Directory to open in the terminal.
  - `color`: Terminal color for Windows terminals (optional).
  - `commands`: List of additional commands to execute after opening the terminal (optional).

## Supported Platforms
- **Windows**: Opens the Command Prompt with optional color customization and executes commands.
- **Linux**: Opens a terminal (e.g., gnome-terminal) and executes commands.
- **macOS**: Uses AppleScript to open the terminal and execute commands (limited customization).

## Error Handling
- Displays a message if the specified directory does not exist.
- Handles unsupported operating systems gracefully.
- Catches and logs exceptions during execution.

## How to Run
1. Clone this repository or download the script file.
2. Ensure Python is installed on your machine.
3. Customize the `directory_to_open`, `color_to_set`, and `custom_commands` variables as needed.
4. Run the script using the command:
   ```bash
   python open_terminal_script.py
   ```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Kyle
