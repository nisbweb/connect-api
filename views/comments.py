import connexion


def add_comment(body):  # noqa: E501
    """Add a new comment

     # noqa: E501

    :param body: Comment details to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()
    return 'do some magic!'


def delete_comment(commentID):  # noqa: E501
    """delete a comment and make it [deleted]

     # noqa: E501

    :param commentID: ID of comment
    :type commentID: str

    :rtype: None
    """
    return 'do some magic!'


def get_comments(postID):  # noqa: E501
    """Finds all comments of a post

    Get a list of comments for a particular post # noqa: E501

    :param postID: Post ID for getting comments
    :type postID: str

    :rtype: List[Comment]
    """
    return 'do some magic!'


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
    return 'do some magic!'
