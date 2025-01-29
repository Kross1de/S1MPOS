import enum
import os
import json
import random
import sys
import msvcrt
import time
import platform
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama
init(autoreset=True)

# Constants for the system
MAX_DISK_SIZE_KB = 1024
MAX_DISKS = 3
DISK_NAMES = ['diskC', 'diskD', 'diskE']
USER_DATA_FILE = 'user_data.json'
ROOT_PREFIX = 'SUDO '
ROOT_PROMPT = '*'
USER_PROMPT = '$'
S1MP9OS_VERSION = "2.0"
SCREEN_WIDTH = 80
MENU_WIDTH = 60
DECORATION_CHAR = "#~"

BOX_CHARS = {
    'top_left': '╔',
    'top_right': '╗',
    'bottom_left': '╚',
    'bottom_right': '╝',
    'horizontal': '═',
    'vertical': '║',
    't_right': '╠',
    't_left': '╣',
    'cross': '╬'
}

# Color constants for console output
PYTHON_KEYWORDS = {
    'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
    'else', 'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import',
    'in', 'is', 'lambda', 'None', 'nonlocal', 'not', 'or', 'pass', 'raise',
    'return', 'True', 'try', 'while', 'with', 'yield'
}

C_KEYWORDS = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
    'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int',
    'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
    'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'
}

COLORS = {
    'green': Fore.GREEN,
    'white': Fore.WHITE,
    'yellow': Fore.YELLOW,
    'red': Fore.RED,
    'blue': Fore.BLUE,
    'light_blue': Fore.CYAN,
    'purple': Fore.MAGENTA
}

SYNTAX_COLORS = {
    'text': Fore.WHITE,
    'number': Fore.BLUE,
    'string': Fore.GREEN,
    'comment': Fore.CYAN,
    'keyword': Fore.YELLOW,
    'function': Fore.MAGENTA,
    'bracket': Fore.RED,
    'operator': Fore.WHITE,
    'reset': Style.RESET_ALL
}

