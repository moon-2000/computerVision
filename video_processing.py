import cv2



# To connect to the default camera
cap = cv2.VideoCapture(0)

# To get the width and height of the captured frame
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()
    """
    ret (short for "return"): A boolean value indicating whether the frame was successfully read or not.
    
    frame: The actual frame that is read from the video source. It is a NumPy array representing the image.
    """

    if not ret:
        print('Frame has not been read successfully!')
        continue
    
    # To convert the frame to grayscale 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # To show the frame
    cv2.imshow('frame', gray)

    # To exit the frame after every 1 second or when pressing q button
    if (cv2.waitKey(10) & 0xFF) == ord('q'):
        break


# To stop capturing the video
cap.release()

# After finishing reading the whole video 
cv2.destroyAllWindows()
print('the video reading has been done successfully!')

