from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="irfan-razi",
    description="A small package for dvc dl_tf pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/irfan-razi/DVC_DL_TF",
    author_email="15.irfan.razi@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "dvc",
        "tensorflow",
        "matplotlib",
        "pandas",
        "numpy",
        "tqdm",
        "PyYAML",
        "boto3"
    ]
)