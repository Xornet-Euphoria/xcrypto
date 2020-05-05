from setuptools import setup, find_packages


print(find_packages(where="src"))

setup(
    name="xcrypto",
    version="0.1",
    install_requires=["pycryptodome"],
    package_dir={"": "src"},
    packages=find_packages("src")
)