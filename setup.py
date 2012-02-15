from setuptools import setup, find_packages

version = __import__('taggittokenfield').VERSION

setup(
		name='django-taggit-tokenfield',
		version='.'.join([str(v) for v in version]),
		description='Autocompleting, tokenizing widget for django-taggit.',
		packages = find_packages(),
	)