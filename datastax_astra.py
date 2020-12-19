# connection to datastax astra database

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {"secure_connect_bundle": "secure-connect-respend.zip"}
auth_provider = PlainTextAuthProvider("ReSpend", "respend!")
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect("ReSpend")
# session.execute("USE ReSpend;")


def connect():
    row = session.execute("select release_version from system.local").one()
    if row:
        print(row[0])
    else:
        print("An error occurred.")


# receipts: stores images of user's receipts as blobs and assigns each one a uniqueid (timestamp)
#     receipt blob,
#     id timestamp,
#     vendor text,
#     total_spent double,
#     user_id text,
#     PRIMARY KEY (id)
def insert_receipt(img, id, vendor, total_spent, user_id):
    session.execute(
        """
        INSERT INTO receipts (receipt, id, vendor, total_spent)
        VALUES (%s, %s, %s, %s)
        """,
        (img, id, vendor, total_spent, user_id),
    )


# food_items: stores food item and its corresponding info
#     item text,
#     category text,
#     total_spent double,
#     units double,
#     receipt_id timestamp,
#     user_id text,
#     PRIMARY KEY (category)
def insert_food(item, category, total_spent, units, receipt_id, user_id):
    session.execute(
        """
        INSERT INTO food_items (item, category, total_spent, units, receipt_id)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (item, category, total_spent, units, receipt_id, user_id),
    )


# users: stores user information
#     first text,
#     last text,
#     profile_pic text,
#     user_id text,
#     PRIMARY KEY (user_id)
# );
def insert_user(id, first_name, last_name, profile_pic):
    session.execute(
        """
        INSERT INTO users (user_id, first, last, profile_pic)
        VALUES (%s, %s, %s, %s)
        IF NOT EXISTS
        """,
        (id, first_name, last_name, profile_pic),
    )