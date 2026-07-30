"""
Command Processor for SAKSHAM AI
Maps user voice commands to actions and spoken responses.
"""


class CommandProcessor:

    def process(self, command):

        command = command.lower().strip()

        # ------------------------
        # Greetings
        # ------------------------

        if any(word in command for word in ["hello", "hi", "hey"]):
            return {
                "action": "NONE",
                "response": "Hello! Welcome to Saksham AI. How can I assist you today?"
            }

        elif "good morning" in command:
            return {
                "action": "NONE",
                "response": "Good morning! I hope you have a wonderful day."
            }

        elif "good afternoon" in command:
            return {
                "action": "NONE",
                "response": "Good afternoon! How may I help you?"
            }

        elif "good evening" in command:
            return {
                "action": "NONE",
                "response": "Good evening! How can I assist you today?"
            }

        # ------------------------
        # Conversation
        # ------------------------

        elif "how are you" in command:
            return {
                "action": "NONE",
                "response": "I am functioning well and ready to assist you."
            }

        elif "what is your name" in command or "who are you" in command:
            return {
                "action": "NONE",
                "response": "I am Saksham AI, your offline accessibility assistant."
            }

        elif "what can you do" in command:
            return {
                "action": "NONE",
                "response": "I can read documents aloud, translate Indian Sign Language, detect nearby objects, and help you navigate the application using voice commands."
            }

        elif "thank you" in command or "thanks" in command:
            return {
                "action": "NONE",
                "response": "You're welcome! Happy to help."
            }

        # ------------------------
        # OCR
        # ------------------------

        elif any(word in command for word in ["read", "document", "ocr", "text"]):
            return {
                "action": "OCR",
                "response": "Opening Reading Assistant. Please upload or capture a document."
            }

        # ------------------------
        # ISL
        # ------------------------

        elif any(word in command for word in ["sign", "isl", "gesture"]):
            return {
                "action": "ISL",
                "response": "Opening Indian Sign Language Interpreter."
            }

        # ------------------------
        # Object Detection
        # ------------------------

        elif any(word in command for word in ["object", "detect", "camera"]):
            return {
                "action": "OBJECT",
                "response": "Opening Object Detection."
            }

        # ------------------------
        # Dashboard
        # ------------------------

        elif any(word in command for word in ["home", "dashboard"]):
            return {
                "action": "HOME",
                "response": "Returning to the home dashboard."
            }

        # ------------------------
        # Help
        # ------------------------

        elif any(word in command for word in ["help", "assist", "support"]):
            return {
                "action": "HELP",
                "response": "You can ask me to read documents, translate sign language, detect objects, or navigate through the application."
            }

        # ------------------------
        # Exit
        # ------------------------

        elif any(word in command for word in ["bye", "goodbye", "exit", "quit"]):
            return {
                "action": "EXIT",
                "response": "Goodbye! Have a wonderful day."
            }

        # ------------------------
        # Unknown
        # ------------------------

        else:
            return {
                "action": "UNKNOWN",
                "response": "Sorry, I didn't understand that command. Please try again."
            }


# ------------------------
# Testing
# ------------------------

if __name__ == "__main__":

    processor = CommandProcessor()

    while True:

        user_command = input("You: ")

        result = processor.process(user_command)

        print("\nAction :", result["action"])
        print("Assistant :", result["response"])

        if result["action"] == "EXIT":
            break