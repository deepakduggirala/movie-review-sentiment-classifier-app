from flask import Flask, request, jsonify
from build_library.utils import normalize_corpus
import joblib
import numpy as np
import os
DECISION_THRESHOLD = 0.5

def load_model():
  return joblib.load('tf-idf-linear-regression.pkl')

def get_reponse_body(proba):
  neg_proba, pos_proba = proba[0]
  return {
      "proba":{
        'negative': neg_proba,
        'positive': pos_proba
        },
      'class': 'positive' if pos_proba > DECISION_THRESHOLD else 'negative'
  }

# test_review = "N.T.R, Savitri, A.N.R in Mayabazar acted brilliantly. Dialogues look fresh!!!. Music and lyrics are super."
pipeline = load_model()
# print(pipeline.predict_proba(np.array([test_review])))

### SETTING UP FLASK APP AND FLAKS ENDPOINTS ###
# Create the flaks App
app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

# Define an endpoint for calling the predict function based on your ml library/framework
@app.route("/predict", methods=["GET","POST"])
def predict():
  body = request.json
  if 'review' in body:
    review = body['review']
    print(review)
    proba = pipeline.predict_proba(np.array([review]))
    return jsonify(get_reponse_body(proba))

if __name__ == '__main__':
  print('running main in app.py')
  app.run(debug=True, host= '0.0.0.0', port=int(os.environ.get('PORT', 8080)))