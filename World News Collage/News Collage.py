import os
import random
from PIL import Image

# Folder containing the images
folder_path = "news_images"
# Output image size
output_width = 5184
output_height = 3546
# Background color (black)
background_color = (0, 0, 0)
# Output file name
output_file = "collage.png"
# High overlap ratios for more precise coverage
horizontal_overlap_ratio = 0.35  # 35% horizontal overlap
vertical_overlap_ratio = 0.4     # 40% vertical overlap

# Create a new image with a black background
collage = Image.new('RGBA', (output_width, output_height), background_color)

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Shuffle the images for a random order
random.shuffle(image_files)

# Determine optimal grid size based on image count and aspect ratio
num_images = len(image_files)
optimal_cols = int((num_images * output_width / output_height) ** 0.5)
optimal_rows = num_images // optimal_cols + (1 if num_images % optimal_cols != 0 else 0)

# Calculate the effective size of each cell considering the overlaps
effective_cell_width = output_width // (optimal_cols - int(optimal_cols * horizontal_overlap_ratio))
effective_cell_height = output_height // (optimal_rows - int(optimal_rows * vertical_overlap_ratio))

# Calculate the actual overlaps in pixels
horizontal_overlap = int(effective_cell_width * horizontal_overlap_ratio)
vertical_overlap = int(effective_cell_height * vertical_overlap_ratio)

# Adjusted cell size for images to ensure full coverage with precise overlaps
adjusted_width = effective_cell_width + horizontal_overlap
adjusted_height = effective_cell_height + vertical_overlap

# Use only the required number of images for the calculated grid
image_files = image_files[:optimal_cols * optimal_rows]

# Iterate through each cell and place images with precise overlap adjustments
for idx, image_file in enumerate(image_files):
    img_path = os.path.join(folder_path, image_file)
    img = Image.open(img_path).convert('RGBA')
    
    # Calculate position in the grid with overlap adjustment
    row = idx // optimal_cols
    col = idx % optimal_cols
    x = col * (effective_cell_width - horizontal_overlap)
    y = row * (effective_cell_height - vertical_overlap)
    
    # Resize image maintaining aspect ratio to fit the adjusted cell
    img_ratio = img.width / img.height
    cell_ratio = adjusted_width / adjusted_height
    
    if img_ratio > cell_ratio:
        # Image is wider than cell, fit to width and crop height
        new_width = adjusted_width
        new_height = int(adjusted_width / img_ratio)
        img = img.resize((new_width, new_height), Image.LANCZOS)
        if new_height > adjusted_height:
            # Crop the height to fit
            top_crop = (new_height - adjusted_height) // 2
            img = img.crop((0, top_crop, new_width, top_crop + adjusted_height))
    else:
        # Image is taller than cell, fit to height and crop width
        new_height = adjusted_height
        new_width = int(adjusted_height * img_ratio)
        img = img.resize((new_width, new_height), Image.LANCZOS)
        if new_width > adjusted_width:
            # Crop the width to fit
            left_crop = (new_width - adjusted_width) // 2
            img = img.crop((left_crop, 0, left_crop + adjusted_width, new_height))
    
    # Calculate offset for placement considering the precise overlap
    offset_x = x + (effective_cell_width - img.width) // 2
    offset_y = y + (effective_cell_height - img.height) // 2
    
    # Paste the image onto the collage with precision
    collage.paste(img, (offset_x, offset_y), img)

# Save the final collage
collage.save(output_file)
print(f"Collage saved as {output_file}")
