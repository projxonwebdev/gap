import colorsys
r, g, b = 255/255.0, 200/255.0, 0/255.0
h, s, v = colorsys.rgb_to_hsv(r, g, b)
print(f"momentum-gold (#FFC800): HSV = ({h*360:.1f}°, {s*100:.1f}%, {v*100:.1f}%)")

r, g, b = 255/255.0, 215/255.0, 0/255.0
h, s, v = colorsys.rgb_to_hsv(r, g, b)
print(f"momentum-gold-bright (#FFD700): HSV = ({h*360:.1f}°, {s*100:.1f}%, {v*100:.1f}%)")