def check_inst():
    """Check if the system directory exists."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    system_folder_path = os.path.join(current_dir, 'System')

    if os.path.exists(system_folder_path) and os.path.isdir(system_folder_path):
        print(set_color('green') + 'THE SYSTEM FOLDER EXISTS')
    else:
        print(set_color('green') + 'THE SYSTEM FOLDER NOT EXISTS. INSTALLING SYSTEM')
        install_sys()


def install_system_files():
    """Simulate the installation of system files with a progress bar."""
    total_files = 100
    files_installed = 0

    while files_installed < total_files:
        progress = (files_installed / total_files) * 100
        sys.stdout.write(set_color('light_blue') + 
            '\r[{0}] {1}%'.format('#' * int(progress // 2) + '-' * (50 - int(progress // 2)), int(progress)))
        sys.stdout.flush()

        time.sleep(0.07)
        files_installed += 1

    sys.stdout.write(set_color('green') + '\r[{0}] 100%\n'.format('#' * 50))
    sys.stdout.flush()
    print(set_color('green') + "SYSTEM DIRECTORY DOWNLOADING")


def install_sys():
    """Create the system directory."""
    system_folder = "System"
    if not os.path.exists(system_folder):
        os.makedirs(system_folder)
        print(set_color('green') + "SYSTEM DIRECTORY WAS CREATED")

    manuals_folder = os.path.join(system_folder, "manuals")
    if not os.path.exists(manuals_folder):
        os.makedirs(manuals_folder)
        print(set_color('green') + "CREATED MANUALS DIRECTORY")


def set_color(color_name):
    """Set the text color for console output."""
    color = COLORS.get(color_name.lower())
    if color is None:
        print(Fore.RED +  "ERROR: INVALID COLOR. DEFAULTING TO WHITE...")
        return Fore.WHITE
    return color

def draw_menu_box(title, options):
    """draw a menu box with a title and options"""
    width = MENU_WIDTH
    print(set_color('blue') + BOX_CHARS['top_left'] + BOX_CHARS['horizontal'] * (width-2) + BOX_CHARS['top_right'])
    print(BOX_CHARS['vertical'] + title.center(width-2) + BOX_CHARS['vertical'])
    print(BOX_CHARS['t_right'] + BOX_CHARS['horizontal'] * (width-2) + BOX_CHARS['t_left'])

    for idx, option in enumerate(options, 1):
        print(BOX_CHARS['vertical'] + f" {idx}. {option}".ljust(width-2) + BOX_CHARS['vertical'])

    print(BOX_CHARS['bottom_left'] + BOX_CHARS['horizontal'] * (width-2) + BOX_CHARS['bottom_right'])

def draw_status_bar(message, status="OK"):
    """Draw a status bar at the bottom of the screen"""
    width = SCREEN_WIDTH
    status_line = f"[ {status } ] {message}"
    print(set_color('blue') + BOX_CHARS['t_right'] + BOX_CHARS['horizontal'] * (width-2) + BOX_CHARS['t_left'])
    print(BOX_CHARS['vertical'] + status_line.ljust(width-2) + BOX_CHARS['vertical'])
    print(BOX_CHARS['bottom_left'] + BOX_CHARS['horizontal'] * (width-2) + BOX_CHARS['bottom_right'])

# notepad

class Notepad:
    def __init__(self, disk_system=None):
        self.current_file = None
        self.content = []
        self.disk_system = disk_system
        self.syntax_highlight = True

    def check_disk_selected(self):
        """check if a disk is selected"""
        if not self.disk_system or not self.disk_system.current_disk:
            print("ERROR: NO DISK SELECTED. USE 'SUDO CREDISK' TO SELECT A DISK")
            return False
        return True
    

    def write(self):
        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # display existing lines 
        for i, line in enumerate(self.lines, 1):
            print(f"{i}. {line}")

        while True:
            try: 
                line_input("\nEnter text (or 'q' to quit, 'd line_number) to delete a line): ")

                if line_input.lower() == 'q':
                    break
                elif line_input.lower().startswith('d '):
                    try:
                        line_num = int(line_input.split()[1])
                        if 1 <= line_num <= len(self.lines):
                            del self.lines[line_num - 1]
                        else:
                            print("INVALID LINE NUMBER")
                    except (ValueError, IndexError):
                        print("INVALID DELETE COMMAND. USE 'd line_number '")
                else:
                    self.lines.append(line_input)

                # clear screen and redisplay 
                os.system('cls' if os.name == 'nt' else 'clear')
                for i, line in enumerate(self.lines, 1):
                    print(f"{i}. {line}")

            except KeyboardInterrupt:
                break
    
    def create_new(self):
        """create a new text file"""
        if not self.check_disk_selected():
            return
        
        self.current_file = input("ENTER FILENAME TO CREATE: ")
        self.current_file = os.path.join(self.disk_system.current_path, self.current_file)
        
        print("\nNEW FILE: ", self.current_file)
        print("-" * 50)
        print("START TYPING (TYPE ':w' TO SAVE, ':q' TO QUIT): ")
        self.content = []

        file_ext = os.path.splitext(self.current_file)[1]
        use_highlighting = self.syntax_highlight and file_ext in ['.py', '.c']

        while True:
            line = input()
            if line == ":q":
                if self.confirm_quit():
                    break
            elif line == ":w":
                self.save_file()
                break
            else:
                self.content.append(line)
                # show syntax highlighted version after each line
                if use_highlighting:
                    print("\033[F", end='')
                    print(highlight_syntax(line))

    def open_file(self):
        """open and read an existing text file"""
        if not self.check_disk_selected():
            return
        
        filename = input("ENTER FILE NAME TO OPEN: ")
        filename = os.path.join(self.disk_system.current_path, filename)
        
        try:
            with open(filename, 'r') as file:
                self.content = file.read().splitlines()
                self.current_file = filename
                self.display_content()
                self.edit_mode()
        except FileNotFoundError:
            print("FILE NOT FOUND")
        except Exception as e:
            print(f"ERROR OPENING FILE: {e}")

    def save_file(self):
        """save content to file"""
        if not self.current_file:
            self.current_file = input("ENTER FILENAME TO SAVE: ")
        try:
            with open(self.current_file, 'w') as file:
                file.write('\n'.join(self.content))
            print(f"FILE SAVED SUCCESSFULLY AS: {self.current_file}")
        except Exception as e:
            print(f"ERROR SAVING FILE: {str(e)}")

    def display_content(self):
        """display the current content"""
        print("\nCURRENT CONTENT: ")
        print("-" * 50)
        for i, line in enumerate(self.content, 1):
            print(f"{i}: {line}")
        print("-" * 50)

        file_ext = os.path.splitext(self.current_file)[1] if self.current_file else ''
        use_highlighting = self.syntax_highlight and file_ext in ['.py', '.c']

        for i, line in enumerate(self.content, 1):
            if use_highlighting:
                highlighted_line = highlight_syntax(line)
                print(f"{i}: {highlighted_line}")
            else:
                print(f"{i}: {line}")
        print("-" * 50)

    def edit_mode(self):
        """enter edit mode of current content"""
        print('\nEDIT MODE')
        print("COMMANDS:")
        print("  :w    - save file")
        print("  :q    - quit")
        print("  :n    - add new line")
        print("  :d N  - delete line number N")
        print("  :e N text - edit line N with new text")
        print("  :l    - list content")
        print("  :h    - toggle syntax highlighting")

        file_ext = os.path.splitext(self.current_file)[1]
        use_highlighting = self.syntax_highlight and file_ext in ['.py', '.c']

        while True:
            command = input(">> ")
            if command == ":q":
                if self.confirm_quit():
                    break
            elif command == ":w":
                self.save_file()
            elif command == ":n":
                new_line = input("ENTER NEW LINE: ")
                self.content.append(new_line)
                if use_highlighting:
                    print("\033[F", end='')
                    print(highlight_syntax(new_line))
                else:
                    self.display_content()
            elif command == ":l":
                self.display_content()
            elif command.startswith(":d "):
                try:
                    line_num = int(command.split()[1]) - 1
                    if 0 <= line_num < len(self.content):
                        del self.content[line_num]
                        self.display_content()
                    else:
                        print("INVALID LINE NUMBER")
                except (ValueError, IndexError):
                    print("INVALID COMMAND FORMAT")
            elif command.startswith(":e "):
                try:
                    parts = command.split(maxsplit=2)
                    if len(parts) < 3:
                        print("INVALID COMMAND FORMAT")
                        continue
                    line_num = int(parts[1]) - 1
                    new_text = parts[2]
                    if 0 <= line_num < len(self.content):
                        self.content[line_num] = new_text
                        if use_highlighting:
                            print(f"{line_num + 1}: {highlight_syntax(new_text)}")
                        else:
                            self.display_content()
                    else:
                        print("INVALID LINE NUMBER")
                except (ValueError, IndexError):
                    print("INVALID COMMAND FORMAT")
            elif command == ":h":
                self.syntax_highlighting = not self.syntax_highlighting
                print(f"SYNTAX HIGHLIGHTING: {'ON' if self.syntax_highlighting else 'OFF'}")
                self.display_content()
            else:
                print("INVALID COMMAND")

    def confirm_quit(self):
        """confirm before quitting"""
        while True:
            response = input("SAVE CHANGES BEFORE QUITTING? (y/n): ").lower()
            if response == 'y':
                self.save_file()
                return True
            elif response == 'n':
                return True
            return False
    
    def display_interface(self):
        """display notepad interface"""
        clear_terminal()
        width = MENU_WIDTH
        print(set_color('blue') + BOX_CHARS['top_left'] + BOX_CHARS['horizontal'] * (width-2) + BOX_CHARS['top_right'])
        print(BOX_CHARS['vertical'] + "NOTEPAD".center(width-2) + BOX_CHARS['vertical'])
        print(BOX_CHARS['t_right'] + BOX_CHARS['horizontal'] * (width-2) + BOX_CHARS['t_left'])

        if self.current_file:
            print(BOX_CHARS['vertical'] + f" File: {self.current_file}".ljust(width-2) + BOX_CHARS['vertical'])
        else:
            print(BOX_CHARS['vertical'] + " No file opened".ljust(width-2) + BOX_CHARS['vertical'])

        print(BOX_CHARS['t_right'] + BOX_CHARS['horizontal'] * (width-2) + BOX_CHARS['t_left'])
        print(BOX_CHARS['vertical'] + " Content:".ljust(width-2) + BOX_CHARS['vertical'])

        # display content with line numbers 
        if self.content:
            for i, line in enumerate(self.content, 1):
                print(BOX_CHARS['vertical'] + f" {i:2d}| {line[:width-6]}".ljust(width-2) + BOX_CHARS['vertical'])
        else:
            print(BOX_CHARS['vertical'] + " No content".ljust(width-2) + BOX_CHARS['vertical'])

        print(BOX_CHARS['bottom_left'] + BOX_CHARS['horizontal'] * (width-2) + BOX_CHARS['bottom_right'])

    def run(self):
        """run the notepad application"""
        while True:
            clear_terminal()
            draw_menu_box("NOTEPAD", [
                "1. CREATE NEW FILE",
                "2. OPEN EXISTING FILE",
                "3. EXIT",
                "",
                "Current Disk: " + (self.disk_system.current_disk or "None")
            ])

            choice = input("ENTER CHOICE (1-3): ").strip()

            if choice == '1':
                self.create_new()
            elif choice == '2':
                self.open_file()
            elif choice == '3':
                break
            else:
                print("INVALID CHOICE. TRY AGAIN.")

# snake

class SnakeGame:
    def __init__(self):
        self.width = 20
        self.height = 10
        self.snake = [(self.height//2, self.width//2)] # start at center
        self.direction = 'RIGHT'
        self.food = self._generate_food()
        self.score = 0
        self.game_speed = 0.2
        self.running = True 

    def _generate_food(self):
        """generate food at random position"""
        while True:
            food = (random.randint(0, self.height-1),
                    random.randint(0, self.width-1))
            if food not in self.snake:
                return food
            
    def _move_snake(self):
        """move the snake in the current direction"""
        head = self.snake[0]
        if self.direction == 'UP':
            new_head = ((head[0] - 1) % self.height, head[1])
        elif self.direction == 'DOWN':
            new_head = ((head[0] + 1) % self.height, head[1])
        elif self.direction == 'LEFT':
            new_head = (head[0], (head[1] - 1) % self.width)
        else: # right
            new_head = (head[0], (head[1] + 1) % self.width)

        # check if snake hits itself
        if new_head in self.snake:
            self.running = False
            return 
        
        self.snake.insert(0, new_head)

        # check if snake eats food
        if new_head == self.food:
            self.score += 1
            self.food = self._generate_food()
            # snake grows so we don't remove the tail
        else:
            self.snake.pop()

    def _draw(self):
        """draw the game board"""
        clear_terminal()
        print(f"SCORE: {self.score}")
        print("+" + "-" * (self.width + 2) + "+")

        for i in range(self.height):
            print("|", end="")
            for j in range(self.width):
                if (i, j) == self.snake[0]:
                    print("O ", end="")  # Snake head
                elif (i, j) in self.snake[1:]:
                    print("o ", end="")  # Snake body
                elif (i, j) == self.food:
                    print("* ", end="")  # Food
                else:
                    print("  ", end="")  # Empty space
            print("|")
        
        print("+" + "-" * (self.width * 2) + "+")
        print("USE WASD TO MOVE, Q TO QUIT")

    def play(self):
        """main game loop"""
        clear_terminal()
        draw_menu_box("SNAKE GAME", [
            "USE 'W' FOR UP",
            "USE 'S' FOR DOWN", 
            "USE 'A' FOR LEFT",
            "USE 'D' FOR RIGHT",
            "PRESS 'Q' TO QUIT",
            "",
            "PRESS ANY KEY TO START..."
        ])
        msvcrt.getch()

        last_update = time.time()

        while self.running:
            current_time = time.time()

            # handle input 
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 'w' and self.direction != 'DOWN':
                    self.direction = 'UP'
                elif key == 's' and self.direction != 'UP':
                    self.direction = 'DOWN'
                elif key == 'a' and self.direction != 'RIGHT':
                    self.direction = 'LEFT'
                elif key == 'd' and self.direction != 'LEFT':
                    self.direction = 'RIGHT'
                elif key == 'q':
                    self.running = False
                    break

            # update game state 
            if current_time - last_update > self.game_speed:
                self._move_snake()
                self._draw()
                last_update = current_time

        print(f"\nGAME OVER! SCORE: {self.score}")
        print("PRESS ANY KEY TO CONTINUE...")
        msvcrt.getch()

# pong

class PongGame:
    def __init__(self):
        self.width = 40
        self.height = 20
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_dx = 1
        self.ball_dy = 1
        self.paddle_left = self.height // 2
        self.paddle_right = self.height // 2
        self.paddle_size = 3
        self.score_left = 0
        self.score_right = 0
        self.game_speed = 0.1
        self.difficulty = 1
        self.ai_reaction_speed = 0.2
        self.running = True

    def move_ball(self):
        """Move the ball and handle collisions"""
        new_x = self.ball_x + self.ball_dx
        new_y = self.ball_y + self.ball_dy

        if new_y <= 0 or new_y >= self.height - 1:
            self.ball_dy *= -1
            new_y = max(0, min(self.height - 1, new_y))

        if new_x <= 1:
            if abs(self.ball_y - self.paddle_left) <= self.paddle_size // 2:
                self.ball_dx *= -1
                new_x = 1
            else:
                self.score_right += 1
                self.reset_ball()
                return

        if new_x >= self.width - 2:
            if abs(self.ball_y - self.paddle_right) <= self.paddle_size // 2:
                self.ball_dx *= -1
                new_x = self.width - 2
            else:
                self.score_left += 1
                self.reset_ball()
                return

        self.ball_x = new_x
        self.ball_y = new_y

    def reset_ball(self):
        """Reset ball to center with random direction"""
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_dx = random.choice([-1, 1])
        self.ball_dy = random.choice([-1, 1])

    def move_ai_paddle(self):
        """AI paddle movement based on difficulty level"""
        if self.ball_dx > 0:  # Only move when ball is moving towards AI
            predicted_y = self.ball_y
            random_factor = (6 - self.difficulty) * 0.4
            predicted_y += random.uniform(-random_factor, random_factor)
            
            if self.paddle_right < predicted_y - self.paddle_size // 2:
                if self.paddle_right < self.height - self.paddle_size // 2:
                    self.paddle_right += 1
            elif self.paddle_right > predicted_y + self.paddle_size // 2:
                if self.paddle_right > self.paddle_size // 2:
                    self.paddle_right -= 1

    def draw(self):
        """Draw the game state"""
        clear_terminal()
        print(f"PLAYER: {self.score_left}  BOT: {self.score_right}")

        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if x == int(self.ball_x) and y == int(self.ball_y):
                    row += "O"
                elif x == 0 and abs(y - self.paddle_left) <= self.paddle_size // 2:
                    row += "█"
                elif x == self.width - 1 and abs(y - self.paddle_right) <= self.paddle_size // 2:
                    row += "█"
                else:
                    row += " "
            print("|" + row + "|")
        print("-" * (self.width + 2))

    def handle_input(self):
        """Handle keyboard input"""
        if msvcrt.kbhit():
            try:
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 'w' and self.paddle_left > self.paddle_size // 2:
                    self.paddle_left -= 1
                elif key == 's' and self.paddle_left < self.height - self.paddle_size // 2:
                    self.paddle_left += 1
                elif key == 'q':
                    self.running = False
            except (UnicodeDecodeError, ValueError):
                pass

    def play(self):
        """Main game loop"""
        clear_terminal()
        draw_menu_box("PONG GAME", [
            "SELECT DIFFICULTY LEVEL:",
            "1 - EASY",
            "2 - MEDIUM",
            "3 - HARD",
            "4 - EXPERT",
            "5 - IMPOSSIBLE",
            "",
            "USE 'W' AND 'S' TO MOVE YOUR PADDLE",
            "PRESS 'Q' TO QUIT",
            "",
            "FIRST TO 5 POINTS WINS!"
        ])

        while True:
            try:
                self.difficulty = int(input("ENTER DIFFICULTY (1-5): "))
                if 1 <= self.difficulty <= 5:
                    break
                print("PLEASE ENTER A NUMBER BETWEEN 1 AND 5")
            except ValueError:
                print("PLEASE ENTER A VALID NUMBER")

        print("PRESS ANY KEY TO START...")
        msvcrt.getch()

        self.game_speed = 0.1 + (0.02 * (5 - self.difficulty))
        last_update = time.time()

        while self.running:
            current_time = time.time()
            
            # Handle input first
            self.handle_input()
            
            # Update game state if enough time has passed
            if current_time - last_update > self.game_speed:
                self.move_ball()
                self.move_ai_paddle()
                self.draw()
                last_update = current_time

                if self.score_left >= 5 or self.score_right >= 5:
                    winner = "PLAYER" if self.score_left >= 5 else "BOT"
                    print(f"\n{winner} WINS THE GAME!")
                    print("PRESS ANY KEY TO CONTINUE...")
                    msvcrt.getch()
                    break

            # Small sleep to prevent CPU overuse
            time.sleep(0.01)
                
# tic-tac-toe

class TicTacToe:
    def __init__(self):
        """initialize the game board"""
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        """print the game board"""
        clear_terminal()
        print("\n")
        for i in range(3):
            print(' | '.join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print('-' * 9)
        print("\n")

    def is_winner(self, player):
        """check if the specified player has won the game"""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], #horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8], #vertical
            [0, 4, 8], [2, 4, 6]             #diagonal
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def is_board_full(self):
        return ' ' not in self.board 

    def make_move(self, position):
        """make a move on the board at the given position"""
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True 
        return False

    def switch_player(self):
        """switch current player"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_bot_move(self):
        """get the bot move"""
        available_moves = [i for i, spot in enumerate(self.board) if spot == ' ']
        return random.choice(available_moves) if available_moves else None

    def play_game(self):
        """game loop for play tic-tac-toe"""
        clear_terminal()
        draw_menu_box("TIC-TAC-TOE", [
            "ENTER POSITIONS (0-8):",
            "",
            "0 | 1 | 2",
            "---------",
            "3 | 4 | 5", 
            "---------",
            "6 | 7 | 8",
            "",
            "YOU ARE 'X', BOT IS 'O'"
        ])
        time.sleep(2)
        
        while True:
            self.print_board()
            if self.current_player == 'X':
                try:
                    position = int(input("ENTER MOVE: (0-8): "))
                    if position < 0 or position > 8:
                        raise ValueError("POSITION MUST BE BETWEEN 0 AND 8")
                except ValueError as e:
                    print(f"INVALID INPUT: {e}")
                    time.sleep(1)
                    continue 
            else:
                position = self.get_bot_move()
                print(f"BOT CHOOSES POSITION: {position}")
                time.sleep(1)

            if self.make_move(position):  # This line now correctly calls make_move
                if self.is_winner(self.current_player):
                    self.print_board()
                    print(f"PLAYER '{self.current_player}' WINS!")
                    break
                elif self.is_board_full():
                    self.print_board()
                    print("IT'S A DRAW")
                    break
                self.switch_player()
            else:
                print("POSITION ALREADY TAKEN")
                time.sleep(1)

