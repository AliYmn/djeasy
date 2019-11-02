from setuptools import setup
import os
import sys

if sys.version_info[0] < 3:
    with open('README.md') as f:
        README = f.read()
else:
    with open('README.md', encoding='utf-8') as f:
        README = f.read()

setup(
    name="djeasy",
    version="2.0.1",
    author="Ali Yaman",
    author_email="aliymn.db@gmail.com",
    description="Django Deploy on Server",
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=README,
    keywords="django deploy on server",
    packages=['djeasy', 'djeasy/client', 'djeasy/package'],
    url='https://github.com/AliYmn/djeasy',
    download_url='https://github.com/AliYmn/djeasy',
    install_requires=[
        'termcolor', 'validators',
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': ['djeasy=djeasy.client.management:main']
    }
)
