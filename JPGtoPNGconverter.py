import sys
import os
from PIL import Image

# run this code in terminal, not in IDE
# first argument is the folder name in which the image is present
# second argument is the folder name where we want to save the converted image
# grab first and second argument
img_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/exists, if not create it
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

# loop through image folder and convert it into png
for filename in os.listdir(img_folder):
	clean_name = os.path.splitext(filename)[0]
	img = Image.open(f'{img_folder}{filename}')
	img.save(f'{output_folder}{clean_name}.png', 'png')

print('ALL DONE!!')
