from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dissect",
    version="1.0.0",
    author="Fox-IT",
    description="Namespace and collection package for all dissect projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="dissect",
    url="https://github.com/fox-it/dissect",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=[
        'dissect.cstruct'
    ]
)
