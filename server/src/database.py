import os
import requests
from pymongo import MongoClient, DESCENDING


# Connect to mongo database
CLIENT = MongoClient(f"{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}")
DB = CLIENT[os.environ.get("DB_NAME")]


def initialize_collection_posts():
    """
    The function is responsible for inserting all posts from external API into database.
    """
    posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    DB.posts.drop()
    DB.posts.insert_many(posts)


def get_post(id: int):
    """
    The function is responsible for returning post from database by its id.
    """
    global DB
    post = DB.posts.find_one({"id": id}, {"_id": 0})
    return post


def get_posts():
    """
    The function is responsible for returning all posts from database.
    """
    global DB
    posts = {
        "posts": list(DB.posts.find({}, {"_id": 0}))
    }
    return posts


def delete_post(id: int):
    """
    The function is responsible for deleting post from database by its id.
    """
    global DB
    DB.posts.delete_one({"id": id})


def update_post(id: int, title: str, body: str):
    """
    The function is responsible for updating post's title and body by its id.
    """
    global DB
    DB.posts.update({"id": id}, {"$set": {"title": title, "body": body}})


def get_id_max():
    """
    The function is responsible for returning maximum post id.
    """
    # https://stackoverflow.com/questions/32076382/mongodb-how-to-get-max-value-from-collections
    id_max = list(DB.posts.find({}, {"id": 1, "_id": 0}).sort("id", DESCENDING).limit(1))[0]["id"]
    return id_max


def create_post(userId: int, title: str, body: str):
    """
    The function is responsible for inserting post into database.
    """
    global DB
    id_max = get_id_max()
    post = {
        "id": id_max + 1,
        "userId": userId,
        "title": title,
        "body": body,
    }
    DB.posts.insert_one(post)
