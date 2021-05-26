from datetime import datetime
from PIL import ImageGrab
from numpy import array
import cv2


# Video name
now = str(datetime.now())[:19].replace(':', '_')
screen_video_filename = "tt%s.avi" % now

allow_record = True

class VideoRecording:

    def start_video(self):
        # Record screen
        im = ImageGrab.grab()
        video = cv2.VideoWriter(screen_video_filename,
                                cv2.VideoWriter_fourcc(*'XVID'),
                                10, im.size)  # Frame rate = 10
        while allow_record:
            im = ImageGrab.grab()
            im = cv2.cvtColor(array(im), cv2.COLOR_RGB2BGR)
            video.write(im)

        video.release()