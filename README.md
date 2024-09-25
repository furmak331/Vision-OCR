# Hindi-English OCR with Keyword Search

## Description
This is a simple web application that performs Optical Character Recognition (OCR) on images containing text in both Hindi and English. It also includes a basic keyword search feature that lets users search for specific words in the extracted text.

## Features
- Upload image (JPEG, PNG)
- OCR to extract text in Hindi and English
- Keyword search within the extracted text
- Deployed online via Streamlit Sharing

## Setup Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/furmak331/vision-ocr.git
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
``` 

### 3. Run the Streamlit app:
```bash
streamlit run app.py
```

### 4. Access the app:
Open your web browser and navigate to `http://localhost:8501` to access the OCR application.

## Note
- This app uses Tesseract OCR for text extraction. Make sure to have Tesseract installed on your system.
- The app is designed for basic OCR tasks and keyword searches. For more advanced features, consider using specialized OCR libraries.   

