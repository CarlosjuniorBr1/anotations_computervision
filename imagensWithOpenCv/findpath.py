import os

#como carregar uma imagem e descobri o seu path

cwd = os.getcwd()

my_image = "lenna.png"

image_path = os.path.join(cwd, my_image)
print(image_path)

