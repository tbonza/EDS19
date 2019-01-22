from setuptools import setup, find_packages

setup(
    name='okra',
    version='0.4dev1',
    packages=["okra", "okra/protobuf"],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=[
        'protobuf==3.6.1',
    ],
    scripts=['bin/assn1'],
    setup_requires=['pytest-runner'],
    test_requires=[
        'pytest',
    ],
    test_suite='pytest',
    zip_safe=False
)
