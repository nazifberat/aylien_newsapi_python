# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import aylien_news_api
from aylien_news_api.api.default_api import DefaultApi  # noqa: E501
from aylien_news_api.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = aylien_news_api.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_autocompletes(self):
        """Test case for list_autocompletes

        List autocompletes  # noqa: E501
        """
        pass

    def test_list_clusters(self):
        """Test case for list_clusters

        List Clusters  # noqa: E501
        """
        pass

    def test_list_coverages(self):
        """Test case for list_coverages

        List coverages  # noqa: E501
        """
        pass

    def test_list_histograms(self):
        """Test case for list_histograms

        List histograms  # noqa: E501
        """
        pass

    def test_list_related_stories(self):
        """Test case for list_related_stories

        List related stories  # noqa: E501
        """
        pass

    def test_list_stories(self):
        """Test case for list_stories

        List Stories  # noqa: E501
        """
        pass

    def test_list_time_series(self):
        """Test case for list_time_series

        List time series  # noqa: E501
        """
        pass

    def test_list_trends(self):
        """Test case for list_trends

        List trends  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
