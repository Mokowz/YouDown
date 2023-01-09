from pytube import YouTube
import os
import cv2

# Capture the video from the URL
link = input("Enter a link: ")
yt = YouTube(link)
video = yt.streams.first()
video.download("./")

# Load the video file
video_capture = cv2.VideoCapture(video.default_filename)

# Save the video file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# output_video = cv2.VideoWriter("C:\Users\ronni\Videos\YouDown\Cartoonified_vid.mp4", fourcc, 30.0, (int(video_capture.get(3)), int(video_capture.get(4))))
output_video = cv2.VideoWriter("C:/Users/ronni/Videos/YouDown/Cartoonified_vid.mp4",fourcc, 20,(320,180))



# input_file = ffmpeg.input('input.3gp')
# output_file = ffmpeg.output(input_file, 'output.mp4')
# ffmpeg.run(output_file)


# Check if the video was successfully captured
if not video_capture.isOpened():
    print("Error opening video")

# Read the video frame by frame
success, frame = video_capture.read()

while success:
    # Cartoonify the frame
    cartoon_frame = cv2.stylization(frame, sigma_s=60, sigma_r=0.07)

    # Display the cartoonified frame
    cv2.imshow("Video", cartoon_frame)

    # Check if the user pressed 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Read the next frame
    success, frame = video_capture.read()

# Release the video capture
video_capture.release()
output_video.release()