#!/usr/bin/env python

import sys, os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


# Hack to prevent "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when setup.py exits
# (see http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing
except ImportError:
    pass

PY3 = sys.version_info[0] == 3

install_requires = [
    'wagtail>=2.2.2',
    'django>=1.11.15',
    'django-password-policies-iplweb>=0.4.4b1',
    'django-axes==4.4.3',
    'pyClamd>=0.4.0',
]

setup(
    name='wagtailenforcer2',
    version='1.1.7a',
    description='WagtailEnforcer, the Wagtail arm of the law.',
    author='Springload',
    author_email='hello@springload.co.nz',
    url='https://github.com/samm-insite/wagtailenforcer',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    install_requires=install_requires,
    zip_safe=False,
)
