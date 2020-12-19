from google.cloud import vision
import io
import os

# import argparse

# seems to able to read in jpg fine
image_path = "test_r1.jpg" # to work locally, need to look at how python access files in mobile devices.


class ImageToText:
    def __init__(self, input_img_path=None, input_img_json=None, local_file=False):
    '''
    takes takes in image(s) and detect text in it.
    input:
    input_img_path = the local file path to the image, default is None 
    input_img_json = the JSON file that is pass as JSON from the database, default is None
    local_file = whether or not the file we want to get text from is stored locally or remotely.  Default to be True.
    '''
        self.image = None
        self.client = None
        if local_file:
            self.set_image_local(input_img_path)
        else:
            self.set_image(input_img_json)
        self.texts = []
        self.set_client()

    def get_image(self):
        return self.image

    # for local image file
    def set_image_local(self, path):
        # path to image file
        try:
            with io.open(path, "rb") as image_file:
                content = image_file.read()
        except FileNotFoundError as fnf_error:
            print(fnf_error)
        # pass image to be readable by the api
        self.image = vision.Image(content=content)
    
    # set image file from the json file
    def set_image_json(self, json):
        try:
            image_data = json.image.content
        except:
            print("unable get the image from JSON.")
        self.image = vision.Image(content=image_data)

    def set_client(self):
        # setup credential and create a vision client
        # TODO: make sure to update this to match the path of gcp credential file
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "hackumass2020-e3653d7fe8eb.json"
        self.client = vision.ImageAnnotatorClient()

    # detect text from image
    def detect_text(self):

        # more general detection of each letter and its xy positions in the image
        # The JSON including the entire extracted string, as well as individual words, and their bounding boxes.
        # response = self.client.text_detection(image=image) #uncomment to use

        # ====== this seems to work better with receipts, since it recognize line and spacing better.
        # Optimized for dense text and documents.
        # The JSON includes page, block, paragraph, word, and break information.
        response = self.client.document_text_detection(image=self.image)  # uncomment to use

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

text_parse = image_to_text(input_img_path = image_path, local_file=True)
=======
text_parse.detect_text()
text_parse.get_text_all()

# if __name__=="__main__":
#     parser
