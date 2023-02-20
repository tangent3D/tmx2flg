from setuptools import setup, find_packages

setup(
    name="tmx2flg",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        "console_scripts": ["tmx2flg=tmx2flg.cmd:main"]
    },
)
