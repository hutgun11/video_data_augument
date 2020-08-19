import cv2
top=1#y1
left=640#x1
width=1480-640#x2-x1
height=1081-1#y2-y1
img = cv2.imread("data_pepsi_big_1/frame8_pepsi_big_1.jpg")
crop = img[ top:top+height, left:left+width ]

cv2.imshow("cropped", crop)
cv2.waitKey(0)