import cv2 

def camera_feed(url):
    cam = cv2.VideoCapture(url)
    while True:
        try:
          ret, frame = cam.read()
          if ret:
            resize = cv2.resize(frame, (620, 480))
            cv2. imshow('camera', resize)
            if cv2.waitKey(1) == ord('q'):
                break
            else:
                print("no cam feed")
        except Exception as e:
            print("Camera offline")
        cam.release()
        cv2.destroyAllWindows()