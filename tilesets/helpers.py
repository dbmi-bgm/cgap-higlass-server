


def dict_extract(key, var):
    '''
    Find all occurrences of a key in nested dictionaries and lists

    Args:

    key (string): key to search for
    var (object): (nested) dict that contains the key, maybe multiple times

    Returns:

     A list of values for each key occurence
    '''
    if hasattr(var,'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in dict_extract(key, d):
                        yield result
