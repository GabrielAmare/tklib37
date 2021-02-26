import setuptools
import pkg_resources

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = list(map(str, pkg_resources.parse_requirements(fh.read())))

setuptools.setup(
    name="tklib37",
    version="1.0.5",
    author="Gabriel Amare",
    author_email="gabriel.amare.31@gmail.com",
    description="Tkinter additional widgets library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    url="https://github.com/GabrielAmare/tklib37",
    packages=['tklib37'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
