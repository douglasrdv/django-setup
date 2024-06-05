import os

from .misc import yaml_coerce


def get_settings_from_environment(prefix):
    '''
    if
    'CORESETTINGS_IN_DOCKER = 1'

    function returns
    {
        'IN_DOCKER': 1
    }

    '''
    prefix_len = len(prefix)
    return {key[prefix_len:]: yaml_coerce(value) for key, value in os.environ.items() if key.startswith(prefix)}
