# -*- coding: utf-8 -*-
"""Installer for the imio.transmogrifier.PloneFormGen package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read() +
    '\n' +
    'Contributors\n' +
    '============\n' +
    '\n' +
    open('CONTRIBUTORS.rst').read() +
    '\n' +
    open('CHANGES.rst').read() +
    '\n')


setup(
    name='imio.transmogrifier.PloneFormGen',
    version='0.4.dev0',
    description="New blueprint to help Transmogrifier to migrate PloneFormGen objects.",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='boulch',
    author_email='christophe.boulanger@imio.be',
    url='https://pypi.python.org/pypi/imio.transmogrifier.PloneFormGen',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['imio', 'imio.transmogrifier'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'setuptools',
        'z3c.jbot',
        'collective.transmogrifier==1.4',
        'plone.app.transmogrifier==1.2',
        'quintagroup.transmogrifier==0.5',
        'Products.PloneFormGen>=1.7.16',
        'collective.captcha==1.7',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