#disksystem

class DiskSystem:
    """class to manage disk operations"""

    def __init__(self):
        self.disks = {}
        self.valid_disk_names = {'diskC', 'diskD', 'diskE'}
        self.current_disk = None
        self.current_path = None
        self.load_existing_disks()
        self.disk_data_file = 'disk_data.json'
        self.load_disk_data()

    def load_disk_data(self):
        """load disk data from json file"""
        try:
            if os.path.exists(self.disk_data_file):
                with open(self.disk_data_file, 'r') as f:
                    self.disks = json.load(f)
                for disk_name in list(self.disks.keys()):
                    if not os.path.exists(disk_name):
                        os.makedirs(disk_name)
        except Exception as e:
            print(f"ERROR LOADING DISK DATA: {str(e)}")
            self.disks = {}

    def save_disk_data(self):
        """save disk data to json file"""
        try:
            with open(self.disk_data_file, 'w') as f:
                json.dump(self.disks, f)
        except Exception as e:
            print(f"ERROR SAVING DISK DATA: {str(e)}")

    def select_disk(self, disk_name):
        """select a disk to work with"""
        if disk_name not in self.disks:
            print(f"ERROR: DISK '{disk_name}' NOT FOUND")
            return False
        if not os.path.exists(disk_name):
            print(f"ERROR: DISK '{disk_name}' NOT MOUNTED")
            return False
        self.current_disk = disk_name
        self.current_path = disk_name
        print(f"SELECTED DISK: {disk_name}")
        return True

    def list_contents(self):
        """list all files and directories in the current path"""
        if not self.current_disk:
            print("ERROR: NO DISK SELECTED. USE 'SELECT' COMMAND FIRST")
            return

        print(f"\nCONTENTS OF {self.current_path}")
        print("-" * 70)
        print(f"{'NAME':<30}{'TYPE':<10}{'SIZE':<15}{'MODIFIED':<20}")
        print("-" * 70)

        try:
            items = os.listdir(self.current_path)
            for item in sorted(items):
                item_path = os.path.join(self.current_path, item)
                is_dir = os.path.isdir(item_path)
                size = self.get_directory_size(item_path) if is_dir else os.path.getsize(item_path) // 1024
                mod_time = datetime.fromtimestamp(os.path.getmtime(item_path)).strftime('%Y-%m-%d %H:%M:%S')
                item_type = "DIR" if is_dir else "FILE"
                print(f"{item:<30}{item_type:<10}{size:<15}{mod_time:<20}")
        except Exception as e:
            print(f"ERROR LISTING CONTENTS: {str(e)}")
        print("-" * 70)

    def create_file(self):
        """Create a new file on the current disk."""
        if not self.current_disk:
            print("ERROR: NO DISK SELECTED. USE 'SELECT' COMMAND FIRST")
            return

        filename = input("ENTER FILE NAME: ")
        file_path = os.path.join(self.current_disk, filename)

        if os.path.exists(file_path):
            print("ERROR: FILE ALREADY EXISTS")
            return

        content = input("ENTER FILE CONTENT (PRESS ENTER WHEN DONE):\n")
        try:
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"FILE '{filename}' CREATED SUCCESSFULLY")
        except Exception as e:
            print(f"ERROR CREATING FILE: {str(e)}")

    def edit_file(self):
        """Edit an existing file on the current disk."""
        if not self.current_disk:
            print("ERROR: NO DISK SELECTED. USE 'SELECT' COMMAND FIRST")
            return

        self.list_files()
        filename = input("ENTER FILE NAME TO EDIT: ")
        file_path = os.path.join(self.current_disk, filename)

        if not os.path.exists(file_path):
            print("ERROR: FILE DOES NOT EXIST")
            return

        # Show current content
        try:
            with open(file_path, 'r') as f:
                current_content = f.read()
            print("\nCURRENT CONTENT:")
            print("-" * 50)
            print(current_content)
            print("-" * 50)

            # Get new content
            print("\nENTER NEW CONTENT (PRESS ENTER TWICE WHEN DONE):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            
            new_content = '\n'.join(lines)

            # Save changes
            with open(file_path, 'w') as f:
                f.write(new_content)
            print("FILE UPDATED SUCCESSFULLY")
        except Exception as e:
            print(f"ERROR EDITING FILE: {str(e)}")

    def delete_file(self):
        """Delete a file from the current disk."""
        if not self.current_disk:
            print("ERROR: NO DISK SELECTED. USE 'SELECT' COMMAND FIRST")
            return

        self.list_files()
        filename = input("ENTER FILE NAME TO DELETE: ")
        file_path = os.path.join(self.current_disk, filename)

        if not os.path.exists(file_path):
            print("ERROR: FILE DOES NOT EXIST")
            return

        try:
            os.remove(file_path)
            print(f"FILE '{filename}' DELETED SUCCESSFULLY")
        except Exception as e:
            print(f"ERROR DELETING FILE: {str(e)}")
    
    def create_directory(self):
        """create a new directory"""
        if not self.current_disk:
            print("ERROR: NO DISK SELECTED. USE 'SELECT' COMMAND FIRST")
            return

        dirname = input("ENTER NEW DIRECTORY NAME: ")
        dirpath = os.path.join(self.current_path, dirname)

        if os.path.exists(dirpath):
            print("ERROR: DIRECTORY ALREADY EXISTS")
            return

        try:
            os.mkdir(dirpath)
            print(f"DIRECTORY '{dirname}' CREATED SUCCESSFULLY")
        except Exception as e:
            print(f"ERROR CREATING DIRECTORY: {str(e)}")

    def delete_directory(self):
        """delete a directory and its contents"""
        if not self.current_disk:
            print("ERROR: NO DISK SELECTED. USE 'SELECT' COMMAND FIRST")
            return

        self.list_contents()
        dirname = input("ENTER DIRECTORY NAME TO DELETE: ")
        dirpath = os.path.join(self.current_path, dirname)

        if not os.path.exists(dirpath):
            print("ERROR: DIRECTORY NOT FOUND")
            return
        if not os.path.isdir(dirpath):
            print("ERROR: NOT A DIRECTORY")
            return

        confirm = input(f"ARE YOU SURE YOU WANT TO DELETE '{dirname}' AND ALL ITS CONTENTS? (y/n): ")
        if confirm != 'yes':
            print("OPERATION CANCELLED")
            return

        try:
            import shutil
            shutil.rmtree(dirpath)
            print(f"DIRECTORY '{dirname}' AND ALL ITS CONTENTS DELETED SUCCESSFULLY")
        except Exception as e:
            print(f"ERROR DELETING DIRECTORY: {str(e)}")

    def rename_directory(self):
        """rename a directory"""
        if not self.current_disk:
            print("ERROR: NO DISK SELECTED. USE 'SELECT' COMMAND FIRST")
            return
        
        self.list_contents()
        old_name = input("ENTER CURRENT NAME OF YOUR DIRECTORY: ")
        old_path = os.path.join(self.current_path, old_name)

        if not os.path.exists(old_path) or not os.path.isdir(old_path):
            print("ERROR: DIRECTORY NOT FOUND")
            return

        new_name = input("ENTER NEW NAME DIRECTORY: ")
        new_path = os.path.join(self.current_path, new_name)

        if os.path.exists(new_path):
            print("ERROR: DIRECTORY ALREADY EXISTS")
            return

        try:
            os.rename(old_path, new_path)
            print(f"DIRECTORY RENAMED FROM '{old_name}' TO '{new_name}' SUCCESSFULLY")
        except Exception as e:
            print(f"ERROR RENAMING DIRECTORY: {str(e)}")

    def change_directory(self):
        """change the current directory"""
        if not self.current_disk:
            print("ERROR: NO DISK SELECTED. USE 'SELECT' COMMAND FIRST")
            return

        print("\nCURRENT PATH:", self.current_path)
        path = input("ENTER NEW PATH: (.. FOR PARENT DIRECTORY, OR DIRECTORY NAME): ")

        if path == "..":
            # move to parent directory but not above disk root
            if self.current_path != self.current_disk:
                self.current_path = os.path.dirname(self.current_path)
                print(f"MOVED TO: {self.current_path}")
            else:
                print("ALREADY AT DISK ROOT")
            return

        new_path = os.path.join(self.current_path, path)

        # ensure we don't navigate outside the current disk
        if not new_path.startswith(self.current_disk):
            print("ERROR: CANNOT NAVIGATE OUTSIDE CURRENT DISK")
            return

        if not os.path.exists(new_path) or not os.path.isdir(new_path):
            print("ERROR: INVALID DIRECTORY")
            return

        self.current_path = new_path
        print(f"MOVED TO: {self.current_path}")

    def rename_file(self):
        """Rename a file on the current disk."""
        if not self.current_disk:
            print("ERROR: NO DISK SELECTED. USE 'SELECT' COMMAND FIRST")
            return

        self.list_files()
        old_name = input("ENTER CURRENT FILE NAME: ")
        old_path = os.path.join(self.current_disk, old_name)

        if not os.path.exists(old_path):
            print("ERROR: FILE DOES NOT EXIST")
            return

        new_name = input("ENTER NEW FILE NAME: ")
        new_path = os.path.join(self.current_disk, new_name)

        if os.path.exists(new_path):
            print("ERROR: A FILE WITH THAT NAME ALREADY EXISTS")
            return

        try:
            os.rename(old_path, new_path)
            print(f"FILE RENAMED FROM '{old_name}' TO '{new_name}' SUCCESSFULLY")
        except Exception as e:
            print(f"ERROR RENAMING FILE: {str(e)}")
    
    def load_existing_disks(self):
        """load existing disks directories into the system"""
        for disk_name in self.valid_disk_names:
            if os.path.exists(disk_name) and os.path.isdir(disk_name):
                # assume default size if disk exists but size unknown
                self.disks[disk_name] = self.get_directory_size(disk_name)
    
    def get_directory_size(self, directory):
        """calculate the total size of a directory in KB"""
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size // 1024

    def list_files(self):
        """List all files in the current disk."""
        if not self.current_disk:
            print("ERROR: NO DISK SELECTED. USE 'SELECT' COMMAND FIRST")
            return

        print(f"\nFILES ON {self.current_disk}:")
        print("-" * 50)
        files = os.listdir(self.current_disk)
        if not files:
            print("NO FILES ON DISK")
        else:
            for file in files:
                file_path = os.path.join(self.current_disk, file)
                size = os.path.getsize(file_path) // 1024  # Size in KB
                print(f"{file:<30} {size:>5} KB")
        print("-" * 50)
    
    def view_disk_info(self):
        """View detailed information about the current disk."""
        if not self.current_disk:
            print("ERROR: NO DISK SELECTED. USE 'SELECT' COMMAND FIRST")
            return

        try:
            total_size = self.disks[self.current_disk]
            used_size = self.get_directory_size(self.current_disk)
            free_size = total_size - used_size
            file_count = len(os.listdir(self.current_disk))

            print(f"\nDISK INFORMATION FOR {self.current_disk}:")
            print("-" * 50)
            print(f"TOTAL SIZE: {total_size} KB")
            print(f"USED SPACE: {used_size} KB")
            print(f"FREE SPACE: {free_size} KB")
            print(f"USAGE: {(used_size/total_size)*100:.1f}%")
            print(f"NUMBER OF FILES: {file_count}")
            print("-" * 50)

            # List all files with details
            print("\nFILE DETAILS:")
            print(f"{'NAME':<30}{'SIZE (KB)':<15}{'CREATED':<25}")
            print("-" * 70)
            
            for filename in os.listdir(self.current_disk):
                file_path = os.path.join(self.current_disk, filename)
                file_size = os.path.getsize(file_path) // 1024
                created_time = datetime.fromtimestamp(os.path.getctime(file_path))
                created_str = created_time.strftime('%Y-%m-%d %H:%M:%S')
                print(f"{filename:<30}{file_size:<15}{created_str:<25}")
            
            print("-" * 70)

        except Exception as e:
            print(f"ERROR GETTING DISK INFO: {str(e)}")
    
    def list_disks(self):
        """list all created disks and their details"""
        if not self.disks:
            print("NO DISKS CREATED YET")
            print(f"AVAILABLE DISK NAMES: {', '.join(self.valid_disk_names)}")
            return
        
        print("\nDISK SYSTEM STATUS:")
        print("-" * 50)
        print(f"{'DISK NAME':<15}{'STATUS':<20}")
        print("-" * 50)

        # list existing disks
        for disk_name in self.valid_disk_names:
            if disk_name in self.disks:
                size = self.disks[disk_name]
                status = "MOUNTED" if os.path.exists(disk_name) else "ERROR"
                print(f"{disk_name:<15}{size:<15}{status:<20}")
            else:
                print(f"{disk_name:<15}{'--':<20}{'NOT CREATED':<20}")

        # show total usage 
        total_size = sum(self.disks.values())
        max_total_size = MAX_DISKS + MAX_DISK_SIZE_KB
        print("-" * 50)
        print(f"TOTAL SPACE USED: {total_size} KB / {max_total_size} KB")
        print(f"FREE SPACE: {max_total_size - total_size} KB")
        print(f"AVAILABLE SLOTS: {MAX_DISKS - len(self.disks)} OF {MAX_DISKS}")
        print("-" * 50)

    def create_disk(self, disk_name, size_kb):
        """create a new disk with the specified name and size"""
        # check if disk name is valid
        if disk_name not in self.valid_disk_names:
            print(f"ERROR: INVALID DISK NAME '{disk_name}'")
            print(f"VALID DISK NAMES ARE: {', '.join(self.valid_disk_names)}")
            return 

        # check maximum disk limit
        if len(self.disks) >= MAX_DISKS:
            print(f"ERROR: MAXIMUM DISK LIMIT OF {MAX_DISKS} REACHED")
            return

        # check disk size limit 
        if size_kb > MAX_DISK_SIZE_KB:
            print(f"ERROR: DISK SIZE CANNOT EXCEED {MAX_DISK_SIZE_KB} KB")
            return

        # check if disk already exists
        if disk_name in self.disks:
            print(f"ERROR: DISK '{disk_name}' ALREADY EXISTS")
            return

        # create directory to represent disk
        try:
            if not os.path.exists(disk_name):
                os.mkdir(disk_name)
                self.disks[disk_name] = size_kb
                print(f"DISK '{disk_name}' CREATED WITH SIZE {size_kb} KB")
                print("STATUS: MOUNTED SUCCESSFULLY")
            else:
                print(f"ERROR: DIRECTORY '{disk_name}' ALREADY EXISTS")
        except Exception as e:
            print(f"ERROR CREATING DISK: {str(e)}")

        try:
            if not os.path.exists(disk_name):
                os.makedirs(disk_name)
                self.disks[disk_name] = size_kb
                self.save_disk_data()
                print(f"DISK '{disk_name}' CREATED WITH SIZE {size_kb} KB")
                print("STATUS: MOUNTED SUCCESSFULLY")
            else:
                print(f"ERROR: DIRECTORY '{disk_name}' ALREADY EXISTS")
        except Exception as e:
            print(f"ERROR CREATING DISK: {str(e)}")

    def view_file(self):
        """view contents of a file"""
        if not self.current_disk:
            print("ERROR: NO DISK SELECTED. USE 'SELECT' COMMAND FIRST")
            return

        self.list_files()
        filename = input("ENTER FILE NAME TO VIEW")
    
    def display_interface(self):
        """Display the DiskSystem interface"""
        clear_terminal()
        width = MENU_WIDTH
        print(set_color('blue') + BOX_CHARS['top_left'] + BOX_CHARS['horizontal'] * (width-2) + BOX_CHARS['top_right'])
        print(BOX_CHARS['vertical'] + "DISK SYSTEM".center(width-2) + BOX_CHARS['vertical'])
        print(BOX_CHARS['t_right'] + BOX_CHARS['horizontal'] * (width-2) + BOX_CHARS['t_left'])
    
        # Display current disk info
        if self.current_disk:
            print(BOX_CHARS['vertical'] + f" Current Disk: {self.current_disk}".ljust(width-2) + BOX_CHARS['vertical'])
            print(BOX_CHARS['vertical'] + f" Current Path: {self.current_path}".ljust(width-2) + BOX_CHARS['vertical'])
        else:
            print(BOX_CHARS['vertical'] + " No disk selected".ljust(width-2) + BOX_CHARS['vertical'])
    
        print(BOX_CHARS['t_right'] + BOX_CHARS['horizontal'] * (width-2) + BOX_CHARS['t_left'])
    
        # Display disk usage
        for disk_name in self.valid_disk_names:
            if disk_name in self.disks:
                size = self.disks[disk_name]
                if size > 0:  # Check if size is greater than 0
                    used = self.get_directory_size(disk_name)
                    usage_percent = (used / size) * 100 if size > 0 else 0
                    status = "MOUNTED" if os.path.exists(disk_name) else "ERROR"
                    disk_info = f" {disk_name}: {used}/{size}KB ({usage_percent:.1f}%) [{status}]"
                else:
                    disk_info = f" {disk_name}: ERROR - Invalid disk size"
                print(BOX_CHARS['vertical'] + disk_info.ljust(width-2) + BOX_CHARS['vertical'])
    
        print(BOX_CHARS['bottom_left'] + BOX_CHARS['horizontal'] * (width-2) + BOX_CHARS['bottom_right'])
    
    def run(self):
        """run the disk system"""
        
        while True:
            self.display_interface()
            draw_menu_box("DISK SYSTEM MENU", [
                "1.  CREATE DISK",
                "2.  LIST DISKS",
                "3.  SELECT DISK",
                "4.  LIST CONTENTS",
                "5.  CREATE FILE",
                "6.  EDIT FILE",
                "7.  DELETE FILE",
                "8.  VIEW FILE",
                "9.  RENAME FILE",
                "10. CREATE DIR",
                "11. DELETE DIR",
                "12. RENAME DIR",
                "13. CHANGE DIR",
                "14. DISK INFO",
                "Q.  QUIT"
            ])

            command = input("\nENTER CHOICE: ").strip().lower()

            if command == "q":
                break
            elif command in ["1", "create disk"]:
                print(f"\nAVAILABLE DISK NAMES: {', '.join(self.valid_disk_names)}")
                disk_name = input("ENTER DISK NAME: ")
                try:
                    size_kb = int(input(f"ENTER SIZE IN KB (max {MAX_DISK_SIZE_KB} KB): "))
                    self.create_disk(disk_name, size_kb)
                except ValueError:
                    print("INVALID INPUT. PLEASE ENTER A VALID NUMBER")
            elif command in ["2", "list disks"]:
                self.list_disks()
            elif command in ["3", "select disk"]:
                disk_name = input("ENTER DISK NAME TO SELECT: ")
                self.select_disk(disk_name)
            elif command in ["4", "list contents"]:
                self.list_contents()
            elif command in ["5", "create file"]:
                self.create_file()
            elif command in ["6", "edit file"]:
                self.edit_file()
            elif command in ["7", "delete file"]:
                self.delete_file()
            elif command in ["8", "view file"]:
                self.view_file()
            elif command in ["9", "rename file"]:
                self.rename_file()
            elif command in ["10", "create dir"]:
                self.create_directory()
            elif command in ["11", "delete dir"]:
                self.delete_directory()
            elif command in ["12", "rename dir"]:
                self.rename_directory()
            elif command in ["13", "change dir"]:
                self.change_directory()
            elif command in ["14", "disk info"]:
                self.view_disk_info()
            else:
                print("INVALID COMMAND")


def display_screensaver():
    """Display the screensaver with the S1MP9OS version."""
    clear_terminal()

    version_text = f"S1MP9OS VERSION {S1MP9OS_VERSION}"
    center_position = (SCREEN_WIDTH - len(version_text)) // 2

    decoration_line = set_color('white') + DECORATION_CHAR * SCREEN_WIDTH
    print(decoration_line)

    for _ in range(5):
        print()

    print(set_color('white') + " " * center_position + version_text)

    for _ in range(5):
        print()

    print(decoration_line)

    print(set_color('white') + "Press any key to start the system...")
    msvcrt.getch()


def print_current_time():
    """Print the current date and time."""
    now = datetime.now()
    print(set_color('green') + f"Year: {now.year}")
    print(f"Month: {now.month}")
    print(f"Day: {now.day}")
    print(f"Hour: {now.hour}")
    print(f"Minute: {now.minute}")
    print(f"Second: {now.second}")
    print(f"Microsecond: {now.microsecond}")



def random_number():
    """Print a random number between 1 and 100."""
    print(set_color('green') + str(random.randint(1, 100)))

def reverse_command(text):
    """Print the given text in reverse order."""
    print(set_color('green') + text[::-1])


def load_user_data():
    """Load user data from a JSON file."""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}


