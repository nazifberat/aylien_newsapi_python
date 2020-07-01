# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class Author(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'avatar_url': 'str',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'avatar_url': 'avatar_url',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, avatar_url=None, id=None, name=None, local_vars_configuration=None):  # noqa: E501
        """Author - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._avatar_url = None
        self._id = None
        self._name = None
        self.discriminator = None

        if avatar_url is not None:
            self.avatar_url = avatar_url
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this Author.  # noqa: E501

        A URL which points to the author avatar  # noqa: E501

        :return: The avatar_url of this Author.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this Author.

        A URL which points to the author avatar  # noqa: E501

        :param avatar_url: The avatar_url of this Author.  # noqa: E501
        :type avatar_url: str
        """

        self._avatar_url = avatar_url

    @property
    def id(self):
        """Gets the id of this Author.  # noqa: E501

        A unique identification for the author  # noqa: E501

        :return: The id of this Author.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Author.

        A unique identification for the author  # noqa: E501

        :param id: The id of this Author.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Author.  # noqa: E501

        The extracted author full name  # noqa: E501

        :return: The name of this Author.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Author.

        The extracted author full name  # noqa: E501

        :param name: The name of this Author.  # noqa: E501
        :type name: str
        """

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Author):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Author):
            return True

        return self.to_dict() != other.to_dict()
