import sys, os, datetime, uuid
from lesionDetection.pipeline.training_pipeline import TrainPipeline
from lesionDetection.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template, Response, send_from_directory, url_for
from flask_cors import CORS, cross_origin
from lesionDetection.constant.application import APP_HOST, APP_PORT


app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"

@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successfull!!" 


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        os.chdir(os.getcwd())
        os.system(f"yolo task=detect mode=predict model=best.pt conf=0.25 source=data/inputImage.jpg save=true project={os.getcwd()} exist_ok=true")

        opencodedbase64 = encodeImageIntoBase64("predict/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}
        os.system("rm -rf runs")

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)



if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT)
    app.run(host='0.0.0.0', port=80) #for AZURE



