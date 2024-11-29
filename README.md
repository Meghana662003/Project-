PDF to Audio Converter

A web application built with Django that converts PDF documents into audio files. This project is designed to help users convert written content into audio for accessibility or convenience.

Features
Upload a PDF file.
Extract text from the PDF.
Convert the extracted text to an audio file (MP3 format).
Download the generated audio file.
Support for multiple pages and large PDFs.
Simple and user-friendly interface.
Prerequisites
Make sure you have the following installed:

Python (>= 3.7)
pip (Python package manager)
Virtualenv (optional but recommended)
Installation
Clone the repository

bash
Copy code
git clone https://github.com/yourusername/pdf-to-audio-converter.git
cd pdf-to-audio-converter
Create a virtual environment (optional but recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Set up the Django project

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the development server

bash
Copy code
python manage.py runserver
Access the application
Open your browser and go to http://127.0.0.1:8000.

Usage
Open the application in your browser.
Upload a PDF file using the upload form.
Click on the "Convert" button.
Once the audio file is generated, click the download link to save it.
Dependencies
Django: Web framework for the application.
PyPDF2: Extracts text from PDF files.
gTTS (Google Text-to-Speech): Converts text to audio.
File Storage: Manages uploaded PDFs and generated audio files.
Folder Structure
graphql
Copy code

pdf-to-audio-converter/
├── audio_converter/     # Django app for the core functionality
├── media/               # Stores uploaded PDFs and audio files
├── static/              # Static assets (CSS, JS)
├── templates/           # HTML templates
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

Future Enhancements

Support for multiple languages.
Option to choose audio formats (e.g., WAV, OGG).
Improved text extraction for complex PDFs.
Cloud storage integration for handling large files.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch for your feature/bugfix.
Commit your changes and push to your fork.
Submit a pull request with a detailed description.
License
This project is licensed under the MIT License. See the LICENSE file for details.
