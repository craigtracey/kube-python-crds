# coding: utf-8

from pprint import pformat
from six import iteritems
import re

from generic_obj import GenericObject


class V1MyJobSpec(GenericObject):

    swagger_types = {
        'job_id': 'int',
    }

    attribute_map = {
        'job_id': 'jobId',
    }

    def __init__(self, job_id):
        self.job_id = job_id
