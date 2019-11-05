import sys, json, csv, shutil, os
from google.cloud import automl_v1beta1 as automl
from google.cloud.automl_v1beta1.proto import service_pb2
from google.oauth2 import service_account
from flask import Flask

datos = sys.argv[1]

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='./stunning-hue-255412-48f860da88af.json'

def get_prediction(content, project_id, model_id):
  compute_region = 'us-central1'
  automl_client = automl.AutoMlClient()
  prediction_client = automl.PredictionServiceClient()
  name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
  model_full_id = automl_client.model_path(project_id,compute_region ,model_id)
  payload = {'text_snippet': {'content': content, 'mime_type': 'text/plain'}}
  params = {}
  request = prediction_client.predict(name, payload, params)
  return request  # waits till request is returned


# Desarrollo de una aplicacion en Xamarin para gestion de ingredientes en un restaurant
output = (get_prediction(datos, "stunning-hue-255412",  "TCN4845958667344202348"))
print(output)
sys.stdout.flush()