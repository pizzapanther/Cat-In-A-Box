from distutils.core import setup

setup(
  name='Cat-In-A-Box',
  version='14.8.1',
  author='Paul Bailey',
  author_email='paul@neutrondrive.com',
  packages=['catbox'],
  scripts=['bin/catbox.py'],
  url='https://github.com/pizzapanther/Cat-In-A-Box',
  license='LICENSE',
  description='Example Project to Teach Creating Your First Python Package',
  long_description=open('README.md').read(),
  install_requires=['tornado==4.0'],
)