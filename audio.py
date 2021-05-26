import pyaudio
import wave


# Record audio for x seconds
REC_SECONDS = 20

class AudioRecording:

    def start_audio(self):
        filename = "recorded_audio.wav"
        chunk = 1024
        FORMAT = pyaudio.paInt16
        # 1 = Mono, 2 = Stereo
        channels = 2
        sample_rate = 44100
        record_seconds = REC_SECONDS
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        output=True,
                        frames_per_buffer=chunk)

        frames = []

        print("Recording audio...")
        for i in range(int(44100 / chunk * record_seconds)):
            data = stream.read(chunk)
            frames.append(data)
        print("Finished recording audio.")

        # Stop and close stream
        stream.stop_stream()
        stream.close()
        # Terminate pyaudio object
        p.terminate()

        # Save audio file
        wf = wave.open(filename, "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))
        wf.close()

