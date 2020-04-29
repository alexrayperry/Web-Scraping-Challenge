# Import Dependencies

from flask import Flask, render_template

import pymongo

# Set up flask app

app = Flask(__name__)

# Set up MongoDB Connection

conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance. 

client = pymongo.MongoClient(conn)

# Example of connecting to db for flask

db = client.store_inventory
produce = db.produce

# Connect to a database. Will create one if one is not available.

db = client.database_name

# Drops collection if available to remove duplicates

db.collection_name.drop()

# Creates a collection in the database and inserts documents

db.collection_name.insert_many(
    [
        {
            'player':"Jessica",
            'position':"Point Guard"
        },
        {
            'player': "mark",
            'position':'bench'
        }
    ]
)

# Set Variables

# Create route that renders index.html

@app.route("/")
def index():
    # passing in list of dictionaries from finding collection in mongo
    teams = list.(db.collection_name.find())

    # passing in dictionary variable
    dictionary = [{"name": "Fido", "type":"Lab",}
                    "name": "rex", "Type": "Collie"}]

    # write a statement that finds all the items in the db and sets it to a variable.
    inventory = list(produce.find())

    return render_template("index.html", dict=dictionary OR teams=teams OR inventory=inventory)


if __name__ == "__main__":
    app.run(debug=True)