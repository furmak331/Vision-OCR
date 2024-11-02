import pytesseract
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import os

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def create_hindi_test_image():
    img = Image.new('RGB', (400, 100), color='white')
    d = ImageDraw.Draw(img)
    
    # Use a font that supports Hindi characters
    font_path = "C:/Windows/Fonts/NotoSansDevanagari-Regular.ttf"  # Adjust this path if necessary
    try:
        font = ImageFont.truetype(font_path, 36)
    except IOError:
        print(f"Font not found at {font_path}. Using default font.")
        font = ImageFont.load_default()
    
    d.text((10,10), "नमस्ते दुनिया", fill=(0,0,0), font=font)
    
    img.save('hindi_test.png')
    return 'hindi_test.png'

def preprocess_image(image_path):
    with Image.open(image_path) as img:
        # Convert to grayscale
        img = img.convert('L')
        
        # Enhance contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2.0)  # Increase contrast
        
        # Apply a median filter to reduce noise
        img = img.filter(ImageFilter.MedianFilter(size=3))
        
        # Resize the image for better recognition
        img = img.resize((img.width * 2, img.height * 2), Image.LANCZOS)
        
        # Save the processed image
        processed_image_path = "temp_processed_image.png"
        img.save(processed_image_path)
    return processed_image_path

def extract_text(image_path, lang='hin'):
    processed_image_path = preprocess_image(image_path)
    image = Image.open(processed_image_path)
    
    custom_config = r'--oem 3 --psm 7'  # Change PSM to 7
    text = pytesseract.image_to_string(image, lang=lang, config=custom_config)
    
    return text

# Create and verify test image
test_image_path = create_hindi_test_image()
if os.path.exists(test_image_path):
    print(f"Test image created successfully: {test_image_path}")
    Image.open(test_image_path).show()
else:
    print(f"Failed to create test image at {test_image_path}")

# Print Tesseract information
print("Tesseract version:", pytesseract.get_tesseract_version())
print("Available languages:", pytesseract.get_languages())

# Try OCR with different language configurations
languages = ['hin']
for lang in languages:
    print(f"\nTrying OCR with language: {lang}")
    text = extract_text(test_image_path, lang)
    print(f"OCR result:")
    print(text)
    print(f"OCR result (encoded):", text.encode('utf-8').decode('utf-8'))

# Try OCR on processed image
processed_image_path = preprocess_image(test_image_path)
print("\nTrying OCR on processed image:")
text = pytesseract.image_to_string(Image.open(processed_image_path), lang='hin', config=r'--oem 3 --psm 6')
print(f"OCR result:")
print(text)
print(f"OCR result (encoded):", text.encode('utf-8').decode('utf-8'))