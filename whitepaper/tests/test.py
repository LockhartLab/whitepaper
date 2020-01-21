
import numpy as np
import pandas as pd
import whitepaper as wp


# Initialize the Whitepaper
doc = wp.Whitepaper(title='Test')

# Create a section
abstract = wp.Section(title='Abstract', whitepaper=doc)
abstract.add_text("This is me adding abstract text!")
abstract.add_equation('x + y = 7')

# Create another section
introduction = wp.Section(title='Introduction', whitepaper=doc)
introduction.add_text("This is me adding introduction text!")
introduction.add_equation('x + y = 7')

# Add chart to section
x = np.arange(10)
y = np.random.rand(10)
gc = wp.GoogleChart(kind='line')
gc.plot(x, y)
gc.xlabel('x')
gc.ylabel('y')
introduction.add_code(gc.show())

doc.add_section(wp.Text('can I add text as its own section?'))
# x = wp.Section(title='Test', whitepaper=doc)
# x.add_text('test')

# Render
doc.render_html(header=True)


