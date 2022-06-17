
import ipywidgets as widgets
from IPython.display import display

w = widgets.IntSlider(value=20)
display(w)

w.layout.margin = 'auto'
w.layout.height = '75px'

x = widgets.IntSlider(value=15,description='New slider')
display(x)
