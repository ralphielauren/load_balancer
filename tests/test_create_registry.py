import yaml
from utils.registry import create_registry
from src.server_model import Server

CONFIG = yaml.load(
    """
    hosts:
      - host: www.cat.com
        servers:
          - localhost:8081
          - localhost:8082
      - host: www.apple.com
        servers:
          - localhost:9081
          - localhost:9082
    paths:
      - path: /cat
        servers:
          - localhost:8081
          - localhost:8082
      - path: /apple
        servers:
          - localhost:9081
          - localhost:9082
""",
    Loader=yaml.FullLoader,
)


def test_create_registry():
    output_registry = create_registry(CONFIG)
    assert list(output_registry.keys()) == [
        "www.cat.com",
        "www.apple.com",
        "/cat",
        "/apple",
    ]
    assert output_registry["www.cat.com"][0] == Server("localhost:8081")
    assert output_registry["www.cat.com"][1] == Server("localhost:8082")
    assert output_registry["www.apple.com"][0] == Server("localhost:9081")
    assert output_registry["www.apple.com"][1] == Server("localhost:9082")
    assert output_registry["/cat"][0] == Server("localhost:8081")
    assert output_registry["/cat"][1] == Server("localhost:8082")
    assert output_registry["/apple"][0] == Server("localhost:9081")
    assert output_registry["/apple"][1] == Server("localhost:9082")
