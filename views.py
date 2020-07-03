import connexion
import db


def get_error(msg):
    return {
        "status": "error",
        "error": msg
    }


def add_topic(body):  # noqa: E501
    """Add a new topic

     # noqa: E501

    :param body: Topic details to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()
        if set(["name", "created_by"]).issubset(list(body.keys())):
            print(db.get_topic_by_name(name=body["name"]))
            if not db.get_topic_by_name(name=body["name"]):
                return {
                    "id": db.add_topic(body)
                }
            else:
                return get_error("Topic already exists"), 409
    return get_error("Invalid Input"), 400


def delete_topic(topicID):  # noqa: E501
    """delete a topic and associated resources

     # noqa: E501

    :param topicID: ID of topic
    :type topicID: str

    :rtype: None
    """
    if db.delete_topic(topicID).deleted_count == 1:
        return {
            "status": "ok"
        }
    return get_error("could not delete")


def get_topic(topicID):  # noqa: E501
    """get a topic by ID

     # noqa: E501

    :param topicID: ID of topic
    :type topicID: str

    :rtype: Topic
    """
    topic = db.get_topic(topicID)
    if topic:
        return topic
    else:
        return {
            "status": "error",
            "error": "The topic was not found"
        }, 404


def get_topics(user=None):  # noqa: E501
    """Get a list of topics

     # noqa: E501

    :param user: Filter Topics by user
    :type user: str

    :rtype: List[Topic]
    """
    topics = db.get_topics()
    return topics


def update_topic(topicID, body):  # noqa: E501
    """update a topic

     # noqa: E501

    :param topicID: ID of topic
    :type topicID: str
    :param body: Topic details to be updated
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()
        body["id"] = topicID
        if db.update_topic(body).modified_count == 1:
            return {"status": "ok"}
    return get_error("no topic was updated")


def add_post(body):
    """Add a new post
    :param body: Post details to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()
        
    return {
        "id": db.add_post(body)
    }


def delete_post(postID):
    """delete a post and associated resources
    :param postID: ID of post
    :type postID: str

    :rtype: None
    """
    db.delete_post(postID)
    return 'do some magic!'


def get_post(postID):
    """get a post by ID
    :param postID: ID of post
    :type postID: str

    :rtype: Post
    """
    post = db.get_post(postID)
    if post:
        return post
    else:
        return {
            "status": "error",
            "error": "The post was not found"
        }, 404


def get_posts(topicID):
    """Finds all posts by topic

    Get a list of posts for a particular topic ID

    :param topicID: Topic ID for filtering posts
    :type topicID: str

    :rtype: List[Post]
    """
    posts = db.get_posts_by_topic(topicID)
    return posts


def update_post(postID, body):
    """update a post
    :param postID: ID of post
    :type postID: str
    :param body: Post details to be updated
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()
        body["id"] = postID
        db.update_post(body)
    return 'do some magic!'


def add_comment(body):  # noqa: E501
    """Add a new comment

     # noqa: E501

    :param body: Comment details to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()
        db.add_comment(body)
    return 'do some magic!'


def delete_comment(commentID):  # noqa: E501
    """delete a comment and make it [deleted]

     # noqa: E501

    :param commentID: ID of comment
    :type commentID: str

    :rtype: None
    """
    db.delete_comment(commentID)
    return 'do some magic!'


def get_comments(postID):  # noqa: E501
    """Finds all comments of a post

    Get a list of comments for a particular post # noqa: E501

    :param postID: Post ID for getting comments
    :type postID: str

    :rtype: List[Comment]
    """
    comments = db.get_comments(postID)
    return comments


def update_comment(commentID, body):  # noqa: E501
    """update a comment

     # noqa: E501

    :param commentID: ID of comment
    :type commentID: str
    :param body: Comment details to be updated
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()
        body["id"] = commentID
        db.update_comment(body)
    return 'do some magic!'
