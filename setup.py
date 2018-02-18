from setuptools import setup, find_packages
from codecs import open
from os import path

base_dir = path.abspath(path.dirname(__file__))

with open(path.join(base_dir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-npb',
    version='0.1.0.dev1',
    description='Pastebin module for Django',
    long_description=long_description,
    url='https://github.com/breard-r/django-npb',
    author='Rodolphe Bréard',
    author_email='rodolphe@breard.tf',
    license='CeCILL-B',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'License :: CeCILL-B Free Software License Agreement (CECILL-B)',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='django pastebin',
    packages=find_packages(exclude=['contrib', 'demo', 'docs', 'tests']),
    install_requires=[
        'Django',
        'Pygments',
        'pytimeparse',
    ],
    python_requires='~=3.3',
    data_files=[
        ('license', ['LICENSE-EN.txt', 'LICENSE-FR.txt']),
    ],
)