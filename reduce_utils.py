#
#
# Запуск нескольких утилит сразу
#
#
#
#

from argparse import ArgumentParser
import subprocess
import time



def log(prefix):
    def func(msg):
        print(f"[{prefix}] {msg}")
    return func

error = log("ERROR")


parser = ArgumentParser(
    prog='ProgramName',
    description='What the program does',
    epilog='Text at the bottom of help'
)

parser.add_argument('scripts')  
args = parser.parse_args()
print(f"args = {args}")
script_files = args.scripts.split(",")

import os

def exec(cmd):
    try:
        subprocess.run(cmd, shell=True, check=False)
    except Exception as e:
        error(e)


cwd = os.path.dirname(os.path.abspath(__file__))

for script in script_files:
    print('-'*100)
    path = f'{cwd}/{script}.py'
    print(f"Запускаю скрипт {path}\n{'-'*100}")
    exec(f'python3 {path}') 

