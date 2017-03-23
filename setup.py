from setuptools import setup

setup(
    name='spamfinder',
    version='0.1',
    packages=['spam'],
    url='https://github.com/orf/spam/',
    license='',
    author='orf',
    author_email='tom@tomforb.es',
    description='Find the most common senders in your inbox',
    entry_points={
        'console_scripts': [
            'spam = spam.command:main'
        ]
    },
    install_requires=[
        'tqdm',
        'ascii-graph',
        'docopt'
    ]
)
