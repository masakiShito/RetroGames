# setup.py
from setuptools import setup, find_packages

setup(
    name="retrogames",
    version="0.1.0",
    packages=find_packages(),
    description="A Python library that mimics classic games like Tetris and Snake.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Masaki Shito",
    author_email="happy.engineer.life@gmail.com",
    url="https://github.com/masakiShito/RetroGames",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
