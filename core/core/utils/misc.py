import yaml


def yaml_coerce(value):
    # Convert value to proper Python

    # Check if the value is a string
    if isinstance(value, str):
        # yaml.load returns a Python object (creating yaml data with a dummy)
        # Converts string dict "{'apples': 1, 'bacon': 2}" to Python dict
        # Useful because sometimes we need to stringify seetings this way (like in Dockerfile)
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']
    
    return value
