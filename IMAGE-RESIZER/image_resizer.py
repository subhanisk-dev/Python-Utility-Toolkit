from PIL import Image
import os
 
path = input("Enter the image file name : ")
 
if not os.path.isfile(path):
    print("Image not found.")
else:
    img = Image.open(path)
    print("Original size (width x height) :", img.size)
 
    choice = input("Resize by (1) Exact size or (2) Percentage ? : ")
 
    if choice == "1":
        w = int(input("Enter new width  : "))
        h = int(input("Enter new height : "))
    else:
        p = float(input("Enter percentage (example 50) : "))
        w = int(img.width * p / 100)
        h = int(img.height * p / 100)
 
    resized = img.resize((w, h), Image.LANCZOS)
 
    name, ext = os.path.splitext(path)
    out = name + "_resized" + ext
    resized.save(out)
 
    print("Resized image saved as :", out, "with size", resized.size)
