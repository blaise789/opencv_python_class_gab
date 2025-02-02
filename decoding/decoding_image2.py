import cv2
from pylibdmtx.pylibdmtx import decode
from PIL import Image
import numpy as np

image_path = "image2.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded
if image is None:
    print(f"Error: Could not load image at {image_path}")
    exit()

# Convert OpenCV image (NumPy array) to PIL image for decoding
pil_image = Image.fromarray(image)
decoded_objects = decode(pil_image)

if not decoded_objects:
    print("No Data Matrix code found.")
else:
    for obj in decoded_objects:
        decoded_text = obj.data.decode("utf-8")
        print("Decoded Data:", decoded_text)

        # Draw the decoded text on the image
        image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Convert to color for annotation
        cv2.putText(image_color, decoded_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (0, 255, 0), 2, cv2.LINE_AA)

        # Save the annotated image
        output_file = "decoded_image2.png"
        cv2.imwrite(output_file, image_color)
        print(f"Annotated image saved as {output_file}")

    cv2.imshow("Barcode Image", image_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