def save_user_data(user_data):
    """Save user data to a JSON file."""
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(user_data, file)


def register_user():
    """Register a new user."""
    user_data = load_user_data()
    username = input(set_color('green') + "ENTER USERNAME: ")
    if username in user_data:
        print(set_color('red') + "USERNAME ALREADY EXISTS. PLEASE CHOOSE A DIFFERENT USERNAME")
        return
    password = input(set_color('green') + "ENTER PASSWORD: ")
    user_data[username] = password
    save_user_data(user_data)
    print(set_color('green') + "USER REGISTERED SUCCESSFULLY!")

def login_user():
    """Log in an existing user."""
    user_data = load_user_data()
    username = input(set_color('green') + "ENTER USERNAME: ")
    password = input(set_color('green') + "ENTER PASSWORD: ")
    if user_data.get(username) == password:
        print(set_color('green') + "LOGIN SUCCESSFUL!")
        return True
    else:
        print(set_color('red') + "INVALID CREDENTIALS. PLEASE TRY AGAIN")
        return False


def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def convert_to_binary(number: int) -> str:
    if not isinstance(number, int):
        raise ValueError("INPUT MUST BE AN INTEGER")
    if number < 0:
        raise TypeError("INPUT MUST BE A NON-NEGATIVE INTEGER")

    binary_representation = bin(number)
    return binary_representation

