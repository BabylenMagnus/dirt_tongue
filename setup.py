from distutils.core import setup, find_packages
import dirt_tongue
import os 


setup(
    name = "dirt_tongue",
    version = dirt_tongue.__version__,
    author = "Evgeniy Sevostyanihin",
    description = "search russian dirty word",
    long_description = open(os.join(dirname(__file__), 'README.md')).read(),
    packages = find_packages(),
    url = "https://github.com/BabylenMagnus/dirt_tongue",
    author_email='sevostyanikhin02@gmail.com',
    license="GPL3",
)