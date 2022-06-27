import setuptools

setuptools.setup(
	name="compressor",
	version="0.1",
	author="Hamano0813",
	description="SRWα Compressor",
	packages=setuptools.find_packages(),
	ext_modules=[setuptools.Extension("compressor", ["program\\compressor.c"])],
)
