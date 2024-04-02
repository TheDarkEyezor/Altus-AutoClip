import cv2
from moviepy.editor import *

aspect_ratio = (9, 16) 

def process_frame_custom(frame, center) :
    height, width = frame.shape[:2]
    crop_height = height
    crop_width = int(height*aspect_ratio[0]/aspect_ratio[1])
    # Calculate crop dimensions
    if center - crop_width//2 < 0:
        cx = 0 + crop_width//2 + 1
    elif center + crop_width/2 > width:
        cx = width - crop_width//2 - 1
    else:
        cx = int(center)
    x = cx - crop_width//2
    y = 0
    # print((x, crop_x), (y, crop_y))
    
    # Crop frame
    cropped_frame = frame[y:y+crop_height, x:x+crop_width, :]
    return cropped_frame

if __name__ == "__main__":

    # Input video file
    input_video = "/Users/adiprabs/original.mp4"

    # Output video file
    output_video = "output_video5.mp4"

    # Desired aspect ratio
     # Example aspect ratio

    # Function to crop and adjust center of the frame

    # Open input video
    video_clip = VideoFileClip(input_video)
    audio_clip = video_clip.audio
    frames = video_clip.iter_frames()

    number = 0
    processed_frames = []
    height, width = video_clip.get_frame(1).shape[:2]
    crop_height = height
    crop_width = int(height*aspect_ratio[0]/aspect_ratio[1])

    for frame in frames:
        processed_frames.append(process_frame_custom(frame, number))
        number += 10
        if number > width:
            number = number%width


    output_clip = ImageSequenceClip(processed_frames, fps=video_clip.fps)
    output_clip = output_clip.set_audio(audio_clip)
    output_clip.write_videofile(output_video,fps=video_clip.fps, codec="mpeg4", audio_codec="aac")

