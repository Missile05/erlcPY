from setuptools import setup, find_packages

setup(
    name='ErlcPY',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['requests'],
    author='Missile / Arimuon',
    description='The First ERLC Python Wrapper',
    url='https://github.com/Arimuon/ErlcPY',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
