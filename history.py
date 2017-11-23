import kubernetes
kubernetes.config.load_kube_config()
kubernetes.client.CoreV1Api()
k8s = _
k8s.list_node()
k8s.list_node??
k8s.__file__
kubernetes.__file__
k8s.list_node()
k8s.list_node?
k8s.list_node(pretty=True)
k8s.list_node?
nodes = k8s.list_node()
nodes?
nodes.metadata
nodes.kind
nodes.items
nodes.items.keys()
nodes.items.count()
nodes.items
nodes.items?
nodes.items[0]
nodes.items[1]
nodes.items[2]
nodes.items[3]
len(nodes.items)
node = nodes[0]
nodes
nodes.items[0]
node = nodes.items[0]
node.spec
node.status
node.status.keys
status = node.status
status.images
status.images[0]
status.images[1]
k8s.list_namespace
k8s.list_namespace()
namespaces = _
namespaces.items[0]
namespaces.items[1]
namespaces.items[0]
namespaces.items[1]
namespaces.items[0]
namespaces.items[0]['metadata']
aws_cluster_autoscaler = namespaces.items[0]
aws_cluster_autoscaler.name
aws_cluster_autoscaler.metadata
aws_cluster_autoscaler.metadata.name
namespaces.items[0].metadata
namespaces.items[0].metadata.finalizers
namespaces.items[0].metadata.name
[ns.metadata.name for ns in namespaces.items]
