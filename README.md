![banner](https://github.com/Kross1de/S1MPOS/blob/main/banner.png?raw=true)
# <p align="center">SimpOS<p align="center">

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x"></a>
  <a href="#"><img src="https://img.shields.io/badge/Version-2.1.0-green.svg" alt="Version 2.1.0"></a>
</p>

## Description

SimpOS is a pseudo—operating system written in Python. It provides basic file system management functions, a text editor, games, and other utilities. Version 2.1 includes an improved interface, syntax support for a text editor, and new games.

## Installation

### Requirements
- Python 3.x
- `colorama` library (install with the command below):
```bash
pip install colorama
```

### Installation Steps
1. Clone the repository:
```bash
git clone https://github.com/Kross1de/S1MPos.git
```

2. Go to the project directory:
```bash
cd S1MPos
```
   
2. Go to the directory of the desired version:
```bash
 cd "S1MP9osV2.1 [LATEST]"
 ```

3. Start the system:
```bash
python S1MP9osV2.1.py 
```

## Usage

### Interface
When you start the system, you will see a welcome menu. Enter commands to interact with the system. Available commands:
- `HELP` — a list of available commands.
- `CALCULATOR` is a simple calculator.
- `TIME` — the current time.
- `NOTEPAD` — is a text editor.
- `SNAKE`, `PONG`, `TIC-TAC-TOE` — games.
- `SUDO CREDISK` — disk management.
- `Q` — log out.

### Functionality

#### 1. **Disk Management**
The SUDO CREDISK command opens the disk management menu. You can:
- Create disks (`CREATE DISK').
- View the list of disks (`LIST DISKS').
- Select a disk to work on (`SELECT DISK').
- Create, edit, and delete files and directories.

Example of creating a disk:
```bash
SUDO CREDISK
1. CREATE DISK
Enter disk name: diskC
Enter size in KB: 512
```

#### 2. **Text Editor (Notepad)**
The NOTEPAD command opens a text editor. Supports:
- Create and edit files.
- Save files to the selected disk.
- Syntax highlighting for `.py` and `.c` files.

Usage example:
```bash
NOTEPAD
1. CREATE NEW FILE
Enter filename to create: example.py
Start typing (type ':w' to save, ':q' to quit):
```

#### 3. **Games**
The following games are available in the system:
- **Snake**: Classic snake.
- **Pong**: A ping pong game with an AI opponent.
- **Tic-Tac-Toe**: Tic-Tac-toe vs bot.

Launching the game:
```bash
SNAKE
```

#### 4. **System Commands**
- `TIME`: Shows the current date and time.
- `RANDINT`: Generates a random number from 1 to 100.
- `BINARY`: Converts a number to binary format.

Usage example:
```bash
BINARY
Enter number: 10
Binary representation: 0b1010
```

#### 5. **User Management**
- New user registration:
```bash
WOULD YOU LIKE (R)EGISTER, (L)OGIN, (Q)UIT? R
Enter username: user1
Enter password: pass123
```
- Log in to the system:
```bash
WOULD YOU LIKE (R)EGISTER, (L)OGIN, (Q)UIT? L
Enter username: user1
Enter password: pass123
```
