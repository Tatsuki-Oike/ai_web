from flask import request, Flask, send_file
from flask_restful import Resource, Api
from flask_cors import CORS
from PIL import Image, ImageOps
import tempfile

from segmentation import segmentation


# アプリの設定
app = Flask(__name__)
CORS(app)
api = Api(app)


# APIの作成
class Segmentation(Resource):

    def post(self):
        try:
            # 画像のデータ取得
            image = request.files['image']
            image_pil = Image.open(image).convert('RGB')
            resized_image = ImageOps.pad(image_pil, (224, 224), method=0, color=0)
            result_image = segmentation(resized_image)

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

    api.add_resource(Segmentation, '/api/segmentation')
    app.run(debug=True)