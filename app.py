from flask import Flask, render_template, request
from keras.applications import ResNet50
import cv2
import numpy as np
import pandas as pd
import datetime
import sys

app = Flask(__name__)

resnet = ResNet50(weights='imagenet',input_shape=(224,224,3),pooling='avg')
print("+"*50, "Model is loaded")

labels_list = pd.read_csv("labels.txt", sep="\r\n").values


@app.route('/')
def index():
	return render_template("index.html", data="hey")


@app.route("/prediction", methods=["POST"])
def prediction():

	start_time=datetime.datetime.now()

	img = request.files['img']

	img.save("img.jpg")

	image = cv2.imread("img.jpg")

	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	image = cv2.resize(image, (224,224))

	image = np.reshape(image, (1,224,224,3))

	prediction = resnet.predict(image)

	prediction = np.argmax(pred)

	prediction = labels_list[prediction]

	end_time=datetime.datetime.now()

	time_consumed=end_time-start_time

	print("time taken"+ str(time_consumed) , file=sys.stdout)

	return render_template("prediction.html", data=pred , time=time_consumed)


if __name__ == "__main__":
	app.run(debug=True)
