from utilities.speech_to_text import speech_to_text
from utilities.text_to_speech import text_to_speech


def main():
    while True:
        user_input = speech_to_text()
        if user_input:
            response = process_text(user_input)
            text_to_speech(response)

if __name__ == "__main__":
    main()
