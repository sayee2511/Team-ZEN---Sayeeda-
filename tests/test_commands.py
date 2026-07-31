from voice.commands import CommandProcessor

cp = CommandProcessor()

commands = [
    "Hello",
    "How are you",
    "What can you do",
    "Read document",
    "Open sign language",
    "Detect object",
    "Goodbye"
]

for command in commands:
    result = cp.process(command)

    print(command)
    print(result)
    print("-" * 40)