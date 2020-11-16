import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gcp_access_tokens",
    version="0.0.1",
    author="Brighton Balfrey",
    author_email="balfrey@usc.edu",
    description="Fetch GCP api access token via metadata endpoints from GCE instances",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brighton1101/gcp-metadata-access-token",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