def binary_number():
    try:
        user_input = input(set_color('green') + "ENTER NUMBER: ")
        number = int(user_input)
        binary_result = convert_to_binary(number)
        print(set_color('green') + f"BINARY REPRESENTATION: {binary_result}")

    except ValueError as ve:
        print(set_color('red') + f"ValueError: {ve}")
    except TypeError as te:
        print(set_color('red') + f"TypeError: {te}")
    except Exception as e:
        print(set_color('red') + f"AN UNEXCEPECTED ERROR OCCURED: {e}")

def draw_header(users_computer):
    """Draw the header of the interface."""
    width = SCREEN_WIDTH
    print(set_color('blue') + "╔" + "═" * (width-2) + "╗")
    print("║" + " " * (width-2) + "║")
    system_text = f"S1MP9OS Version {S1MP9OS_VERSION}"
    print("║" + system_text.center(width-2) + "║")
    computer_text = f"Computer: {users_computer}"
    print("║" + computer_text.center(width-2) + "║")
    print("║" + " " * (width-2) + "║")
    print("╠" + "═" * (width-2) + "╣")

def draw_footer():
    """Draw the footer of the interface."""
    width = SCREEN_WIDTH
    print(set_color('blue') + "╠" + "═" * (width-2) + "╣")
    help_text = "Type 'HELP' for commands list | 'SHELP' for SUDO commands | 'Q' to quit"
    print("║" + help_text.center(width-2) + "║")
    print("╚" + "═" * (width-2) + "╝")

