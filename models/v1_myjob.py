# coding: utf-8

from pprint import pformat
from six import iteritems
import re

from generic_obj import GenericObject


class V1MyJob(GenericObject):

    swagger_types = {
        'api_version': 'str',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'spec': 'V1MyJobSpec',
        'status': 'V1MyJobStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, **kwargs):
        super(V1MyJob, self).__init__(**kwargs)
        self.kind = 'MyJob'
        self.api_version = 'test.example.com/v1'
