import command
import pyttsx3 as pt
import apps


def do(cmd: command.Command):
    if cmd.object is None:
        e = pt.Engine()
        e.say('sorry sir, i do not understand that')
        e.runAndWait()
    else:
        cmd.object['main'].__call__(cmd)


