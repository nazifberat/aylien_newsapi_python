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


class Scope(object):
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
        'city': 'str',
        'country': 'str',
        'level': 'ScopeLevel',
        'state': 'str'
    }

    attribute_map = {
        'city': 'city',
        'country': 'country',
        'level': 'level',
        'state': 'state'
    }

    def __init__(self, city=None, country=None, level=None, state=None, local_vars_configuration=None):  # noqa: E501
        """Scope - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._city = None
        self._country = None
        self._level = None
        self._state = None
        self.discriminator = None

        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if level is not None:
            self.level = level
        if state is not None:
            self.state = state

    @property
    def city(self):
        """Gets the city of this Scope.  # noqa: E501

        The scope by city  # noqa: E501

        :return: The city of this Scope.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Scope.

        The scope by city  # noqa: E501

        :param city: The city of this Scope.  # noqa: E501
        :type city: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this Scope.  # noqa: E501

        The source scope by country code. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes.   # noqa: E501

        :return: The country of this Scope.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Scope.

        The source scope by country code. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes.   # noqa: E501

        :param country: The country of this Scope.  # noqa: E501
        :type country: str
        """

        self._country = country

    @property
    def level(self):
        """Gets the level of this Scope.  # noqa: E501


        :return: The level of this Scope.  # noqa: E501
        :rtype: ScopeLevel
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Scope.


        :param level: The level of this Scope.  # noqa: E501
        :type level: ScopeLevel
        """

        self._level = level

    @property
    def state(self):
        """Gets the state of this Scope.  # noqa: E501

        The scope by state  # noqa: E501

        :return: The state of this Scope.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Scope.

        The scope by state  # noqa: E501

        :param state: The state of this Scope.  # noqa: E501
        :type state: str
        """

        self._state = state

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
        if not isinstance(other, Scope):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Scope):
            return True

        return self.to_dict() != other.to_dict()
