import initiate
import pyttsx3 as pt
import disturbance as d
import command
import action

sentence = ['']
activations = ['iris', 'Irish', 'irish', 'IRS']
engine = pt.engine.Engine()
engine.say("welcome to Iris")
engine.runAndWait()
engine.say("Intelligent Recognition Integrated System")
engine.runAndWait()
engine.say("boot")
engine.runAndWait()
engine.say("complete")
engine.runAndWait()

while True:
    if initiate.waitcall():
        cmd = initiate.recognize_command()
        cmd = command.Command(cmd)
        print(cmd)
        action.do(cmd)
