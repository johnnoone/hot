H.O.T
=====

Play with monkey patching.

This project is a sandbox for monkey patching.

Beware: Use it under a safe virtualenv (it may breaks pths).

Very important when installing this package though is that you cannot
use ``easy_install`` or ``python setup.py install``. One can only install
this package using ‘pip’.

The reason for this is that if not using ``pip``, then the package installation
tool can install the package as an egg. In this situation the custom ``.pth``
file will actually be installed within the egg directory and not actually
within the ``site-packages`` directory.



Reading
-------

Cool monkeypatch:

  Safely applying monkey patches in Python
  http://blog.dscpl.com.au/2015/03/safely-applying-monkey-patches-in-python.html

  It is based on wrapt http://wrapt.readthedocs.io/en/latest/


Execute code at startup:

  The **.pth "import" hack** slide of Beazley

  http://nedbatchelder.com/blog/201001/running_code_at_python_startup.html


startup and wrapt:

  http://blog.dscpl.com.au/2015/04/automatic-patching-of-python.html
