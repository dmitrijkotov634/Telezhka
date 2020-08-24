import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Telezhka",
    version="0.0.11",
    author="dmitrijkotov",
    author_email="dmitrijkotov634@mail.ru",
    description="Telegram bot api library in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmitrijkotov634/Telezhka",
    packages=setuptools.find_packages(),
    license="MIT",
    keywords="Telegram",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    install_requires=[
        "requests"
    ]
)