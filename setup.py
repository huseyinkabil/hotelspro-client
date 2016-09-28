from setuptools import find_packages, setup

setup(
    name='hotelspro_client',
    version='1.1.0',
    packages=find_packages(),
    url='https://github.com/huseyinkabil/hotelspro-client',
    license='GNU GPLv3',
    author='Huseyin Kabil',
    author_email='hsynkabil@gmail.com',
    description='Hotelspro.com api client',
    install_requires=['requests'],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
