import cv2
import time

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

cTime = 0
pTime = 0

while True:
    success, frame1 = cam1.read()
    success2, frame2 = cam2.read()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(frame1, f"FPS: {int(fps)}", (100,100), 
                cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,255), 2)
    cv2.putText(frame2, f"FPS: {int(fps)}", (100,100), 
                cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,255), 2)
    
    cv2.imshow("frame1", frame1)
    cv2.imshow("frame2", frame2)
    
    Key = cv2.waitKey(1)
    if Key == ord("q"):
        break

cam1.release()
cam2.release()

cv2.destroyAllWindows()