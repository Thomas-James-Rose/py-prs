from setuptools import setup, find_packages

setup(
    name="py-prs",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pyprs = py_prs:parse",
        ]
    },
    install_requires=[
        "pytest",
        "requests",
    ],
)
