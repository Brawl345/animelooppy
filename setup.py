from setuptools import setup

setup(
    name="animelooppy",
    version="1.0.0",
    description="A simple API wrapper for animeloop.org",
    author="Andreas Bielawski (@Brawl345)",
    url="http://github.com/Brawl345/animelooppy",
    packages=["animelooppy"],
    install_requires=["requests>=2.8"],
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",

        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
)
