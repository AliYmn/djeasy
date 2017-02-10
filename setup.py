from setuptools import setup

setup(
    name="djeasy",
    version="0.0.1",
    author="Ali Yaman",
    author_email="aliymn.db@gmail.com",
    description="Django Easy Engine",
    license="MIT",
    keywords="django install server",
    packages=['djeasy','djeasy/client','djeasy/package'],
    install_requires=[
        'termcolor',
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': [
            'djeasy = djeasy.client.management:main',
        ]
    }
)