import cv2

video_path = '/home/amany/Desktop/video_draw_entry/2023_10_09/008/19/train_008_cam_19_dt_2023_10_09_tc_02_53_04_Puttgarden.mp4'
cap = cv2.VideoCapture(video_path)

# Counter to keep track of processed frames
frame_count = 0
max_frames = 400
start_frame = 300

# Set the starting frame
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

# To save the captured video
fps = 20  # frame per second

# To get the width and height of the captured frame
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Change the codec to MJPEG
output_path = 'processed_video.avi'
writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Define points for start/entry line and cross line
entry_line_start = (268, 238)
entry_line_end = (246, 323)
cross_line_start = (340, 250)
cross_line_end = (320, 350)

if not cap.isOpened():
    print('Error! File NOT Found.')

while cap.isOpened() and frame_count < max_frames:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Draw start/entry point line
    cv2.line(frame, entry_line_start, entry_line_end, (0, 0, 255), 2)
    
    # Draw cross line
    cv2.line(frame, cross_line_start, cross_line_end, (0, 0, 255), 2)

    # Display the frame with the lines
    cv2.imshow('Frame with Lines', frame)

    # Increment the frame count
    frame_count += 1

    # Save the frame into processed_video
    writer.write(frame)

    # Press 'q' to exit the video
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
writer.release()  # To stop saving frames
cv2.destroyAllWindows()
