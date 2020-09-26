import yaml

__config = None

def config():
    global__config
    if not__config:
        with open('config.yaml', mode='r') as f:
            __config = yaml.safe_load(f)

    return __config


