import freenect
import cv2
import numpy as np
import subprocess

# Start FFmpeg process to stream RGB frames
ffmpeg = subprocess.Popen(
    ['ffmpeg', '-f', 'rawvideo', '-pixel_format', 'rgb24', '-video_size', '640x480', '-i', '-', 
     '-vcodec', 'libx264', '-f', 'rtsp', 'rtsp://localhost:8554/live.sdp'],
    stdin=subprocess.PIPE
)

def get_video():
    frame, _ = freenect.sync_get_video()
    return frame

while True:
    frame = get_video()
    # Write the frame to FFmpeg stdin
    ffmpeg.stdin.write(frame.tobytes())

    cv2.imshow('Kinect Video', frame)
    
    if cv2.waitKey(1) == 27:  # Press ESC to quit
        break

ffmpeg.stdin.close()
ffmpeg.wait()
cv2.destroyAllWindows()
