import numpy as np
import cv2


cap = cv2.VideoCapture(0) # if have 2 cam defind capture 0-1
#cam2
cap2 = cv2.VideoCapture(1)
name_product = 'AQUAFINA_BIO'
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('cam1'+'_'+name_product+'.mp4',fourcc, 20.0, (640,480))
out2 = cv2.VideoWriter('cam2'+'_'+name_product+'.mp4',fourcc, 20.0, (640,480))

# out = cv2.VideoWriter('cam1'+'_'+name_product+'.mp4',fourcc, 20.0, (640,480))
# out2 = cv2.VideoWriter('cam2'+'_'+name_product+'.mp4',fourcc, 20.0, (640,480))


while(cap.isOpened()):
    ret, frame = cap.read()
    #
    ret2, frame2 = cap2.read()
    if ret==True:
        frame = cv2.flip(frame,1) # rotate
        #cam2
        frame2 = cv2.flip(frame2,1)
        # # write the flipped frame
        out.write(frame)# need
        out2.write(frame2)

        cv2.imshow('frame',frame)
        cv2.imshow('frame',frame2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
#cam2
cap2.release()
out2.release()

cv2.destroyAllWindows()
