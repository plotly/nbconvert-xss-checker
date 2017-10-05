{#
   This file shares its code partially with streambed.
   Please make sure to update the relevant code in streambed when
   making changes to this file.
#}
<div class="output_subarea output_html rendered_html">
	<div id="{{ unique_div_id }}"
			 style="height: {{ height }}px; width: {{ width }}px;"
			 class="plotly-graph-div">
	</div>

	<div id="figure" type="text/json" style="display:none">
			{{ figure }}
	</div>

	<script type="text/javascript">
			requirejs.config(
							{paths:  {'plotly': ['https://cdn.plot.ly/plotly-latest.min']}},
			);

			if(!window.Plotly) {
					require(['plotly'], function(plotly) {
							window.Plotly=plotly;
					});
			}


	    require(["plotly"], function(Plotly) {

	        window.PLOTLYENV=window.PLOTLYENV || {};
	        window.PLOTLYENV.BASE_URL="{{PLOTLY_BASE_URL}}";

	        var figure = JSON.parse(document.getElementById('figure').innerText);
	        {% if 'frames' in figure %}
	            Plotly.plot(
	                "{{ unique_div_id}}", figure.data, figure.layout
	            ).then(function() {
	                return Plotly.addFrames("{{ unique_div_id }}", figure.frames);
	            }).then(function() {
	                Plotly.animate("{{ unique_div_id }}");
	            })
	        {% else %}
	            Plotly.newPlot("{{ unique_div_id}}", figure.data, figure.layout);
	        {% endif %}
			 });

	</script>
</div>
