import setuptools
import os.path


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="homework_package",
    version="0.0.1",
    author="Matthew Essenburg",
    author_email="matthew@essenburg.com",
    description="A solution for the Tatari.tv homework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codersbrew/tatari-homework",
    packages=setuptools.find_packages(),
    data_files=[
        # Weird thing you need to put a file in an empty dir /shrug
        ('data', ['data/rotations.csv', 'data/spots.csv']),
        ('output', ['data/rotations.csv', 'data/spots.csv'])
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
