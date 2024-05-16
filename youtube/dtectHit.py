import cv2


# Function to detect movement
def detect_movement(current_frame, previous_frame):
    # Convert frames to grayscale
    current_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    previous_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)

    # Calculate absolute difference between frames
    frame_diff = cv2.absdiff(current_gray, previous_gray)

    # Apply threshold to highlight regions of significant change
    _, threshold = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours to draw bounding boxes around moving objects
    for contour in contours:
        if cv2.contourArea(contour) > 1000:  # Adjust threshold as needed
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(current_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return current_frame


# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize previous frame as None
previous_frame = None

while True:
    # Read frame from camera
    ret, frame = cap.read()
    if not ret:
        break

    # If previous frame is not None, detect movement
    if previous_frame is not None:
        frame_with_movement = detect_movement(frame, previous_frame)
        cv2.imshow('Movement Detection', frame_with_movement)

    # Set current frame as previous frame for next iteration
    previous_frame = frame.copy()

    # Check for user input to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
cv2.destroyAllWindows()