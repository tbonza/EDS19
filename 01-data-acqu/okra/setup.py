from setuptools import setup

setup(
    name='okra',
    version='0.3dev',
    packages=['okra',],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=[
    ],
    scripts=['bin/assn1'],
    setup_requires=['pytest-runner'],
    test_requires=[
        'pytest',
    ],
    test_suite='pytest',
    zip_safe=False
)
