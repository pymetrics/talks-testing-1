:title: Intro to Testing
:css: style.css

An introduction to effective testing for Python applications.


.. footer::

    .. image:: images/logo-icon.png

    http://github.com/pymetrics

----

Let's start with something interesting
======================================

We can't write tests in a void, we need somethign to test! Let's say we're
building a Slack bot that will tell us our crypto-coin balances, converted
to fiat units.



----

Here's our ``CoinAccount`` model
================================

.. include:: src/coinbot/accounts/models.py
    :code: python

----


What's that `get_price` function all about?
===========================================

Pretty simple, a ``GET`` to the Coinbase API using the ``requests`` library

.. include:: src/coinbot/coinbase.py
    :code: python

----


This is a basic unit test.
==========================

Some content manage.py

.. include:: src/coinbot/accounts/tests/test_account_creation.py
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
