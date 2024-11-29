from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from PyPDF2 import PdfReader
from gtts import gTTS
import os

def pdf_to_audio(request):
    if request.method == 'POST' and 'pdf_file' in request.FILES:
        pdf_file = request.FILES['pdf_file']

        # Extract text from PDF
        reader = PdfReader(pdf_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

        if not text.strip():
            return HttpResponse("The PDF does not contain readable text.", status=400)

        # Get the project's root directory
        project_root = os.path.dirname(os.path.abspath(__file__))

        # Convert text to audio
        audio = gTTS(text=text, lang='en')
        output_file = f"{pdf_file.name.rsplit('.', 1)[0]}.mp3"
        output_path = os.path.join(project_root, output_file)

        audio.save(output_path)

        # Provide download link
        return FileResponse(open(output_path, 'rb'), as_attachment=True, filename=output_file)

    return render(request, 'upload.html')
