import cv2
import matplotlib.pyplot as plt
# reading the image
img=cv2.imread("lena.jpg")
# resizing the image
img=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
cv2.imshow("image show",img)
cv2.waitKey(0)
# saving the image
cv2.imwrite("lena_resized.png",img)
cv2.destroyAllWindows()
