import yaml


def load_configuration(path):
    with open(path) as config_file:
        # use FullLoader for direct python objects on which we iterate
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return config
