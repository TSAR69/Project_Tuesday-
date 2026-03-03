import os

# Voice Settings
WAKE_WORD = "tuesday"

# App Paths (Common Windows Paths)
# Note: For many apps, 'start <name>' works if they are in PATH.
# We will use this dictionary for specific overrides or just key mnemonics.
APPS = {
    "chrome": "chrome",
    "vscode": "code",
    "calculator": "calc",
    "notepad": "notepad",
    "file explorer": "explorer",
    "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
    "documents": os.path.join(os.path.expanduser("~"), "Documents"),
}

# Jokes
JOKES = [
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "Why do Java programmers have to wear glasses? Because they don't C#.",
    "I told my computer I needed a break, and now it won't stop sending me Kit-Kats.",
    "What is a computer's favorite beat? An algo-rhythm.",
    "Why was the cell phone wearing glasses? It lost its contacts.",
    "Hardware: The part of a computer that you can kick.",
    "There are 10 types of people in the world: those who understand binary, and those who don't.",
    "How many programmers does it take to change a light bulb? None. It's a hardware problem.",
    "What do you call a computer floating in the ocean? A Dell Rolling in the Deep.",
]
