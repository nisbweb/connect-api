import pymongo
import os
import uuid
import datetime

mongo_token = os.getenv("MONGO")

client = pymongo.MongoClient(mongo_token)
db = client.connectdb


def get_topics():
    topics = []
    for e in db.topics.find():
        e.pop("_id")
        topics.append(e)
    return topics


def get_topic(id):
    topic = db.topics.find_one({"id": id})
    if topic:
        topic.pop("_id")
    return topic


def get_topic_by_name(name):
    topic = db.topics.find_one({"name": name})
    if topic:
        topic.pop("_id")
    return topic


def add_topic(topic_dict):
    e_id = uuid.uuid4().hex
    topic_dict["id"] = e_id
    topic_dict["created_at"] = datetime.datetime.now()
    topic_dict["updated_at"] = datetime.datetime.now()
    db.topics.insert_one(topic_dict)
    return e_id


def delete_topic(id):
    return db.topics.delete_one({"id": id})


def update_topic(topic_dict):
    id = topic_dict["id"]
    topic_dict["updated_at"] = datetime.datetime.now()
    return db.topics.update_one({"id": id}, {"$set": topic_dict})


# -------------------------------------------------------------
# POSTS

def get_posts(after=None):
    posts = []
    for e in db.posts.find():
        e.pop("_id")
        posts.append(e)
    return posts


def get_posts_by_topic(topicID):
    posts = []
    for e in db.posts.find({"topic": topicID}):
        e.pop("_id")
        posts.append(e)
    return posts


def get_post(id):
    post = db.posts.find_one({"id": id})
    if post:
        post.pop("_id")
    return post


def add_post(post_dict):
    e_id = uuid.uuid4().hex
    post_dict["id"] = e_id
    post_dict["created_at"] = datetime.datetime.now()
    post_dict["updated_at"] = datetime.datetime.now()
    db.posts.insert_one(post_dict)
    return e_id


def delete_post(id):
    return db.posts.delete_one({"id": id})


def update_post(post_dict):
    id = post_dict["id"]
    return db.posts.update_one({"id": id}, {"$set": post_dict})


# -------------------------------------------------------------
# COMMENTS

def get_comments(post_id=None, reply_of=None):
    comments = []
    query = {}
    if post_id:
        query["post_id"] = post_id
    if reply_of:
        query["reply_of"] = reply_of
    for e in db.comments.find(query):
        e.pop("_id")
        comments.append(e)
    return comments


def get_comment(id):
    comment = db.comments.find_one({"id": id})
    comment.pop("_id")
    return comment


def add_comment(comment_dict):
    e_id = uuid.uuid4().hex
    comment_dict["id"] = e_id
    comment_dict["created_at"] = datetime.datetime.now()
    comment_dict["updated_at"] = datetime.datetime.now()
    db.comments.insert_one(comment_dict)
    return e_id


def delete_comment(id):
    return db.comments.delete_one({"id": id})


def update_comment(comment_dict):
    id = comment_dict["id"]
    return db.comments.find_one_and_replace({"id": id}, comment_dict)


if __name__ == "__main__":
    t = add_topic({
        "name": "nisb notifications",
        "created_by": "nisbweb@gmail.com",
        "created_at": datetime.datetime.now().isoformat(),
        "updated_at": datetime.datetime.now().isoformat()
    })



    print(t)

    t = get_topic(t)
    print(t)

    ts = get_topics()
    print(ts)

    print(delete_topic(t))

    ts = get_topics()
    print(ts)
