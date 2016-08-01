H.O.T
=====

Play with monkey patching.

This project is a sandbox for monkey patching.

Beware: Use it under a safe virtualenv (it may breaks pths).

Very important when installing this package though is that you SHOULD use
``pip install hot``. The fact is using ``python setup.py install`` will not
track the path file ``zyx-hot.pth``.

The reason for this is that if not using ``pip``, then the package installation
will not track the customs ``.pth`` file and uninstall will let dirty files
into your `site-packages`.

``pip install -e .`` doesn't work either. .pth files are not installed with this
context.

``zyx-hot.pth`` is named ``zyx**`` in order to load at very last. Investigate if
there is a better way to hook sys.path, sys.path_hooks, etc...


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
