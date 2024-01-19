import sys, os, datetime, uuid
from lesionDetection.pipeline.training_pipeline import TrainPipeline
from lesionDetection.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template, Response, send_from_directory
from flask_cors import CORS, cross_origin
from lesionDetection.constant.application import APP_HOST, APP_PORT

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        pass

    def generate_unique_filename(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        unique_id = str(uuid.uuid4())[:8]  # Shortened UUID
        return f"inputImage_{timestamp}_{unique_id}.jpg"

@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successfull!!" 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        input_filename = clApp.generate_unique_filename()
        decodeImage(image, input_filename)

        # Ensuring the output directory exists
        output_dir = "runs/detect/predict"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        os.system(f"yolo task=detect mode=predict model=best.pt conf=0.25 source=data/{input_filename} save=true project=./runs/detect name=predict")
        
        output_image_path = os.path.join(output_dir, "predict", input_filename)

        if not os.path.isfile(output_image_path):
            raise FileNotFoundError("Output image not found after detection.")

        opencodedbase64 = encodeImageIntoBase64(output_image_path)
        result = {"image": opencodedbase64.decode('utf-8')}
        os.system("rm -rf runs")

    except ValueError as val:
        print(val)
        return Response("Value not found inside json data")
    except KeyError:
        return Response("Key value error: incorrect key passed")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return Response("File not found error: " + str(fnf_error))
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)

@app.route('/output-images/<filename>')
def output_images(filename):
    return send_from_directory('runs/detect/predict', filename)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT)
