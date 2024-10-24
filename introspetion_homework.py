import inspect
import matplotlib.pyplot as plt


def introspection_info(object):
    types_of_data = (int, str, list, tuple, dict)
    attr_dict = {}
    methods = []
    attributes = []

    for item in dir(object):
        if callable(getattr(object, item)):
            methods.append(item)
        else:
            attributes.append(item)

    attr_dict['type'] = type(object).__name__
    attr_dict['attributes'] = attributes
    attr_dict['methods'] = methods
    if isinstance(object, types_of_data):
        attr_dict['module'] = inspect.getmodule(introspection_info).__name__
    else:
        attr_dict['module'] = inspect.getmodule(object).__name__

    return attr_dict


number_info = introspection_info(42)
print(number_info)

list_info = introspection_info([1, 2, 3, 4])
print(list_info)

dict_info = introspection_info({'test1': 1, 'test2': 2})
print(dict_info)

test_func = plt.hist
func_info = introspection_info(test_func)
print(func_info)
