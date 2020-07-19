# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name='auto_exp',
    version='1.0',
    author='minhdao',
    description='Auto Exp',
    packages=find_packages(exclude=[
        'docs',
        'tests',
        'static',
        'templates',
        '.gitignore',
        'README.md'
    ]),
    entry_points={'scrapy': ['settings = auto_exp.settings']},
    install_requires=[
        'scrapy',
        'w3lib',
    ]
)
