from setuptools import find_packages, setup
setup(
    name='mylibrary',
    packages=find_packages(include=['mylibrary']),
    version='0.1.0',
    description='My first Python library',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)