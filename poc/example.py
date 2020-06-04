from os import environ
from google.cloud import vision
from google.cloud.vision import types

environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"google-service-key.json"

client = vision.ImageAnnotatorClient()

image = vision.types.Image()
image.source.image_uri = "https://www.wolkdirekt.com/blaetter/600/111142.jpg"

response = client.text_detection(image=image)

texts = response.text_annotations
print(texts)
