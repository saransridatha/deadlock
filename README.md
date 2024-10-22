# Deadlock Detection and Prevention

## Overview
This project implements a deadlock detection and prevention application using Python's `tkinter` library for a graphical user interface (GUI). The application allows users to input the number of processes and resources, along with their allocation and request matrices, to detect deadlocks in a system.

## Features
- User-friendly Graphical User Interface(GUI).
- Input for the number of processes and resources.
- Entry fields for allocation matrix, request matrix, and available vector.
- Detection of deadlocks with a safe sequence if applicable.
- Error handling for invalid inputs.

## Requirements
- Python 3 (or later)
- tkinter (usually included with Python)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/saransridatha/deadlock.git
   cd deadlock
   ```
2. Ensure you have Python installed on your system.

## Usage
To run the application, execute the following command in your terminal:
```bash
python deadlock.py
```
## How to Use
1. Enter the number of processes and resources.
2. Click the "Next" button to proceed to input the allocation and request matrices.
3. Fill in the matrices and the available vector.
4. Click the "Detect Deadlock" button to check for deadlocks.
5. A message box will inform you if a deadlock was detected or if a safe sequence exists.

## Screenshots

<div style="display: flex; justify-content: space-around;">
  <img src="/screenshots/1.png" alt="Image 1" width="300">
  <img src="/screenshots/2.png" alt="Image 2" width="300">
  <img src="/screenshots/3.png" alt="Image 3" width="300">
</div>




