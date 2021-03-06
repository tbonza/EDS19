from setuptools import setup, find_packages

setup(
    name='okra',
    version='1.0dev33',
    packages=["okra", "okra/protobuf"],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=[
        'google-cloud-storage==1.14.0',
        'pandas==0.24.2',
        'protobuf==3.6.1',
        'pyarrow==0.13.0',
        'sqlalchemy>=1.3.0',
        'redis==3.2.0',
    ],
    scripts=['bin/okra', 'bin/dokra'],
    setup_requires=['pytest-runner'],
    test_requires=[
        'pytest',
        'pytype',
    ],
    test_suite='pytest',
    zip_safe=False
)
