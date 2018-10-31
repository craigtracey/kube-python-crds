Example of creating CRDs with the Python API bindings
===

In this example we create a new CRD type called `MyJob`, and will use the Python API bindings to programmatically create new MyJob resources with Kubernetes.

Setup your environment:
```
$ kubectl apply -f myjob.yml
$ pip install -r requirements.txt
```

Create a new MyJob resource:
```
$ kubectl create ns <namespace>
$ python tester.py <namespace> <name> <jobid> <command>
```

An example:
```
$ kubectl create ns test1
$ python tester.py test1 mytestjob 1234 "/bin/somecommand"
About to create MyJob:
{'api_version': 'test.example.com/v1',
 'discriminator': None,
 'kind': 'MyJob',
 'metadata': {'annotations': None,
 'cluster_name': None,
 'creation_timestamp': None,
 'deletion_grace_period_seconds': None,
 'deletion_timestamp': None,
 'finalizers': None,
 'generate_name': None,
 'generation': None,
 'initializers': None,
 'labels': None,
 'name': 'mytestjob',
 'namespace': 'test1',
 'owner_references': None,
 'resource_version': None,
 'self_link': None,
 'uid': None},
 'spec': {'command': '/bin/somecommand', 'job_id': 1234},
 'status': None}
$ kubectl get myjob -n test1 mytestjob -oyaml
apiVersion: test.example.com/v1
kind: MyJob
metadata:
  clusterName: ""
  creationTimestamp: 2018-10-31T18:05:35Z
  generation: 1
  name: mytestjob
  namespace: test1
  resourceVersion: "8560631"
  selfLink: /apis/test.example.com/v1/namespaces/test1/myjobs/mytestjob
  uid: 90771615-dd37-11e8-8456-0e7c5c8ddfc6
spec:
  command: /bin/somecommand
  jobId: 1234
```
