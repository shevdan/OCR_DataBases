import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OCR_DataBases", # Replace with your own username
    version="0.0.3",
    author="Bohdan Shevchuk",
    author_email="shevdan007@gmail.com",
    description="Package to prepare data for ML training",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shevdan/OCR_DataBases",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)