:title: Intro to Testing
:css: style.css

An introduction to effective testing for Python applications.


.. footer::

    http://github.com/pymetrics

----

We're all Animals
=================

Let's write a test to see if our ``Animal`` class can speak properly

.. include:: src/myapp/models.py
    :code: python

----


X & Y
=====

This is a basic unit test.

.. include:: src/test_ex01.py
    :code: python

----


Running Tests
==================

::

    $ python -m unittest
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

----


Verbose option
==============

.. include:: src/test_ex01.py
    :code: python

::

    $ python -m unittest discover -v
    test_animals_can_speak (test_ex01.AnimalTestCase)
    Animals that can speak are correctly identified ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
