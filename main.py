import speech_recognition as sr


def recognize_from_file(
    file_path="test.wav", language="fa-IR", output_file="recognized_text.txt"
):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language=language)
        print("From file:", text)
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(text + "\n")
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error with the recognition service: {e}")


def listen_and_recognize(language="fa-IR", output_file="recognized_text.txt"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Speak ...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language=language)
        print("You said :", text)
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(text + "\n")
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error with the recognition service: {e}")


if __name__ == "__main__":
    while True:
        cmd = input(
            "\nOptions:\n1. Press Enter to listen with microphone\n2. Type 'f filename.wav' for file input\n3. Type 'q' to quit\n> "
        )
        if cmd.strip().lower() == "q":
            break
        elif cmd.strip().lower().startswith("f"):
            parts = cmd.split()
            file_name = parts[1] if len(parts) > 1 else "test.wav"
            recognize_from_file(file_name)
        else:
            listen_and_recognize()
