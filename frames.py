import cv2
import os

def video_to_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Read and save frames
    frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Save the frame as an image
        frame_name = f"frame_{frame_count:04d}.png"
        frame_path = os.path.join(output_folder, frame_name)
        cv2.imwrite(frame_path, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()

    print(f"Frames extracted: {frame_count}/{total_frames}")
    print(f"Frames saved in: {output_folder}")

if __name__ == "__main__":
    # Replace 'input_video.mp4' with the path to your input video file
    input_video_path = 'lol.mp4'

    # Replace 'output_frames' with the desired output folder
    output_frames_folder = 'output_frames'

    video_to_frames(input_video_path, output_frames_folder)
