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
from aylien_news_api.models.clusters import Clusters  # noqa: E501
from aylien_news_api.rest import ApiException

class TestClusters(unittest.TestCase):
    """Clusters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Clusters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = aylien_news_api.models.clusters.Clusters()  # noqa: E501
        if include_optional :
            return Clusters(
                cluster_count = 56, 
                clusters = [
                    aylien_news_api.models.cluster.Cluster(
                        earliest_story = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = 56, 
                        latest_story = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        location = aylien_news_api.models.location.Location(
                            city = '0', 
                            country = '0', 
                            state = '0', ), 
                        representative_story = aylien_news_api.models.representative_story.RepresentativeStory(
                            id = 56, 
                            permalink = '0', 
                            published_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            title = '0', ), 
                        story_count = 56, 
                        time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
                next_page_cursor = '0'
            )
        else :
            return Clusters(
        )

    def testClusters(self):
        """Test Clusters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
