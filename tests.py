'''Tests for gitversion.'''
# pylint: disable=C0103
# pylint: disable=R0904

import contextlib
import versionfromgit
import os
import shutil
import tempfile
import unittest
import logging

LOGGER = logging.getLogger(__name__)


class GitVersionCase(unittest.TestCase):

    '''Test the correct versions are detected (and written, if applicable).'''

    repos = {
        'repo1': {'versionstring': '0.1'},
    }

    def setUp(self):

        self.tempdir = tempfile.mkdtemp()
        LOGGER.debug("Created temporary directory %r", self.tempdir)
        self.testdir = os.path.join(self.tempdir, 'repo')
        self.gitdir = os.path.join(self.testdir, '.git')

    def tearDown(self):

        LOGGER.debug('Removing %r', self.tempdir)
        shutil.rmtree(self.tempdir)


    def test_git_describe(self):
        '''
        Tests that the version is determined correctly.
        '''

        for repo in self.repos:
            LOGGER.debug('investigating %r', repo)
