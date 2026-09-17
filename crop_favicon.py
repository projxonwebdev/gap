from PIL import Image

def crop_a_from_gap(input_path, output_path):
    # Open the image
    img = Image.open(input_path).convert("RGBA")
    
    # Get bounding box of all non-transparent pixels
    bbox = img.getbbox()
    if not bbox:
        return
        
    # Crop to the exact text bounds first
    img_cropped = img.crop(bbox)
    width, height = img_cropped.size
    
    # Assuming G, A, P are roughly evenly spaced, the 'A' is in the middle third
    # We will grab from 30% to 70% of the width just to be safe
    left = int(width * 0.28)
    right = int(width * 0.72)
    
    # Crop the middle section (the 'A')
    a_img = img_cropped.crop((left, 0, right, height))
    
    # Trim the 'A' to its exact bounding box
    a_bbox = a_img.getbbox()
    if a_bbox:
        a_img = a_img.crop(a_bbox)
        
    # Resize to make it a square favicon (e.g. 256x256)
    # Paste the A in the center of a transparent square
    a_width, a_height = a_img.size
    max_dim = max(a_width, a_height)
    
    # Add a little padding (10%)
    padding = int(max_dim * 0.1)
    square_size = max_dim + (padding * 2)
    
    final_img = Image.new("RGBA", (square_size, square_size), (0, 0, 0, 0))
    offset = (
        (square_size - a_width) // 2,
        (square_size - a_height) // 2
    )
    final_img.paste(a_img, offset)
    
    # Resize to standard favicon size
    final_img = final_img.resize((128, 128), Image.Resampling.LANCZOS)
    
    # Save as PNG
    final_img.save(output_path, format="PNG")
    print(f"Saved favicon to {output_path}")

crop_a_from_gap('public/GAP-logo-justgap.png', 'public/favicon.png')
