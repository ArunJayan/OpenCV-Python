import numpy as np
import cv2

#subject = str(self.get('subject_nr'))
cap = cv2.VideoCapture(0)
#w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH ))
#h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))

#Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('path\to\output'+ 'jkm' + '.avi', -1, 20.0, (w,h))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        #out.write(frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(13,13),0)
        canny = cv2.Canny(blur,20,130)
        (cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print "I count %d coins in this image" % (len(cnts))


        cv2.imshow('frame',canny)
        if cv2.waitKey(33) == ord('a'):
            break
    else:
        break

#Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()