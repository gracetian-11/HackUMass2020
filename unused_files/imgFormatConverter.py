from PIL import Image
import base64
import os

# convert image file format to match what we need, PDF, TIFF or GIF
class imgFormatConverter:
    '''
    Use getter and setter to set input and output
    '''
    def __init__(self):
        self.input = None
        self.output = None

    # set the input data from file path
    def set_input_path(self, input):
        image = Image.open(input)
        self.input = image
        
    # set the input data from base64string in JSON file
    def set_input_b64(self, input):
        content = input.images.content
        self.input = base64.decodebytes(content)

    def get_input(self):
        return self.input

    def get_output(self):
        return self.output

    def to_pdf(self):
        print("input image format: {}".format(self.input.format))
        pdf = self.input.convert('RGB')
         
        pdf.save('{}.pdf'.format(self.input.filename.split(".")[0]))
        
        pdf = open('{}.pdf'.format(self.input.filename.split(".")[0]))
        self.output = pdf
        pdf.close()
        os.remove('{}.pdf'.format(self.input.filename.split(".")[0]))
    
    # def to_tiff(self):

converter = imgFormatConverter()
converter.set_input_path('test_r1.jpg')
converter.to_pdf()
        
