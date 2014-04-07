'''Setup file for versionfromgit.'''
from setuptools import setup
from versionfromgit import __version__

setup(
    name='versionfromgit',
    version=__version__,
    packages=['versionfromgit'],
    description='Utility to version non-distutils python projects using git tags.',
    author='Dries Desmet',
    author_email='dries@urga.be',
    include_package_data=True,
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Version Control',
    ],
)
