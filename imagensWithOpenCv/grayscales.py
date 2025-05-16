import cv2 
import matplotlib.pyplot as plt 

image = cv2.imread("lenna.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10,10))
plt.imshow(image_gray , cmap='gray')
plt.show()

#salvando a imagem no diretorio
cv2.imwrite('lena_gray_cv.jpg', image_gray)

