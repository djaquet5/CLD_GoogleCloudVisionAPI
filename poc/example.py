#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import environ
from argparse import ArgumentParser
from distutils.util import strtobool

from google.cloud import vision
from google.cloud.vision import types


"""
A small demo program meant to show some possible operations using Google Vision API.
1. Read an image from a URL and return the text written in the image and its language.
"""


def text_from_url(url):
    """
    Read an image from a URL and return the text written in the image and its language.
    :param url: The URL of the image to read.
    :returns: A tuple (language, text read) for the image in question.
    """
    client = vision.ImageAnnotatorClient()

    image = vision.types.Image()
    image.source.image_uri = url

    response = client.text_detection(image=image)

    texts = response.text_annotations

    return texts[0].locale, texts[0].description



def main():
    """Main function for the program"""
    environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"google-service-key.json"

    # Read program arguments
    parser = ArgumentParser(description="OCR application using Google Vision API")
    parser.add_argument("url", help="The URL of the image to read")

    args = parser.parse_args()
    URL = args.url

    # Read text using Google Vision API
    locale, text = text_from_url(URL)

    # Print results
    print("The detected language is:", locale)
    print("The read text is:")
    print("-----------------")
    print(text)


if __name__ == "__main__":
    main()
