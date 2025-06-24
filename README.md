# SPEECH-RECOGNITION-SYSTEM

COMPANY : CODTECH IT SOLUTIONS

NAME : HARANI C

INTERN ID : CT04DF167

DOMAIN : ARTIFICIAL INTELLIGENCE

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH KUMAR

# DESCTIPTION OF TASK 2 - SPEECH RECOGNITION SYSTEM #

In this task, I built a basic Speech-to-Text system using Python and the speech_recognition library. The goal of the project was to create a functional system that can transcribe short audio clips into readable text using pre-trained models like Google Web Speech API.

# Technologies Used:
1.Python

2.SpeechRecognition library

3.Google Web Speech API (via the recognizer)

# How It Works:
The speech_recognition module is used to initialize a recognizer object.

The system reads an audio file named sample.wav using the AudioFile class.

It captures the audio data and then sends it to Google’s pre-trained speech recognition model using the recognize_google() method.

If the audio is clear and recognized, the transcribed text is printed in the console.

The system also includes error handling for two common issues:

If the speech is not recognized (UnknownValueError)

If there’s a connection issue with the API (RequestError)

# Input and Output:
Input: A .wav audio file (e.g., sample.wav)

Output: Printed text transcription of the spoken words

# Key Features:
Uses a pre-trained model (Google API) — no manual training required.

Capable of handling short audio clips.

Lightweight and easy to use — suitable for beginners.

Error-handling for smoother user experience.

# Conclusion:
This task demonstrates how pre-trained models and Python libraries can be effectively used to convert speech to text. It provides the foundation for more advanced applications like voice assistants, audio note-taking tools, or accessibility software. The system works offline for reading audio files and online when connecting to the API for transcription.

