import os
import subprocess
from dotenv import load_dotenv

load_dotenv()
ASCII_OUTPUT_WIDTH=int(os.getenv("ASCII_OUTPUT_WIDTH"))
ASCII_OUTPUT_HEIGHT=int(os.getenv("ASCII_OUTPUT_HEIGHT"))

script_path = ".\\play_bad_apple.py"

cmd_command = f'cmd /c "mode con: cols={ASCII_OUTPUT_WIDTH + 1} lines={ASCII_OUTPUT_HEIGHT} & python {script_path}"'
subprocess.Popen("start cmd /k " + cmd_command, shell=True)