def main():
    """Main function to run the console program."""
    
    display_screensaver()
    print(set_color('light_blue') + "Starting S1MP9OS...")
    time.sleep(1)

    print(set_color('white') + "WELCOME TO THE SYSTEM!")
    while True:
        clear_terminal()
        draw_menu_box("USER SYSTEM", [
            "Register new user",
            "Login to existing user",
            "Quit system"
        ])

        action = input(set_color('yellow') + "WOULD YOU LIKE (R)EGISTER, (L)OGIN, (Q)UIT? ").strip().upper()
        
        if action == 'R':
            register_user()
            draw_status_bar("USER REGISTERED SUCCESSFULLY")
        elif action == 'L':
            if login_user():
                draw_status_bar("Login successful", "SUCCESS")
                time.sleep(1)
                break
            else:
                draw_status_bar("Login failed", "ERROR")
        elif action == 'Q':
            draw_status_bar("System shutdown initiated", "SHUTDOWN")
            time.sleep(1)
            return
        else:
            draw_status_bar("Invalid option selected", "ERROR")

        time.sleep(1)

    users_computer = input(set_color('yellow') + "ENTER YOUR PC NAME: ")
    start_system = input(f"{users_computer}, START SYSTEM? (yes/no): ").lower()
    if start_system != "yes":
        print(set_color('red') + "SYSTEM NOT STARTED")
        return

    disk_system = DiskSystem()

    while True:
        clear_terminal()
        draw_header(users_computer)
        print(set_color('white') + "\n" * 2)


        command = input(set_color('green') + f"{users_computer}@root>> ").strip().upper()
        
        print("\n")

        command_executed = False 

        if command == "Q":
            print(set_color('red') + "SHUTDOWN IN 2 SEC")
            time.sleep(2)
            break
        elif command.startswith(ROOT_PREFIX):
            command = command[len(ROOT_PREFIX):]
            if command == "CREDISK":
                disk_system.run()
                command_executed = True
            elif command == "ENDPROC":
                end_proc()
                command_executed = True
            elif command == "SYSTEMINFO":
                print_system_info(users_computer)
                command_executed = True
            else:
                print(set_color('red') + "INVALID ROOT COMMAND")
        elif command == "HELP":
            print_help()
            command_executed = True
        elif command == "TIME":
            print_current_time()
            command_executed = True
        elif command == "CALCULATOR":
            calculator()
            command_executed = True
        elif command == "RANDINT":
            random_number()
            command_executed = True
        elif command == "REVERSE":
            reverse_command(input("ENTER TEXT TO REVERSE: "))
            command_executed = True
        elif command == "CLEAR":
            clear_terminal()
            command_executed = True
        elif command == "NOTEPAD":
            notepad = Notepad(disk_system)
            notepad.run()
            command_executed = True
        elif command == "GUESS":
            play_guess()
            command_executed = True
        elif command == "TIC-TAC-TOE":
            print("WELCOME TO TIC-TAC-TOE!")
            game = TicTacToe()
            game.play_game()
            command_executed = True
        elif command == "PONG":
            game = PongGame()
            game.play()
            command_executed = True
        elif command == "SNAKE":
            game = SnakeGame()
            game.play()
            command_executed = True
        elif command == "SHELP":
            sudo_help_manual()
            command_executed = True
        elif command == "SETTEXT":
            set_color(input("ENTER COLOR NAME: "))
            command_executed = True
        elif command == "BINARY":
            binary_number()
            command_executed = True
        
        if not command_executed:  
            print(set_color('red') + "INVALID OPERATION: CHECK YOUR CALCULATION")
            print("\n" * 2)
            draw_footer()
            input(set_color('green') + "\nPress enter to continue...")
        else:
            input(set_color('green') + "\nPress enter to continue...")


