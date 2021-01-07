from distutils.core import setup
import dirt_tongue


setup(
    name = "dirt_tongue",
    version = dirt_tongue.__version__,
    author = "Evgeniy Sevostyanihin",
    description = "search russian dirty word",
    long_description = open('README.md').read(),
    packages = ['dirt_tongue'],
    url = "https://github.com/BabylenMagnus/dirt_tongue",
    author_email='sevostyanikhin02@gmail.com',
    license="GPL3",
)
