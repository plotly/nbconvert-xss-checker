import jinja2
import json
import uuid
import os

from nbconvert.preprocessors.sanitize import SanitizeHTML

DEFAULT_CHART_WIDTH = 600
DEFAULT_CHART_HEIGHT = 400


class PlotlySanitizeHTML(SanitizeHTML):
    template = 'plot.tpl'

    def __init__(self, **kw):
        super(PlotlySanitizeHTML, self).__init__(**kw)
        self.template_file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'templates', 'plot.tpl')

        # Add Plotly JSON key to safe_output_keys:
        safe_keys = self.safe_output_keys.update(['application/vnd.plotly.v1+json'])

    def template(self):
        path, filename = os.path.split(self.template_file)
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(path))
        return env.get_template(filename)

    def sanitize_code_outputs(self, outputs):
        """
        Overwritten to allow Plotly outputs be rendered as text/html.

        """
        outputs = super(PlotlySanitizeHTML, self).sanitize_code_outputs(outputs)

        context = {'unique_div_id': uuid.uuid4()}

        # Parse `application/vnd.plotly.v1+json` content and make it available as 'text/html'
        for output in outputs:
            if output['output_type'] in ('stream', 'error'):
                continue

            data = output.data
            for key in data:
                if key == 'application/vnd.plotly.v1+json':
                    figure = data[key]

                    context['figure'] = json.dumps(figure)
                    context['width'] = figure.get(
                        'layout', {}).get('width', DEFAULT_CHART_WIDTH)
                    context['height'] = figure.get(
                        'layout', {}).get('height', DEFAULT_CHART_HEIGHT)
                    data['text/html'] = self.template().render(**context)

        return outputs
