import cv2

input_image_path = "input.png"
scale_factor = 4

input_image = cv2.imread(input_image_path)
height, width = input_image.shape[:2]

sr_image = cv2.resize(input_image, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_CUBIC)

cv2.imwrite("resolution.png", sr_image)
