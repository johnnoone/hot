__all__ = ['process_startup']

HOT_FIXES = [
    ('http.client', 'HTTPConnection.request', lambda: http_request),
    ('a.package.that.is.not.present', 'Foo', lambda: http_request)
]


def process_startup():
    """Apply patch to modules
    """
    import wrapt
    from colorama import Fore, Back, Style
    from importlib.util import find_spec

    print(Fore.YELLOW + 'THIS is becoming HOT' + Style.RESET_ALL)
    for module, name, wrapper in HOT_FIXES:
        try:
            if find_spec(module):
                wrapt.wrap_function_wrapper(module, name, wrapper())
        except ImportError:
            # parent module may not exists
            print(Fore.RED + '  ✗' + Style.RESET_ALL, module, name)
        else:
            print(Fore.GREEN + '  ✓' + Style.RESET_ALL, module, name)


def http_request(wrapped, instance, args, kwargs):
    """Inspect the out bounding calls
    """
    from colorama import Fore, Back, Style
    import inspect

    try:
        sign = inspect.signature(wrapped)
        arguments = sign.bind(*args, **kwargs).arguments

        url = '{1[method]} {0.host}:{0.port}{1[url]}'.format(instance, arguments)

        print(Fore.YELLOW + 'Oh boy, make me scream with: ' + Style.RESET_ALL + url)
        return wrapped(*args, **kwargs)
    finally:
        print(Fore.YELLOW + 'I am done' + Style.RESET_ALL)
