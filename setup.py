import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="itay-bardugo/flask_version",
    version="0.0.1",
    author="Itay Bardugo",
    author_email="itaybardugo91@gmail.com",
    description="a package to handle flask routes endpoints by versions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itay-bardugo/flask_version",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)