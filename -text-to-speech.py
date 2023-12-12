import pyttsx3

def text_to_speech(text, voice_id=None):
    engine = pyttsx3.init()

    if voice_id is not None:
        engine.setProperty('voice', voice_id)

    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    input_text = input("Enter the text you want to convert to speech: ")
    voice_id = input("Enter the voice ID (leave empty for default voice): ")
    text_to_speech(input_text, voice_id)
