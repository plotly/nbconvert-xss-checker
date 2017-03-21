from setuptools import setup

__version__ = '0.0.1'


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='plotlyhtmlexporter',
      version=__version__,
      use_2to3=False,
      author='Tarun G',
      author_email='tarun@plot.ly',
      maintainer='Tarun G',
      maintainer_email='tarun@plot.ly',
      url='https://plot.ly/ipython-notebooks/',
      description="Plotly friendly, Jupyter Notebook HTML Exporter.",
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Scientific/Engineering :: Visualization',
      ],
      license='MIT',
      packages=['plotlyhtmlexporter', ],
      install_requires=['jupyter',
                        'nbconvert>=5.1.1',
                        'nbformat>=4.2'
                        'traitlets',
                        ],
      zip_safe=False,
      entry_points={
          'nbconvert.exporters': [
            'plotlyhtml = plotlyhtmlexporter:PlotlyHTMLExporter',
          ],
      },
      )
