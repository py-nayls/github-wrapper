import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-nayls-github-client",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/py-nayls/github-client/",
    packages=["github_client"],

    author="Gagarin Svyatoslav",
    author_email="nayls@bk.ru",
    maintainer="Gagarin Svyatoslav",
    maintainer_email="nayls@bk.ru",

    python_requires=">=3.5",
    install_requires=[
        "pytest>=4.0.1",
        "requests>=2.21.0"
    ],

    classifiers=[
        "Framework :: Pytest"
    ]
)
