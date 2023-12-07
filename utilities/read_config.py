import configparser


def read_config(category, key):
    config = configparser.ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)
