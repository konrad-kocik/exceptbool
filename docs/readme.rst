==========
exceptbool
==========

.. image:: https://img.shields.io/pypi/v/exceptbool.svg
        :target: https://pypi.python.org/pypi/exceptbool

.. image:: https://pepy.tech/badge/exceptbool
        :target: https://pepy.tech/badge/exceptbool

.. image:: https://readthedocs.org/projects/exceptbool/badge/?version=latest
        :target: https://exceptbool.readthedocs.io/en/latest/?badge=latest

Converts caught exception into bool value.

* Free software: MIT license
* Documentation: https://exceptbool.readthedocs.io.

Features
--------

How many of those have you written in your life?

.. code-block:: python

    def is_something_possible():
        try:
            do_something()
            return True
        except DoingSomethingError:
            return False

Ugh! A perfect example of six-line boilerplate code. With exceptbool you can shorten that into only three lines!

.. code-block:: python

 @except_to_bool(exc=DoingSomethingError)
 def is_something_possible():
     do_something()

Exceptbool makes decorated function return bool instead of raising an exception by converting given exception(s) into given bool value. If no exception will be raised, then negation of given bool will be returned. If exception different than given one will be raised, then it will not be caught.