def print_help():
    """Print the available commands."""
    draw_menu_box("AVAILABLE COMMANDS", [
        "HELP      - Show this help menu",
        "CALCULATOR- Basic calculator",
        "TIME      - Show current time",
        "EXIT      - Exit system",
        "RANDINT   - Generate random number",
        "REVERSE   - Reverse input text",
        "NOTEPAD   - Text editor",
        "BINARY    - Convert to binary",
        "CLEAR     - Clear screen",
        "SETTEXT   - Change text color"
    ])
    print("\nDEV GITHUB: https://github.com/Kross1de/S1MP9os")


def sudo_help_manual():
    """Print help manual for sudo commands."""
    draw_menu_box("SUDO COMMANDS", [
        "CREDISK    - Disk management system",
        "SYSTEMINFO - Show system information",
        "ENDPROC    - End process by PID"
    ])
    print("\nPrefix all commands with 'SUDO' to execute")

def random_number_game():
    """Play a number guessing game."""
    number_to_guess = random.randint(1, 1000)
    attempts = 0
    print("WELCOME TO NUMBER GUESSING GAME! GUESS THE NUMBER BETWEEN 1 TO 1000")

    while True:
        try:
            guess = int(input("ENTER YOUR GUESS: "))
            attempts += 1

            if guess < 1 or guess > 1000:
                print("PLEASE GUESS A NUMBER BETWEEN 1 TO 1000")
                continue

            if guess < number_to_guess:
                print("TOO LOW! TRY AGAIN")
            elif guess > number_to_guess:
                print("TOO HIGH! TRY AGAIN")
            else:
                print(f"CONGRATULATIONS! YOU'VE GUESSED NUMBER {number_to_guess} IN {attempts} ATTEMPTS")
                break
        except ValueError:
            print("INVALID INPUT. PLEASE ENTER A VALID NUMBER")

