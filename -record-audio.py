import os
import pyaudio
import wave

def record_audio(file_name, duration=10, sample_rate=44100, chunk_size=1024, channels=2):
    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=channels,
        rate=sample_rate,
        input=True,
        frames_per_buffer=chunk_size
    )

    print("Recording audio...")

    frames = []

    for i in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    save_audio(file_name, frames, sample_rate)

def save_audio(file_name, frames, sample_rate):
    output_folder = os.path.join(os.path.expanduser("~"), "Desktop", "audio_recordings")
    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(output_folder, file_name)

    wave_file = wave.open(output_path, 'wb')
    wave_file.setnchannels(2)
    wave_file.setsampwidth(2)
    wave_file.setframerate(sample_rate)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

if __name__ == "__main__":
    file_name = input("Enter the name of the audio file (e.g., recording.wav): ")
    record_audio(file_name)
