import pyaudio
import wave

def recording_audio():
    # Audio settings
    samplerate = 44100
    channels = 2
    duration = 6  # seconds
    filename = "system_audio.wav"

    # Initialize pyaudio
    p = pyaudio.PyAudio()

    # Open the stream to record from the stereo mix (adjust the device index accordingly)
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=samplerate,
                    input=True,
                    input_device_index=0,  # Adjust to the correct input device index for Stereo Mix
                    frames_per_buffer=1024)

    print("Recording system audio...")

    # Record audio
    frames = []
    for i in range(0, int(samplerate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    # Stop the recording
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio to a file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(samplerate)
        wf.writeframes(b''.join(frames))

    print(f"Audio recorded and saved to {filename}.")
