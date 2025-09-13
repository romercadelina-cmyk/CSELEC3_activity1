from PIL import Image, ImageDraw, ImageFont

# Create a blank white canvas
width, height = 400, 500
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)

# Colors
gold = (212, 175, 55)
dark_gold = (180, 140, 40)
red = (200, 0, 0)

# Draw ribbon (two red triangles)
draw.polygon([(150, 250), (180, 250), (140, 400)], fill=red)
draw.polygon([(220, 250), (250, 250), (260, 400)], fill=red)

# Draw medal circle
center = (200, 165)
radius = 100
circle_box = [center[0]-radius, center[1]-radius,
              center[0]+radius, center[1]+radius]

draw.ellipse(circle_box, fill=gold, outline=dark_gold, width=8)

# Load fonts
try:
    font_large = ImageFont.truetype("arialbd.ttf", 80)   # Bold Arial for "1"
    font_small = ImageFont.truetype("arialbd.ttf", 40)   # For MVP
    font_name = ImageFont.truetype("arialbd.ttf", 42)    # For top name
except:
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_name = ImageFont.load_default()

# Texts
text1 = "1"
text2 = "MVP"
name_text = "Cadeliña"   # <--- change this

# Get sizes
bbox1 = draw.textbbox((0, 0), text1, font=font_large)
w1, h1 = bbox1[2] - bbox1[0], bbox1[3] - bbox1[1]

bbox2 = draw.textbbox((0, 0), text2, font=font_small)
w2, h2 = bbox2[2] - bbox2[0], bbox2[3] - bbox2[1]

# Combined block height (for 1 + MVP inside circle)
spacing = 10
total_height = h1 + h2 + spacing

# Circle center
circle_cx = (circle_box[0] + circle_box[2]) / 2
circle_cy = (circle_box[1] + circle_box[3]) / 2

# Start Y so block is centered inside circle
start_y = circle_cy - total_height / 2

# Draw "1"
draw.text((circle_cx - w1/2, start_y), text1, font=font_large, fill="black")

# Draw "MVP"
draw.text((circle_cx - w2/2, start_y + h1 + spacing), text2, font=font_small, fill="black")

# Draw Name at the TOP of canvas
bbox_name = draw.textbbox((0, 0), name_text, font=font_name)
w_name = bbox_name[2] - bbox_name[0]
h_name = bbox_name[3] - bbox_name[1]
draw.text((width/2 - w_name/2, 20), name_text, font=font_name, fill="black")

# Show image
img.show()

img.save("CSELEC3_3B_CadeliñaRomer_Activity1.png")