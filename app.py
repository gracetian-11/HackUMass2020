from flask import Flask
from datastax_astra.py import connect, insert_receipt, insert_food
import datetime

app = Flask(__name__)

@app.route('/')
def ReSpend(img):
    ## CONNECT TO DATABASE ##
    connect()

    ## GET TEXT FROM IMAGE ##

    ## STORE INFORMATION INTO DATABASE ##

    # receipt_id: current time
    receipt_id = datetime.datetime.now()

    # convert image to blob
    img_blob = 0

    # filter text for following info: vendor, total_spent, food items and corresponding prices
    vendor = ""
    total_spent = ""
    foods = {}
    # get category of each food
    category = ""
    units = 0
    for food in foods:
        total_spent = foods[food]
        insert_food (food, category, total_spent, units, receipt_id)

    insert_receipt (img_blob, id, vendor, total_spent)

    ## RETURN REQUESTED INFO ##

if __name__ == '__main__':
    app.run()