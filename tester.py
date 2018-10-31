import argparse
import pprint

from models.v1_myjob import V1MyJob
from models.v1_myjob_spec import V1MyJobSpec

from kubernetes import client, config, watch
from kubernetes.client.models.v1_object_meta import V1ObjectMeta

API_NAMESPACE = "test.example.com"
API_VERSION = "v1"
API_KIND = "myjobs"


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('namespace')
    parser.add_argument('name')
    parser.add_argument('jobid', type=int)
    parser.add_argument('command')

    args = parser.parse_args()

    try:
        config.load_incluster_config()
    except Exception as e:
        config.load_kube_config()

    crdApi = client.CustomObjectsApi()

    meta = V1ObjectMeta(name=args.name, namespace=args.namespace)

    myjob_spec = V1MyJobSpec(job_id=args.jobid, command=args.command)
    myjob = V1MyJob(metadata=meta, spec=myjob_spec)

    print "About to create MyJob:"
    pprint.pprint(myjob.__dict__)

    crdApi.create_namespaced_custom_object(API_NAMESPACE, API_VERSION,
                                           args.namespace, API_KIND, myjob)


if __name__ == '__main__':
    main()
