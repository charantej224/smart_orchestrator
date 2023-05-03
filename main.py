import triggers.feature_functions


def trigger_functions(name):
    trigger_function = getattr(triggers.feature_functions, name)
    trigger_function()


if __name__ == '__main__':
    trigger_functions("function_one")
