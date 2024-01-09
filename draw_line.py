import cv2
import os


# Path to the directory containing the videos
video_directory = '/home/amany/Desktop/video_draw_entry/2023_10_09/008/19'

# Path to the directory to save processed videos
output_directory = '/home/amany/Desktop/video_draw_entry/2023_10_09/008/19_processed'


#video_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(video_directory) for f in filenames if f.endswith('.mp4')]
video_files = [f for dp, dn, filenames in os.walk(video_directory) for f in filenames if f.endswith('.mp4')]
print(f'number of videos to be processed is {len(video_files)}')
print(f'video files {video_files}')


for video_file in video_files:
    # Construct the full path of the video file
    input_video_path = os.path.join(video_directory, video_file)
    cap = cv2.VideoCapture(input_video_path)

    # To get the width and height of the captured frame
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Change the codec to MJPEG

    # To save the captured video
    fps = 20  # frame per second

    
    # Construct the output video path
    output_name = video_file.replace('.mp4', '_processed.avi')
    output_path = os.path.join(output_directory, output_name)
    print(f'\n\n output path {output_path}')
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))


    # Define points for start/entry line and cross line
    entry_line_start = (268, 238)
    entry_line_end = (246, 323)
    cross_line_start = (340, 250)
    cross_line_end = (326, 326)

    if not cap.isOpened():
        print('Error! File NOT Found.')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Draw start/entry point line
        cv2.line(frame, entry_line_start, entry_line_end, (0, 0, 255), 2)
        
        # Draw cross line
        cv2.line(frame, cross_line_start, cross_line_end, (0, 0, 255), 2)

        # Display the frame with the lines
        cv2.imshow('Frame with Lines', frame)


        # Save the frame into processed_video
        writer.write(frame)

        # Press 'q' to exit the video
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    writer.release()  # To stop saving frames
    cv2.destroyAllWindows()








