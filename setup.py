from setuptools import find_packages, setup

setup(
    name="bs_python_lib",
    packages=find_packages(include=["bs_python_lib"]),
    version="1.0",
    description="Required models for Barsense serverless Python functions.",
    author="Frederick Holland",
    license="MIT",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
