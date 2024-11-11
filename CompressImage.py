import os
from PIL import Image

def convert_and_compress_images(input_folder, output_folder, output_format='webp', quality=80):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
            with Image.open(os.path.join(input_folder, filename)) as img:
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.{output_format}")

                # Save the image in the specified format with compression
                img.save(output_file, format=output_format.upper(), quality=quality)
                print(f"Converted and compressed {filename} to {output_file}")

# Example usage
input_folder = './files/crifter-experiences-raw'
output_folder = './files/crifter-experiences-processed-60'
output_format = 'webp'  # You can change this to 'jpg' or other supported formats
quality = 60  # Compression quality (1-100)

convert_and_compress_images(input_folder, output_folder, output_format, quality)
