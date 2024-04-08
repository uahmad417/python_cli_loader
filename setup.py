from setuptools import setup, find_packages

VERSION = "0.1"
DESCRIPTION = "Python CLI Loader"
LONG_DESCRIPTION = "An animated cli loader for your python scripts"

setup(
    name="cli-loader",
    version=VERSION,
    author="Umair Ahmad",
    author_email="18u.ahmad@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "loader", "animation"],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)