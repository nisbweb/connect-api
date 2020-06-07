import connexion


def add_topic(body):  # noqa: E501
    """Add a new topic

     # noqa: E501

    :param body: Topic details to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()
    return 'do some magic!'


def delete_topic(topicID):  # noqa: E501
    """delete a topic and associated resources

     # noqa: E501

    :param topicID: ID of topic
    :type topicID: str

    :rtype: None
    """
    return 'do some magic!'


def get_topic(topicID):  # noqa: E501
    """get a topic by ID

     # noqa: E501

    :param topicID: ID of topic
    :type topicID: str

    :rtype: Topic
    """
    return 'do some magic!'


def get_topics(user=None):  # noqa: E501
    """Get a list of topics

     # noqa: E501

    :param user: Filter Topics by user
    :type user: str

    :rtype: List[Topic]
    """
    return 'do some magic!'


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
    return 'do some magic!'
