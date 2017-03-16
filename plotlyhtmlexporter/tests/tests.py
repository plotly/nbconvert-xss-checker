import os
import nbformat

from unittest import TestCase

from plotlyhtmlexporter import PlotlyHTMLExporter, PlotlySanitizeHTML


def get_sample_notebook(filename):

    loc = os.path.join(os.getcwd(), 'files', filename)
    content = open(loc, 'r').read()
    nb = nbformat.reads(content, 4)
    return nb


class TestPlotlySanitizeHTML(TestCase):

    def test_sanitize_html(self):
        # Non Plotly HTML present in the notebook outputs should be escaped.
        nb = get_sample_notebook('plotly_offline.ipynb')

        preprocessor = PlotlySanitizeHTML()

        output, resources = preprocessor.preprocess(nb, [])

        # Cells with Plotly output should remain as it is:
        self.assertEqual(output.cells[0], nb.cells[0])
        self.assertEqual(output.cells[1], nb.cells[1])

        # Cell with general HTML should be sanitized
        expected_output = ('&lt;iframe height="480" src="https://fr.wikipedi'
                           'a.org/wiki/Main_Page" width="640"&gt;&lt;/'
                           'iframe&gt;')
        html_output = output.cells[2].outputs[0]['data']['text/html']
        self.assertEqual(html_output, expected_output)


class TestPlotlyHTMLExporter(TestCase):

    def test_exporter(self):

        # Exporter should convert HTML to text, but retain Plotly charts.
        nb = get_sample_notebook('plotly_offline.ipynb')
        exp = PlotlyHTMLExporter()

        body, resources = exp.from_notebook_node(nb)

        loc = os.path.join(os.getcwd(), 'files', 'plotly_offline.html')
        expected_html = open(loc).read()
        self.assertEqual(body, expected_html)
