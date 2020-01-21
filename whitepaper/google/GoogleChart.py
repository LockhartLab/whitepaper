"""
GoogleChart.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>

Examples
--------
>>> gc = GoogleChart(kind='line')
>>> gc.plot(x, y)
>>> gc.plot(x, y)
>>> gc.legend()
>>> gc.render()
"""

import numpy as np
import pandas as pd
import string
import sys


# Reference to this module
this = sys.modules[__name__]

# Cache to store data in session
this.cache = []


# TODO: split this off into its own package
class GoogleChart:
    """
    Generate the HTML for charts with Google Visualization API
    """

    # Initialize class instance
    def __init__(self, kind='line'):
        """
        Initialize instance of GoogleChart class

        Parameters
        ----------
        kind : str
            Kind of chart to create (e.g., line, ...)
        """

        # Kind of chart
        self.kind = kind

        # Generate _id randomly
        while True:
            _id = ''.join(np.random.choice(list(string.ascii_lowercase), 10))
            if _id not in this.cache:
                break
        this.cache.append(_id)
        self._id = _id

        # Data for plotting
        self._data = pd.DataFrame({'x': []})
        self._labels = []
        self._colors = []
        self._styles = []

        # Chart style
        self._x_title = None
        self._y_title = None
        self._legend = None

    # Legend
    def legend(self, position='bottom'):
        self._legend = position

    # Plot
    def plot(self, x, y, label=None, color=None, style=None):
        # Create label for y if necessary
        if label is None:
            label = 'y' + str(len(self._data.columns) - 1)

        # Create DataFrame for x, y and combine with class data
        _data = pd.DataFrame({'x': x, label: y})
        self._data = self._data.merge(_data, how='outer', on='x')

        # Save information
        self._labels.append(label)
        self._colors.append(color)
        self._styles.append(style)

    # Show the Google Chart
    def show(self, render_loader=True):
        # Render loader if necessary
        output = '' if not render_loader else """
            <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        """

        # Open script section
        output += """
            <script type="text/javascript">
        """

        # Script preamble
        output += """
            google.charts.load("current", {{packages: ["corechart", "{kind}"]}});
            google.charts.setOnLoadCallback(drawChart_{id});
            function drawChart_{id}() {{
        """.format(kind=self.kind, id=self._id)

        # Specify data, initialize options
        output += """
            var data = google.visualization.arrayToDataTable({data});
            var options = {{
        """.format(data=repr(np.vstack([self._data.columns, self._data.values]).tolist()))

        # Formatting for x axis
        output += """
            vAxis: {{title: "{x_title}"}},
        """.format(x_title=self._x_title if self._x_title is not None else '')

        # Formatting for y axis
        output += """
            hAxis: {{title: "{y_title}"}},
        """.format(y_title=self._y_title if self._y_title is not None else '')

        # Legend
        output += """
            legend: {{position: "{legend}"}},
        """.format(legend=self._legend if self._legend is not None else 'none')

        # Close out script
        output += """
            }};
            var chart = new google.visualization.LineChart(document.getElementById("{id}"));
                chart.draw(data, options);
            }}
            </script>
            <div id="{id}" style="width: 100%; height: 300px;"></div>
        """.format(id=self._id)

        # Return
        return output

    # Set x label
    def xlabel(self, label):
        self._x_title = label

    # Set y label
    def ylabel(self, label):
        self._y_title = label
