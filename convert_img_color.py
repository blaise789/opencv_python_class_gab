import cv2

img=cv2.imread("lena.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("image show",img)
cv2.waitKey(0)
cv2.imwrite("lena_gray.png",img)
cv2.destroyAllWindows()