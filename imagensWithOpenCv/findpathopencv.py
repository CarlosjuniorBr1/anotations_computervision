import cv2
import matplotlib.pyplot as plt

my_image = "lenna.png"
image = cv2.imread(my_image)  # The result is a numpy array with intensity values as 8-bit unsigned integers.

#image.shape mostra os valores (B, G, R)
print(image.shape)

# plotando a imagem com opencv, poderia ser com matplotlib bt 
# cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


plt.figure(figsize=(10,10))
plt.imshow(image)
plt.show()

#converte a imagem pro rgb
new_image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10,10))
plt.imshow(new_image)
plt.show()

# You can also load the image using its path, this comes in handy if the image is not in your working directory:

# image = cv2.imread(image_path)
# image.shape
# You can save the image as in jpg format.

# cv2.imwrite("lenna.jpg", image)