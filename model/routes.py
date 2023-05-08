from flask import make_response, request, jsonify
from model import app, baseline, utils, clustering
import json
import numpy as np


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def predict():
    if not request.data: return make_response('Missing data.', 403)
    # decode data to json
    content = request.data.decode('utf-8')
    content = json.loads(content)
    if not utils.check_data_format(content):
            return make_response('Wrong data format.', 403)
    # transform to list input and predict
    X = list(content.values())
    preds = baseline.forward(X)
    res = json.dumps({"data": int(preds)})
    return make_response(res, 200)


@app.route('/cluster', methods=['POST'])
def cluster():
    if not request.data: return make_response('Missing data.', 403)
    # decode data to json
    content = request.data.decode('utf-8')
    content = json.loads(content)
    if not utils.check_data_format4PCA(content):
            return make_response('Wrong data format.', 403)
    # array = np.asarray(content['logs'])
    # # transform to list input and predict
    X = content['logs']
    res = json.dumps({"data": clustering.fit(X)})
    return make_response(res, 200)

