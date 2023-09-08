import os
from PIL import Image

# Set the directory containing the image files
directory = "C:/Users/ityle/Downloads/Edit"

# Set the pixel trim size
trim = 16
trim_top = 300  # New trim for the top

# Get a list of the files in the directory
files = os.listdir(directory)

# Start with quality 100 and decrease to 1
start_quality = 100
end_quality = 1

# Store file paths, sizes, and quality settings
file_info = []

# Iterate through the files
for file in files:
    # Check if the file is a PNG
    if file.endswith(".png"):
        print(f"Processing {file}...")

        # Open the image file
        im = Image.open(os.path.join(directory, file))

        # Trim the top part of the image
        width, height = im.size
        im = im.crop((0, trim_top, width, height - trim))

        # Loop through quality settings
        for quality in range(start_quality, end_quality - 1, -1):
            # Save the image with the current quality setting
            webp_filename = os.path.join(directory, f"{quality}_q_" + file.replace(".png", ".webp"))
            im.save(webp_filename, "WebP", quality=quality)

            # Get the file size
            file_size = os.path.getsize(webp_filename)

            # Store file path, size, and quality
            file_info.append((webp_filename, file_size, quality))

            # Print information
            print(f"Quality: {quality}, File: {webp_filename}, Size: {file_size} bytes")

# Find the file closest to X KB
closest_file = min(file_info, key=lambda x: abs(x[1] - 15000))

# Delete all other generated WebP files
for webp_file, _, _ in file_info:
    if webp_file != closest_file[0]:
        os.remove(webp_file)
        print(f"Deleted {webp_file}")

print(f"Closest file to 35KB: {closest_file[0]}, Size: {closest_file[1]} bytes, Quality: {closest_file[2]}")
