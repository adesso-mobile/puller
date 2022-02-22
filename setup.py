import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ams_puller",  # Replace with your own username
    version="0.5.0",
    author="adesso mobile solutions GmbH",
    author_email="it-operations@adesso-mobile.de",
    description="An automatic repo puller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adesso-mobile/puller",
    project_urls={
        "Bug Tracker": "https://github.com/adesso-mobile/puller",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["fastapi", "pyyaml", "uvicorn", "shellescape"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={  
        "console_scripts": [
            "puller=puller:start_server",
        ],
    },
)
