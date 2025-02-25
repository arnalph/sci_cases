from setuptools import setup, find_packages

setup(
    name="sci_cases",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    author="Arnav Kamath",
    author_email="arnkamath2004@gmail.com",
    description="A package to fetch and parse Supreme Court of India case data",
    url="https://github.com/arnalph/sci_cases",  # Update with your repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
