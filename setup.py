from setuptools import setup

setup(
    name='script',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'script=script:main'
        ]
    }
)

