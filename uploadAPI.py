from flask import request
from flask import Flask
import os
from filetomp4 import makeVideo
from example import uploadVideo
app = Flask(__name__)
# from flask_cors import CORS, cross_origin
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/upload', methods=['POST'])
def upload_file():
    if (request.method == 'POST'):
        file = request.files['file']
        file.save('uploaded_file.txt')
        # processing of rohit''s code and sending to youtube
        makeVideo('uploaded_file.txt')
        video_id = uploadVideo()
        os.remove('uploaded_file.txt')

        return {"status": "Ok!","videoid":video_id}, 200

app.run()