
import setuptools

setuptools.setup(

    name='pyclasp',
    version='0.5.0',

    author='Matt Wilson',
    author_email='matthew@synesis.com.au',
    description='Command-Line Argument Sorting and Parsing, for Python',
    keywords='Command-line CLI parsing',
    license='BSD-3-Clause',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=['pyclasp', 'examples', 'tests'],
    url='https://github.com/synesissoftware/clasp.Python',
    classifiers=[

        'Intended Audience :: Developers',
        "License :: OSI Approved :: BSD License",
        'Natural Language :: English',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)

