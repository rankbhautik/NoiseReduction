import cv2

# Load the image
image_path = 'your_image.png'
original_image = cv2.imread(image_path)

# Apply Gaussian blur filter
kernel_size = (5, 5)
blurred_image = cv2.GaussianBlur(original_image, kernel_size, 0)

# Display the original and filtered images
cv2.imshow('Original Image', original_image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
