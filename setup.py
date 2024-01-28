import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="ezbmi",
    version="1.0.0",
    description="Calculates and Assesses the BMI",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/anmolsmann/ezbmi",
    author="Anmol Preet Singh",
    author_email="anmolpreet2528@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
    packages=["bmi"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "bmi=bmi.__main__:main",
        ]
    },
)