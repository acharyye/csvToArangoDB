import os
from arango import ArangoClient
import csv

# ArangoDB configuration
DB_HOST = "YOURHOST"
DB_DATABASE = "DATABASENAME"
DB_USERNAME = "USERNAME"
DB_PASSWORD = "PASSWORD"

# Initialize ArangoDB client and database connection
client = ArangoClient(hosts=[DB_HOST])
db = client.db(DB_DATABASE, username=DB_USERNAME, password=DB_PASSWORD)

# Specify the path to your CSV file
csv_file = 'YOUR DATA.CSV'

# Specify the collection where you want to insert the data
collection_name = 'COLLECTION NAME'
collection = db.collection(collection_name)

# Open the CSV file and insert its contents into the collection
with open(csv_file, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        # Insert each row from the CSV as a document in the collection
        collection.insert(row)
