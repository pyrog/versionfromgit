from versionfromgit import versions_from_git
    
__version__ = versions_from_git(tag_prefix="v")['version']
del versions_from_git