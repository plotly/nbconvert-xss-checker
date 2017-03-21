from nbconvert.preprocessors.sanitize import SanitizeHTML
from traitlets import Set


class PlotlySanitizeHTML(SanitizeHTML):

    def __init__(self, **kw):
        super(PlotlySanitizeHTML, self).__init__(**kw)

        # Add Plotly key to safe_output_keys:
        safe_keys = self.safe_output_keys.update(['text/vnd.plotly.v1+html'])

    def sanitize_code_outputs(self, outputs):
        """
        Overwritten to allow Plotly outputs be rendered as text/html.

        """
        outputs = super(PlotlySanitizeHTML, self).sanitize_code_outputs(outputs)

        # Make `text/vnd.plotly.v1+html` content (which is trusted)
        # available as `text/html`.
        for output in outputs:
            if output['output_type'] in ('stream', 'error'):
                continue
            data = output.data
            for key in data:
                if key == 'text/vnd.plotly.v1+html':
                    data['text/html'] = data[key]
        return outputs
