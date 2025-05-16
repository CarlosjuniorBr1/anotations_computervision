#Use the image baboon.png from this lab or take any image you like.
#Open the image and create a OpenCV Image object called baboon_blue, convert the image from BGR format to RGB format, get the blue channel out of it, and finally plot the image

import cv2 
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("baboon.png")
baboon_blue = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10,10))
plt.imshow(baboon_blue)
plt.title("Imagem Baboon em RGB")
plt.show()


baboon_blue_channel = image[:, :, 0]  # Canal 0 = Azul no OpenCV (BGR)

    # Exibe o canal azul em tons de cinza
plt.figure(figsize=(10,10))
plt.imshow(baboon_blue_channel, cmap='gray')
plt.title("Canal Azul da imagem Baboon")
plt.axis('off')
plt.show()


only_blue = np.zeros_like(image)
only_blue[:, :, 0] = image[:, :, 0]  # Mantém o azul (canal 0 do BGR)

# Converte para RGB para exibir corretamente no matplotlib
only_blue_rgb = cv2.cvtColor(only_blue, cv2.COLOR_BGR2RGB)

# Exibe a imagem com o azul realçado
plt.figure(figsize=(10, 10))
plt.imshow(only_blue_rgb)
plt.title("Somente Canal Azul Realçado (em azul)")
plt.axis('off')
plt.show()