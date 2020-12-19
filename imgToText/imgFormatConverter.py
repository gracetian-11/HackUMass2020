from PIL import Image
import base64
import img2pdf

# convert image file format to match what we need, PDF, TIFF or GIF
class imgFormatConverter:
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

    def to_pdf(self):
        print("input image format: {}".format(self.input.format))
        self.output = self.input.convert('RGB')
         
        self.output.save('{}.pdf'.format(self.input.filename))
    
    # def to_tiff(self):

converter = imgFormatConverter()
converter.set_input_path('test_r1.jpg')
converter.to_pdf()
        
