# Print all available voices
import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)


# Set the voice
import pyttsx3
engine = pyttsx3.init()

# Voice IDs pulled from engine.getProperty('voices')
# These will be system specific
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

# Use female English voice
engine.setProperty('voice', en_voice_id)
engine.say('Hello with my new voice')


# use the male English voice with an if else clause
engine.setProperty('voice', ru_voice_id)

x = 1
y = 2

z = 2

if z == x:
    engine.say(x)
else:
    engine.say(y)




# make sure the program doesn't keep running until everything has been said
engine.runAndWait()