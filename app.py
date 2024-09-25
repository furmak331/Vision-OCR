import pytesseract
from PIL import Image

def extract_text(image_path):
    image = Image.open(image_path)
    # Specifying languages 'hin' for Hindi and 'eng' for English
    text = pytesseract.image_to_string(image, lang='hin+eng')
    return text
image_path = 'images/image1.jpg'
text = extract_text(image_path)
print(text)
