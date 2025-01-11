import cv2
img=cv2.imread("lena.jpg")
cv2.circle(img,(300,300),100,(0,0,255),4)
cv2
cv2.imshow("image show",img)
cv2.waitKey(0)
cv2.imwrite("lena_circle.png",img)
cv2.destroyAllWindows()