import configparser
import os


def read_config_data_key(section, key):
    cfg_filename = os.path.join(os.path.dirname(__file__), '..', 'resources', 'config.cfg')
    cp = configparser.RawConfigParser()
    cp.read(cfg_filename)
    return cp.get(section, key)


def read_config_data_given_keys(section, *keys, all_value=True):
    cfg_filename = os.path.join(os.path.dirname(__file__), '..', 'resources', 'config.cfg')
    cp = configparser.RawConfigParser()
    cp.read(cfg_filename)
    data = dict.fromkeys(keys, None)
    for k, v in cp.items(section):
        if k in keys:
            data[k] = v
        if all_value:
            if all(data.values()):
                break

    return data
