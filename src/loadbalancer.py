import random
import requests
from flask import Flask, request

from utils.yaml_utils import load_configuration

load_balancer = Flask(__name__)

CONFIG = load_configuration("configs/loadbalancer.yaml")


@load_balancer.route("/")
def router():
    host_header = request.headers["Host"]
    for entry in CONFIG["hosts"]:
        if host_header == entry["host"]:
            response = requests.get(
                f'http://{random.choice(entry["servers"])}'
            )
            return response.content, response.status_code
    return "Not Found", 404


@load_balancer.route("/<path>")
def path_router(path):
    for entry in CONFIG["paths"]:
        if ("/" + path) == entry["path"]:
            response = requests.get(
                f'http://{random.choice(entry["servers"])}'
            )
            return response.content, response.status_code
    return "Not Found", 404
