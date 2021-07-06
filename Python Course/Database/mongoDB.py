from pymongo import MongoClient
from auth import username,password
import string
import datetime
from pprint import pprint

client = MongoClient("mongodb://"+username+":"+password+"@ds263740.mlab.com:63740/acadview")
db = client['acadview']
collection = db.testdb

single_post = {"name":"Satyam","text":"My first document","tags":["mongodb","python","pymongo"]}
multiple_post = [{"name":"Mrinal","text":"Hello","tags":["Node","Mongoose","Mongodb"]},{"name":"Abhishek","text":"testing things","tags":["one","two","three"]}]

'''for i in range(0,26):
    post[string.ascii_lowercase[i]] = i
'''

def insert_single():
    post_id = collection.insert_one(single_post).inserted_id
def insert_multiple():
    post_id = collection.insert_many(multiple_post).inserted_id
def print_previous():
    pprint(collection.find_one())
def fetch_all():
    for post in collection.find():
        pprint.pprint(post)
def find_element():
    pprint(collection.find_one({"name":"Satyam"}))
try:
   connect_to_database()
##    insert_single()
##    insert_multiple()
##    print_previous()
    # find_element()
except Exception as e:
    print(e)
finally:
    client.close()
