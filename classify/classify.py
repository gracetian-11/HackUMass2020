import argparse
import io
import json
import os

from google.cloud import language_v1
import numpy
import six

def classify(text, verbose=True):
    """Classify the input text into categories. """

    language_client = language_v1.LanguageServiceClient()

    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )
    response = language_client.classify_text(request={'document': document})
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print(u"=" * 20)
            print(u"{:<16}: {}".format("category", category.name))
            print(u"{:<16}: {}".format("confidence", category.confidence))
    print("HELLO" + result)
    return result

if __name__ == "__main__":
    classify("""
    Walmart
    Save money. Live better.
    (526) - 237-0154
    MANAGER TONY ESCARIO
    DEATH VALLEY, OU
    ST: 1088 OP# 00009045 TE# 45 TR# 08570
    AIDS
    002840001408 51.74 X
    GAMECOM X40 0074100514919 2.50 X
    PEPSI 001200080994 4,38 R
    SUBTOTAL 12.84
    TAX 1 8.875
    5,20
    TOTAL
    63.82
    DEBIT TEND 63.82
    EFT DEBIT PAY FROM PRIMARY
    ACOUNT # olek Holok Selek 7428 S
    APPROVAL # 001824
    REF # 224500487251
    TERMINAL # 52084660
    09/01/12 14:16:00
    CHANGE DE 0.00
    # ITEMS SOLD 3
    TCH 7884 0145 2857 6283 1227
    "Like" Walmart on Facebook
    www.facebook.com/Walmart
    09/01/12 14:16:00
    """)