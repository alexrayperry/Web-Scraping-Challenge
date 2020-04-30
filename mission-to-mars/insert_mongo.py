import pymongo
import scrape_mars


# # app.config["MONGO_URI"] = 'mongodb://localhost:27017'

conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance. 

client = pymongo.MongoClient(conn)

# Will create a database if one isn't already created
db = client.mars

#Creates a collection in the database
mars_collection = db.mars_collection

# Drops collection if available to remove duplicates

db.mars_collection.drop()

mars_data = scrape_mars.scrape()

# Creates a collection in the database and inserts documents

db.mars_collection.insert_many([mars_data])

# collection = db.mars_collection

# results = collection.find({"news_title":"news_title"})

# for result in results:
#     print(result)