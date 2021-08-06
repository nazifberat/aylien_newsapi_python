# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.0
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class Autocomplete(object):
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
        'id': 'str',
        'text': 'str'
    }

    attribute_map = {
        'id': 'id',
        'text': 'text'
    }

    def __init__(self, id=None, text=None, local_vars_configuration=None):  # noqa: E501
        """Autocomplete - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._text = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if text is not None:
            self.text = text

    @property
    def id(self):
        """Gets the id of this Autocomplete.  # noqa: E501

        ID of the autocomplete  # noqa: E501

        :return: The id of this Autocomplete.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Autocomplete.

        ID of the autocomplete  # noqa: E501

        :param id: The id of this Autocomplete.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this Autocomplete.  # noqa: E501

        Text of the autocomplete  # noqa: E501

        :return: The text of this Autocomplete.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Autocomplete.

        Text of the autocomplete  # noqa: E501

        :param text: The text of this Autocomplete.  # noqa: E501
        :type text: str
        """

        self._text = text

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
        if not isinstance(other, Autocomplete):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Autocomplete):
            return True

        return self.to_dict() != other.to_dict()
