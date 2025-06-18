import cv2

def ig(url):
    cam = cv2.VideoCapture(url)

    # Check if camera opened successfully
    if not cam.isOpened():
        print("❌ Unable to open camera stream.")
        return

    while True:
        ret, frame = cam.read()

        if ret:
            resize = cv2.resize(frame, (900, 900))
            cv2.imshow('📷 Camera Feed', resize)

            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("✅ Exiting stream.")
                break
        else:
            print("❌ Camera offline or unable to fetch frame.")
            break  # Stop the loop if frame is not received

    # Clean up
    cam.release()
    cv2.destroyAllWindows()

# Replace the URL with your RTSP stream link
ig(url="rtsp://admin:admin@192.168.1.187:554/media/media1")
