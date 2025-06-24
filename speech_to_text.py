import speech_recognition as sr

# Step 1: Initialize the recognizer
recognizer = sr.Recognizer()

# Step 2: Load your audio file
with sr.AudioFile('sample.wav') as source:
    print("🎧 Listening to audio...")
    audio_data = recognizer.record(source)

    # Step 3: Transcribe speech to text
    try:
        text = recognizer.recognize_google(audio_data)
        print("\n📝 Transcribed Text:")
        print(text)
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError:
        print("❌ Could not connect to the speech recognition service.")
