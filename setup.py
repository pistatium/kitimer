# coding: utf-8

from setuptools import setup, find_packages


setup(
    name='kitimer',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'Django',
        'pytz',
        'djangorestframework',
        'django-filter',
    ],
    entry_points={
        'console_scripts': [
            'kitimer=manage:main'
        ]
    }
)
