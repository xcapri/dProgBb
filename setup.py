from setuptools import setup, find_packages

setup(
    name='dProgBb',
    version='1.0',
    description='Detect Program Bug Bounty',
    author='pikpikcu&Hasim',
    author_email='N/A',
    url='https://github.com/pikpikcu/dProgBb',
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'dprog=core.main:main',
        ],
    },
    package_data={'core.helper': ['regex.json', 'path.txt']},
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.11',
    ],
)
