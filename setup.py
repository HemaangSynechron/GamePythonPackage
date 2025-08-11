import setuptools

setuptools.setup(
    name="GamesPackage",
    version="0.1a",
    packages=setuptools.find_packages(),
	install_requires=['rich','inquirer','tabulate'],
	author="monke",
	author_email="hemaangsood@gmail.com"
)
