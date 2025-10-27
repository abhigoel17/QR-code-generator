 #QRcode generator

import qrcode
from PIL import Image
import os

# Input data from user to encode in QR code
data = input("🔹Enter data to encode in QR code: ").strip()
if not data:
    print("❌ Error: Data cannot be empty!")
    exit()

# Ask user where to save the QR code
default_folder = os.path.join(os.getcwd(), "QRcodes")                           
os.makedirs(default_folder, exist_ok=True)

print(f"\n📁 Default save location: {default_folder}")
custom_path = input("👉 Enter custom folder path (or press Enter to use default): ").strip()

save_folder = custom_path if custom_path else default_folder
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

file_name = input("📄 Enter file name (without extension): ").strip()
if not file_name:
    file_name = "my_qrcode"

save_path = os.path.join(save_folder, f"{file_name}.png")

# Create QR code object 
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create image of QR code
img = qr.make_image(fill_color="black", back_color="white")

# (Optional) Add logo in center of QR code 
add_logo = input("🖼️ Do you want to add a logo in center? (y/n): ").lower()
if add_logo == "y":
    logo_path = input("Enter logo image path: ").strip()
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        logo_size = (img.size[0] // 4, img.size[1] // 4)
        logo = logo.resize(logo_size)

        pos = ((img.size[0] - logo_size[0]) // 2, (img.size[1] - logo_size[1]) // 2)
        img = img.convert("RGBA")
        logo = logo.convert("RGBA")
        img.paste(logo, pos, mask=logo)
    else:
        print("⚠️ Logo path not found, skipping logo addition.")

# Save and show output 
img.save(save_path)
print(f"\n✅ QR Code generated successfully!")
print(f"📍 Saved at: {save_path}")

# Optional: show the QR image 
try:
    img.show()
except Exception:
    print("🖼️ Image preview not supported on this system.")
