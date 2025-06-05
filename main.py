import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# تعيين مفتاح API الخاص بك
API_KEY = 'YOUR_API_KEY'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['image']
        image_bytes = image_file.read()

        # إرسال الصورة إلى Gemini API
        response = requests.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-2_0-flash:generateContent?",
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {API_KEY}'
            },
            json={
                "contents": [{
                    "parts": [{
                        "text": "Find the product in this image"
                    }]
                }]
            }
        )

        results = response.json()
        return render_template('index.html', results=results)

    return render_template('index.html', results=None)

if __name__ == '__main__':
    app.run()
