from ansa import base,session,constants
import subprocess,os

session.New("discard")
base.SetCurrentDeck(constants.LSDYNA)

# os.environ['BCS_RUNS_VSC'] = '1'
# os.environ['ANSA_RUNS_VSC'] = '1'


# command = ["D:\Program Files\Microsoft VS Code\Code.exe"]
# subprocess.Popen(command,shell=False)