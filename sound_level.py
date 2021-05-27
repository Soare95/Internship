from pydub import AudioSegment
import numpy as np
import soundfile as sfile
import matplotlib.pyplot as plt


class SoundLevel:

    def decibel_sound(self):
        filename = 'recorded_audio.wav'

        audio = AudioSegment.from_mp3(filename)
        signal, sr = sfile.read(filename)
        samples = audio.get_array_of_samples()
        samples_sf = 0
        try:
            samples_sf = signal[:, 0]  # use the first channel for dual
        except:
            samples_sf = signal  # for mono

        # Convert to db
        def convert_to_decibel(arr):
            ref = 1
            if arr != 0:
                return 20 * np.log10(abs(arr) / ref)

            else:
                return -60

        data = [convert_to_decibel(i) for i in samples_sf]
        plt.plot(data)
        plt.xlabel('Samples')
        plt.ylabel('dB Full Scale (dB)')
        plt.tight_layout()
        plt.savefig('plot.png', dpi=300, bbox_inches='tight')
        plt.show()
