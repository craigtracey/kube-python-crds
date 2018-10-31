from generic_obj import GenericObject


class V1MyJobSpec(GenericObject):

    swagger_types = {
        'job_id': 'int',
        'command': 'string',
    }

    attribute_map = {
        'job_id': 'jobId',
        'command': 'command',
    }

    def __init__(self, job_id, command):
        self.job_id = job_id
        self.command = command
