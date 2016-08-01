from __future__ import absolute_import, print_function, unicode_literals
from collections import namedtuple
__all__ = ['process_startup']

Hook = namedtuple('Hook', 'module name wrapper')

HOT_FIXES = [
    Hook('http.client', 'HTTPConnection.request', lambda: http_request),
    Hook('a.package.that.is.not.present', 'Foo', lambda: dummy),
    Hook('importlib', 'import_module', lambda: dummy)
]

FORBIDDEN_MODULES = [
    'importlib',
    'inspect'
]


def is_forbidden(module):
    """Check if module must be keept pure
    """
    parts = module.__name__.split('.')
    while parts:
        name = '.'.join(parts)
        if name in FORBIDDEN_MODULES:
            return True
        parts.pop()
    return False


class ForbiddenError(RuntimeError):
    pass


def process_startup():
    """Apply patch to modules

    .. todo:: sort HOT_FIXES by lower to higher code
        for example stdlibs first, then userlibs, etc...

    .. todo:: drop unallowed modules from HOT_FIXES, like inspect, importlib...
    """
    import wrapt
    from colorama import Fore, Back, Style
    from importlib import import_module

    print(Fore.YELLOW + 'THIS is becoming HOT' + Style.RESET_ALL)
    for module, name, wrapper in HOT_FIXES:
        try:
            if isinstance(module, str):
                module = import_module(module)
            if is_forbidden(module):
                raise ForbiddenError()
            wrapt.wrap_function_wrapper(module, name, wrapper())
        except ImportError:
            # parent module may not exists
            print(Fore.RED + '  ✗' + Style.RESET_ALL, module, name,
                  Fore.RED + '(import error)' + Style.RESET_ALL)
        except ForbiddenError:
            # module must not be wrapped
            print(Fore.RED + '  ✗' + Style.RESET_ALL, module.__name__, name,
                  Fore.RED + '(forbidden)' + Style.RESET_ALL)
        except Exception:
            # what append with wrapt?
            print(Fore.RED + '  ✗' + Style.RESET_ALL, module.__name__, name,
                  Fore.RED + '(unknown error)' + Style.RESET_ALL)
        else:
            print(Fore.GREEN + '  ✓' + Style.RESET_ALL, module.__name__, name)


def http_request(wrapped, instance, args, kwargs):
    """Inspect the out bounding calls
    """
    from colorama import Fore, Back, Style
    import inspect

    try:
        sign = inspect.signature(wrapped)
        arguments = sign.bind(*args, **kwargs).arguments

        url = '{1[method]} {0.host}:{0.port}{1[url]}'.format(instance, arguments)

        print(Fore.YELLOW + 'Oh boy, make me scream with: ' + Style.RESET_ALL, url)
        return wrapped(*args, **kwargs)
    finally:
        print(Fore.YELLOW + 'I am done' + Style.RESET_ALL)


def dummy(wrapped, instance, args, kwargs):
    print(Fore.YELLOW + 'Nothing special: ' + Style.RESET_ALL, wrapped.__name__)
    return wrapped(*args, **kwargs)
