from setuptools import setup

setup(
    name='cliw',
    version='0.1',
    py_modules=['cliw', 'env'],
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'get-weather=cliw:get_weather',
        ]
    }
)