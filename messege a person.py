

# Twilio account credentials
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"
twilio_phone_number = "YOUR_TWILIO_PHONE_NUMBER"

# Function to recognize voice command
def get_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Optional noise adjustment
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"Your command: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your command.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error connecting to the speech recognition service.")
        return ""

# Function to send the message
def send_message(to_number, message_body):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=to_number
    )
    return message.sid

if __name__ == "__main__":
    # Get user inputs using voice commands
    recipient_name = input("Please say the recipient's name: ")
    recipient_number = input("Please say the recipient's phone number (with country code): ")
    message = input("Please say the message you would like to send: ")

    # Example usage of voice command (you can modify this part as per your needs)
    while True:
        command = get_voice_command()
        if "send message" in command:
            send_message(recipient_number, message)
            print(f"Message sent to {recipient_name}!")
            break
        elif "exit" in command:
            print("Exiting...")
            break
        else:
            print("Please say 'send message' to send the message or 'exit' to quit.")
