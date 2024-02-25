import cv2
import argparse

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

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Path to the input MP4 video", required=True)
    parser.add_argument("--output", help="Path to save the output PNG file", required=True)
    args = parser.parse_args()

    # Call the function to extract the first frame
    extract_first_frame(args.input, args.output)

    print("First frame extracted and saved successfully.")
