from setuptools import setup, find_packages

install_requires = ['asyncio']

setup(
    name='client',
    author='',
    author_email='',
    version='0.0.3',
    description='Listen for socket events',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'scripts']),
    entry_points={
        'console_scripts': [
            'client = client.main: main'
        ],
    },
    install_requires=install_requires,
    test_suit='tests',
    zip_safe=False)
