## auto-copy-paste

Contributors: Kayra Ege ARDA & Baturalp KIZILTAN

### INSTALLATION

1-) install python v3.x

2-) set up pyperclip library via python-pip (https://pypi.org/project/pyperclip/)

3-) install AutoHotkey scripting software from its official website (https://www.autohotkey.com/)

### USAGE

1-) at first, execute your java program

2-) then, run "auto-copy-paste.ahk" & "copy.py" scripts respectively

3-) after the process, close off AutoHotkey software from taskbar

#### Sample Video: https://streamable.com/5ttbok

## REMINDERS!

- "command.txt" file includes the list of input commands for your java program and it has to be inside the same folder with "cop.py" script.
- Do NOT forget to run scripts in order (first .ahk script then .py) - After 5 seconds delay, the process will be started.
- Do NOT forget to click the java console that you've just executed, before start of the process.
- If there occurs an unexpected problem at runtime, try to change parameter of "time.sleep(0.2)" method (in the line 14 of ".py" script).
