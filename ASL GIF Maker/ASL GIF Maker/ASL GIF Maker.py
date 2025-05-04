# ASL GIF Maker
# Copyright (C) 2024, Sourceduty - All Rights Reserved.


import os
from PIL import Image

def create_gif_from_word(word, input_folder='Images', output_folder='GIFs'):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # List of image files based on the letters in the word
    image_files = [f"{letter.upper()}.jpeg" for letter in word]
    
    # Check if all files exist
    missing_files = [file for file in image_files if not os.path.exists(os.path.join(input_folder, file))]
    if missing_files:
        raise FileNotFoundError(f"The following files are missing: {', '.join(missing_files)}")
    
    # Load images
    images = [Image.open(os.path.join(input_folder, img)) for img in image_files]
    
    # Define the output GIF path
    output_gif_path = os.path.join(output_folder, f'{word}.gif')
    
    # Save images as a GIF
    images[0].save(
        output_gif_path,
        save_all=True,
        append_images=images[1:], 
        duration=500,  # Duration in milliseconds
        loop=0  # Loop forever
    )
    
    print(f'GIF for the word "{word}" has been saved to {output_gif_path}')

# Example usage
if __name__ == "__main__":
    user_word = input("Enter the word for the GIF: ").strip()
    create_gif_from_word(user_word)

