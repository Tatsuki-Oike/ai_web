from flask import request, Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import json

from translation import translate


# アプリの設定
app = Flask(__name__)
CORS(app)
api = Api(app)


# APIの作成
class Translation(Resource):

    def post(self):
        try:
            
            data = json.loads(request.data)
            input_text = data["input_text"]
            output_text = translate(input_text)

            response = {
                "status": "SUCCESS",
                "output_text": output_text
                }
        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }
            
        return response


if __name__ == '__main__':

    api.add_resource(Translation, '/api/translation')
    app.run(debug=True)