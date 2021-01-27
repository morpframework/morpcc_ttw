from setuptools import setup, find_packages
import sys
import os

version = '0.1.0'

def readfile(name):
    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        out = f.read()
    return out

desc = '\n\n'.join([readfile('README.rst'), readfile('CHANGELOG.rst')])

setup(name='morpcc_ttw',
      version=version,
      description="",
      long_description=desc,
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Izhar Firdaus',
      author_email='kagesenshi.87@gmail.com',
      url='http://gitlab.com/morpframework/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      python_requires=">=3.7",
      install_requires=[
          # -*- Extra requirements: -*-
          'morpfw>=0.4.0b1',
          # 
          'morpcc>=0.1.0a4'
          # 
      ],
      extras_require={
          'test': [
              'morpfw[test]',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
