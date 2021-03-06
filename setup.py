import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OCR_DataBases", # Replace with your own username
    version="0.1.0",
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
    install_requires=[
        'absl-py',
        'tensorflow',
        'alabaster',
        'astunparse',
        'azure-cognitiveservices-vision-computervision',
        'azure-common',
        'Babel',
        'cachetools',
        'certifi',
        'chardet',
        'docutils',
        'flatbuffers',
        'gast',
        'google-auth',
        'google-auth-oauthlib',
        'google-pasta',
        'grpcio',
        "h5py",
        'idna' ,
        'imagesize',
        'isodate',
        'Jinja2',
        'keras-nightly',
        'Keras-Preprocessing',
        'Markdown',
        'MarkupSafe',
        'msrest',
        'numpy',
        'oauthlib',
        'opt-einsum',
        'packaging',
        'pathlib',
        'Pillow',
        'protobuf',
        'pyasn1',
        'pyasn1-modules',
        'Pygments',
        'pyparsing',
        'pytz',
        'requests',
        'requests-oauthlib',
        'rsa',
        'six',
        'snowballstemmer',
        'Sphinx',
        'sphinxcontrib-applehelp',
        'sphinxcontrib-devhelp',
        'sphinxcontrib-htmlhelp',
        'sphinxcontrib-jsmath',
        'sphinxcontrib-qthelp',
        'sphinxcontrib-serializinghtml',
        'tensorboard',
        'tensorboard-data-server',
        'tensorboard-plugin-wit',
        'tensorflow-estimator',
        'termcolor',
        'typing-extensions',
        'urllib3',
        'Werkzeug',
        'wrapt',
        'imageio'
    ],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)