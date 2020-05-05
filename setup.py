import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_osrsapi",
    version="0.0.2",
    author="Chasesc",
    description="Oldschool Runescape API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chasesc/OSRS-API-Wrapper",
    packages=setuptools.find_packages(exclude=["tests"]),
    keywords=[
        "osrs",
        "runescape",
        "jagex",
        "api",
        "grandexchange",
        "hiscores",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', # due to f-strings
    project_urls= {
        'Bug Reports': 'https://github.com/Chasesc/OSRS-API-Wrapper/issues',
        'Source': 'https://github.com/Chasesc/OSRS-API-Wrapper/',
    },
    package_data={
        "" : ["*.json"]
    }
)