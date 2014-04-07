==============
versionfromgit
==============


This package lets you use git tags to version python projects that don't use setup.py or other distutils. The idea is
to only use a requirements file to pin dependancies as is common for django or other web applications that need to get
'deployed' as opposed to 'installed'.

It doesn't write to any file to update the version so no changes need to be re-committed.

Usage
=====


``<package>/__init__.py``:

.. code-block:: python

    from versionfromgit import versions_from_git

    __version__ = versions_from_git(tag_prefix="v")['version']
    del versions_from_git