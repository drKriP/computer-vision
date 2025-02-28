import cv2

# Open the webcam (0 for default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    ret, frame = cap.read()  # Capture frame-by-frame
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Webcam", frame)  # Show the video frame

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
