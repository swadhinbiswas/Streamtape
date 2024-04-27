from setuptools import setup



setup(
   
    name="Streamtape",
    version="1.0.0",
    description="Unofficial Streamtape API Wrapper for Python by Swadhin Biswas",
    long_description=open("/home/swadhin/GitHubproject/Streamtape/README.md", "r").read(),
    long_description_content_type="text/markdown,unlimited",
    keywords="api, streamtape, video, hosting",
    url="https://github.com/swadhinbiswas/Streamtape",
    author="Swadhin Biswas",
    author_email="swadhinbiswas.cse@gmail.com",
    packages=["pystreamtape"],
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    zip_safe=False,
)


"""This is the setup.py file for the Streamtape API Wrapper. It contains all the metadata about the package.
    The metadata includes the name, version, description, long description, keywords, URL, author, author email, packages, install_requires, classifiers, and zip_safe.
    The metadata is used by PyPI to display information about the package.
    
    The setup() function is used to create a package distribution. It takes the following arguments:
    - name: The name of the package.
    - version: The version of the package.
    - description: A short description of the package.
    - long_description: A long description of the package.
    - long_description_content_type: The content type of the long description.
    - keywords: Keywords related to the package.
    - url: The URL of the package.
    """