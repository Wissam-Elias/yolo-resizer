from PIL import Image
import os

input_folder = "images"
output_folder = "resized-images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Adjust this according to your YOLO model requirements
resize_width = 416 
resize_height = 416

for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        with Image.open(os.path.join(input_folder, filename)) as img:
            img_resized = img.resize((resize_width, resize_height), Image.ANTIALIAS)
            output_path = os.path.join(output_folder, filename)
            img_resized.save(output_path)
            print(f"{filename} resized and saved to {output_path}")
