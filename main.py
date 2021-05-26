import threading
from youtube import YoutubeScrape
from audio import AudioRecording
from video import VideoRecording
from sound_level import SoundLevel


audio = AudioRecording()
video = VideoRecording()
youtube = YoutubeScrape()
decibel = SoundLevel()

# Record video and audio
t1 = threading.Thread(target=video.start_video)
t2 = threading.Thread(target=audio.start_audio)

event = threading.Event()
event.clear()
for t in (t1, t2):
    t.start()
print('Start recording video')

youtube.youtube_scrape()

for i in (t1, t2):
    t.join()

decibel.decibel_sound()
