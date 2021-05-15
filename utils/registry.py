from src.server_model import Server


def create_registry(config):
    """Instantiate Server objects from config and
    assign to hosts, paths in registry."""
    registry = {}
    for entry in config["hosts"]:
        registry[entry["host"]] = [
            Server(endpoint) for endpoint in entry["servers"]
        ]
    for entry in config["paths"]:
        registry[entry["path"]] = [
            Server(endpoint) for endpoint in entry["servers"]
        ]
    return registry
