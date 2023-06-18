def create_argument_dictionary(**kwargs):
    argument_dictionary = {}
    for key, value in kwargs.items():
        try:
            hash(key)
            argument_dictionary[key] = value
        except TypeError:
            argument_dictionary[str(key)] = value
    return argument_dictionary

arguments = create_argument_dictionary(arg1=10, arg2='Hello', arg3=[1, 2, 3])

print(arguments)