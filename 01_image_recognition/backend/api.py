from flask import request, Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from PIL import Image

from recognition import image_recognition


# アプリの設定
app = Flask(__name__)
CORS(app)
api = Api(app)


# APIの作成
class ImageRecognition(Resource):

    def post(self):
        try:
            
            image = request.files['image']
            image_pil = Image.open(image).convert('RGB')
            score, category_name = image_recognition(image_pil)

            response = {
                'status': "SUCCESS",
                'result': f"{category_name}: {100 * score:.1f}%",
                }
        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }
            
        return response


if __name__ == '__main__':

    api.add_resource(ImageRecognition, '/api/image_recognition')
    app.run(debug=True)