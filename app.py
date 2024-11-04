from flask import Flask, request, send_file
import requests

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    url = request.json['url']
    # Di sini, tambahkan logika untuk mengunduh video dari URL TikTok.
    # Anda dapat menggunakan library seperti 'tiktokdownloader' atau lainnya
    # Setelah mendapatkan file video, kembalikan file tersebut.
    # Contoh dummy:
    # video_file = "path_to_video_file.mp4"
    return send_file(video_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
