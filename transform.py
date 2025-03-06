import speech_recognition as sr
import wave

def speech_recognition():
    # Load the recorded audio file
    filename = "system_audio.wav"

    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Open the recorded audio file and recognize speech
    with wave.open(filename, 'rb') as wf:
        # Set the recognizer to use the audio file
        audio_data = sr.AudioData(wf.readframes(wf.getnframes()), wf.getframerate(), wf.getsampwidth())
        
        try:
            # Use Google's speech recognition service
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio_data)
            return float(text.replace(" ","").strip())
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
