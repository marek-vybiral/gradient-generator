import pathlib
from setuptools import setup


def read(f):
    return open(f, 'r', encoding='utf-8').read()


setup(
    name="gradient-generator",
    version="0.1.1",
    description="Generate random but beautiful gradients in a super simple way.",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/marek-vybiral/gradient-generator",
    author="Marek Vybíral",
    author_email="me@marekvybiral.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=["pillow",],
    py_modules=['gradient_generator',],
)
