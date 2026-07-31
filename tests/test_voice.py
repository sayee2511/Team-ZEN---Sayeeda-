from voice.commands import CommandProcessor
from voice.text_to_speech import tts

cp = CommandProcessor()

result = cp.process("hello")

print(result)

tts.speak(result["response"])