from setuptools import setup, find_packages

setup(
    name='pol-parser',
    version='1.0.0',
    description='Parser for Windows .pol (Registry Policy) files',
    author='crwdctrl',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'polparser=polparser:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
