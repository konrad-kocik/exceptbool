=====
Usage
=====

First import ``except_to_bool`` decorator into current namespace:

.. code-block:: python

     from exceptbool import except_to_bool

To catch any exception and convert it into False:

.. code-block:: python

    @except_to_bool
    def decorated_function():
        error_raising_function()

Now ``decorated_function`` will return False if ``error_raising_function`` raises Exception, True otherwise.

To catch given exception and convert it into given bool value:

.. code-block:: python

    @except_to_bool(exc=ValueError, to=True)
    def decorated_function():
       error_raising_function()

Now ``decorated_function`` will return True if ``error_raising_function`` raises ValueError, False otherwise.

To catch any of multiple exceptions:

.. code-block:: python

    @except_to_bool(exc=(TypeError, TimeoutError))
    def decorated_function():
       error_raising_function()

Now ``decorated_function`` will return False if ``error_raising_function`` raises TypeError or TimeoutError, True otherwise.

Function decorated with ``except_to_bool`` is perfectly capable of accepting positional and keyword arguments:

.. code-block:: python

    @except_to_bool
    def decorated_function(*args, **kwargs):
        error_raising_function(*args, **kwargs)

    decorated_function("foo", bar="baz")  # no error