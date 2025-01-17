# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.1.0
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import aylien_news_api
from aylien_news_api.models.logicals import Logicals  # noqa: E501
from aylien_news_api.rest import ApiException

class TestLogicals(unittest.TestCase):
    """Logicals unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Logicals
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = aylien_news_api.models.logicals.Logicals()  # noqa: E501
        if include_optional :
            return Logicals(
                _and = [
                    null
                    ], 
                _or = [
                    null
                    ], 
                _not = [
                    null
                    ]
            )
        else :
            return Logicals(
        )

    def testLogicals(self):
        """Test Logicals"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
