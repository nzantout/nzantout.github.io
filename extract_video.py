import cv2
import argparse
import imageio

def extract_first_frame(video_path, output_path):
    # Load the video
    cap = cv2.VideoCapture(video_path)
    
    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video.")
        return
    
    # Read the first frame
    ret, frame = cap.read()
    
    # Check if frame is read successfully
    if not ret:
        print("Error: Unable to read frame.")
        cap.release()
        return
    
    # Save the first frame as PNG
    cv2.imwrite(output_path, frame)
    
    # Release the video capture object
    cap.release()


def video_to_gif(video_path, gif_path, fps=30):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    frames = []
    
    # Read each frame from the video
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Convert the frame from BGR (OpenCV format) to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame_rgb)
    
    # Release the video capture object
    cap.release()
    
    # Save the frames as a GIF
    imageio.mimsave(gif_path, frames, fps=fps, loop=0)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Path to the input MP4 video", required=True)
    parser.add_argument("--output", help="Path to save the output PNG file", required=True)
    args = parser.parse_args()

    # Call the function to extract the first frame
    video_to_gif(args.input, args.output)

    print("First frame extracted and saved successfully.")
