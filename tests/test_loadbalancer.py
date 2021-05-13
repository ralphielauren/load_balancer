from src.loadbalancer import load_balancer
import pytest

#
#
# @pytest.fixture
# def client():
#     with load_balancer.test_client() as client:
#         yield client
#
#
# def test_hello(client):
#     result = client.get("/")
#     assert b"hello" in result.data


@pytest.fixture
def client():
    with load_balancer.test_client() as client:
        yield client


def test_host_routing_mango(client):
    result = client.get("/", headers={"Host": "www.mango.com"})
    assert b"This is the mango application." in result.data


def test_host_routing_apple(client):
    result = client.get("/", headers={"Host": "www.apple.com"})
    assert b"This is the apple application" in result.data


def test_host_routing_not_found(client):
    result = client.get("/", headers={"Host": "www.notapple.com"})
    assert b"Not Found" == result.data
    assert result.status_code == 404


def test_path_routing_mango(client):
    result = client.get("/mango")
    assert b"This is the mango application." in result.data


def test_path_routing_apple(client):
    result = client.get("/apple")
    assert b"This is the apple application." in result.data


def test_path_routing_notfound(client):
    result = client.get("/notapple")
    assert b"Not Found" in result.data
    assert 404 == result.status_code
