from flask import Flask, render_template
import qrcode
from PIL import Image
import os

app = Flask(__name__)

# Your media files (place in a folder named 'static')
PHOTOS = ["IMG-20250328-WA0006.jpg", "IMG-20250328-WA0007.jpg", "IMG-20250328-WA0008.jpg", "IMG-20250328-WA0009.jpg", "IMG-20250328-WA0010.jpg", "IMG-20250328-WA0011.jpg", "IMG-20250328-WA0012.jpg", "IMG-20250328-WA0013.jpg", "IMG-20250328-WA0014.jpg", "IMG-20250328-WA0015.jpg", "IMG-20250328-WA0016.jpg", "IMG-20250328-WA0017.jpg", "IMG-20250328-WA0018.jpg", "IMG-20250328-WA0019.jpg", "IMG-20250328-WA0020.jpg" ]  # Replace with your filenames
VIDEOS = ["VID-20250328-WA0022.mp4", "VID-20250328-WA0023.mp4", "VID-20250328-WA0024.mp4", "VID-20250328-WA0025.mp4", "VID-20250328-WA0026.mp4", "VID-20250328-WA0027.mp4", "VID-20250328-WA0028.mp4", "VID-20250328-WA0029.mp4" ]  # Replace with your video
LOVE_TEXT = "To the love of my life, every moment with you is magical. ❤️"

# Generate the webpage
@app.route('/')
def home():
    return render_template('love_page.html', 
                          photos=PHOTOS, 
                          videos=VIDEOS, 
                          love_text=LOVE_TEXT)

# Generate QR code
def generate_qr():
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data("https://girlfriend-qr.onrender.com")  # Replace later with public URL
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Add a heart logo (optional)
    logo = Image.open("static/heart.png")  # Replace if needed
    logo_size = 50
    logo = logo.resize((logo_size, logo_size))
    pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
    img.paste(logo, pos)
    
    img.save("static/girlfriend_qr.png")
    print("QR code saved to 'static/girlfriend_qr.png'")

if __name__ == '__main__':
    generate_qr()  # Generate QR first
    app.run(debug=True)  # Run the Flask app