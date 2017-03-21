==================
PlotlyHTMLExporter
==================

Plotly_ friendly, Jupyter Notebook HTML Exporter.

NBConvert_ is a module to convert `Jupyter Notebooks`_ to other formats (pdf, html etc.).
It supplies `HTMLExporter` which is used to convert Jupyter Notebooks to html.

`PlotlyHTMLExporter` is a custom Exporter derived from `HTMLExporter`. It sanitizes the JS/HTML
present in output cells, but keeps the trusted plotly.js output intact, thus allowing the plotly
charts to be rendered in the resulting html.

Installation:
~~~~~~~~~~~~~

Using `pip`::

    $ pip install plotlyhtmlexporter

From Source::

    $ git clone https://github.com/plotly/plotlyhtmlexporter
    $ cd plotlyhtmlexporter
    $ python setup.py install

Usage:
~~~~~~

From Command Line (with NBConvert)::

    $ jupyter nbconvert --to plotlyhtml mynotebook.ipynb

From the Python interpreter::

    >>> import nbformat
    >>> nb = nbformat.read('mynotebook.ipynb', 4)
    >>> from plotlyhtmlexporter import PlotlyHTMLExporter
    >>> exp = PlotlyHTMLExporter()
    >>> body, resources = exp.from_notebook_node(nb)


License: MIT

    .. _Plotly: https://plot.ly
    .. _Jupyter Notebooks: https://jupyter.org/
    .. _NBConvert: https://nbconvert.readthedocs.io/en/latest/
