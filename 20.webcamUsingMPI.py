from mpi4py import MPI
import cv2
import time
from ultralytics import YOLO
from ultralytics.utils.plotting import colors, Annotator

model = YOLO("yolov8s.pt")
names = model.model.names

cam1 = cv2.VideoCapture(2)
cam2 = cv2.VideoCapture(0)

cTime = 0
pTime = 0

centerPoint = (10, 10)

# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size


if rank == 0:
    while True:
        success, frame1 = cam1.read()

        results = model.predict(frame1)
        boxes = results[0].boxes.xyxy.cpu()
        clss = results[0].boxes.cls.cpu().tolist()

        annotator = Annotator(frame1)

        for box, cls in zip(boxes, clss):
            annotator.box_label(box, label=names[int(cls)], color=colors(int(cls)))
            annotator.visioneye(box, centerPoint)
            
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(frame1, f"FPS: {int(fps)}", (100,100), 
                    cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,255), 2)
        
        cv2.imshow("frame1", frame1)
        
        Key = cv2.waitKey(1)
        if Key == ord("q"):
            break
    cam1.release()
    cv2.destroyAllWindows()

if rank == 1:
    while True:
        success2, frame2 = cam2.read()

        # results = model.predict(frame1)
        # boxes = results[0].boxes.xyxy.cpu()
        # clss = results[0].boxes.cls.cpu().tolist()

        # annotator = Annotator(frame1)

        # for box, cls in zip(boxes, clss):
        #     annotator.box_label(box, label=names[int(cls)], color=colors(int(cls)))
        #     annotator.visioneye(box, centerPoint)
            
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(frame2, f"FPS: {int(fps)}", (100,100), 
                    cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,255), 2)
        
        cv2.imshow("frame2", frame2)
        
        Key = cv2.waitKey(1)
        if Key == ord("q"):
            break
    cam2.release()
    cv2.destroyAllWindows()