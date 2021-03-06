import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mdsearch", # Replace with your own username
    version="0.0.6",
    author="Low-level Maseter Do Search",
    author_email="3120201103@bit.edu.cn",
    description="mdsearch is a python package for paper search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lydia07/mdsearch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries", 
        "Topic :: Software Development :: Libraries :: Python Modules", 
        "Intended Audience :: Developers", 
    ],
    python_requires='>=3.6',
    install_requires=['elasticsearch5', 'scipy==1.5.4', 'torch==1.7.1', 'transformers==4.1.1', 'flask==1.1.2'],
)