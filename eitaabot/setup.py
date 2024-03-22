from setuptools import setup, find_packages

setup(
    name='eitaabot',
    version='1.0.0',
    description='A Python package for interacting with Eitaa Bot API',
    long_description='A Python package that provides a convenient way to interact with Eitaa Bot API.',
    author='AmirhossiKhazai',
    author_email='h34691217@gmail.com',
    url='https://github.com/amirhossinpython/eitaabot',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
