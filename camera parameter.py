import cv2
import datetime


cap= cv2.VideoCapture(0);
cap.set(3,720)#3=cv2.CAP_PROP_FRAME_HEIGHT
print(cap.get(3)) #4=cv2.CAP_PROP_FRAME_WEIGHT

while cap.isOpened():
    ret,frame=cap.read()
    text='weight'+str(cap.get(3))
    datet=str(datetime.datetime.now())
    font=cv2.FONT_HERSHEY_DUPLEX
    frame=cv2.putText(frame,datet,(0,255),font,1,(0,255,0),6,cv2.LINE_AA)

    cv2.imshow('image',frame)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


