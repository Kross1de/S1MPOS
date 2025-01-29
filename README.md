![banner](https://github.com/Kross1de/S1MPOS/blob/main/banner.png?raw=true)
# <p align="center">SimpOS<p align="center">

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x"></a>
  <a href="#"><img src="https://img.shields.io/badge/Version-2.1.0-green.svg" alt="Version 2.1.0"></a>
</p>

## Описание

SimpOS — это псевдооперационная система, написанная на Python. Она предоставляет базовые функции управления файловой системой, текстовый редактор, игры и другие утилиты. Версия 2.1 включает улучшенный интерфейс, поддержку синтаксиса для текстового редактора и новые игры.

## Установка

### Требования
- Python 3.x
- Библиотека `colorama` (установите командой ниже):
  ```bash
  pip install colorama
  ```

### Шаги установки
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Kross1de/S1MPos.git
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd S1MPos
   ```

3. Запустите систему:
   ```bash
   python simpos.py
   ```

## Использование

### Интерфейс
При запуске системы вы увидите приветственное меню. Введите команды для взаимодействия с системой. Доступные команды:
- `HELP` — список доступных команд.
- `CALCULATOR` — простой калькулятор.
- `TIME` — текущее время.
- `NOTEPAD` — текстовый редактор.
- `SNAKE`, `PONG`, `TIC-TAC-TOE` — игры.
- `SUDO CREDISK` — управление дисками.
- `Q` — выход из системы.

### Функционал

#### 1. **Управление дисками**
Команда `SUDO CREDISK` открывает меню управления дисками. Вы можете:
- Создавать диски (`CREATE DISK`).
- Просматривать список дисков (`LIST DISKS`).
- Выбирать диск для работы (`SELECT DISK`).
- Создавать, редактировать, удалять файлы и директории.

Пример создания диска:
```bash
SUDO CREDISK
1. CREATE DISK
Enter disk name: diskC
Enter size in KB: 512
```

#### 2. **Текстовый редактор (Notepad)**
Команда `NOTEPAD` открывает текстовый редактор. Поддерживает:
- Создание и редактирование файлов.
- Сохранение файлов на выбранный диск.
- Подсветку синтаксиса для `.py` и `.c` файлов.

Пример использования:
```bash
NOTEPAD
1. CREATE NEW FILE
Enter filename to create: example.py
Start typing (type ':w' to save, ':q' to quit):
```

#### 3. **Игры**
В системе доступны следующие игры:
- **Snake**: Классическая змейка.
- **Pong**: Игра в пинг-понг с AI противником.
- **Tic-Tac-Toe**: Крестики-нолики против бота.

Запуск игры:
```bash
SNAKE
```

#### 4. **Системные команды**
- `TIME`: Показывает текущую дату и время.
- `RANDINT`: Генерирует случайное число от 1 до 100.
- `BINARY`: Преобразует число в двоичный формат.

Пример использования:
```bash
BINARY
Enter number: 10
Binary representation: 0b1010
```

#### 5. **Управление пользователями**
- Регистрация нового пользователя:
  ```bash
  WOULD YOU LIKE (R)EGISTER, (L)OGIN, (Q)UIT? R
  Enter username: user1
  Enter password: pass123
  ```
- Вход в систему:
  ```bash
  WOULD YOU LIKE (R)EGISTER, (L)OGIN, (Q)UIT? L
  Enter username: user1
  Enter password: pass123
  ```
