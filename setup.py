from setuptools import setup
from setuptools import find_packages

with open('README.MD') as f:
    long_description = f.read()

setup(
    name='PythonAI',
    version='0.0.5',
    url='www.iamdedeye.com',
    license='MIT',
    long_description=long_description,
    author='Elliott Mitchell',
    author_email='elliott@iamdedeye.com',
    description='dedAI',
    install_requires=[
        'cryptography',
        'csv',
        'pandas',
        'os',
        'json',
        'spotipy',
        'urllib',
        're',
        'pytube',
        'tkinter',
        'functools',
        'multiprocessing',
        'bz2',
        'zipfile',
        'shutil',
        'sounddevice',
        'numpy',
        'scipy',
        'matplotlib',
        'soundfile',
        'gc',
        'time'
    ],
    packages=find_packages()
)
