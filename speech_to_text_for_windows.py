# speech to text in python for windows (imp)
# its works by operating system hence won't work in online compiler

# Start by importing the win32com package
# it is an built in module
import win32com.client as win

say = win.Dispatch("SAPI.SpVoice")

text = "demo Python text-to-speech test. using win32com.client"
say.Speak(text)
