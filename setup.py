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
    packages=["streamtape"],
    install_requires=[
        "requests",
    ],
    requires_python=">=3.8",
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