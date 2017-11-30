import kubernetes


def client():
    """
    returns a CoreV1Api client from the current context
    """
    kubernetes.config.load_kube_config()
    return kubernetes.client.CoreV1Api()


def clients():
    """
    returns a dict mapping context names to CoreV1Api client instances
    """
    kubernetes.config.load_kube_config()
    return {c['name']: kubernetes.client.CoreV1Api(
                kubernetes.config.new_client_from_config(
                    context=c['name']))
            for c in kubernetes.config.list_kube_config_contexts()[0]}

def pods(k8s=None, namespace=None):
    if not k8s:
        k8s = client()
    if namespace:
        return k8s.list_namespaced_pod(namespace)
    else:
        return k8s.list_pod_for_all_namespaces()
