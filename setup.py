from distutils.core import setup
import dirt_tongue


#with open("README.md", "r", encoding='utf-8') as t:
#    long_description = t.read()


setup(
    name = "dirt_tongue",
    version = dirt_tongue.__version__,
    author = "Evgeniy Sevostyanihin",
    description = "search russian dirty word",
#    long_description = long_description,  # idk how fix
    packages = ['dirt_tongue'],
    url = "https://github.com/BabylenMagnus/dirt_tongue",
    author_email='sevostyanikhin02@gmail.com',
    license="GPL3",
)
