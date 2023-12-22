from flask import request, Flask, send_file
from flask_restful import Resource, Api
from flask_cors import CORS
import tempfile
import json

from generation import image_generation


# アプリの設定
app = Flask(__name__)
CORS(app)
api = Api(app)


# APIの作成
class ImageGeneration(Resource):

    def post(self):
        try:

            data = json.loads(request.data)
            prompt = data["prompt"]
            steps = data["steps"]
            size = data["size"]
            result_image = image_generation(prompt, steps, size)

            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
            result_image.save(temp_file.name, format="JPEG")

            return send_file(temp_file.name,
                             mimetype='image/jpeg', 
                             as_attachment=True, 
                             download_name='image.jpg')
        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }
            return response


if __name__ == '__main__':

    api.add_resource(ImageGeneration, '/api/image_generation')
    app.run(debug=True)