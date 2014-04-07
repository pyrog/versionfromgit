"""
This module offers a way of getting a version string using git and returns nothing if git isn't used.

I first thought of using setup.py to put the version string and the idea came from here:
https://blog.mozilla.org/warner/2012/01/31/version-string-management-in-python-introducing-python-versioneer/

but then I reckoned using setup.py is cumbersome for python web applications to keep in sync.
Also, setup.py should not contain explicit versions but mostly implicit version ranges.

Requirements.txt is a better fit to recreate an explicit environment. With that, I'm not using source distributions or
other tarballs for deploying, but just use git to update a remote deployment fast.

Basically, this module is a stripped down version of Brian Warner's python-versioneer and assumes you only want to
install using pip install -r requirements.txt. Distutils or similar simply won't work (but are broken anyway).

"""

__version__ = '0.1-alpha'

import sys
import subprocess
import errno

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False):
    assert isinstance(commands, list)
    p = None
    for c in commands:
        try:
            # remember shell=False, so use git.cmd on windows, not just git
            p = subprocess.Popen([c] + args, cwd=cwd, stdout=subprocess.PIPE,
                                 stderr=(subprocess.PIPE if hide_stderr
                                         else None))
            break
        except EnvironmentError:
            e = sys.exc_info()[1]
            if e.errno == errno.ENOENT:
                continue
            if verbose:
                print("unable to run %s" % args[0])
                print(e)
            return None
    else:
        if verbose:
            print("unable to find command, tried %s" % (commands,))
        return None
    stdout = p.communicate()[0].strip()
    if sys.version >= '3':
        stdout = stdout.decode()
    if p.returncode != 0:
        if verbose:
            print("unable to run %s (error)" % args[0])
        return None
    return stdout


def versions_from_git(tag_prefix="", verbose=False):
    """
    Returns a dictionary with a version and a full version.

    A 'version' is based on git describe and strips 'tag_prefix'.
    A 'full version' is simply the complete revision number with '-dirty' attached if we are in between commits.

    @param tag_prefix: strip this tag_prefix to get version eg: for v0.1 return 0.1
    @param verbose:
    @return: {'version': version, 'full': fullversion}
    """

    GITS = ["git"]
    if sys.platform == "win32":
        GITS = ["git.cmd", "git.exe"]
    stdout = run_command(GITS, ["describe", "--tags", "--dirty", "--always"])
    if stdout is None:
        return {}
    if not stdout.startswith(tag_prefix):
        # simply don't strip the prefix
        if verbose:
            print("tag '%s' doesn't start with prefix '%s'" % (stdout, tag_prefix))
        tag = stdout
    else:
        tag = stdout[len(tag_prefix):]
    stdout = run_command(GITS, ["rev-parse", "HEAD"])
    if stdout is None:
        return {}
    full = stdout.strip()
    if tag.endswith("-dirty"):
        full += "-dirty"
    return {"version": tag, "full": full}