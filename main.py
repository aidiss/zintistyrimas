from bokeh.io import curdoc, set_curdoc
from bokeh.plotting import figure, output_file, ColumnDataSource
from bokeh.layouts import column, row, widgetbox, layout
from bokeh.models.widgets import TextInput, Paragraph, Div, Select
from bokeh.models import Span, BoxAnnotation, Title
import jinja2

curdoc().template =  jinja2.Template(source='''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>{{ title if title else "Bokeh Plot" }}</title>
        {{ bokeh_css }}
        {{ bokeh_js }}
        <style>
          html {
            width: 100%;
            height: 100%;
          }
          body {
            width: 90%;
            height: 100%;
            margin: auto;
            # font-family: 'Noto Sans', sans-serif;
            #   -webkit-font-smoothing: antialiased;
            #   text-rendering: optimizeLegibility;
            #   color: #fff;
            #   background: #243831;
          }
          .bk-widget input[name$="vard"] {
             min-width: 50px !important;
             width: 100px !important;
           }
           .bk-widget input[name$="pavard"] {
             min-width: 50px !important;
             width: 130px !important;
           }
           .bk-widget input[name$="amz"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="ugis"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="krut"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="juos"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="klub"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="mase"] {
             min-width: 25px !important;
             width: 25px !important;
           }
        </style>
    </head>
    <body>
        {{ plot_div|indent(8) }}
        {{ plot_script|indent(8) }}
    </body>
</html>
''')

factors = ["a", "b", "c", "d", "e", "f", "g", "h"]

source = ColumnDataSource(data=dict(x=[], y=[]))
source1 = ColumnDataSource(data=dict(x=[], y=[]))
source2 = ColumnDataSource(data=dict(x=[], y=[]))
sourcet = ColumnDataSource(data=dict(x=[], y=[]))

p = figure(x_axis_label='kh', y_axis_label='ph', x_range = [-60, 60], y_range = factors, width=350,
            plot_height=150, toolbar_location = None)
p.title.text = "Katabolizmas|Anabolizmas"
p.title.align = "center"
p.yaxis.visible =False
p.xaxis.visible =False

p.add_layout(Span(location=0, dimension='height', line_color='black', line_dash='solid', line_width=4))
p.add_layout(BoxAnnotation(right = 0, left=15, fill_alpha=0.5, fill_color='green'))
p.add_layout(BoxAnnotation(right=15, left=30, fill_alpha=0.5, fill_color='red'))
p.add_layout(BoxAnnotation(right=30, left=45, fill_alpha=0.5, fill_color='DarkRed'))
p.add_layout(BoxAnnotation(right=45, left=60, fill_alpha=0.7, fill_color='DarkRed'))
p.add_layout(BoxAnnotation(right=0, left=-15, fill_alpha=0.5, fill_color='green'))
p.add_layout(BoxAnnotation(left=-15, right=-30, fill_alpha=0.5, fill_color='red'))
p.add_layout(BoxAnnotation(left=-30, right=-45, fill_alpha=0.5, fill_color='DarkRed'))
p.add_layout(BoxAnnotation(left=-45, right=-60, fill_alpha=0.7, fill_color='DarkRed'))

# add a line renderer with legend and line thickness
r = p.circle('x', 'y', source = source, fill_color="orange", line_color="green", line_width=11)
t = p.line('x', 'y', source = sourcet, line_color = "black", line_width = 10)
r1 = p.line('x', 'y', source = source1, line_color = "black", line_width = 10)
r2 = p.line('x', 'y', source = source2, line_color = "black", line_width = 10)

dt = t.data_source
ds = r.data_source
ds1 = r1.data_source
ds2 = r2.data_source

# create some widgets
pav = Div(text = "<b>ORGANIZMO BŪKLĖS TYRIMO PROTOKOLAS</b>", width=500, height=None)

invard = TextInput(name = "vard", value="", title = "Vardas", width = 130)
inpavard = TextInput(name = "pavard", value="", title = "Pavardė", width = 160)
lytis = Select(title="Lytis:", value="", options=["Vyras", "Moteris"], width = 110)
inamz = TextInput(name = "amz", value="", title = "Amžius", width = 80) 
# indata = TextInput(value="", title = "Data")

pav1 = Div(text = "<b>Kūno fiziniai parametrai</b>", width=350)

aprugis = Div(text = "<br>Ūgis (Stovint išsitiesus, centimetrais)</b>", width=250)
inugis = TextInput(name = "ugis", value="", width=220, height=None)

aprkrut = Div(text = "<br>Krūtinės ląstos apimtis (Pažąstų aukštyje, nuleidus rankas, centimetrais)", width=250)
inkrut = TextInput(name = "krut", value="", width=220, height=None)

aprjuos = Div(text = "<br>Juosmens apimtis (Per siauriausią vietą, centimetrais)", width=250)
injuos = TextInput(name = "juos", value="", width=220, height=None)

aprklub = Div(text = "<br>Klubų apimtis (Per plačiausią vietą, maždaug genitalijų aukštyje, centimetrais)", width=250)
inklub= TextInput(name = "klub", value="", width=220, height=None)

aprmase = Div(text = "<br>Masė (Ryte, išsituštinus, pasišlapinus, nusirengus, kg)", width=250)
inmase= TextInput(name = "mase", value="", width=220, height=None)

pav2 = Div(text = "<b>Šlapimo parametrai</b>", width=550, height=None)

input = TextInput(name = "input", value="", title = "Ivesk ph")
input1 = TextInput(name = "input1", value="", title = "Ivesk seiliu ph")
input2 = TextInput(name = "input2", value="", title = "Ivesk")
# input3= TextInput(value="", title = "Ivesk ph")
# input4 = TextInput(value="", title = "Ivesk seiliu ph")
# input5 = TextInput(value="", title = "Ivesk")

# add a callback to a widget

def t_update(attr, old, new):
	b = float(input.value)
	t_new_data={'x':[0,b],'y':[1,1]}
	sourcet.data.update(t_new_data)
input.on_change("value", t_update)


def update1(attr, old, new):
	b1 = float(input1.value)
	new_data1={'x':[0, b1*1.5],'y':[2, 2]}
	source1.data.update(new_data1)
input1.on_change("value", update1)

def update2(attr, old, new):
	b2 = float(input2.value)
	if b2 < 50:
		new_data2={'x':[0, b2*-1.5],'y':[3, 3]}
		source2.data.update(new_data2)
	else:
		new_data2={'x':[0, b2*1.5],'y':[3, 3]}
		source2.data.update(new_data2)
input2.on_change("value", update2)

# create a layout for everything
# varpavdata = row(invard, inpavard, indata)
# lytamzugis = row(inlyt, inamz, inugis)
# pav1 = column(output1, lytamzugis)
# krutjuosklub = row(inpkrut, injuos, inklub)
# layout = row(input, input1, input2)
# out = row(layout, p, )
# bendr = column(varpavdata, pav1, krutjuosklub, inmase, output2, out)
# layout1 = column(output, bendr)


l = layout(children=[[pav],
	[invard , inpavard, lytis, inamz],
	[pav1, pav2],
	[aprugis, inugis],
	[aprkrut, inkrut],
	[aprjuos, injuos],
	[aprklub, inklub],
	[aprmase, inmase],
	[input2, p]
	])

# add the layout to curdoc
curdoc().add_root(l)
