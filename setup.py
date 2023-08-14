from setuptools import setup

setup(
  name='cat-in-a-box',
  version='14.8.1',
  author='Paul Bailey',
  author_email='paul@neutrondrive.com',
  url='https://github.com/pizzapanther/Cat-In-A-Box',
  license='LICENSE',
  description='Example Project to Teach Creating Your First Python Package',
  long_description=open('README.md').read(),
  install_requires=['tornado==6.3.3'],
  entry_points = {
      "console_scripts": [
          "cbox = catbox.main:run",
      ],
  },
  include_package_data = True,
  packages = ['catbox']
)
