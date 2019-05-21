
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import mars_scraping

#------------------------------------------------------------------------
# Flask Setup #
#------------------------------------------------------------------------

app = Flask(__name__)

#-----------------------------------------------------------------------
# local Mongo DB Connection
#-----------------------------------------------------------------------

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn, ConnectTimeoutMS=30000)
db = client.mars_db
coll = db.mars_data_collection


@app.route("/")
def index():
    mars_mission_data = coll.find_one()

    return render_template("index.html", mars_mission_data=mars_mission_data)


@app.route("/scrape")
def scrape():
    mars_mission_data = mars_scraping.mars_scrape()

    coll.update_many({"id": 1}, {"$set": mars_mission_data}, upsert=True)

    #return redirect("http://localhost:5000", code=302)
    return "Scraping Successful"


if __name__ == "__main__":
    app.run(debug=True)
