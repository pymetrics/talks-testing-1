:title: Intro to Testing
:css: style.css

An introduction to effective testing for Python applications.


.. footer::

    .. image:: images/logo-icon.png

    http://github.com/pymetrics

----

Let's start with something interesting
======================================

We can't write tests in a void, we need somethign to test!

.. include:: src/coinchecker/accounts/models.py
    :code: python

----


What's that `get_price` function all about?
===========================================

Pretty simple, a ``GET`` to the Coinbase API using the ``requests`` library

.. include:: src/coinchecker/coinbase.py
    :code: python

----


This is a basic unit test.
==========================

Some content manage.py

.. include:: src/coinchecker/accounts/tests/test_account_creation.py
    :code: python

----


Running Tests
==================

::

    $ python manage.py test

::

    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
