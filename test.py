import subprocess
import sys


Input = "iram xin pony"
splitted_input = Input.split(" ")

for i in range(len(splitted_input)):
    if(i+1) % 2 == 0:
        print(i+1)
cmd = 'python notes/eso.py'
result = subprocess.run(cmd, shell=True)