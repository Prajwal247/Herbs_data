from PIL import Image
import os

def convert(source_path, target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    for filename in os.listdir(source_path):
        if filename.endswith('.jpg') or filename.endswith('.png'): # or any other image format you want to include
            # Open the image
            img = Image.open(os.path.join(source_path, filename))

            # Resize the image to 64x64
            img_resized = img.resize((64, 64))

            # Save the resized image to the output directory
            output_path = os.path.join(target_path, filename)
            img_resized.save(output_path)

convert('/home/prazzwalthapa/Desktop/Herbs_classification_data/Herbs/Terminalia_Chebula', '/home/prazzwalthapa/Desktop/Herbs_classification_data/Herbs/Terminalia_Chebula_converted')