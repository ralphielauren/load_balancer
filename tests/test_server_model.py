import pytest
import responses

from src.server_model import Server


@pytest.fixture
def server():
    server = Server('localhost:8080')
    yield server


@responses.activate
def test_healthy_server(server):
    responses.add(responses.GET, "http://localhost:8080/healthcheck", status=200)
    server.check_health()
    assert server.healthy


@responses.activate
def test_unhealthy_server(server):
    responses.add(responses.GET, "http://localhost:8080/healthcheck", status=500)
    server.check_health()
    assert not server.healthy


def test_server_equality(server):
    other_server = Server("localhost:8080")
    assert server == other_server


def test_server_inequality(server):
    other_server = Server("localhost:6666")
    assert server != other_server