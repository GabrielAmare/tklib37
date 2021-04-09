from install37 import setup
from tklib37.__meta__ import __version__

if __name__ == "__main__":
    setup(
        name="tklib37",
        version=__version__,
        author="Gabriel Amare", 
        author_email="gabriel.amare.31@gmail.com",
        description="Tkinter additional widgets library", 
        url="https://github.com/GabrielAmare/tklib37", 
        packages=["tklib37"],
        classifiers=[], 
        python_requires=">=3.7"
    )
