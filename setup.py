from setuptools import setup, find_packages
from approx_count import VERSION, PROJECT


MODULE_NAME = 'approx_count'
PACKAGE_DATA = list()
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
]


setup(
    name=PROJECT,
    version=VERSION,
    packages=find_packages(),
    zip_safe=True,

    author='Park Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='Park Hyunwoo',
    maintainer_email='ez.amiryo' '@' 'gmail.com',
    url='http://github.com/lqez/django-admin-approx-count',

    description='A dirty mixin to rescue from dumb count(*) query of Django admin',
    classifiers=CLASSIFIERS,

    install_requires=['django'],
)
