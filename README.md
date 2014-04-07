#versionfromgit

This package lets you use git tags to version python projects that don't use python distributions but are simply
'installed' by cloning their repository and then use pip to install it's requirements. This is common for django or
other web applications and avoids the trap of using setup.py.

It doesn't write to any file to update the version so no changes need to be re-committed. Simply tag your repo.

Tag prefixes allowed, meaning if your latest tag is 'v0.1' then the version will be '0.1'.


##Usage

`<package>/__init__.py`

```python
from versionfromgit import versions_from_git

__version__ = versions_from_git(tag_prefix="v")['version']
del versions_from_git
```