from google.cloud import vision
import io
import os

# import argparse

# seems to able to read in jpg fine
image_path = "test_r1.jpg"


class ImageToText:
    def __init__(self, input_img_path=None, input_img=None, local_file=True):
        self.image = None
        if local_file:
            self.set_image_local(input_img_path)
        else:
            self.set_image(input_img)
        self.texts = []
        self.set_client()

    def get_image(self):
        return self.image

    # for local image file
    def set_image_local(self, path):
        # path to image file
        with io.open(path, "rb") as image_file:
            content = image_file.read()
        # pass image to be readable by the viison client, base-64 encoded form data
        image = vision.Image(content=content)
        self.image = image

    # for directly loading image data
    def set_image_uri(self, img_uri):
        self.image = vision.Image()
        self.image.source.image_uri = img_uri

    # set image to the base-64 string img_b64
    def set_image_base64(self, img_b64: str) -> None:
        """TODO: yeah this."""

    def set_client(self):
        # setup credential and create a vision client
        # TODO: make sure to update this to match the path of gcp credential file
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "hackumass2020-e3653d7fe8eb.json"

        self.client = vision.ImageAnnotatorClient()

    # detect text from image
    def detect_text(self):

        # more general detection of each letter and its xy positions in the image
        # The JSON including the entire extracted string, as well as individual words, and their bounding boxes.
        # response = client.text_detection(image=image) #uncomment to use

        # ====== this seems to work better with receipts, since it recognize line and spacing better.
        # Optimized for dense text and documents.
        # The JSON includes page, block, paragraph, word, and break information.
        response = self.client.document_text_detection(
            image=self.image
        )  # uncomment to use

        # display the text detected.
        # print("Texts:")
        texts = response.text_annotations  # dict of the whole text + each words in text
        # print(texts)
        for text in texts:
            # print('\n"{}"'.format(text.description))
            self.texts.append(text.description)

            # to get the xy position for the given word if uses client.text_detection()
            # vertices = (['({},{})'.format(vertex.x, vertex.y)
            #             for vertex in text.bounding_poly.vertices])

            # print('bounds: {}'.format(','.join(vertices)))
        # print(self.texts)

        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(
                    response.error.message
                )
            )

    def get_text_all(self):
        """
        get all the text that has been detected from the image
        return:
        text = list if text parsed per line
        """
        # get the whole string from self.texts
        bulk_text = self.texts[0]
        print(bulk_text)
        linetext = bulk_text.splitlines()
        print(linetext)
        return linetext

    # not sure if needed yet
    def get_text_single(self):
        pass


if __name__ == "__main__":
    text_parse = ImageToText(input_img_path=image_path, local_file=True)
    text_parse.detect_text()
    text_parse.get_text_all()
