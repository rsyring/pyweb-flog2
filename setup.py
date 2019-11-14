from setuptools import setup


setup(
    name='flog',
    entry_points={
        'console_scripts': [
            'flog=flog.app:cli'
        ],
    },
)
