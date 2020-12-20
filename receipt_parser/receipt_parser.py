import os
from google.cloud import documentai_v1beta3 as documentai
# https://us-documentai.googleapis.com/v1beta3/projects/457995383238/locations/us/processors/3f0d1ab7f53ab145:process # hackumass2020 project
# https://us-documentai.googleapis.com/v1beta3/projects/251887149747/locations/us/processors/b59cbc5119e37d4e #respend project
project_id= '457995383238'
location = 'us' # Format is 'us' or 'eu'
processor_id = '3f0d1ab7f53ab145' # Create processor in Cloud Console
file_path = '..\imgToText\\test_r1.pdf'

def process_document_sample(
    project_id: str, location: str, processor_id: str, file_path: str
):

    # Instantiates a client
    client = set_client()

    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
    # You must create new processors in the Cloud Console first
 
    name = "projects/{}/locations/{}/processors/{}".format(project_id, location, processor_id)

    with open(file_path, "rb") as image:
        image_content = image.read()

    # Read the file into memory
    document = {"content": image_content, "mime_type": "application/pdf"}

    # Configure the process request
    request = {"name": name, "document": document}

    # Recognizes text entities in the PDF document
    result = client.process_document(request=request)

    document = result.document

    print("Document processing complete.")

    # For a full list of Document object attributes, please reference this page: https://googleapis.dev/python/documentai/latest/_modules/google/cloud/documentai_v1beta3/types/document.html#Document

    document_pages = document.pages

    # Read the text recognition output from the processor
    print("The document contains the following paragraphs:")
    for page in document_pages:
        paragraphs = page.paragraphs
        for paragraph in paragraphs:
            paragraph_text = get_text(paragraph.layout, document)
            print(f"Paragraph text: {paragraph_text}")


# Extract shards from the text field
def get_text(doc_element: dict, document: dict):
    """
    Document AI identifies form fields by their offsets
    in document text. This function converts offsets
    to text snippets.
    """
    response = ""
    # If a text segment spans several lines, it will
    # be stored in different text segments.
    for segment in doc_element.text_anchor.text_segments:
        start_index = (
            int(segment.start_index)
            if segment in doc_element.text_anchor.text_segments
            else 0
        )
        end_index = int(segment.end_index)
        response += document.text[start_index:end_index]
    return response


def set_client():
    # setup credential and create a vision client
    # TODO: make sure to update this to match the path of gcp credential file
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "..\imgToText\hackumass2020-e3653d7fe8eb.json"

    client = documentai.DocumentProcessorServiceClient()
    return client

if __name__ == "__main__":
    process_document_sample(project_id, location, processor_id, file_path)