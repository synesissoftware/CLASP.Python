
import setuptools

setuptools.setup(

    name="pyclasp",
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*',
    version='0.8.11',

    author="Matt Wilson",
    author_email="matthew@synesis.com.au",
    classifiers=[

        'Intended Audience :: Developers',
        "License :: OSI Approved :: BSD License",
        'Natural Language :: English',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    description="Command-Line Argument Sorting and Parsing, for Python",
    keywords="Command-line CLI parsing",
    license="BSD-3-Clause",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=[
        "examples",
        "tests",
    ]),
    url="https://github.com/synesissoftware/clasp.Python",
)

