import random
import requests
import yaml
from flask import Flask, request

load_balancer = Flask(__name__)


def load_configuration(path):
    with open(path) as config_file:
        # use FullLoader for direct python objects on which we iterate
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return config


config = load_configuration("configs/loadbalancer.yaml")


@load_balancer.route("/")
def router():
    host_header = request.headers["Host"]
    print("HOST: " + host_header)
    for entry in config["hosts"]:
        if host_header == entry["host"]:
            print("ENTRY: " + entry["host"])
            response = requests.get(
                f'http://{random.choice(entry["servers"])}'
            )
            return response.content, response.status_code
    return "Not Found", 404


@load_balancer.route("/<path>")
def path_router(path):
    for entry in config["paths"]:
        print(entry)
        if ("/" + path) == entry["path"]:
            print("PATH: " + path)
            response = requests.get(
                f'http://{random.choice(entry["servers"])}'
            )
            return response.content, response.status_code
    return "Not Found", 404
