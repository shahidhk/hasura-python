from setuptools import setup, find_packages
from os import path
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hasura',
    version='0.1',
    description='Hasura API client library for Python',
    long_description=long_description,
    url='https://github.com/shahidhk/hasura-python',
    author='Shahidh K Muhammed',
    author_email='shahidhkmuhammed@gmail.com',
    license='MIT',
    keywords='hasura python sdk',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        'requests'    
    ]
)
