# connection to datastax astra database

# food_items stores food item and its corresponding info
# food_items:
#     item text,
#     category text,
#     price double,
#     units double,
#     receipt_id int,
#     summary text,
#     PRIMARY KEY (category)

# receipts stores images of user's receipts as blobs and assigns each one a uniqueid
# receipts:
#     receipt blob,
#     id int,
#     PRIMARY KEY (id)

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


def connect():
    cloud_config = {"secure_connect_bundle": "secure-connect-respend.zip"}
    auth_provider = PlainTextAuthProvider("ReSpend", "respend!")
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()

    row = session.execute("select release_version from system.local").one()
    if row:
        print(row[0])
    else:
        print("An error occurred.")

    return session