def play_guess():
    """Play the guess game."""
    while True:
        clear_terminal()
        draw_menu_box("NUMBER GUESSING GAME", [
            "Try to guess the number between 1 and 1000",
            "",
            "(P) PLAY GAME",
            "(Q) QUIT TO MAIN MENU"
        ])
        
        action = input(set_color('yellow') + "SELECT OPTION: ").strip().upper()
        if action == 'P':
            random_number_game()
        elif action == 'Q':
            draw_status_bar("Returning to main menu", "EXIT")
            time.sleep(1)
            break
        else:
            draw_status_bar("Invalid option selected", "ERROR")
            time.sleep(1)

def end_proc():
    """End a process by PID."""
    process_id = input(set_color('green') + "ENTER PROCESS PID: ")
    os.system(f"taskkill /PID {process_id}")

def print_system_info(users_computer):
    """Print system information."""
    print(set_color('green') + f"COMPUTER NAME: {users_computer}")
    print(f"MACHINE TYPE: {platform.machine()}")
    print(f"PROCESSOR TYPE: {platform.processor()}")
    print("PLATFORM TYPE: S1MP9osV2.0")
    print("OPERATION SYSTEM: S1MP9OS")
    print("OPERATION SYSTEM RELEASE: JANUARY I THINK")
    print("OPERATION SYSTEM VERSION: 2.0")

def calculator():
    """Perform a simple calculation."""
    calc1 = float (input(set_color('green') + "NUMBER 1: "))
    calc2 = float (input("NUMBER 2: "))
    calc3 = input("WHAT YOU WANT TO DO (+, -, *, /, **, %, //): ")
    if calc3 in ["+", "-", "*", "/", "**", "%", "//"]:
        result = eval(f"{calc1} {calc3} {calc2}")
        print(set_color('green') + str(result))
    else:
        print(set_color('red') + "INVALID OPERATION: CHECK YOUR CALCULATION")



if __name__ == "__main__":
    main()