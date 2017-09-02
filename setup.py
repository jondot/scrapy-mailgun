# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='scrapy-mailgun',
    version='0.1.0',
    description='scrapy-mailgun: Hook emails with scrapy.',
    long_description=readme,
    author='Dotan Nahum',
    author_email='jondotan@gmail.com',
    url='https://github.com/jondot/scrapy-mailgun',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['requests', 'jinja2'])
