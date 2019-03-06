# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os, sys
from setuptools import setup, find_packages

version = __import__('ckeditor5').__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

long_description = "\n".join([
    open('README.md', 'r', encoding='utf-8').read(),
])

def get_source_files():
    for dirname, _, files in os.walk('ckeditor5/static/ckeditor5/ckeditor5/_source'):
        for filename in files:
            yield os.path.join('/'.join(dirname.split('/')[1:]), filename)


setup(
    name='django-ckeditor5',
    version=version,
    description='Django CKEditor 5 集成',
    long_description=long_description,
    author='n37r06u3',
    author_email='n37r06u3@gmail.com',
    url='https://github.com/n37r06u3/django-ckeditor5',
    packages=find_packages(exclude=["*.demo"]),
    zip_safe=False,
    install_requires=[
        'django',
        'django-js-asset',
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)