# connection to datastax astra database

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {"secure_connect_bundle": "secure-connect-respend.zip"}
auth_provider = PlainTextAuthProvider("ReSpend", "respend!")
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()


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
#     PRIMARY KEY (id)
def insert_receipt(img, id, vendor, total_spent):
    session.execute(
        """
    INSERT INTO receipts (receipt, id, vendor, total_spent)
    VALUES (%s, %s, %s, %s)
    """,
        (img, id, vendor, total_spent),
    )


# food_items: stores food item and its corresponding info
#     item text,
#     category text,
#     total_spent double,
#     units double,
#     receipt_id timestamp,
#     PRIMARY KEY (category)
def insert_food(item, category, total_spent, units, receipt_id):
    session.execute(
        """
    INSERT INTO food_items (item, category, total_spent, units, receipt_id)
    VALUES (%s, %s, %s, %s, %s)
    """,
        (item, category, total_spent, units, receipt_id),
    )


# user_info: stores user information
#     id          int,
#     first_name  text,
#     last_name   text,
#     profile_pic text,
#     PRIMARY KEY (category)
def insert_user(id, first_name, last_name, profile_pic):
    session.execute(
        """
    INSERT INTO food_items (item, category, total_spent, units, receipt_id)
    VALUES (%s, %s, %s, %s, %s)
    """,
        (item, category, total_spent, units, receipt_id),
    )
