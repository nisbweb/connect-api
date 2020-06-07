import connexion


def add_post(body):
    """Add a new post
    :param body: Post details to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()
    return 'do some magic!'


def delete_post(postID):
    """delete a post and associated resources
    :param postID: ID of post
    :type postID: str

    :rtype: None
    """
    return 'do some magic!'


def get_post(postID):
    """get a post by ID
    :param postID: ID of post
    :type postID: str

    :rtype: Post
    """
    return 'do some magic!'


def get_posts(topicID):
    """Finds all posts by topic

    Get a list of posts for a particular topic ID

    :param topicID: Topic ID for filtering posts
    :type topicID: str

    :rtype: List[Post]
    """
    return 'do some magic!'


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
    return 'do some magic!'
