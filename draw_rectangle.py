import cv2  

image = cv2.imread('lena.jpg')

cv2.rectangle(image, (200, 202), (340, 374), (0, 255, 0), 8)

cv2.imshow('Image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the grayscale image to a new file
cv2.imwrite('lena_shapes.jpg', image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()
