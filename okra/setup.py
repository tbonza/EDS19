from setuptools import setup, find_packages

setup(
    name='okra',
    version='0.7dev0',
    packages=["okra", "okra/protobuf", "okra/playbooks"],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=[
        'boto3==1.9.93',
        'protobuf==3.6.1',
        'sqlalchemy==1.2.17',
        'eralchemy==1.2.10',
    ],
    scripts=['bin/okra'],
    setup_requires=['pytest-runner'],
    test_requires=[
        'pytest',
    ],
    test_suite='pytest',
    zip_safe=False
)
