from PIL import Image
import numpy as np

img = Image.open('public/venn.png').convert('RGBA')
data = np.array(img)

# The image is white lines on black bg.
# We want to replace it so that black becomes transparent, and white/gray becomes #FFC800 (momentum-gold) with varying alpha based on luminance.
# Luminance: L = 0.299*R + 0.587*G + 0.114*B
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
luminance = 0.299 * r + 0.587 * g + 0.114 * b

# Set the RGB to #FFC800 (255, 200, 0)
data[:,:,0] = 255
data[:,:,1] = 200
data[:,:,2] = 0
# Set alpha to the luminance of the original pixel
data[:,:,3] = luminance.astype(np.uint8)

new_img = Image.fromarray(data, 'RGBA')
new_img.save('public/venn-gold.png')
print("Saved venn-gold.png")
