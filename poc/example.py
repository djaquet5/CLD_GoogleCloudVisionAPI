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
2. Read an image from the disk and return the text written in the image and its language.
"""


def text_detection(image):
    """Actually executes the request to the API"""
    client = vision.ImageAnnotatorClient()

    response = client.text_detection(image=image)
    data = response.text_annotations

    return data[0].locale, data[0].description


def text_from_url(url):
    """
    Read an image from a URL and return the text written in the image and its language.
    :param url: The URL of the image to read.
    :returns: A tuple (language, text read) for the image in question.
    """
    image = types.Image()
    image.source.image_uri = url

    return text_detection(image)


def text_from_local(filepath):
    """
    Read an image from disk and return the text written in the image and its language.
    :param filepath: The path on disk of the image to read.
    :returns: A tuple (language, text read) for the image in question.
    """
    with open(filepath, 'rb') as file:
        content = file.read()
    image = types.Image(content=content)

    return text_detection(image)


def main():
    """Main function for the program"""
    environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"google-service-key.json"

    # Read program arguments
    parser = ArgumentParser(description="OCR application using Google Vision API")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", help="The URL of the image to read")
    group.add_argument("--filepath", help="The path on disk of the image to read")

    args = parser.parse_args()
    URL = args.url
    FILEPATH = args.filepath

    # Read text using Google Vision API
    if URL is not None:
        locale, text = text_from_url(URL)

    if FILEPATH is not None:
        locale, text = text_from_local(FILEPATH)

    # Print results
    print("----------------------------")
    print("The detected language is:", locale)
    print("----------------------------")
    print("The read text is:\n")
    print(text + "----------------------------")


if __name__ == "__main__":
    main()
