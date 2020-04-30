# Import Dependencies

from flask import Flask, render_template, redirect

from flask_pymongo import PyMongo

import scrape_mars

# Set up flask app

app = Flask(__name__)

# Set up MongoDB Connection

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")

# Create route that renders index.html

@app.route("/")
def index():
    
    mars_info = mongo.db.mars_collection.find()

    return render_template("index.html", info=mars_info)

@app.route("/scrape")
def scrape():
    
    mars_data = scrape_mars.scrape()

    mongo.db.mars_collection.update({}, mars_data, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

