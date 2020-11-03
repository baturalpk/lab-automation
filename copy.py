import pyperclip
import time

file1 = open('command.txt', 'r')
time.sleep(5)

while True:
    line = file1.readline()
    a = (line.strip())
    pyperclip.copy(a)
    new_text = a.replace('\n', "")
    print(a)
    
    time.sleep(0.2)
    
    if not line:
        file1.close()
        exit()