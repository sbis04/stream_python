import subprocess
import cv2
rtmp_url = "url"

# In my mac webcamera is 0, also you can set a video file name instead, for example "/home/user/demo.mp4"
path = 0
cap = cv2.VideoCapture(path)

# gather video info to ffmpeg
# fps = 30
# width = 1080
# height = 1080
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# command and params for ffmpeg
command = ['ffmpeg',
           '-y',
           '-f', 'rawvideo',
           '-vcodec', 'rawvideo',
           '-pix_fmt', 'bgr24',
           '-s', "{}x{}".format(width, height),
           '-r', str(fps),
           '-i', '-',
           '-c:v', 'libx264',
           '-pix_fmt', 'yuv420p',
           '-preset', 'ultrafast',
           '-f', 'flv',
           '-flvflags', 'no_duration_filesize',
           rtmp_url]

# using subprocess and pipe to fetch frame data
p = subprocess.Popen(command, stdin=subprocess.PIPE)


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("frame read failed")
        break

    # YOUR CODE FOR PROCESSING FRAME HERE

    # write to pipe
    p.stdin.write(frame.tobytes())
