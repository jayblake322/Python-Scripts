
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")

speak.Speak("Watashiwa Jay Desu")
##bla bla