import cv2

# Load the image
image = cv2.imread('assignment-001-given.jpg')

def add_text_with_background(
    image, text, position, font, font_scale, font_thickness, text_color, bg_color, opacity, padding=10
):
    img_cp = image.copy()
    text_size, baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_width, text_height = text_size

    rect_x1 = position[0] - padding
    rect_y1 = position[1] - text_height - padding
    rect_x2 = position[0] + text_width + padding
    rect_y2 = position[1] + baseline + padding

    cv2.rectangle(img_cp, (rect_x1, rect_y1), (rect_x2, rect_y2), bg_color, -1)
    cv2.addWeighted(img_cp, opacity, image, 1 - opacity, 0, image)

    cv2.putText(image, text, position, font, font_scale, text_color, font_thickness)


text = 'RAH972U'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2.5
font_thickness = 5
text_color = (0, 255, 0) 
bg_color = (0, 0, 0)  
opacity = 0.5
padding = 18 

large_rect_top_left = (900, 180) 
text_x = large_rect_top_left[0]  
text_y = large_rect_top_left[1] - 30  
add_text_with_background(
    image, text, (text_x, text_y), 
    font, font_scale, font_thickness, text_color, bg_color, opacity, padding
)

cv2.rectangle(image, (260, 197), (985, 930), (0, 255, 0), 9)

cv2.imshow('Image Assignment', image)
cv2.waitKey(0)
cv2.imwrite('assignment-001-result.jpg', image)
cv2.destroyAllWindows()
