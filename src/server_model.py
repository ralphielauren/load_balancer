import requests


class Server:
    def __init__(self, endpoint, path="/healthcheck"):
        self.endpoint = endpoint
        self.path = path
        self.protocol = "http://"
        self.timeout = 1
        self.healthy = True

    def check_health(self):
        try:
            response = requests.get(
                self.protocol + self.endpoint + self.path, timeout=self.timeout
            )
            if not response.ok:
                self.healthy = False
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
            requests.exceptions.HTTPError,
        ):
            self.healthy = False
        except requests.exceptions.RequestException as e:  # fatal error, exit
            SystemExit(e)

    def __str__(self):
        return (
            f"Server {self.protocol} + {self.endpoint} + "
            f"' is healthy: ' + {self.healthy}"
        )

    def __eq__(self, other):
        if isinstance(other, Server):
            return self.endpoint == other.endpoint
        return False
