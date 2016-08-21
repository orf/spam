from setuptools import setup

setup(
    name='spamfinder',
    version='0.1',
    packages=['spam'],
    url='',
    license='',
    author='orf',
    author_email='tom@tomforb.es',
    description='Find the most common senders in your inbox',
    entry_points={
        'console_scripts': [
            'spam = spam.__main__:main'
        ]
    },
    install_requires = [
        'tqdm',
        'ascii-graph',
        'docopt'
    ]
)
