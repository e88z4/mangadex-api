from setuptools import setup, find_packages

setup(
    name='mangadex-api',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A wrapper for the MangaDex API with synchronous and asynchronous implementations.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'httpx',  # For making HTTP requests
        'asyncio',  # For asynchronous support
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)