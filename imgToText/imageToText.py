from google.cloud import vision
import io
import os
# import argparse

# seems to able to read in jpg fine
image_path = "test_r1.jpg"

# get text from local image file
def detect_text(path):
    
    # setup credential and create a vision client
    # TODO: make sure to update this to match the path of gcp credential file
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'hackumass2020-e3653d7fe8eb.json'
    
    client = vision.ImageAnnotatorClient()
    
    # path to image file
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    # pass image to be readable by the viison client, base-64 encoded form data
    image = vision.Image(content=content)
    # the response contain detection information of each letter and its xy positions in the image
    # returns a nested dict. from blocks -> words -> symbols(characters).
    # along with annotated text.
    response = client.text_detection(image=image)
    
    # display the text detected. 
    print("Texts:")
    # TODO: result doesn't group the text in the same line right.  Seems to be issue with how space or tab-space being view as line-break
    texts = response.text_annotations  # dict of the whole text + each words in text
    # print(texts)
    for text in texts:
        print('\n"{}"'.format(text.description))

        # to get the xy position for the given word
        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in text.bounding_poly.vertices])

        # print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))




detect_text(image_path)

# if __name__=="__main__":
#     parser 