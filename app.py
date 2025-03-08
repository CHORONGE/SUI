from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

MEDIA_DIR = "static/media"  # 미디어 파일들이 저장된 폴더

@app.route('/')
def index():
    files = os.listdir(MEDIA_DIR)
    return render_template('index.html', files=files)

@app.route('/media/<filename>')
def media(filename):
    return send_from_directory(MEDIA_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

