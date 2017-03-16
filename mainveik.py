from bokeh.io import curdoc, set_curdoc
from bokeh.plotting import figure, output_file, ColumnDataSource
from bokeh.layouts import column, row, widgetbox, layout
from bokeh.models.widgets import TextInput, Paragraph, Div, Select
from bokeh.core.properties import Dict, Int, String
from bokeh.models import Span, BoxAnnotation, Title, ColorBar, LinearColorMapper, Plot, Range1d, LinearAxis, FixedTicker, FuncTickFormatter, NumeralTickFormatter
from bokeh.util.compiler import CoffeeScript
from bokeh.models.ranges import DataRange1d, FactorRange
import jinja2
import math

curdoc().template =  jinja2.Template(source='''
	<!DOCTYPE html>
	<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>{{ title if title else "Bokeh Plot" }}</title>
        {{ bokeh_css }}
        {{ bokeh_js }}
        <style>
        @import url(https://fonts.googleapis.com/css?family=Noto+Sans);
          body {
            width: 90%;
            height: 100%;
            margin: auto;
            text-align: justify;
            text-justify: inter-word;
            font-family: 'Noto Sans', sans-serif;
            -webkit-font-smoothing: antialiased;
            text-rendering: optimizeLegibility;
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
           .bk-widget input[name$="rytas1"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus1"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras1"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas2"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus2"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras2"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas3"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus3"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras3"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas4"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus4"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras4"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas5"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus5"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras5"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas6"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus6"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras6"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas7"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus7"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras7"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas8"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus8"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras8"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas9"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus9"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras9"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas10"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus10"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras10"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas11"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus11"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras11"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas12"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus12"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras12"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas13"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus13"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras13"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas14"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus14"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras14"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas15"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus15"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras15"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas16"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus16"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras16"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas17"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus17"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras17"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas18"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus18"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras18"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas19"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus19"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras19"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas20"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus20"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras20"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas21"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus21"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras21"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas22"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus22"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras22"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas23"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus23"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras23"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="rytas24"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="pietus24"] {
             min-width: 25px !important;
             width: 25px !important;
           }
           .bk-widget input[name$="vakaras24"] {
             min-width: 25px !important;
             width: 25px !important;
           }


 #outer-circle {
   background: white;
   border-radius: 50%;
   border: 1px solid;
   height: 40px;
   width: 40px;
   position: relative;
 }
 #inner-circle {
   position: absolute;
   background: black;
   border-radius: 50%;
   height: 24px;
   width: 24px;
   top: 20%;
   left: 20%;
   margin: 50x 50px 50px 50x;
 }
 #outer-circle1 {
   background: white;
   border-radius: 50%;
   border: 1px solid;
   height: 40px;
   width: 40px;
   position: relative;
 }
 #inner-circle1 {
   position: absolute;
   background: black;
   border-radius: 50%;
   height: 22px;
   width: 22px;
   top: 22%;
   left: 22%;
   margin: 50x 50px 50px 50x;
 }
#outer-circle2 {
   background: white;
   border-radius: 50%;
   border: 1px solid;
   height: 40px;
   width: 40px;
   position: relative;
 }
 #inner-circle2 {
   position: absolute;
   background: black;
   border-radius: 50%;
   height: 20px;
   width: 20px;
   top: 24%;
   left: 24%;
   margin: 50x 50px 50px 50x;
 }
#outer-circle3 {
   background: white;
   border-radius: 50%;
   border: 1px solid;
   height: 40px;
   width: 40px;
   position: relative;
 }
 #inner-circle3 {
   position: absolute;
   background: black;
   border-radius: 50%;
   height: 18px;
   width: 18px;
   top: 26%;
   left: 26%;
   margin: 50x 50px 50px 50x;
 }
 #outer-circle4 {
   background: white;
   border-radius: 50%;
   border: 1px solid;
   height: 40px;
   width: 40px;
   position: relative;
 }
 #inner-circle4 {
   position: absolute;
   background: black;
   border-radius: 50%;
   height: 16px;
   width: 16px;
   top: 28%;
   left: 28%;
   margin: 50x 50px 50px 50x;
 }
 #outer-circle5 {
   background: white;
   border-radius: 50%;
   border: 1px solid;
   height: 40px;
   width: 40px;
   position: relative;
 }
 #inner-circle5 {
   position: absolute;
   background: black;
   border-radius: 50%;
   height: 14px;
   width: 14px;
   top: 30%;
   left: 30%;
   margin: 50x 50px 50px 50x;
 }
#outer-circle6 {
   background: white;
   border-radius: 50%;
   border: 1px solid;
   height: 40px;
   width: 40px;
   position: relative;
 }
 #inner-circle6 {
   position: absolute;
   background: black;
   border-radius: 50%;
   height: 12px;
   width: 12px;
   top: 32%;
   left: 32%;
   margin: 50x 50px 50px 50x;
 }
 #outer-circle7 {
   background: white;
   border-radius: 50%;
   border: 1px solid;
   height: 40px;
   width: 40px;
   position: relative;
 }
 #inner-circle7 {
   position: absolute;
   background: black;
   border-radius: 50%;
   height: 10px;
   width: 10px;
   top: 34%;
   left: 34%;
   margin: 50x 50px 50px 50x;
 }
 #outer-circle8{
   background: white;
   border-radius: 50%;
   border: 1px solid;
   height: 40px;
   width: 40px;
   position: relative;
 }
 #inner-circle8 {
   position: absolute;
   background: black;
   border-radius: 50%;
   height: 8px;
   width: 8px;
   top: 38%;
   left: 38%;
   margin: 50x 50px 50px 50x;
 }


.foo {
  float: left;
  width: 20px;
  height: 20px;
  margin: 5px;
  border: 1px solid rgba(0, 0, 0, .2);
}

.blue {
  background: #13b4ff;
}

.purple {
  background: #ab3fdd;
}

.wine {
  background: #ae163e;
}





table {
  border-collapse: collapse;
  margin-bottom:3%;
}
th,td {
  border: 1px solid #c6c7cc;
  padding: 10px 15px;
}
th {
  font-weight: bold;
}



.overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(1, 0, 0, 0.8);
  transition: opacity 0ms;
  visibility: hidden;
  opacity: 1;
  overflow-y:scroll;
  z-index: 99;
}
.overlay:target {
  visibility: visible;
  opacity: 1;
}

.popup {
  margin: 70px auto;
  padding: 20px;
  background: #fff;
  border-radius: 5px;
  width: 30%;
  position: relative;
}

.popup h2 {
  color: #333;
  padding: 
  font-family: Verdana, Arial, sans-serif;
}
.popup .close {
  position: absolute;
  right: 20px;
  bottom:0px;
  padding: 0 20 20 0:
  transition: all 0ms;
  font-size: 30px;
  font-weight: bold;
  text-decoration: none;
  color: #333;
}
.popup .close:hover {
  color: #06D85F;
}
.popup .content {
  max-height: 50%;
  overflow: auto;
  text-align: justify;
  text-justify: inter-word;
}

@media screen and (max-width: 100%){
  .box{
    width: 80%;
  }
  .popup{
    width: 80%;
  }
}
           </style>
    </head>
    <body>
        {{ plot_div|indent(8) }}
        {{ plot_script|indent(8) }}
    </body>
</html>
''')

factorssp = ["sklv", "sargv", "nosv", "tremv", "vyzdv", "vasov", "dermv", "tempv", "kriv", "ppv", "sdv", "ps1v", "bla1", "sklp", "sargp", "nosp", "tremp", "vyzdp",
"vasop", "dermp", "tempp", "krip", "ppp", "sdp", "ps1p", "sklr", "sargr", "nosr", "tremr", "vyzdr", "vasor", "dermr", "tempr", "krir", "ppr", "sdr", "ps1r", 
"bla3"]

count = len(factorssp)

p = figure(x_range = [-5, 5], y_range=FactorRange(factors=factorssp), height = 350, tools= "")
p.title.text = "<-Katabolizmas|Anabolizmas->"
p.title.align = "center"
p.text(x=[-4.7], y =[(count-12)], text = ["Rytas"], text_font_size='10pt', text_font_style = "bold", angle = 1.56)
p.text(x=[-4.7], y =[(count-24)], text = ["Pietūs"], text_font_size='10pt', text_font_style = "bold", angle = 1.56)
p.text(x=[-4.7], y =[(count-(count-1))], text = ["Vakaras"], text_font_size='10pt', text_font_style = "bold", angle = 1.56)
p.x_range.bounds = 'auto'
p.y_range.bounds = 'auto'
p.xaxis.axis_label = '<-Simpatinis|Parasimpatinis->'
p.yaxis.visible =False
p.xaxis.ticker = FixedTicker(ticks=[-4, -3, -2, -1, 1, 2, 3, 4])
p.xaxis.formatter = FuncTickFormatter(code="""
    data = {"-4": "Didelis", "-3": "Vidutinis", "-2": 'Mažas', "-1": "Norma", 1: 'Norma', 2: 'Mažas', 3: 'Vidutinis', 4: 'Didelis'}
    return data[tick]
""")

p1 = figure(x_range = [-65, 65], y_range = factorssp, height = 350, toolbar_location = None)
p1.title.text = "<-Katabolizmas|Anabolizmas->"
p1.title.align = "center"
p1.text(x=[-62], y =[(count-12)], text = ["Rytas"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p1.text(x=[-62], y =[(count-24)], text = ["Pietūs"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p1.text(x=[-62], y =[(count-(count-1))], text = ["Vakaras"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p1.x_range.bounds = 'auto'
p1.y_range.bounds = 'auto'
p1.xaxis.axis_label = '<-Simpatinis|Parasimpatinis->'
p1.yaxis.visible =False
p1.xaxis.ticker = FixedTicker(ticks=[-60, -45, -30, -15, 15, 30, 45, 60])
p1.xaxis.formatter = FuncTickFormatter(code="""
    data = {"-60": "Didelis", "-45": "Vidutinis", "-30": 'Mažas', "-15": "Norma", 15: 'Norma', 30: 'Mažas', 45: 'Vidutinis', 60: 'Didelis', 65: "Didelis"}
    return data[tick]
""")

p2 = figure(x_range = [-65, 65], y_range = factorssp, height = 350, toolbar_location = None)
p2.title.text = "<-Katabolizmas|Anabolizmas->"
p2.title.align = "center"
p2.text(x=[-62], y =[(count-12)], text = ["Rytas"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p2.text(x=[-62], y =[(count-24)], text = ["Pietūs"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p2.text(x=[-62], y =[(count-(count-1))], text = ["Vakaras"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p2.x_range.bounds = 'auto'
p2.y_range.bounds = 'auto'
p2.xaxis.axis_label = '<-Simpatinis|Parasimpatinis->'
p2.yaxis.visible =False
p2.xaxis.ticker = FixedTicker(ticks=[-60, -45, -30, -15, 15, 30, 45, 60])
p2.xaxis.formatter = FuncTickFormatter(code="""
    data = {"-60": "Didelis", "-45": "Vidutinis", "-30": 'Mažas', "-15": "Norma", 15: 'Norma', 30: 'Mažas', 45: 'Vidutinis', 60: 'Didelis', 65: "Didelis"}
    return data[tick]
""")

p3 = figure(x_range = [-65, 65], y_range = factorssp, height = 350, toolbar_location = None)
p3.title.text = "<-Katabolizmas|Anabolizmas->"
p3.title.align = "center"
p3.text(x=[-62], y =[(count-12)], text = ["Rytas"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p3.text(x=[-62], y =[(count-24)], text = ["Pietūs"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p3.text(x=[-62], y =[(count-(count-1))], text = ["Vakaras"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p3.x_range.bounds = 'auto'
p3.y_range.bounds = 'auto'
p3.xaxis.axis_label = '<-Simpatinis|Parasimpatinis->'
p3.yaxis.visible =False
p3.xaxis.ticker = FixedTicker(ticks=[-60, -45, -30, -15, 15, 30, 45, 60])
p3.xaxis.formatter = FuncTickFormatter(code="""
    data = {"-60": "Didelis", "-45": "Vidutinis", "-30": 'Mažas', "-15": "Norma", 15: 'Norma', 30: 'Mažas', 45: 'Vidutinis', 60: 'Didelis', 65: "Didelis"}
    return data[tick]
""")

p4 = figure(x_range = [-65, 65], y_range = factorssp, height = 350, toolbar_location = None)
p4.title.text = "<-Katabolizmas|Anabolizmas->"
p4.title.align = "center"
p4.text(x=[-62], y =[(count-12)], text = ["Rytas"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p4.text(x=[-62], y =[(count-24)], text = ["Pietūs"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p4.text(x=[-62], y =[(count-(count-1))], text = ["Vakaras"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p4.x_range.bounds = 'auto'
p4.y_range.bounds = 'auto'
p4.xaxis.axis_label = '<-Simpatinis|Parasimpatinis->'
p4.yaxis.visible =False
p4.xaxis.ticker = FixedTicker(ticks=[-60, -45, -30, -15, 15, 30, 45, 60])
p4.xaxis.formatter = FuncTickFormatter(code="""
    data = {"-60": "Didelis", "-45": "Vidutinis", "-30": 'Mažas', "-15": "Norma", 15: 'Norma', 30: 'Mažas', 45: 'Vidutinis', 60: 'Didelis', 65: "Didelis"}
    return data[tick]
""")

p5 = figure(x_range = [-65, 65], y_range = factorssp, height = 350, toolbar_location = None)
p5.title.text = "<-Katabolizmas|Anabolizmas->"
p5.title.align = "center"
p5.text(x=[-62], y =[(count-12)], text = ["Rytas"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p5.text(x=[-62], y =[(count-24)], text = ["Pietūs"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p5.text(x=[-62], y =[(count-(count-1))], text = ["Vakaras"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p5.x_range.bounds = 'auto'
p5.y_range.bounds = 'auto'
p5.xaxis.axis_label = '<-Simpatinis|Parasimpatinis->'
p5.yaxis.visible =False
p5.xaxis.ticker = FixedTicker(ticks=[-60, -45, -30, -15, 15, 30, 45, 60])
p5.xaxis.formatter = FuncTickFormatter(code="""
    data = {"-60": "Didelis", "-45": "Vidutinis", "-30": 'Mažas', "-15": "Norma", 15: 'Norma', 30: 'Mažas', 45: 'Vidutinis', 60: 'Didelis', 65: "Didelis"}
    return data[tick]
""")

p6 = figure(x_range = [-65, 65], y_range = factorssp, height = 350, toolbar_location = None)
p6.title.text = "<-Katabolizmas|Anabolizmas->"
p6.title.align = "center"
p6.text(x=[-62], y =[(count-12)], text = ["Rytas"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p6.text(x=[-62], y =[(count-24)], text = ["Pietūs"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p6.text(x=[-62], y =[(count-(count-1))], text = ["Vakaras"], text_font_size='10pt', text_font_style = "bold", angle = 1.55)
p6.x_range.bounds = 'auto'
p6.y_range.bounds = 'auto'
p6.xaxis.axis_label = '<-Simpatinis|Parasimpatinis->'
p6.yaxis.visible =False
p6.xaxis.ticker = FixedTicker(ticks=[-60, -45, -30, -15, 15, 30, 45, 60])
p6.xaxis.formatter = FuncTickFormatter(code="""
    data = {"-60": "Didelis", "-45": "Vidutinis", "-30": 'Mažas', "-15": "Norma", 15: 'Norma', 30: 'Mažas', 45: 'Vidutinis', 60: 'Didelis', 65: "Didelis"}
    return data[tick]
""")

p.add_layout(Span(location=0, dimension='height', line_color='black', line_dash='solid', line_width=4))
p.add_layout(Span(location=1, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p.add_layout(Span(location=-1, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p.add_layout(Span(location=2, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p.add_layout(Span(location=-2, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p.add_layout(Span(location=3, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p.add_layout(Span(location=-3, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p.add_layout(Span(location=4, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p.add_layout(Span(location=-4, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p.add_layout(BoxAnnotation(top = 13, fill_alpha=0.1, fill_color='black'))
p.add_layout(BoxAnnotation(bottom = 13, top = 25, fill_alpha=0.1, fill_color='cyan'))
p.add_layout(BoxAnnotation(top=count, fill_alpha=0.1, fill_color='yellow'))

p1.add_layout(Span(location=0, dimension='height', line_color='black', line_dash='solid', line_width=4))
p1.add_layout(Span(location=15, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p1.add_layout(Span(location=-15, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p1.add_layout(Span(location=30, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p1.add_layout(Span(location=-30, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p1.add_layout(Span(location=45, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p1.add_layout(Span(location=-45, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p1.add_layout(Span(location=60, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p1.add_layout(Span(location=-60, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p1.add_layout(BoxAnnotation(top = 12, fill_alpha=0.4, fill_color='yellow'))
p1.add_layout(BoxAnnotation(bottom = 12, top = 24, fill_alpha=0.2, fill_color='yellow'))
p1.add_layout(BoxAnnotation(top=36, fill_alpha=0.1, fill_color='yellow'))

p2.add_layout(Span(location=0, dimension='height', line_color='black', line_dash='solid', line_width=4))
p2.add_layout(Span(location=15, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p2.add_layout(Span(location=-15, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p2.add_layout(Span(location=30, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p2.add_layout(Span(location=-30, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p2.add_layout(Span(location=45, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p2.add_layout(Span(location=-45, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p2.add_layout(Span(location=60, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p2.add_layout(Span(location=-60, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p2.add_layout(BoxAnnotation(top = 12, fill_alpha=0.4, fill_color='yellow'))
p2.add_layout(BoxAnnotation(bottom = 12, top = 24, fill_alpha=0.2, fill_color='yellow'))
p2.add_layout(BoxAnnotation(top=36, fill_alpha=0.1, fill_color='yellow'))

p3.add_layout(Span(location=0, dimension='height', line_color='black', line_dash='solid', line_width=4))
p3.add_layout(Span(location=15, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p3.add_layout(Span(location=-15, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p3.add_layout(Span(location=30, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p3.add_layout(Span(location=-30, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p3.add_layout(Span(location=45, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p3.add_layout(Span(location=-45, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p3.add_layout(Span(location=60, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p3.add_layout(Span(location=-60, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p3.add_layout(BoxAnnotation(top = 12, fill_alpha=0.4, fill_color='yellow'))
p3.add_layout(BoxAnnotation(bottom = 12, top = 24, fill_alpha=0.2, fill_color='yellow'))
p3.add_layout(BoxAnnotation(top=36, fill_alpha=0.1, fill_color='yellow'))

p4.add_layout(Span(location=0, dimension='height', line_color='black', line_dash='solid', line_width=4))
p4.add_layout(Span(location=15, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p4.add_layout(Span(location=-15, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p4.add_layout(Span(location=30, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p4.add_layout(Span(location=-30, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p4.add_layout(Span(location=45, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p4.add_layout(Span(location=-45, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p4.add_layout(Span(location=60, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p4.add_layout(Span(location=-60, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p4.add_layout(BoxAnnotation(top = 12, fill_alpha=0.4, fill_color='yellow'))
p4.add_layout(BoxAnnotation(bottom = 12, top = 24, fill_alpha=0.2, fill_color='yellow'))
p4.add_layout(BoxAnnotation(top=36, fill_alpha=0.1, fill_color='yellow'))

p5.add_layout(Span(location=0, dimension='height', line_color='black', line_dash='solid', line_width=4))
p5.add_layout(Span(location=15, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p5.add_layout(Span(location=-15, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p5.add_layout(Span(location=30, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p5.add_layout(Span(location=-30, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p5.add_layout(Span(location=45, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p5.add_layout(Span(location=-45, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p5.add_layout(Span(location=60, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p5.add_layout(Span(location=-60, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p5.add_layout(BoxAnnotation(top = 12, fill_alpha=0.4, fill_color='yellow'))
p5.add_layout(BoxAnnotation(bottom = 12, top = 24, fill_alpha=0.2, fill_color='yellow'))
p5.add_layout(BoxAnnotation(top=36, fill_alpha=0.1, fill_color='yellow'))

p6.add_layout(Span(location=0, dimension='height', line_color='black', line_dash='solid', line_width=4))
p6.add_layout(Span(location=15, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p6.add_layout(Span(location=-15, dimension='height', line_color='green', line_dash='dashed', line_width=4))
p6.add_layout(Span(location=30, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p6.add_layout(Span(location=-30, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
p6.add_layout(Span(location=45, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p6.add_layout(Span(location=-45, dimension='height', line_color='red', line_dash='dashed', line_width=4))
p6.add_layout(Span(location=60, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p6.add_layout(Span(location=-60, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
p6.add_layout(BoxAnnotation(top = 12, fill_alpha=0.4, fill_color='yellow'))
p6.add_layout(BoxAnnotation(bottom = 12, top = 24, fill_alpha=0.2, fill_color='yellow'))
p6.add_layout(BoxAnnotation(top=36, fill_alpha=0.1, fill_color='yellow'))


# create some widgets
def protok():
    return Div(text="""<br><b>ORGANIZMO BŪKLĖS TYRIMO PROTOKOLAS</b>""", width=330, height=None)

invard = TextInput(name = "vard", value="", title = "Vardas", width = 130)
inpavard = TextInput(name = "pavard", value="", title = "Pavardė", width = 160)
lytis = Select(title="Lytis:", value="", options=["Vyras", "Moteris"], width = 110)
inamz = TextInput(name = "amz", value="", title = "Amžius", width = 80) 

def tikslus():
    return Div(text="""Tikslūs organizmo tyrimo metu atliekamų testų rezultatai padeda geriau suprasti
organizme vykstančius procesus, todėl tinkamas pasirengimas tyrimui yra labai svarbus
tikrajai Jūsų organizmo būklei nustatyti:""", width=780)

def eiga():
    return Div(text="""<b>ORGANIZMO BŪKLĖS TYRIMO EIGA</b>
<br><br>Organizmo būklės nustatymo tikslumui lemiamos įtakos turi tikslūs organizmo parametrų išmatavimai. Šiuos parametrus stipriai veikia tiriamojo psichologinė būklė tyrimo metu, taip pat matavimų eilės tvarka. Svarbu, kad organizmo būklės tyrimas būtų vykdomas griežtai pagal nurodytą seką. Taip pat rekomenduotina kelias dienas iki tyrimo pasipraktikuoti jį atlikti, kad tyrimo dieną viskas vyktų sklandžiai. Tyrimo trukmė apie 45 minutės. Pamatuoti duomenys rašomi į <b>„Organizmo būklės tyrimo formos“</b> skiltį <b><i>„Tyrimo protokolas“</i></b>.
<br><br><b>PRIEMONĖS</b>:
<br>•pH metras arba daugiaspalėvės rūgštingumo matavimo juostelės (tikslumas bent 0,5, minimalios skalės ribos nuo 4,5 iki 8)
<br>•Areometras (kuo mažesnis, minimalios skalės ribos nuo 1,000 g/ml iki 1,030 g/ml) ir pritaikytas matavimo cilindras jam.
<br>•Chronometras
<br>•Skaitmeninis kraujospūdžio matuoklis (su manžete ant žasto)
<br>•Kūno termometras
<br>•Kūno svarstyklės
<br>•Indeliai šlapimo mėginiams
<br>•Įrankis brėžimui neužapvalintu galu (įtrauktas tušinukas, bambukinė lazdelė ir pan.)
<br>•Popierinis rankšluostis
<br>•Valgomasis šaukštas
<br>•Minkštas metras
<br><br><b>TYRIMO EIGA:</b>
<br><b>1.</b> 2 valandos iki tyrimo <b><i>nevalgyti</b></i>, jei norisi, <b><i>galima gerti negazuoto vandens</b></i>.
<br><b>2.</b> 30 minučių iki tyrimo <b><i>nieko negerti ir nekramtyti</b></i>.""", width=780)

def slapimo():
    return Div(text="""<b>3. Šlapimo parametrų matavimas:</b>""", width=780)

def prikseil():
    return Div(text="""<b>4.</b><i>Tiriamojo paprašoma prikaupti seilių ir įspjauti į valgomąjį šaukštą. Seilių turi būti
maždaug mažojo piršto galinio narelio dydžio lašas.</i>""", width=780)

def seiliu():
    return Div(text="""<b>5. Seilių parametrų matavimas:</b>""", width=780)

def tiriam():
    return Div(text="""<b>6.</b><i>Tiriamojo paprašoma atsisėsti ant sofos arba lovos per vidurį.</i>""", width=780)

def kraujot():
    return Div(text="""<b>7. Kraujotakos parametrų matavimas:</b>""", width=780)

def refleksu():
    return Div(text="""<b>8. Refleksų tyrimas:</b>""", width=780)

def tiriam1():
    return Div(text="""<i>Tiriamojo paprašoma atsigulti ant sofos ar lovos ant kurios sėdi. Gulamasi
ištiestomis kojomis, galvą dedant taip, kad prie sofos ar lovos krašto būtų tiriamojo kairė
pusė. Paliekamas toks tarpas nuo sofos ar lovos krašto, kad tiriamojo kairė ranka laisvai
gulėtų šalia delnu į viršų. Paprašoma atsipalaiduoti, nekalbėti ir nusiraminti. Taip
tiriamasis turi pagulėti daugiau nei 1 minutę.</i>""", width=780)

def tiriam2():
    return Div(text="""<b>9.</b><i>Tiriamajam pranešama, kad jis jau gali užsidengti pilvą ir paprašoma atsipalaiduoti,
nekalbėti ir nusiraminti. Taip tiriamasis turi pagulėti daugiau nei 1 minutę.</i>""", width=780)

def kvepparmat10():
    return Div(text="""<b>10. Kvėpavimo parametrų matavimas:</b>""", width=780)

def tiriam3():
    return Div(text="""<b>11.</b> <i>Tiriamajam ant kairės rankos žasto uždedama kraujospūdžio matavimo manžetė.</i>""", width=780)

def kraujparmat():
    return Div(text="""<b>12. Kraujotakos parametrų matavimas:</b>""", width=780)

def ortatest():
    return Div(text="""<b>Ortostatinis testas.</b> Tiriamajam atsistojus, kraujospūdžio matuoklio žarnelė neturi
būti tempiama, todėl matuoklį reikia <i>padėti ant paaukštinimo, pritvirtinti prie manžetės
arba duoti laikyti tiriamajam laisvoje rankoje</i>.
<br>• Tiriamajam pranešama, kad paprašius reikės RAMIAI atsistoti šalia ir atsisėsti
TIK LEIDUS.
<br>• Įjungiamas kraujospūdžio matuoklis ir jo pompa paimama dešinės rankos
mažyliu, bevardžiu ir didžiuoju pirštais, taip pat į dešinę ranką paimamas
chronometras ir laikomas taip, kad smiliumi arba nykščiu būtų galima lengvai
nuspausti paleidimo mygtuką.
<br>• Kaire ranka užčiuopiamas tiriamojo pulsas kairėje rankoje taip, kaip nurodyta 8
punkte. Riešą reikia apminti patogiai, kad pirštai testo metu nenuslystų, ir tam,
kad būtų galima testo metu lengvai koreguoti jų padėtį.
<br>• <i>Tiriamojo paprašoma atsistoti</i>. Jo kairė ranka laikoma sulenkta stačiu kampu.
Tiriamajam besistojant, Jūs turite likti sėdėti.""", width=780)

def atsist():
    return Div(text="""<br>Atsistojus<br>(dūžių skaičius per pirmas 15 s,×4)""", width=300)

def po15():
    return Div(text="""<br>Po 15 s.<br>(dūžių skaičius tarp 15-tos ir 45-tos sekundės,×2)""", width=300)

def siskraujatsi():
    return Div(text="""<br>Sistolinis kraujospūdis atsistojus<br>(rodmuo ekrane ties „SYS“ po 45 s)""", width=300)

def diaskraujatsi():
    return Div(text="""<br>Diastolinis kraujospūdis atsistojus<br>(rodmuo ekrane ties „DIA“)""", width=300)

def pulsatsi45():
    return Div(text="""<br>Pulsas atsistojus po 45 s<br>(rodmuo ekrane ties „PULS“)""", width=300)

def tiriam4():
    return Div(text="""<b>13.</b><i> Nuimama manžetė nuo tiriamojo žasto.</i>""", width=780)

def kvepparmat14():
    return Div(text="""<b>14. Kvėpavimo parametrų matavimas:</b>""", width=780)

def kataanab():
    return Div(text="""<b>KATABOLIZMAS|ANABOLIZMAS</b>""", width=780)


def pav1():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup1">3-2 SAVAITĖS IKI TYRIMŲ DIENOS</a>
</div>

<div id="popup1" class="overlay">
    <div class="popup" id="showpopup">
        <h2>3-2 SAVAITĖS IKI TYRIMŲ DIENOS</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Jei tai pirmasis tyrimas, pradedama keisti mityba, jei tai pakartotinis tyrimas, toliau
maitinamasi pagal ankstesnio tyrimo metu pateiktas rekomendacijas. Mitybos keitimas
reikalingas norint padėti:
<br>• organizmui „atidengti“ nukrypimus, nes be pasirengimo, dažnai stebima tiek daug
išsibalansavusių parametrų, kad neįmanoma atskirti nukrypimų.
<br>• tiriamajam įsitikinti, ar šis sveikatinimosi kelias jam tinkamas, nes nustačius
nukrypimų, reikalavimai gali likti tokie patys, sugriežtėti arba sušvelnėti.
<br>• atsistatyti storojo žarnyno mikroflorai, nes nustojus vartoti krakmolą ir pradėjus vartoti
daugiau inertinų (ląstelienos) mikroflora persitvarko mažiausiai per 2 sav.
<br>Keičiant mitybą reikia nustoti vartoti šiuos produktus:
<br><b>Krakmolo šaltinius:</b> <i>Bulves ir jų produktus (traškučius, lietuviškas mišraines, tirštas
sriubas, kisielių ir pan.), miltų gaminius (duoną, batoną, bandeles, pyragus, blynus,
makaronus ir pan.), grūdus (kviečius, rugius, ryžius, grikius, avižas, miežius, soras ir pan.),
visas kruopas, dribsnius, ankštinius (pupas, pupeles, lęšius, žirnius). GALIMA VARTOTI
žaliuosius žirnelis ir visas daržoves neribotais kiekiais.</i>
<br><b>Saldžius produktus:</b> <i>Saldainius, tortus, pyragėlius, sausainius, šokoladą, ledus, medų,
uogienes, sirupus, sultis, limonadus, vaisius, uogas, alų, likerį, saldų bei pusiau sausą vyną,
saldų bei pusiau sausą putojantį vyną.</i>
<br><b>Polinesočiuosius riebalus:</b> <i>Saulėgrąžų, rapsų, sezamų, linų sėmenų, moliūgų sėklų,
nakvišų aliejus, žuvų taukus, saulėgrąžas, sėmenis, sezamų sėklas, visus riešutus (išskyrus
kokosų, migdolų ir lazdyno), pistacijas, soją ir jos produktus, margariną, majonezą, picų
padažus, „tepamus riebalų mišinius", „grietinės ir augalinių riebalų mišinius" , „sūrio
produktus“. GALIMA VARTOTI alyvuogių, avokadų, kokosų, migdolų, lazdyno riešutų aliejus,
kakavos sviestą, pieno sviestą, lašinius.</i>
<br><b>Stipriai pakitusius baltymus ir riebalus:</b> <i>Savo sultis atidavusią kaitintą mėsą, kietai
virtus arba keptus kiaušinius, mėsos ir žuvies konservus, brandintus ir fermentuotus sūrius,
papildomai termiškai apdorotą varškę, pakartotinai pašildytą maistą. GALIMA VARTOTI iki 2
min. kaitintus kiaušinius, iki 3 min. kaitintą žuvį mažais gabaliukais, iki 5 min. kaitintą
paukštieną mažais gabaliukais, iki 7 min. kaitintą kiaulieną, jautieną, žvėrieną mažais
gabaliukais, nekaitintus baltus sūrius, papildomai nekaitintą varškę.</i>
<br><i>Keletas tinkamų patiekalų pavyzdžių:</i>
<br>• Skystai virtas kiaušinis su burokėlių salotomis
<br>• Varškė su grietine ir avokadais
<br>• Troškintos morkos, petražolių šaknys ir pomidorai su mėsos gabaliukais
<br>• Garintas upėtakis su pomidorais, salotomis ir alyvuogių aliejumi
<br>• Grūdėta varškė su žaliaisiais konservuotais žirneliais
<br>• Žali arba troškinti kalafioro griežinėliai grietinės padaže su žolelėmis
<br>• Šaltibarščiai
<br>• Graikiškos salotos
        </div>
    </div>
</div>
    """)

def pav2():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup2">MAŽIAUSIAI 2 DIENOS IKI TYRIMŲ DIENOS</a>
</div>

<div id="popup2" class="overlay">
    <div class="popup" id="showpopup">
        <h2>MAŽIAUSIAI 2 DIENOS IKI TYRIMŲ DIENOS</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Nuo ryto nustojamos vartoti šios medžiagos:
<br><b>Kava, arbata, kakava, šokoladas, energiniai gėrimai, rūkalai, alkoholis, gazuoti
gėrimai, maisto papildai ir vaistai </b>(IŠSKIRTINIAIS ATVEJAIS, kai vaistų nutraukimas tokiam ilgam periodui gali sukelti pavojų gyvybei, <b>vaistų
nevartoti bent 1 dieną prieš tyrimą)</b>. <i>GALIMA VARTOTI žolelių arbatas, rooibos arbatą</i>.
<br>Iki tyrimo neužsiimama intensyvia arba ilgalaike fizine veikla.
        </div>
    </div>
</div>
    """)

def pav3():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup3">TYRIMŲ DIENOS IŠVAKARĖSE</a>
</div>

<div id="popup3" class="overlay">
    <div class="popup" id="showpopup">
        <h2>TYRIMŲ DIENOS IŠVAKARĖSE</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Jei kitą dieną matavimus atliks sutartu metu atvykęs asmuo, nuo pietų pradedami rinkti 3
šlapimo mėginiai:
<br><i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apiepiet – prieš pietus arba bent 2 val. po valgio.</i>
<br><i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Vakare – prieš pat miegą, bent 2 val. po valgio.</i>
<br><i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ryte – prieš pusryčius, ne vėliau nei 30 min. nuo atsikėlimo.</i>
<br>Šlapimo mėginys imamas į indelius, skirtus šlapimui, jų galima įsigyti vaistinėse. Mėginio
tūris turi būti 60 ml. Mėginius reikia pažymėti, kad jie nebūtų supainioti.
<br><b>Jei kitą dieną matavimai bus atliekami 3 kartus, šlapimo mėginiai imami ir tiriami
tyrimų dieną.</b>
        </div>
    </div>
</div>
    """)

def pav4():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup4">TYRIMŲ DIENĄ</a>
</div>

<div id="popup4" class="overlay">
    <div class="popup" id="showpopup">
        <h2>TYRIMŲ DIENĄ</h2>
        <a class="close" href="#showpopup"">&times;</a>
        <div class="content">
Tyrimų dieną galima valgyti, bet vis dar laikantis ankstesnių mitybos nurodymų. Iki tyrimo
reikia būti bent 2 val. nevalgius ir bent 30 min. iki tyrimo nieko nekramtyti, tačiau galima
atsigerti negazuoto nešalto vandens.
<br>Jei tyrimą atlieka sutartu laiku atvykęs asmuo, tyrimo metu ištiriami visi 3 šlapimo
mėginiai ir atliekami kitų parametrų matavimai.
<br>Jei tyrimas atliekamas 3 kartus, kiekvienas šlapimo mėginys tiriamas ir kiti parametrai
matuojami po šlapimo mėginio paėmimo, leidus jam atvėsti iki kambario temperatūros.
<br><b>Šlapimo mėginiai tiriami ir kiti parametrai matuojami pagal „Tyrimo aprašą“</b>,
duomenys surašomi į <b>„Organizmo būklės tyrimo formos“</b> skiltį <i>„Tyrimo protokolas“</i>.
<br><b>Atlikus tyrimą ir nustačius organizmo būklę pradedama maitintis pagal būklę
atitinkančias rekomendacijas.</b>
        </div>
    </div>
</div>
    """)

def aprsrugs():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup5"><br>Rūgštingumas<br>(rodmuo ekrane arba pagal spalvos skalę)</a>
</div>

<div id="popup5" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Rūgštingumas</h2>
        <a class="close" href="#showpopup"">&times;</a>
        <div class="content">
Jei turimas rūgštingumo matuoklis, matuojama pagal jo instrukcijas.
Sukalibruoto matuoklio daviklis merkiamas į šlapimą, lengvai pamaišoma ir laukiama, kol
nusistovės rodmuo. Vertė įrašoma eilutėje 2.1 „Rūgštingumas (matuokliu), U-pH 1 “. Atlikus
matavimą, matuoklio daviklis nuplaunamas pamaišant stiklinėje su čiaupo vandeniu, po
to su distiliuotu vandeniu ir nusausinamas, priglaudus (bet netrinant) švelnia servetėlė.
<i>Jei naudojamos tik rūgštingumo matavimo juostelės, šis punktas praleidžiamas</i>.
<br>Rūgštingumo matavimo juostelės naudojamos pagal jų instrukcijas, nurodytas ant
dėžutės. Juostelės spalvinės zonos merkiamos į šlapimą, pamaišoma, ištraukiama,
padedama ant popierinio rankšluosčio spalvinėmis zonomis į viršų ir paleidžiamas
chronometras. Po instrukcijoje nurodyto laiko stebimi spalvinių zonų atspalviai, jie
lyginami su skale ant dėžutės. Vertė įrašoma eilutėje 2.2 „Rūgštingumas (juostele),
U-pH 2 “. <i>Jei naudojamas tik matuoklis, šis punktas praleidžiamas</i>.
        </div>
    </div>
</div>
    """, width = 250)

srrytas = TextInput(name = "rytas1", value="", title = "Rytas", width = 60)
srpietus = TextInput(name = "pietus1", value="", title = "Pietūs", width = 60)
srvakaras = TextInput(name = "vakaras1", value="", title = "Vakaras", width = 60)

def aprssvies():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup6"><br>Šviesumas<br>(skaičius pagal skalę)</a> 
</div>

<div id="popup6" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Šviesumas</h2>
        <a class="close" href="#showpopup"">&times;</a>
        <div class="content">
Šlapimo mėginys įpilamas į matavimo cilindrą iki atitinkamos ribos, kad
įmerktas areometras galėtų pilnai panirti ir šlapimas neišsilietų. Matavimo cilindras
pastatomas gerai apžviestoje vietoje be tiesioginių spindulių baltame fone (rašomojo
popieriaus lapo), stebimas ir vertinamas vizualiai. Eilutėje 2.4 „Šviesumas, U-šv“ nurodomas šlapimo šviesumas pagal žemiau pateiktoje skalėje šlapimo spalvą
atitinkančio stulpelio numerį:
<table>
    <tr>
      <th scope="col"><b>Vertė</b></th>
      <th scope="col"><b>Spalva</b></th>
      <th scope="col"><b>Aprašymas</b></th>
    </tr>
    <tr>
      <td>+4</td>
      <td><div class="foo blue"></div></td>
      <td>Ruda, artima pieniškam šokoladui arba obuolių kompotui</td>
    </tr>
    <tr>
      <td>+3</td>
      <td><div class="foo purle"></div></td>
      <td>Ruda kaip stipri žalioji arbata</td>
    </tr>
    <tr>
      <td>+2</td>
      <td><div class="foo wine"></div></td>
      <td>Rusva kaip silpna žalioji arbata arba šviesus alus</td>
    </tr>
    <tr>
      <td>+1</td>
      <td><div class="foo blue"></div></td>
      <td>Geltona, bet nešvyti</td>
    </tr>
    <tr>
      <td>0</td>
      <td><div class="foo purle"></div></td>
      <td>Ryški ir švytinti geltona</td>
    </tr>
    <tr>
      <td>-1</td>
      <td><div class="foo wine"></div></td>
      <td>Geltona, šiek tiek švyti, kaip baltas vynas</td>
    </tr>
    r>
      <td>-2</td>
      <td><div class="foo blue"></div></td>
      <td>Gelsva, nešvyti</td>
    </tr>
    r>
      <td>-3</td>
      <td><div class="foo purle"></div></td>
      <td>Spalva labai silpna, bet regima</td>
    </tr>
    r>
      <td>-4</td>
      <td><div class="foo wine"></div></td>
      <td>Visiškai bespalvė, beveik kaip vanduo</td>
    </tr>
</table>
        </div>
    </div>
</div>
    """, width = 250)

ssrytas = TextInput(name = "rytas2", value="", title = "Rytas", width = 60)
sspietus = TextInput(name = "pietus2", value="", title = "Pietūs", width = 60)
ssvakaras = TextInput(name = "vakaras2", value="", title = "Vakaras", width = 60)

def aprstank():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup7"><br>Tankis<br>(rodmuo, g/ml)</a>
</div>

<div id="popup7" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Tankis</h2>
        <a class="close" href="#showpopup"">&times;</a>
        <div class="content">
Matavimo cilindras su šlapimu pastatomas ant tvirto pagrindo ir į jį
įmerkiamas areometras. Kai aerometras nustoja svyruoti, jis labai lengvai stumtelimas iš
viršau, kad dar susvyruotų. Nusistovėjus skalės rodmuo atskaitomas ties menisko
(įgaubto vandens paviršiaus) apačia ir įrašoma eilutėje 2.3 „Tankis, d“. Jei areometras
pritraukiamas prie matavimo cilindro sienelės, reikia jį ištraukti, nuplauti, nusausinti ir
matavimą pakartoti.
        </div>
    </div>
</div>
    """, width = 250)

strytas = TextInput(name = "rytas3", value="", title = "Rytas", width = 60)
stpietus = TextInput(name = "pietus3", value="", title = "Pietūs", width = 60)
stvakaras = TextInput(name = "vakaras3", value="", title = "Vakaras", width = 60)



def aprsputo():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup8"><br>Putojimas<br>(skaičius pagal skalę)</a> 
</div>

<div id="popup8" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Putojimas</h2>
        <a class="close" href="#showpopup"">&times;</a>
        <div class="content">
Šlapimo mėginys supilamas atgal į indelį, tvirtai užsukamas ir plakamas
10 sekundžių. Po to pastatomas ant popierinio rankšluosčio, iškart atsukamas ir
paleidžiamas chronometras. Stebima, kada centre prasiskirs putos. Vertinama pagal
skalę ir įrašoma eilutėje 2.5 „Putojimas, U-put“:
<table>
    <tr>
      <th scope="col"><b>Vertė</b></th>
      <th scope="col"><b>Aprašymas</b></th>
    </tr>
    <tr>
      <td>+3</td>
      <td>putos prasiskiria per daugiau nei 15 min.</td>
    </tr>
    <tr>
      <td>+2</td>
      <td>putos prasiskiria per 15 min.</td>
    </tr>
    <tr>
      <td>+1</td>
      <td>putos prasiskiria per 5 min.</td>
    </tr>
    <tr>
      <td>0</td>
      <td><b>putos prasiskiria per 1 min.</b></td>
    </tr>
    <tr>
      <td>-1</td>
      <td>atsukus putos jau prasiskyrusios</td>
    </tr>
</table>
        </div>
    </div>
</div>
    """, width = 250)

sprytas = TextInput(name = "rytas4", value="", title = "Rytas", width = 60)
sppietus = TextInput(name = "pietus4", value="", title = "Pietūs", width = 60)
spvakaras = TextInput(name = "vakaras4", value="", title = "Vakaras", width = 60)

def aprserugst():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup9"><br>Rūgštingumas<br>(rodmuo ekrane arba skaičius pagal skalę)</a>
</div>

<div id="popup9" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Rūgštingumas</h2>
        <a class="close" href="#showpopup"">&times;</a>
        <div class="content">
Jei turimas rūgštingumo matuoklis, matuojama pagal jo instrukcijas.
Sukalibruoto matuoklio daviklis merkiamas į seiles ir laukiama, kol nusistovės rodmuo (jei
daviklis ne stiklinis, tuomet seilių lašas užlašinamas ant jautrios zonos). Vertė įrašoma
eilutėje 3.1 „Rūgštingumas (matuokliu), S-pH 1 “. Atlikus matavimą, matuoklio daviklis
nuplaunamas pamaišant stiklinėje su čiaupo vandeniu, po to su distiliuotu vandeniu ir
nusausinamas, priglaudus (bet netrinant) švelnia servetėlė. Jei naudojamos tik
rūgštingumo matavimo juostelės, šis punktas praleidžiamas.
<br>Rūgštingumo matavimo juostelės naudojamos pagal jų instrukcijas, nurodytas ant
dėžutės. Juostelės spalvinėmis zonos žemyn merkiamos į seiles, pamaišoma,
ištraukiama, padedama ant popierinio rankšluosčio spalvinėmis zonomis į viršų ir
paleidžiamas chronometras. Po instrukcijoje nurodyto laiko seilių perteklius
nusausinamas į servetėlę nebraukiant, stebimi spalvinių zonų atspalviai, jie lyginami su
skale ant dėžutės. Vertė įrašoma eilutėje 2.2 „Rūgštingumas (juostele), S-pH 2 “. <i>Jei
naudojamas tik matuoklis, šis punktas praleidžiamas</i>.
        </div>
    </div>
</div>
    """, width = 250)

serrytas = TextInput(name = "rytas5", value="", title = "Rytas", width = 60)
serpietus = TextInput(name = "pietus5", value="", title = "Pietūs", width = 60)
servakaras = TextInput(name = "vakaras5", value="", title = "Vakaras", width = 60)

def aprseklamp():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup10"><br>Klampumas<br>(skaičius pagal skalę)</a> 
</div>

<div id="popup10" class="overlay">
    <div class="popup">
        <h2>Klampumas</h2>
        <a class="close" href="#showpopup"">&times;</a>
        <div class="content">
Kol laukiama rūgštingumo duomenų, valgomasis šaukštas su likusiu
seilių mėginiu pavartomas, kad pagal jų tekėjimą vizualiai būtų galima įvertinti jų
klampumą. Klampumas vertinamas pagal skalę ir vertė įrašoma į eilutę 3.3 “Klampumas,
S-kl”:
<table>
    <tr>
      <th scope="col"><b>Vertė</b></th>
      <th scope="col"><b>Aprašymas</b></th>
    </tr>
    <tr>
      <td>+2</td>
      <td>tirštos, daug putų, neteka</td>
    </tr>
    <tr>
      <td>+1</td>
      <td>Labai klampios, kaip sirupas, teka lėtai</td>
    </tr>
    <tr>
      <td>0</td>
      <td><b>vidutiniškai klampios, kaip žalias kiaušinio baltymas</b></td>
    </tr>
    <tr>
      <td>-1</td>
      <td>skystos, bet klampesnės už vandenį, kaip liesas kefyras</td>
    </tr>
    <tr>
      <td>-2</td>
      <td>visiškai skystos, kaip vanduo</td>
    </tr>
</table>
        </div>
    </div>
</div>
    """, width = 250)

sekrytas = TextInput(name = "rytas6", value="", title = "Rytas", width = 60)
sekpietus = TextInput(name = "pietus6", value="", title = "Pietūs", width = 60)
sekvakaras = TextInput(name = "vakaras6", value="", title = "Vakaras", width = 60)

def aprpulsed():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup11"><br>Pulsas sėdint<br>(dūžių skaičius per 15 s,×4)</a>
</div>

<div id="popup11" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Pulsas sėdint</h2>
        <a class="close" href="#showpopup"">&times;</a>
        <div class="content">
Užčiuopiamas pulsas ant tiriamojo riešo, tai geriausia padaryti trimis
pirštais, sudėtais greta – šoninius pirštus spaudžiant prie kaulo šiek tiek stipriau nei
vidurinį tam tikru metu pradedamas justi tvinkčiojimas. Jei tvinkčiojimas matavimo metu
silpnėja, reikia keisti atskirų pirštų spaudimą, kol vėl pajuntamas tvinkčiojimas.
<br>Užčiuopus pulsą, 5-10 dūžių stebima, ar pulsas tolygus, ar nėra aritmijos, ar
tiriamasis nusiraminęs. Tada su dūžiu paleidžiamas chronometras ir 15 sekundžių
skaičiuojami širdies dūžiai. Jei laikas baigėsi anksčiau, nei įvyko paskutinis širdies dūžis,
prie pilnų dūžių skaičiaus dar pridedama 0,5. Gautą skaičių padauginus iš 4 gauname
pulsą sėdint, šis skaičius įrašomas eilutėje 5.1 „Pulsas sėdint, P sėd “.
<br><font size="1"><i>Pvz: Jei chronometras rodo 0:14 , o Jūs mintyse esate suskaičiavęs 18 dūžių, 19-tą dūžį
pajuntate tuo pat metu, kaip chronometras parodo 0:15. Tuomet į juodraštį užsirašote
skaičių „19”, o pulsas bus P sėd = 4×19 = 76.
Jei chronometras rodo 0:14 , o Jūs mintyse esate suskaičiavęs 18 dūžių, tačiau 19-tą dūžį
pajuntate po to, kaip chronometras parodo 0:15. Tuomet į juodraštį užsirašote skaičių
„18,5”, o pulsas bus P sėd = 4×18,5 = 74.</i></font>
        </div>
    </div>
</div>
    """, width = 250)

psrytas = TextInput(name = "rytas7", value="", title = "Rytas", width = 60)
pspietus = TextInput(name = "pietus7", value="", title = "Pietūs", width = 60)
psvakaras = TextInput(name = "vakaras7", value="", title = "Vakaras", width = 60)

def aprkunotemp():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup12"><br>Kūno temperatūra</a>
</div>

<div id="popup12" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Kūno temperatūra</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Kūno termometras naudojamas pagal jo naudojimo instrukciją.
<br>Jei matuojama infraraudonųjų spindulių (IR) termometru, matuojama ausies angos
vidaus temperatūra.
<br>Jei matuojama skaitmeniniu kontaktiniu termometru, matuojama burnos gleivinės
temperatūra po liežuviu.
<br>Jei matuojama skystiniu termometru (gyvsidabriniu, spiritiniu), prieš tai jis
nupurtomas iki 35,5 °C rodmens ir tada tiriamojo paprašoma jį įsidėti į kairės rankos
pažastį, matuojama 5-7 minutes. Temperatūros rodmuo Celsijaus laipsniais su vienu
skaičiumi po kablelio įrašomas eilutėje 4.1 „Kūno temperatūra, Temp“.
        </div>
    </div>
</div>
    """, width = 250)

ktrytas = TextInput(name = "rytas8", value="", title = "Rytas", width = 60)
ktpietus = TextInput(name = "pietus8", value="", title = "Pietūs", width = 60)
ktvakaras = TextInput(name = "vakaras8", value="", title = "Vakaras", width = 60)

def aprdermoref():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup13"><br>Dermografinis refleksas<br>(skaičius pagal skalę)</a> 
</div>

<div id="popup13" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Dermografinis refleksas</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Tiriamojo paprašoma atsiraitoti dešinės rankos rankovę,
atidengiant bicepsą. Žinomo pločio, neaštriu, bet neužapvalintu daiktu (pavyzdžiui,
įtrauktu tušinuku, bambukine valgymo lazdele ir pan.) ne per stipriai brėžiamos
besikryžiuojančios linijos ant paciento dešinės rankos vidinės pusės per 3 pirštus nuo
linkio vietos. Pirma ant dilbio, po to ant žasto. Paleidžiamas chronometras. Stebima
paciento reakcija po 1 min. ir po 6 min. Vertinama pagal skalę ir įrašoma eilutėje 4.2
„Dermografizmas, Dermo“:
<table>
    <tr>
      <th scope="col"><b>Vertė</b></th>
      <th scope="col"><b>Aprašymas</b></th>
    </tr>
    <tr>
      <td>+4</td>
      <td>po 1 minutės paraudimas su iškilumais arba daugiau nei 2 cm pločio paraudimas</td>
    </tr>
    <tr>
      <td>+3</td>
      <td>po 6 minučių paraudimas su iškilumais arba daugiau nei 2 cm pločio paraudimas</td>
    </tr>
    <tr>
      <td>+2</td>
      <td>po 6 minučių raudonos linijos ant žasto ir ant dilbio platesnės nei brėžiklis</td>
    </tr>
    <tr>
      <td>+1</td>
      <td>po 6 minučių raudonos linijos ant žasto ir ant dilbio</td>
    </tr>
    <tr>
      <td>0</td>
      <td><b>po 6 minučių raudonos linijos ant žasto, bet jokio paraudimo ant dilbio</b></td>
    </tr>
    <tr>
      <td>-1</td>
      <td>po 6 minučių jokio paraudimo</td>
    </tr>
    <tr>
      <td>-2</td>
      <td>po 1 minutės jokio paraudimo</td>
    </tr>
</table>
        </div>
    </div>
</div>
    """, width = 250)

drrytas = TextInput(name = "rytas9", value="", title = "Rytas", width = 60)
drpietus = TextInput(name = "pietus9", value="", title = "Pietūs", width = 60)
drvakaras = TextInput(name = "vakaras9", value="", title = "Vakaras", width = 60)

def aprvasomref():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup14"><br>Vasomotorinis refleksas<br>(skaičius pagal skalę)</a> 
</div>

<div id="popup14" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Vasomotorinis refleksas</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Vienos rankos delnu lieskite tiriamojo tricepsą (žasto
nugarinę dalį), o kitos rankos delnu – tiriamojo plaštakos išorinę pusę. Kelis kartus
rankas sukeiskite ir lyginkite tricepso ir plaštakos temperatūrų skirtumą. Vertinama pagal
skalę ir įrašoma eilutėje 4.3 „Vasomotorinis, Vaso“:
<table>
    <tr>
      <th scope="col"><b>Vertė</b></th>
      <th scope="col"><b>Aprašymas</b></th>
    </tr>
    <tr>
      <td>+4</td>
      <td>plaštaka labai stipriai karštesnė už žastą</td>
    </tr>
    <tr>
      <td>+3</td>
      <td>plaštaka ryškiai šiltesnė už žastą ir/arba prakaituotas delnas</td>
    </tr>
    <tr>
      <td>+2</td>
      <td>plaštaka vos šiltesnė už žastą</td>
    </tr>
    <tr>
      <td>+1</td>
      <td>plaštakos ir žasto temperatūros vienodos</td>
    </tr>
    <tr>
      <td>0</td>
      <td><b>plaštaka vos vėsesnė už žastą</b></td>
    </tr>
    <tr>
      <td>-1</td>
      <td>plaštaka ryškiai vėsesnė už žastą</td>
    </tr>
    <tr>
      <td>-2</td>
      <td>plaštaka akivaizdžiai vėsesnė už žastą</td>
    </tr>
     <tr>
      <td>-3</td>
      <td>plaštaka stipriai vėsesnė už žastą ir/arba prakaituotas delnas</td>
    </tr>
    <tr>
      <td>-4</td>
      <td>plaštaka labai stipriai šaltesnė už žastą</td>
    </tr>

</table>
        </div>
    </div>
</div>
    """, width = 250)


vrrytas = TextInput(name = "rytas10", value="", title = "Rytas", width = 60)
vrpietus = TextInput(name = "pietus10", value="", title = "Pietūs", width = 60)
vrvakaras = TextInput(name = "vakaras10", value="", title = "Vakaras", width = 60)

def aprvyzdyd():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup15"><br>Vyzdžio dydis<br>(skaičius pagal skalę)</a> 
</div>

<div id="popup15" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Vyzdžio dydis</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Tiriamojo regos lauke neturi būti ryškios šviesos (lempos ar lango),
geriausia, kad jis sėdėtų priešais šviesios spalvos sieną. Pakeliamas pirštas prieš
tiriamojo akis maždaug per dilbio ilgio atstumą nuo veido. Paprašoma žvilgsnį
sufokusuoti į pirštą, kai vyzdžio dydis nusistovi paprašoma žvilgsnį sufokusuoti į sieną
priešais tiriamąjį, ir vėl laukiama, kol vyzdžio dydis nusistovi. Taip kartojama kelis kartus,
stebima, apie kokį plotį svyruoja vyzdys. Vertinama pagal skalę ir įrašoma eilutėje 4.4
„Vyzdžio dydis, Vyzd“:
<table>
    <tr>
      <th scope="col"><b>Vertė</b></th>
      <th scope="col"><b>Vaizdas</b></th>
      <th scope="col"><b>Aprašymas</b></th>
    </tr>
    <tr>
      <td>+4</td>
      <td><div id="outer-circle">
             <div id="inner-circle">
               </div>
                     </div></td>
      <td>Vyzdys 2 kartus didesnis už rainelės plotį tarp vyzdžio ir krašto</td>
    </tr>
    <tr>
      <td>+3</td>
      <td><div id="outer-circle1">
             <div id="inner-circle1">
               </div>
                     </div></td>
      <td></td>
    </tr>
    <tr>
      <td>+2</td>
      <td><div id="outer-circle2">
             <div id="inner-circle2">
               </div>
                     </div></td>
      <td>Vyzdys 1,5 karto didesnis už rainelės plotį tarp vyzdžio ir krašto</td>
    </tr>
    <tr>
      <td>+1</td>
      <td><div id="outer-circle3">
             <div id="inner-circle3">
               </div>
                     </div></td>
      <td></td>
    </tr>
    <tr>
      <td>0</td>
      <td><div id="outer-circle4">
             <div id="inner-circle4">
               </div>
                     </div></td>
      <td><b>Vyzdžio dydis toks pat, kaip rainelės plotis tarp vyzdžio ir krašto</b></td>
    </tr>
    <tr>
      <td>-1</td>
      <td><div id="outer-circle5">
             <div id="inner-circle5">
               </div>
                     </div></td>
      <td></td>
    </tr>
    <tr>
      <td>-2</td>
      <td><div id="outer-circle6">
             <div id="inner-circle6">
               </div>
                     </div></td>
      <td>Vyzdys 1,5 karto mažesnis už rainelės plotį tarp vyzdžio ir krašto</td>
    </tr>
     <tr>
      <td>-3</td>
      <td><div id="outer-circle7">
             <div id="inner-circle7">
               </div>
                     </div></td>
      <td></td>
    </tr>
    <tr>
      <td>-4</td>
      <td><div id="outer-circle8">
             <div id="inner-circle8">
               </div>
                     </div></td>
      <td>Vyzdys 2 kartus mažesnis už rainelės plotį tarp vyzdžio ir krašto</td>
    </tr>

</table>
        </div>
    </div>
</div>
    """, width = 250)


vdrytas = TextInput(name = "rytas11", value="", title = "Rytas", width = 60)
vdpietus = TextInput(name = "pietus11", value="", title = "Pietūs", width = 60)
vdvakaras = TextInput(name = "vakaras11", value="", title = "Vakaras", width = 60)

def aprtremoref():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup16"><br>Tremoro (drebulio) refleksas<br>(skaičius pagal skalę)</a> 
</div>

<div id="popup16" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Tremoro (drebulio) refleksas</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Tiriamojo paprašoma išsižioti ir iškišti liežuvį tiesiai į
priekį. Stebimas liežuvio judesys ir raumenų drebulys. Jei reikia, patikrinamas ir galūnių
drebulys, padedant popieriaus lapą ant į šoną ištiestos iš delnu į viršų pasuktos
plaštakos, kai tiriamasis žiūri tiesiai. Vertinama pagal skalę ir įrašoma eilutėje 4.5
„Tremoras (drebulys), Trem“:
<table>
    <tr>
      <th scope="col"><b>Vertė</b></th>
      <th scope="col"><b>Aprašymas</b></th>
    </tr>
    <tr>
      <td>+4</td>
      <td>ypatingai didelis liežuvio ir galūnių drebulys</td>
    </tr>
    <tr>
      <td>+3</td>
      <td>didelis liežuvio drebulys ir pastebimas galūnių drebulys</td>
    </tr>
    <tr>
      <td>+2</td>
      <td>vidutinis liežuvio drebulys ir stiprus judesys (negali išlaikyti vietoje)</td>
    </tr>
    <tr>
      <td>+1</td>
      <td>lengvas liežuvio drebulys ir judesys</td>
    </tr>
    <tr>
      <td>0</td>
      <td><b>jokio liežuvio drebulio ir lengvas liežuvio judesys</b></td>
    </tr>
    <tr>
      <td>-1</td>
      <td>jokio liežuvio drebulio ir labai mažas liežuvio judesys</td>
    </tr>
    <tr>
      <td>-2</td>
      <td>absoliučiai jokio liežuvio drebulio ir judesio</td>
    </tr>
</table>
        </div>
    </div>
</div>
    """, width = 250)

trrytas = TextInput(name = "rytas12", value="", title = "Rytas", width = 60)
trpietus = TextInput(name = "pietus12", value="", title = "Pietūs", width = 60)
trvakaras = TextInput(name = "vakaras12", value="", title = "Vakaras", width = 60)

def aprsneruzgu():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup17"><br>Šnervių užgulimas<br>(skaičius pagal skalę)</a> 
</div>

<div id="popup17" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Šnervių užgulimas</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Tiriamojo paprašoma pirštu užspausti dešiniąją šnervę ir kelis
kartus įkvėpti bei iškvėpti per kairiąją, po to paprašoma tą patį padaryti su kita šnerve.
Tiriamojo paprašoma apibūdinti kvėpavimo lengvumą. Vertinama pagal skalę ir įrašoma į
eilutę 4.6 „Šnervių užgulimas, Nos“:
<table>
    <tr>
      <th scope="col"><b>Vertė</b></th>
      <th scope="col"><b>Aprašymas</b></th>
    </tr>
    <tr>
      <td>+4</td>
      <td>Dešinė šnervė visiškai užgulta, pro kairę kvėpuojama lengviau.</td>
    </tr>
    <tr>
      <td>+3</td>
      <td>Dešinė šnervė užgulta labiau nei kairė, bet orą su jėga galima prapūsti.</td>
    </tr>
    <tr>
      <td>+2</td>
      <td>Pro dešinę šnervę kvėpuojama, bet reikia pridėti papildomos jėgos (ilgaikvėpuojant pavargstama), pro kairę kvėpuojama lengviau.</td>
    </tr>
    <tr>
      <td>+1</td>
      <td>Pro dešinę šnervę kvėpuojama laisvai, bet jaučiamas švilpimas, kairėje švilpimas nejaučiamas.</td>
    </tr>
    <tr>
      <td>0</td>
      <td><b>Pro abi šnerves kvėpuojama laisvai be jokio pasipriešinimo ar švilpimo.</b></td>
    </tr>
    <tr>
      <td>-1</td>
      <td>Pro kairę šnervę kvėpuojama laisvai, bet jaučiamas švilpimas, dešinėje švilpimas nejaučiamas.</td>
    </tr>
    <tr>
      <td>-2</td>
      <td>Pro kairę šnervę kvėpuojama, bet reikia pridėti papildomos jėgos (ilgai kvėpuojant pavargstama), pro dešinę kvėpuojama lengviau.</td>
    </tr>
     <tr>
      <td>-3</td>
      <td>Kairė šnervė užgulta labiau nei dešinė, bet orą su jėga galima prapūsti.</td>
    </tr>
    <tr>
      <td>-4</td>
      <td>Kairė šnervė visiškai užgulta, pro dešinę kvėpuojama lengviau.</td>
    </tr>

</table>
        </div>
    </div>
</div>
    """, width = 250)

surytas = TextInput(name = "rytas13", value="", title = "Rytas", width = 60)
supietus = TextInput(name = "pietus13", value="", title = "Pietūs", width = 60)
suvakaras = TextInput(name = "vakaras13", value="", title = "Vakaras", width = 60)

def aprsarglinref():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup18"><br>Sargento linijos refleksas<br>(skaičius pagal skalę)</a> 
</div>

<div id="popup18" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Sargento linijos refleksas</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Tiriamojo paprašoma atidengti pilvą nuo bambos iki
krūtinkaulio. Žinomo pločio, neaštriu daiktu (pavyzdžiui, įtrauktu tušinuku, bambukine
valgymo lazdele ir pan.) labai lengvai, spaudžiant tik daikto svoriui, braukiama per pilvo
odą nuo bambos link krūtinkaulio. Paleidžiamas chronometras ir stebimas linijos
išryškėjimas. Vertinama pagal skalę ir įrašoma į eilutę 4.7 „Sargento linija, Sarg“:
<table>
    <tr>
      <th scope="col"><b>Vertė</b></th>
      <th scope="col"><b>Aprašymas</b></th>
    </tr>
    <tr>
      <td>+4</td>
      <td>balta linija pasirodo per 15 s ir išlieka daugiau nei 1 min.</td>
    </tr>
    <tr>
      <td>+3</td>
      <td>balta linija pasirodo per 15 s ir išlieka mažiau nei 1 min.</td>
    </tr>
    <tr>
      <td>+2</td>
      <td>balta linija pasirodo vėliau nei po 15 s.</td>
    </tr>
    <tr>
      <td>+1</td>
      <td>balta linija pasirodo vėliau nei po 30 s.</td>
    </tr>
    <tr>
      <td>0</td>
      <td><b>balta linija per 1 min. nepasirodo.</b></td>
    </tr>
</table>
        <i>Šio tyrimo metu patogu kartu atlikti ir kvėpavimo dažnio matavimą.</i></div>
    </div>
</div>
    """, width = 250)

slrrytas = TextInput(name = "rytas14", value="", title = "Rytas", width = 60)
slrpietus = TextInput(name = "pietus14", value="", title = "Pietūs", width = 60)
slrvakaras = TextInput(name = "vakaras14", value="", title = "Vakaras", width = 60)

def aprkvepdaz():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup19"><br>Kvėpavimo dažnis<br>(Įkvėpimo-iškvėpimo ciklų<br>skaičius per 30 s,×2)</a> 
</div>

<div id="popup19" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Kvėpavimo dažnis</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Tiriamojo kairėje rankoje užčiuopiamas pulsas (kad tiriamasis
nežinotų, jog stebimas jo kvėpavimas) ir akies kampu stebimas pilvo ir krūtinės
kilnojimasis. Įsitikinama, kad kvėpavimas tolygus ir nėra nevalingų kvėpavimo sulaikymų
ilgesniam laikui. Kai tiriamasis yra iškvėpęs, paleidžiamas chronometras. 30 sekundžių
skaičiuojami pilni įkvėpimo-iškvėpimo ciklai. Jei laikas baigėsi anksčiau, nei tiriamasis
iškvepia paskutinį kartą, tai prie pilnų ciklų skaičiaus pridedama trupmeninė dalis pagal
kriterijus:
<br>• jei laikas baigėsi tiriamajam įkvėpinėjant, tai +0,25
<br>• jei laikas baigėsi tiriamajam įkvėpus, tai +0,5
<br>• jei laikas baigėsi tiriamajam iškvėpinėjant, tai +0,75
<br>Gautą skaičių padauginus iš 2 gaunamas kvėpavimo dažnis, jis įrašomas eilutėje 6.1
„Kvėpavimo dažnis, KD“.
<br><font size="1"><i>Pavyzdžiui: Chronometras rodo 0:29 , o Jūs mintyse esate suskaičiavęs 7 pilnų ciklų.
Chronometras parodo 0:30, kai tiriamais įkvėpinėja, tuomet į juodraštį užsirašote skaičių
„7,25”, ir kvėpavimo dažnis bus KD = 2×7,25 = 14,5.
Chronometras parodo 0:30, kai tiriamais yra pilnai įkvėpęs, tuomet į juodraštį užsirašote
skaičių „7,5”, ir kvėpavimo dažnis bus KD = 2×7,5 = 15.
Chronometras parodo 0:30, kai tiriamais iškvėpinėja, tuomet į juodraštį užsirašote skaičių
„7,75”, ir kvėpavimo dažnis bus KD = 2×7,75 = 15,5.
Chronometras parodo 0:30, kai tiriamais pilnai iškvėpė, tuomet į juodraštį užsirašote
skaičių „8”, ir kvėpavimo dažnis bus KD = 2×8 = 16.</i>/div>
    </div>
</div>
    """, width = 250)

kdrytas = TextInput(name = "rytas15", value="", title = "Rytas", width = 60)
kdpietus = TextInput(name = "pietus15", value="", title = "Pietūs", width = 60)
kdvakaras = TextInput(name = "vakaras15", value="", title = "Vakaras", width = 60)

def aprpulgul():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup20"><br>Pulsas gulint<br>(dūžių skaičius per 15 s,×4)</a>
</div>

<div id="popup20" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Pulsas gulint</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Užčiuopiamas pulsas ant tiriamojo riešo, tai geriausia padaryti trimis
pirštais, sudėtais greta – šoninius pirštus spaudžiant prie kaulo šiek tiek stipriau nei
vidurinį tam tikru metu pradedamas justi tvinkčiojimas. Jei tvinkčiojimas matavimo metu
silpnėja, reikia keisti atskirų pirštų spaudimą, kol vėl pajuntamas tvinkčiojimas.
<br>Užčiuopus pulsą, 5-10 dūžių stebima, ar pulsas tolygus, ar nėra aritmijos, ar
tiriamasis nusiraminęs. Tada su dūžiu paleidžiamas chronometras ir 15 sekundžių
skaičiuojami širdies dūžiai. Jei laikas baigėsi anksčiau, nei įvyko paskutinis širdies dūžis,
prie pilnų dūžių skaičiaus dar pridedama 0,5. Gautą skaičių padauginus iš 4 gauname
pulsą gulint, šis skaičius įrašomas eilutėje 5.1 „Pulsas gulint, P sėd “.
<br><font size="1"><i>Pvz: Jei chronometras rodo 0:14 , o Jūs mintyse esate suskaičiavęs 18 dūžių, 19-tą dūžį
pajuntate tuo pat metu, kaip chronometras parodo 0:15. Tuomet į juodraštį užsirašote
skaičių „19”, o pulsas bus P gul = 4×19 = 76.
Jei chronometras rodo 0:14 , o Jūs mintyse esate suskaičiavęs 18 dūžių, tačiau 19-tą dūžį
pajuntate po to, kaip chronometras parodo 0:15. Tuomet į juodraštį užsirašote skaičių
„18,5”, o pulsas bus P gul = 4×18,5 = 74.</i></font>
        </div>
    </div>
</div>
    """, width = 250)

pgrytas = TextInput(name = "rytas16", value="", title = "Rytas", width = 60)
pgpietus = TextInput(name = "pietus16", value="", title = "Pietūs", width = 60)
pgvakaras = TextInput(name = "vakaras16", value="", title = "Vakaras", width = 60)

def aprsiskraujgul():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup21"><br>Sistolinis kraujospūdis gulint<br>(rodmuo ekrane ties „SYS“)</a>
</div>

<div id="popup21" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Sistolinis kraujospūdis gulint</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Manžetė pripumpuojama oro iki slėgio 180-200 mmHg ir
pamatuojamas kraujospūdis. Sistolinis kraujospūdis (didesnis rodmuo ties užrašu „SYS“)
įrašomas eilutėje 5.3 „Sistolinis kraujospūdis gulint, Sis 1“,
        </div>
    </div>
</div>
    """, width = 250)

skgrytas = TextInput(name = "rytas17", value="", title = "Rytas", width = 60)
skgpietus = TextInput(name = "pietus17", value="", title = "Pietūs", width = 60)
skgvakaras = TextInput(name = "vakaras17", value="", title = "Vakaras", width = 60)

def aprdiakraujgul():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup22"><br>Diastolinis kraujospūdis gulint<br>(rodmuo ekrane ties „DIA“)</a>
</div>

<div id="popup22" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Diastolinis kraujospūdis gulint</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Manžetė pripumpuojama oro iki slėgio 180-200 mmHg ir
pamatuojamas kraujospūdis. Diastolinis kraujospūdis (mažesnis rodmuo ties užrašu „DIA“ ) įrašomas eilutėje 5.4 „Diastolinis kraujospūdis
gulint, Dia 1 “.
        </div>
    </div>
</div>
    """, width = 250)

dkgrytas = TextInput(name = "rytas18", value="", title = "Rytas", width = 60)
dkgpietus = TextInput(name = "pietus18", value="", title = "Pietūs", width = 60)
dkgvakaras = TextInput(name = "vakaras18", value="", title = "Vakaras", width = 60)

def aprpulsatsi15():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup23">• Pulsas tik ką atsistojus ir po 15 s:</a>
</div>

<div id="popup23" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Pulsas tik ką atsistojus ir po 15 s</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Tiriamajam pilnai atsistojus paleidžiamas
chronometras ir pradedami skaičiuoti širdies dūžiai kaip ir 8 punkte.
Skaičiuojama 15 sekundžių, skaičius įsimenamas arba garsiai pasakomas
asistentui, nestabdant chronometro, iškart pradedamas skaičiuoti antras pulsas,
skaičiuojama dar 30 sekundžių, t.y. kol chronometras rodys 0:45, skaičius taip
pat įsimenamas arba garsiai pasakomas asistentui:
        </div>
    </div>
</div>
    """, width = 250)

parytas = TextInput(name = "rytas19", value="", title = "Rytas", width = 60)
papietus = TextInput(name = "pietus19", value="", title = "Pietūs", width = 60)
pavakaras = TextInput(name = "vakaras19", value="", title = "Vakaras", width = 60)

pa15rytas = TextInput(name = "rytas20", value="", title = "Rytas", width = 60)
pa15pietus = TextInput(name = "pietus20", value="", title = "Pietūs", width = 60)
pa15vakaras = TextInput(name = "vakaras20", value="", title = "Vakaras", width = 60)

def aprkraujpulsatsi45():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup24">• Kraujospūdis ir pulsas atsistojus po 45 s:</a>
</div>

<div id="popup24" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Kraujospūdis ir pulsas atsistojus po 45 s</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
<i>Triamojo paprašoma atpalaiduoti
ranką bei stovėti ramiai</i>. Tuomet kairė tiriamojo ranka nuleidžiama, pripučiama
kraujospūdžio matuoklio manžetė ir pamatuojamas kraujospūdis (automatiškai
pamatuojamas ir pulsas).
<br>Tiriamojo paprašoma atsisėsti. Išleidžiamas oras iš manžetės. Juodraštyje
užsirašomi abu įsiminti skaičiai iš eilės. Pirmąjį skaičių padauginę iš 4 gauname
pulsą iškart atsistojus, jis įrašomas eilutėje 5.5 „Puslas tik ką atsistojus, P 2 ”.
Antrąjį skaičių padauginę iš 2, gauname antrąjį pulsą atsistojus, jis įrašomas
eilutėje „Pulsas atsistojus po 15 s, P 3 ”. Užsirašomi kraujospūdžio matuoklio
ekrane rodomi skaičiai: sistolinis kraujospūdis (didesnis rodmuo ties užrašu
„SYS“) įrašomas eilutėje 5.7 „Sistolinis kraujospūdis atsistojus, Sis 2 “, diastolinis
kraujospūdis (mažesnis rodmuo ties užrašu „DIA“) įrašomas eilutėje 5.8
„Diastolinis kraujospūdis atsistojus, Dia 2 “, o ekrane rodomas pulsas – eilutėje 5.9
„Pulsas atsistojus po 45 s, P 4 ”.
        </div>
    </div>
</div>
    """, width = 250)

skarytas = TextInput(name = "rytas21", value="", title = "Rytas", width = 60)
skapietus = TextInput(name = "pietus21", value="", title = "Pietūs", width = 60)
skavakaras = TextInput(name = "vakaras21", value="", title = "Vakaras", width = 60)

dkarytas = TextInput(name = "rytas22", value="", title = "Rytas", width = 60)
dkapietus = TextInput(name = "pietus22", value="", title = "Pietūs", width = 60)
dkavakaras = TextInput(name = "vakaras22", value="", title = "Vakaras", width = 60)

pa45rytas = TextInput(name = "rytas23", value="", title = "Rytas", width = 60)
pa45pietus = TextInput(name = "pietus23", value="", title = "Pietūs", width = 60)
pa45vakaras = TextInput(name = "vakaras23", value="", title = "Vakaras", width = 60)

def aprkvepsu():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup25"><br>Kvėpavimo sulaikymas įkvėpus</a>
</div>

<div id="popup25" class="overlay">
    <div class="popup" id="showpopup">
        <h2>Kvėpavimo sulaikymas įkvėpus</h2>
        <a class="close" href="#showpopup">&times;</a>
        <div class="content">
Įsitikinama, kad tiriamasis sėdi tiesia nugara.
Tiriamojo paprašoma pajausti savo kvėpavimą kelis kartus įkvėpiant ir iškvėpiant, tuomet
įkvėpti, bet IŠLAIKYTI TIESIĄ NUGARĄ, nekelti pečių ar kitaip nepersitempti, sulaikius
kvėpavimą duoti ženklą linktelint galvą. Kvėpavimą sulaikyti kiek įmanoma ilgiau, iškvėpti
tik kai jau visiškai neįmanoma sulaikyti kvėpavimo nė sekundės ilgiau, tačiau nesimuistyti
ar kitaip nebandyti užtęsti laiko. Tiriamajam įkvėpus ir linktelėjus galvą, paleidžiamas
chronometras, jam pilnai iškvėpus, chronometras stabdomas. Chronometro ekrane
rodomas laikas sekundėmis įrašomas eilutėje 6.2 „Kvėpavimo sulaikymas įkvėpus, t“.
        </div>
    </div>
</div>
    """, width = 250)

ksirytas = TextInput(name = "rytas24", value="", title = "Rytas", width = 60)
ksipietus = TextInput(name = "pietus24", value="", title = "Pietūs", width = 60)
ksivakaras = TextInput(name = "vakaras24", value="", title = "Vakaras", width = 60)


sourceps1r = ColumnDataSource(data=dict(x=[], y=[]))
sourceps1p = ColumnDataSource(data=dict(x=[], y=[]))
sourceps1v = ColumnDataSource(data=dict(x=[], y=[]))

r1 = p.line('x', 'y', source = sourceps1r, line_color = "blue", line_width = 5)
r2 = p.line('x', 'y', source = sourceps1p, line_color = "blue", line_width = 5)
r3 = p.line('x', 'y', source = sourceps1v, line_color = "blue", line_width = 5)

sourcesdr = ColumnDataSource(data=dict(x=[], y=[]))
sourcesdp = ColumnDataSource(data=dict(x=[], y=[]))
sourcesdv = ColumnDataSource(data=dict(x=[], y=[]))

r4 = p.line('x', 'y', source = sourcesdr, line_color = "blue", line_width = 5)
r5 = p.line('x', 'y', source = sourcesdp, line_color = "blue", line_width = 5)
r6 = p.line('x', 'y', source = sourcesdv, line_color = "blue", line_width = 5)

sourceppr = ColumnDataSource(data=dict(x=[], y=[]))
sourceppp = ColumnDataSource(data=dict(x=[], y=[]))
sourceppv = ColumnDataSource(data=dict(x=[], y=[]))

r7 = p.line('x', 'y', source = sourceppr, line_color = "blue", line_width = 5)
r8 = p.line('x', 'y', source = sourceppp, line_color = "blue", line_width = 5)
r9 = p.line('x', 'y', source = sourceppv, line_color = "blue", line_width = 5)

sourcekrir = ColumnDataSource(data=dict(x=[], y=[]))
sourcekrip = ColumnDataSource(data=dict(x=[], y=[]))
sourcekriv = ColumnDataSource(data=dict(x=[], y=[]))

r10 = p.line('x', 'y', source = sourcekrir, line_color = "blue", line_width = 5)
r11 = p.line('x', 'y', source = sourcekrip, line_color = "blue", line_width = 5)
r12 = p.line('x', 'y', source = sourcekriv, line_color = "blue", line_width = 5)

sourcetempr = ColumnDataSource(data=dict(x=[], y=[]))
sourcetempp = ColumnDataSource(data=dict(x=[], y=[]))
sourcetempv = ColumnDataSource(data=dict(x=[], y=[]))

r13 = p.line('x', 'y', source = sourcetempr, line_color = "blue", line_width = 5)
r14 = p.line('x', 'y', source = sourcetempp, line_color = "blue", line_width = 5)
r15 = p.line('x', 'y', source = sourcetempv, line_color = "blue", line_width = 5)

sourcedermr = ColumnDataSource(data=dict(x=[], y=[]))
sourcedermp = ColumnDataSource(data=dict(x=[], y=[]))
sourcedermv = ColumnDataSource(data=dict(x=[], y=[]))

r16 = p.line('x', 'y', source = sourcedermr, line_color = "blue", line_width = 5)
r17 = p.line('x', 'y', source = sourcedermp, line_color = "blue", line_width = 5)
r18 = p.line('x', 'y', source = sourcedermv, line_color = "blue", line_width = 5)

sourcevasor = ColumnDataSource(data=dict(x=[], y=[]))
sourcevasop = ColumnDataSource(data=dict(x=[], y=[]))
sourcevasov = ColumnDataSource(data=dict(x=[], y=[]))

r19 = p.line('x', 'y', source = sourcevasor, line_color = "blue", line_width = 5)
r20 = p.line('x', 'y', source = sourcevasop, line_color = "blue", line_width = 5)
r21 = p.line('x', 'y', source = sourcevasov, line_color = "blue", line_width = 5)

sourcevyzdr = ColumnDataSource(data=dict(x=[], y=[]))
sourcevyzdp = ColumnDataSource(data=dict(x=[], y=[]))
sourcevyzdv = ColumnDataSource(data=dict(x=[], y=[]))

r22 = p.line('x', 'y', source = sourcevyzdr, line_color = "blue", line_width = 5)
r23 = p.line('x', 'y', source = sourcevyzdp, line_color = "blue", line_width = 5)
r24 = p.line('x', 'y', source = sourcevyzdv, line_color = "blue", line_width = 5)

sourcetremr = ColumnDataSource(data=dict(x=[], y=[]))
sourcetremp = ColumnDataSource(data=dict(x=[], y=[]))
sourcetremv = ColumnDataSource(data=dict(x=[], y=[]))

r25 = p.line('x', 'y', source = sourcetremr, line_color = "blue", line_width = 5)
r26 = p.line('x', 'y', source = sourcetremp, line_color = "blue", line_width = 5)
r27 = p.line('x', 'y', source = sourcetremv, line_color = "blue", line_width = 5)

sourcenosr = ColumnDataSource(data=dict(x=[], y=[]))
sourcenosp = ColumnDataSource(data=dict(x=[], y=[]))
sourcenosv = ColumnDataSource(data=dict(x=[], y=[]))

r28 = p.line('x', 'y', source = sourcenosr, line_color = "blue", line_width = 5)
r29 = p.line('x', 'y', source = sourcenosp, line_color = "blue", line_width = 5)
r30 = p.line('x', 'y', source = sourcenosv, line_color = "blue", line_width = 5)

sourcesargr = ColumnDataSource(data=dict(x=[], y=[]))
sourcesargp = ColumnDataSource(data=dict(x=[], y=[]))
sourcesargv = ColumnDataSource(data=dict(x=[], y=[]))

r31 = p.line('x', 'y', source = sourcesargr, line_color = "blue", line_width = 5)
r32 = p.line('x', 'y', source = sourcesargp, line_color = "blue", line_width = 5)
r33 = p.line('x', 'y', source = sourcesargv, line_color = "blue", line_width = 5)

sourcesklr = ColumnDataSource(data=dict(x=[], y=[]))
sourcesklp = ColumnDataSource(data=dict(x=[], y=[]))
sourcesklv = ColumnDataSource(data=dict(x=[], y=[]))

r34 = p.line('x', 'y', source = sourcesklr, line_color = "blue", line_width = 5)
r35 = p.line('x', 'y', source = sourcesklp, line_color = "blue", line_width = 5)
r36 = p.line('x', 'y', source = sourcesklv, line_color = "blue", line_width = 5)




normakps1 = -2
normaaps1 = 0
balanps1 = (normaaps1+normakps1)/2
pagrps1 = 2
def ps1r_update(attr, old, new):
    def zenklasps1r():
    	def kryptisps1r():
    		if normakps1-balanps1 < 0:
    			return 1
    		else:
    			return-1
    	psr = float(psrytas.value.replace(",", "."))
    	pgr = float(pgrytas.value.replace(",", "."))
    	verteps1r = psr-pgr
    	if (verteps1r-balanps1)*kryptisps1r()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasps1r())
    def alfaps1r():
    	if zenklasps1r()>0:
    		return (1-pagrps1)/(balanps1-normaaps1)
    	else:
    		return (1-pagrps1)/(balanps1-normakps1)
    print(alfaps1r())
    def betaps1r():
    	if zenklasps1r()>0:
    		return (pagrps1*balanps1-normaaps1)/(balanps1-normaaps1)
    	else:
    		return (pagrps1*balanps1-normakps1)/(balanps1-normakps1)
    print(betaps1r())
    def karareiksmeps1r():
    	psr = float(psrytas.value.replace(",", "."))
    	pgr = float(pgrytas.value.replace(",", "."))
    	verteps1 = psr-pgr
    	if zenklasps1r()<0:
    		return zenklasps1r()*math.log(alfaps1r()*verteps1+betaps1r(), pagrps1)
    	else:
    		return zenklasps1r()*math.log(alfaps1r()*verteps1+betaps1r(), pagrps1)
    ps1rnew_data={'x':[0,karareiksmeps1r()],'y':["ps1r","ps1r"]}
    sourceps1r.data.update(ps1rnew_data)
    print(karareiksmeps1r())
psrytas.on_change("value", ps1r_update)
pgrytas.on_change("value", ps1r_update)

def ps1p_update(attr, old, new):
    def zenklasps1p():
    	def kryptisps1p():
    		if normakps1-balanps1 < 0:
    			return 1
    		else:
    			return-1
    	psp = float(pspietus.value.replace(",", "."))
    	pgp = float(pgpietus.value.replace(",", "."))
    	verteps1p = psp-pgp
    	if (verteps1p-balanps1)*kryptisps1p()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasps1p())
    def alfaps1p():
    	if zenklasps1p()>0:
    		return (1-pagrps1)/(balanps1-normaaps1)
    	else:
    		return (1-pagrps1)/(balanps1-normakps1)
    print(alfaps1p())
    def betaps1p():
    	if zenklasps1p()>0:
    		return (pagrps1*balanps1-normaaps1)/(balanps1-normaaps1)
    	else:
    		return (pagrps1*balanps1-normakps1)/(balanps1-normakps1)
    print(betaps1p())
    def karareiksmeps1p():
    	psp = float(pspietus.value.replace(",", "."))
    	pgp = float(pgpietus.value.replace(",", "."))
    	verteps1 = psp-pgp
    	if zenklasps1p()<0:
    		return zenklasps1p()*math.log(alfaps1p()*verteps1+betaps1p(), pagrps1)
    	else:
    		return zenklasps1p()*math.log(alfaps1p()*verteps1+betaps1p(), pagrps1)
    ps1pnew_data={'x':[0,karareiksmeps1p()],'y':["ps1p","ps1p"]}
    sourceps1p.data.update(ps1pnew_data)
    print(karareiksmeps1p())
pspietus.on_change("value", ps1p_update)
pgpietus.on_change("value", ps1p_update)

def ps1v_update(attr, old, new):
    def zenklasps1v():
    	def kryptisps1v():
    		if normakps1-balanps1 < 0:
    			return 1
    		else:
    			return-1
    	psv = float(psvakaras.value.replace(",", "."))
    	pgv = float(pgvakaras.value.replace(",", "."))
    	verteps1v = psv-pgv
    	if (verteps1v-balanps1)*kryptisps1v()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasps1v())
    def alfaps1v():
    	if zenklasps1v()>0:
    		return (1-pagrps1)/(balanps1-normaaps1)
    	else:
    		return (1-pagrps1)/(balanps1-normakps1)
    print(alfaps1v())
    def betaps1v():
    	if zenklasps1v()>0:
    		return (pagrps1*balanps1-normaaps1)/(balanps1-normaaps1)
    	else:
    		return (pagrps1*balanps1-normakps1)/(balanps1-normakps1)
    print(betaps1v())
    def karareiksmeps1v():
    	psv = float(psvakaras.value.replace(",", "."))
    	pgv = float(pgvakaras.value.replace(",", "."))
    	verteps1 = psv-pgv
    	if zenklasps1v()<0:
    		return zenklasps1v()*math.log(alfaps1v()*verteps1+betaps1v(), pagrps1)
    	else:
    		return zenklasps1v()*math.log(alfaps1v()*verteps1+betaps1v(), pagrps1)
    ps1vnew_data={'x':[0,karareiksmeps1v()],'y':["ps1v","ps1v"]}
    sourceps1v.data.update(ps1vnew_data)
    print(karareiksmeps1v())
psvakaras.on_change("value", ps1v_update)
pgvakaras.on_change("value", ps1v_update)



normaksd = 11
normaasd = 6
balansd = (normaasd+normaksd)/2
pagrsd = 2
def sdr_update(attr, old, new):
    def zenklassdr():
    	def kryptissdr():
    		if normaksd-balansd < 0:
    			return 1
    		else:
    			return-1
    	skar = float(skarytas.value.replace(",", "."))
    	skgr = float(skgrytas.value.replace(",", "."))
    	dkar = float(dkarytas.value.replace(",", "."))
    	dkgr = float(dkgrytas.value.replace(",", "."))
    	vertesd = (skar-skgr)+(dkar-dkgr)
    	if (vertesd-balansd)*kryptissdr()>=0:
    		return 1
    	else:
    		return -1
    print(zenklassdr())
    def alfasdr():
    	if zenklassdr()>0:
    		return (1-pagrsd)/(balansd-normaasd)
    	else:
    		return (1-pagrsd)/(balansd-normaksd)
    print(alfasdr())
    def betasdr():
    	if zenklassdr()>0:
    		return (pagrsd*balansd-normaasd)/(balansd-normaasd)
    	else:
    		return (pagrsd*balansd-normaksd)/(balansd-normaksd)
    print(betasdr())
    def karareiksmesdr():
    	skar = float(skarytas.value.replace(",", "."))
    	skgr = float(skgrytas.value.replace(",", "."))
    	dkar = float(dkarytas.value.replace(",", "."))
    	dkgr = float(dkgrytas.value.replace(",", "."))
    	vertesd = skar-skgr+dkar-dkgr
    	if zenklassdr()<0:
    		return zenklassdr()*math.log(alfasdr()*vertesd+betasdr(), pagrsd)
    	else:
    		return zenklassdr()*math.log(alfasdr()*vertesd+betasdr(), pagrsd)
    sdrnew_data={'x':[0,karareiksmesdr()],'y':["sdr","sdr"]}
    sourcesdr.data.update(sdrnew_data)
    print(karareiksmesdr())
skarytas.on_change("value", sdr_update)
skgrytas.on_change("value", sdr_update)
dkarytas.on_change("value", sdr_update)
dkgrytas.on_change("value", sdr_update)

def sdp_update(attr, old, new):
    def zenklassdp():
    	def kryptissdp():
    		if normaksd-balansd < 0:
    			return 1
    		else:
    			return-1
    	skap = float(skapietus.value.replace(",", "."))
    	skgp = float(skgpietus.value.replace(",", "."))
    	dkap = float(dkapietus.value.replace(",", "."))
    	dkgp = float(dkgpietus.value.replace(",", "."))
    	vertesd = (skap-skgp)+(dkap-dkgp)
    	if (vertesd-balansd)*kryptissdp()>=0:
    		return 1
    	else:
    		return -1
    print(zenklassdp())
    def alfasdp():
    	if zenklassdp()>0:
    		return (1-pagrsd)/(balansd-normaasd)
    	else:
    		return (1-pagrsd)/(balansd-normaksd)
    print(alfasdp())
    def betasdp():
    	if zenklassdp()>0:
    		return (pagrsd*balansd-normaasd)/(balansd-normaasd)
    	else:
    		return (pagrsd*balansd-normaksd)/(balansd-normaksd)
    print(betasdp())
    def karareiksmesdp():
    	skap = float(skapietus.value.replace(",", "."))
    	skgp = float(skgpietus.value.replace(",", "."))
    	dkap = float(dkapietus.value.replace(",", "."))
    	dkgp = float(dkgpietus.value.replace(",", "."))
    	vertesd = (skap-skgp)+(dkap-dkgp)
    	if zenklassdp()<0:
    		return zenklassdp()*math.log(alfasdp()*vertesd+betasdp(), pagrsd)
    	else:
    		return zenklassdp()*math.log(alfasdp()*vertesd+betasdp(), pagrsd)
    sdpnew_data={'x':[0,karareiksmesdp()],'y':["sdp","sdp"]}
    sourcesdp.data.update(sdpnew_data)
    print(karareiksmesdp())
skapietus.on_change("value", sdp_update)
skgpietus.on_change("value", sdp_update)
dkapietus.on_change("value", sdp_update)
dkgpietus.on_change("value", sdp_update)

def sdv_update(attr, old, new):
    def zenklassdv():
    	def kryptissdv():
    		if normaksd-balansd < 0:
    			return 1
    		else:
    			return-1
    	skav = float(skavakaras.value.replace(",", "."))
    	skgv = float(skgvakaras.value.replace(",", "."))
    	dkav = float(dkavakaras.value.replace(",", "."))
    	dkgv = float(dkgvakaras.value.replace(",", "."))
    	vertesd = (skav-skgv)+(dkav-dkgv)
    	if (vertesd-balansd)*kryptissdv()>=0:
    		return 1
    	else:
    		return -1
    print(zenklassdv())
    def alfasdv():
    	if zenklassdv()>0:
    		return (1-pagrsd)/(balansd-normaasd)
    	else:
    		return (1-pagrsd)/(balansd-normaksd)
    print(alfasdv())
    def betasdv():
    	if zenklassdv()>0:
    		return (pagrsd*balansd-normaasd)/(balansd-normaasd)
    	else:
    		return (pagrsd*balansd-normaksd)/(balansd-normaksd)
    print(betasdv())
    def karareiksmesdv():
    	skav = float(skavakaras.value.replace(",", "."))
    	skgv = float(skgvakaras.value.replace(",", "."))
    	dkav = float(dkavakaras.value.replace(",", "."))
    	dkgv = float(dkgvakaras.value.replace(",", "."))
    	vertesd = (skav-skgv)+(dkav-dkgv)
    	if zenklassdv()<0:
    		return zenklassdv()*math.log(alfasdv()*vertesd+betasdv(), pagrsd)
    	else:
    		return zenklassdv()*math.log(alfasdv()*vertesd+betasdv(), pagrsd)
    sdvnew_data={'x':[0,karareiksmesdv()],'y':["sdv","sdv"]}
    sourcesdv.data.update(sdvnew_data)
    print(karareiksmesdv())
skavakaras.on_change("value", sdv_update)
skgvakaras.on_change("value", sdv_update)
dkavakaras.on_change("value", sdv_update)
dkgvakaras.on_change("value", sdv_update)



normakpp = 25
normaapp = 22
balanpp = (normaapp+normakpp)/2
pagrpp = 2
def ppr_update(attr, old, new):
    def zenklasppr():
    	def kryptisppr():
    		if normakpp-balanpp < 0:
    			return 1
    		else:
    			return-1
    	pgr = float(pgrytas.value.replace(",", "."))
    	par = float(parytas.value.replace(",", "."))
    	pa15r = float(pa15rytas.value.replace(",", "."))
    	pa45r = float(pa45rytas.value.replace(",", "."))
    	pp1 = max(pgr, par, pa15r, pa45r)-pgr
    	pp2= max(pgr, par, pa15r, pa45r)-pa45r
    	vertepp = pp1+pp2
    	if (vertepp-balanpp)*kryptisppr()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasppr())
    def alfappr():
    	if zenklasppr()>0:
    		return (1-pagrpp)/(balanpp-normaapp)
    	else:
    		return (1-pagrpp)/(balanpp-normakpp)
    print(alfappr())
    def betappr():
    	if zenklasppr()>0:
    		return (pagrpp*balanpp-normaapp)/(balanpp-normaapp)
    	else:
    		return (pagrpp*balanpp-normakpp)/(balanpp-normakpp)
    print(betappr())
    def karareiksmeppr():
    	pgr = float(pgrytas.value.replace(",", "."))
    	par = float(parytas.value.replace(",", "."))
    	pa15r = float(pa15rytas.value.replace(",", "."))
    	pa45r = float(pa45rytas.value.replace(",", "."))
    	pp1 = max(pgr, par, pa15r, pa45r)-pgr
    	pp2= max(pgr, par, pa15r, pa45r)-pa45r
    	vertepp = pp1+pp2
    	if zenklasppr()<0:
    		return zenklasppr()*math.log(alfappr()*vertepp+betappr(), pagrpp)
    	else:
    		return zenklasppr()*math.log(alfappr()*vertepp+betappr(), pagrpp)
    pprnew_data={'x':[0,karareiksmeppr()],'y':["ppr","ppr"]}
    sourceppr.data.update(pprnew_data)
    print(karareiksmeppr())
pgrytas.on_change("value", ppr_update)
parytas.on_change("value", ppr_update)
pa15rytas.on_change("value", ppr_update)
pa45rytas.on_change("value", ppr_update)

def ppp_update(attr, old, new):
    def zenklasppp():
    	def kryptisppp():
    		if normakpp-balanpp < 0:
    			return 1
    		else:
    			return-1
    	pgp = float(pgpietus.value.replace(",", "."))
    	pap = float(papietus.value.replace(",", "."))
    	pa15p = float(pa15pietus.value.replace(",", "."))
    	pa45p = float(pa45pietus.value.replace(",", "."))
    	pp1 = max(pgp, pap, pa15p, pa45p)-pgp
    	pp2= max(pgp, pap, pa15p, pa45p)-pa45p
    	vertepp = pp1+pp2
    	if (vertepp-balanpp)*kryptisppp()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasppp())
    def alfappp():
    	if zenklasppp()>0:
    		return (1-pagrpp)/(balanpp-normaapp)
    	else:
    		return (1-pagrpp)/(balanpp-normakpp)
    print(alfappp())
    def betappp():
    	if zenklasppp()>0:
    		return (pagrpp*balanpp-normaapp)/(balanpp-normaapp)
    	else:
    		return (pagrpp*balanpp-normakpp)/(balanpp-normakpp)
    print(betappp())
    def karareiksmeppp():
    	pgp = float(pgpietus.value.replace(",", "."))
    	pap = float(papietus.value.replace(",", "."))
    	pa15p = float(pa15pietus.value.replace(",", "."))
    	pa45p = float(pa45pietus.value.replace(",", "."))
    	pp1 = max(pgp, pap, pa15p, pa45p)-pgp
    	pp2= max(pgp, pap, pa15p, pa45p)-pa45p
    	vertepp = pp1+pp2
    	if zenklasppp()<0:
    		return zenklasppp()*math.log(alfappp()*vertepp+betappp(), pagrpp)
    	else:
    		return zenklasppp()*math.log(alfappp()*vertepp+betappp(), pagrpp)
    pppnew_data={'x':[0,karareiksmeppp()],'y':["ppp","ppp"]}
    sourceppp.data.update(pppnew_data)
    print(karareiksmeppp())
pgpietus.on_change("value", ppp_update)
papietus.on_change("value", ppp_update)
pa15pietus.on_change("value", ppp_update)
pa45pietus.on_change("value", ppp_update)


def ppv_update(attr, old, new):
    def zenklasppv():
    	def kryptisppv():
    		if normakpp-balanpp < 0:
    			return 1
    		else:
    			return-1
    	pgv = float(pgvakaras.value.replace(",", "."))
    	pav = float(pavakaras.value.replace(",", "."))
    	pa15v = float(pa15vakaras.value.replace(",", "."))
    	pa45v = float(pa45vakaras.value.replace(",", "."))
    	pp1 = max(pgv, pav, pa15v, pa45v)-pgv
    	pp2= max(pgv, pav, pa15v, pa45v)-pa45v
    	vertepp = pp1+pp2
    	if (vertepp-balanpp)*kryptisppv()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasppv())
    def alfappv():
    	if zenklasppv()>0:
    		return (1-pagrpp)/(balanpp-normaapp)
    	else:
    		return (1-pagrpp)/(balanpp-normakpp)
    print(alfappv())
    def betappv():
    	if zenklasppv()>0:
    		return (pagrpp*balanpp-normaapp)/(balanpp-normaapp)
    	else:
    		return (pagrpp*balanpp-normakpp)/(balanpp-normakpp)
    print(betappv())
    def karareiksmeppv():
    	pgv = float(pgvakaras.value.replace(",", "."))
    	pav = float(pavakaras.value.replace(",", "."))
    	pa15v = float(pa15vakaras.value.replace(",", "."))
    	pa45v = float(pa45vakaras.value.replace(",", "."))
    	pp1 = max(pgv, pav, pa15v, pa45v)-pgv
    	pp2= max(pgv, pav, pa15v, pa45v)-pa45v
    	vertepp = pp1+pp2
    	if zenklasppv()<0:
    		return zenklasppv()*math.log(alfappv()*vertepp+betappv(), pagrpp)
    	else:
    		return zenklasppv()*math.log(alfappv()*vertepp+betappv(), pagrpp)
    ppvnew_data={'x':[0,karareiksmeppv()],'y':["ppv","ppv"]}
    sourceppv.data.update(ppvnew_data)
    print(karareiksmeppv())
pgvakaras.on_change("value", ppv_update)
pavakaras.on_change("value", ppv_update)
pa15vakaras.on_change("value", ppv_update)
pa45vakaras.on_change("value", ppv_update)



normakkri = 6
normaakri = 4
balankri = (normaakri+normakkri)/2
pagrkri = 1.001
def krir_update(attr, old, new):
    def zenklaskrir():
    	def kryptiskrir():
    		if normakkri-balankri < 0:
    			return 1
    		else:
    			return-1
    	psr = float(psrytas.value.replace(",", "."))
    	kdr = float(kdrytas.value.replace(",", "."))
    	vertekri = psr/kdr
    	if (vertekri-balankri)*kryptiskrir()>=0:
    		return 1
    	else:
    		return -1
    print(zenklaskrir())
    def alfakrir():
    	if zenklaskrir()>0:
    		return (1-pagrkri)/(balankri-normaakri)
    	else:
    		return (1-pagrkri)/(balankri-normakkri)
    print(alfakrir())
    def betakrir():
    	if zenklaskrir()>0:
    		return (pagrkri*balankri-normaakri)/(balankri-normaakri)
    	else:
    		return (pagrkri*balankri-normakkri)/(balankri-normakkri)
    print(betakrir())
    def karareiksmekrir():
    	psr = float(psrytas.value.replace(",", "."))
    	kdr = float(kdrytas.value.replace(",", "."))
    	vertekri = psr/kdr
    	if zenklaskrir()<0:
    		return zenklaskrir()*math.log(alfakrir()*vertekri+betakrir(), pagrkri)
    	else:
    		return zenklaskrir()*math.log(alfakrir()*vertekri+betakrir(), pagrkri)
    krirnew_data={'x':[0,karareiksmekrir()],'y':["krir","krir"]}
    sourcekrir.data.update(krirnew_data)
    print(karareiksmekrir())
psrytas.on_change("value", krir_update)
kdrytas.on_change("value", krir_update)

def krip_update(attr, old, new):
    def zenklaskrip():
    	def kryptiskrip():
    		if normakkri-balankri < 0:
    			return 1
    		else:
    			return-1
    	psp = float(pspietus.value.replace(",", "."))
    	kdp = float(kdpietus.value.replace(",", "."))
    	vertekri = psp/kdp
    	if (vertekri-balankri)*kryptiskrip()>=0:
    		return 1
    	else:
    		return -1
    print(zenklaskrip())
    def alfakrip():
    	if zenklaskrip()>0:
    		return (1-pagrkri)/(balankri-normaakri)
    	else:
    		return (1-pagrkri)/(balankri-normakkri)
    print(alfakrip())
    def betakrip():
    	if zenklaskrip()>0:
    		return (pagrkri*balankri-normaakri)/(balankri-normaakri)
    	else:
    		return (pagrkri*balankri-normakkri)/(balankri-normakkri)
    print(betakrip())
    def karareiksmekrip():
    	psp = float(pspietus.value.replace(",", "."))
    	kdp = float(kdpietus.value.replace(",", "."))
    	vertekri = psp/kdp
    	if zenklaskrip()<0:
    		return zenklaskrip()*math.log(alfakrip()*vertekri+betakrip(), pagrkri)
    	else:
    		return zenklaskrip()*math.log(alfakrip()*vertekri+betakrip(), pagrkri)
    kripnew_data={'x':[0,karareiksmekrip()],'y':["krip","krip"]}
    sourcekrip.data.update(kripnew_data)
    print(karareiksmekrip())
pspietus.on_change("value", krip_update)
kdpietus.on_change("value", krip_update)

def kriv_update(attr, old, new):
    def zenklaskriv():
    	def kryptiskriv():
    		if normakkri-balankri < 0:
    			return 1
    		else:
    			return-1
    	psv = float(psvakaras.value.replace(",", "."))
    	kdv = float(kdvakaras.value.replace(",", "."))
    	vertekri = psv/kdv
    	if (vertekri-balankri)*kryptiskriv()>=0:
    		return 1
    	else:
    		return -1
    print(zenklaskriv())
    def alfakriv():
    	if zenklaskriv()>0:
    		return (1-pagrkri)/(balankri-normaakri)
    	else:
    		return (1-pagrkri)/(balankri-normakkri)
    print(alfakriv())
    def betakriv():
    	if zenklaskriv()>0:
    		return (pagrkri*balankri-normaakri)/(balankri-normaakri)
    	else:
    		return (pagrkri*balankri-normakkri)/(balankri-normakkri)
    print(betakriv())
    def karareiksmekriv():
    	psv = float(psvakaras.value.replace(",", "."))
    	kdv = float(kdvakaras.value.replace(",", "."))
    	vertekri = psv/kdv
    	if zenklaskriv()<0:
    		return zenklaskriv()*math.log(alfakriv()*vertekri+betakriv(), pagrkri)
    	else:
    		return zenklaskriv()*math.log(alfakriv()*vertekri+betakriv(), pagrkri)
    krivnew_data={'x':[0,karareiksmekriv()],'y':["kriv","kriv"]}
    sourcekriv.data.update(krivnew_data)
    print(karareiksmekriv())
psvakaras.on_change("value", kriv_update)
kdvakaras.on_change("value", kriv_update)



normaktemp = 36.7
normaatemp = 36.5
balantemp = float((normaatemp+normaktemp)/2)
pagrtemp = 2
def tempr_update(attr, old, new):
    def zenklastempr():
    	def kryptistempr():
    		if normaktemp-balantemp < 0:
    			return 1
    		else:
    			return-1
    	vertetemp = float(ktrytas.value.replace(",", "."))
    	if (vertetemp-balantemp)*kryptistempr()>=0:
    		return 1
    	else:
    		return -1
    print(zenklastempr())
    def alfatempr():
    	if zenklastempr()>0:
    		return (1-pagrtemp)/(balantemp-normaatemp)
    	else:
    		return (1-pagrtemp)/(balantemp-normaktemp)
    print(alfatempr())
    def betatempr():
    	if zenklastempr()>0:
    		return (pagrtemp*balantemp-normaatemp)/(balantemp-normaatemp)
    	else:
    		return (pagrtemp*balantemp-normaktemp)/(balantemp-normaktemp)
    print(betatempr())
    def karareiksmetempr():
    	vertetemp = float(ktrytas.value.replace(",", "."))
    	if zenklastempr()<0:
    		return zenklastempr()*math.log(float(alfatempr())*float(vertetemp)+float(betatempr()), pagrtemp)
    	else:
    		return zenklastempr()*math.log(float(alfatempr())*float(vertetemp)+float(betatempr()), pagrtemp)
    temprnew_data={'x':[0,karareiksmetempr()],'y':["tempr","tempr"]}
    sourcetempr.data.update(temprnew_data)
    print(karareiksmetempr())
ktrytas.on_change("value", tempr_update)

def tempp_update(attr, old, new):
    def zenklastempp():
    	def kryptistempp():
    		if normaktemp-balantemp < 0:
    			return 1
    		else:
    			return-1
    	vertetemp = float(ktpietus.value.replace(",", "."))
    	if (vertetemp-balantemp)*kryptistempp()>=0:
    		return 1
    	else:
    		return -1
    print(zenklastempp())
    def alfatempp():
    	if zenklastempp()>0:
    		return (1-pagrtemp)/(balantemp-normaatemp)
    	else:
    		return (1-pagrtemp)/(balantemp-normaktemp)
    print(alfatempp())
    def betatempp():
    	if zenklastempp()>0:
    		return (pagrtemp*balantemp-normaatemp)/(balantemp-normaatemp)
    	else:
    		return (pagrtemp*balantemp-normaktemp)/(balantemp-normaktemp)
    print(betatempp())
    def karareiksmetempp():
    	vertetemp = float(ktpietus.value.replace(",", "."))
    	if zenklastempp()<0:
    		return zenklastempp()*math.log(float(alfatempp())*float(vertetemp)+float(betatempp()), pagrtemp)
    	else:
    		return zenklastempp()*math.log(float(alfatempp())*float(vertetemp)+float(betatempp()), pagrtemp)
    temppnew_data={'x':[0,karareiksmetempp()],'y':["tempp","tempp"]}
    sourcetempp.data.update(temppnew_data)
    print(karareiksmetempp())
ktpietus.on_change("value", tempp_update)

def tempv_update(attr, old, new):
    def zenklastempv():
    	def kryptistempv():
    		if normaktemp-balantemp < 0:
    			return 1
    		else:
    			return-1
    	vertetemp = float(ktvakaras.value.replace(",", "."))
    	if (vertetemp-balantemp)*kryptistempv()>=0:
    		return 1
    	else:
    		return -1
    print(zenklastempv())
    def alfatempv():
    	if zenklastempv()>0:
    		return (1-pagrtemp)/(balantemp-normaatemp)
    	else:
    		return (1-pagrtemp)/(balantemp-normaktemp)
    print(alfatempv())
    def betatempv():
    	if zenklastempv()>0:
    		return (pagrtemp*balantemp-normaatemp)/(balantemp-normaatemp)
    	else:
    		return (pagrtemp*balantemp-normaktemp)/(balantemp-normaktemp)
    print(betatempv())
    def karareiksmetempv():
    	vertetemp = float(ktvakaras.value.replace(",", "."))
    	if zenklastempv()<0:
    		return zenklastempv()*math.log(float(alfatempv())*float(vertetemp)+float(betatempv()), pagrtemp)
    	else:
    		return zenklastempv()*math.log(float(alfatempv())*float(vertetemp)+float(betatempv()), pagrtemp)
    tempvnew_data={'x':[0,karareiksmetempv()],'y':["tempv","tempv"]}
    sourcetempv.data.update(tempvnew_data)
    print(karareiksmetempv())
ktvakaras.on_change("value", tempv_update)



normakderm= 1
normaaderm = 2
balanderm = float((normaaderm+normakderm)/2)
pagrderm = 1.2
def dermr_update(attr, old, new):
    def zenklasdermr():
    	def kryptisdermr():
    		if normakderm-balanderm < 0:
    			return 1
    		else:
    			return-1
    	vertederm = float(drrytas.value.replace(",", "."))
    	if (vertederm-balanderm)*kryptisdermr()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasdermr())
    def alfadermr():
    	if zenklasdermr()>0:
    		return (1-pagrderm)/(balanderm-normaaderm)
    	else:
    		return (1-pagrderm)/(balanderm-normakderm)
    print(alfadermr())
    def betadermr():
    	if zenklasdermr()>0:
    		return (pagrderm*balanderm-normaaderm)/(balanderm-normaaderm)
    	else:
    		return (pagrderm*balanderm-normakderm)/(balanderm-normakderm)
    print(betadermr())
    def karareiksmedermr():
    	vertederm = float(drrytas.value.replace(",", "."))
    	if zenklasdermr()<0:
    		return zenklasdermr()*math.log(float(alfadermr())*float(vertederm)+float(betadermr()), pagrderm)
    	else:
    		return zenklasdermr()*math.log(float(alfadermr())*float(vertederm)+float(betadermr()), pagrderm)
    dermrnew_data={'x':[0,karareiksmedermr()],'y':["dermr","dermr"]}
    sourcedermr.data.update(dermrnew_data)
    print(karareiksmedermr())
drrytas.on_change("value", dermr_update)

def dermp_update(attr, old, new):
    def zenklasdermp():
    	def kryptisdermp():
    		if normakderm-balanderm < 0:
    			return 1
    		else:
    			return-1
    	vertederm = float(drpietus.value.replace(",", "."))
    	if (vertederm-balanderm)*kryptisdermp()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasdermp())
    def alfadermp():
    	if zenklasdermp()>0:
    		return (1-pagrderm)/(balanderm-normaaderm)
    	else:
    		return (1-pagrderm)/(balanderm-normakderm)
    print(alfadermp())
    def betadermp():
    	if zenklasdermp()>0:
    		return (pagrderm*balanderm-normaaderm)/(balanderm-normaaderm)
    	else:
    		return (pagrderm*balanderm-normakderm)/(balanderm-normakderm)
    print(betadermp())
    def karareiksmedermp():
    	vertederm = float(drpietus.value.replace(",", "."))
    	if zenklasdermp()<0:
    		return zenklasdermp()*math.log(float(alfadermp())*float(vertederm)+float(betadermp()), pagrderm)
    	else:
    		return zenklasdermp()*math.log(float(alfadermp())*float(vertederm)+float(betadermp()), pagrderm)
    dermpnew_data={'x':[0,karareiksmedermp()],'y':["dermp","dermp"]}
    sourcedermp.data.update(dermpnew_data)
    print(karareiksmedermp())
drpietus.on_change("value", dermp_update)

def dermv_update(attr, old, new):
    def zenklasdermv():
    	def kryptisdermv():
    		if normakderm-balanderm < 0:
    			return 1
    		else:
    			return-1
    	vertederm = float(drvakaras.value.replace(",", "."))
    	if (vertederm-balanderm)*kryptisdermv()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasdermv())
    def alfadermv():
    	if zenklasdermv()>0:
    		return (1-pagrderm)/(balanderm-normaaderm)
    	else:
    		return (1-pagrderm)/(balanderm-normakderm)
    print(alfadermv())
    def betadermv():
    	if zenklasdermv()>0:
    		return (pagrderm*balanderm-normaaderm)/(balanderm-normaaderm)
    	else:
    		return (pagrderm*balanderm-normakderm)/(balanderm-normakderm)
    print(betadermv())
    def karareiksmedermv():
    	vertederm = float(drvakaras.value.replace(",", "."))
    	if zenklasdermv()<0:
    		return zenklasdermv()*math.log(float(alfadermv())*float(vertederm)+float(betadermv()), pagrderm)
    	else:
    		return zenklasdermv()*math.log(float(alfadermv())*float(vertederm)+float(betadermv()), pagrderm)
    dermvnew_data={'x':[0,karareiksmedermv()],'y':["dermv","dermv"]}
    sourcedermv.data.update(dermvnew_data)
    print(karareiksmedermv())
drvakaras.on_change("value", dermv_update)



normakvaso= -1
normaavaso = 1
balanvaso = float((normaavaso+normakvaso)/2)
pagrvaso = 1.001
def vasor_update(attr, old, new):
    def zenklasvasor():
    	def kryptisvasor():
    		if normakvaso-balanvaso < 0:
    			return 1
    		else:
    			return-1
    	vertevaso = float(vrrytas.value.replace(",", "."))
    	if (vertevaso-balanvaso)*kryptisvasor()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasvasor())
    def alfavasor():
    	if zenklasvasor()>0:
    		return (1-pagrvaso)/(balanvaso-normaavaso)
    	else:
    		return (1-pagrvaso)/(balanvaso-normakvaso)
    print(alfavasor())
    def betavasor():
    	if zenklasvasor()>0:
    		return (pagrvaso*balanvaso-normaavaso)/(balanvaso-normaavaso)
    	else:
    		return (pagrvaso*balanvaso-normakvaso)/(balanvaso-normakvaso)
    print(betavasor())
    def karareiksmevasor():
    	vertevaso = float(vrrytas.value.replace(",", "."))
    	if zenklasvasor()<0:
    		return zenklasvasor()*math.log(float(alfavasor())*float(vertevaso)+float(betavasor()), pagrvaso)
    	else:
    		return zenklasvasor()*math.log(float(alfavasor())*float(vertevaso)+float(betavasor()), pagrvaso)
    vasornew_data={'x':[0,karareiksmevasor()],'y':["vasor","vasor"]}
    sourcevasor.data.update(vasornew_data)
    print(karareiksmevasor())
vrrytas.on_change("value", vasor_update)

def vasop_update(attr, old, new):
    def zenklasvasop():
    	def kryptisvasop():
    		if normakvaso-balanvaso < 0:
    			return 1
    		else:
    			return-1
    	vertevaso = float(vrpietus.value.replace(",", "."))
    	if (vertevaso-balanvaso)*kryptisvasop()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasvasop())
    def alfavasop():
    	if zenklasvasop()>0:
    		return (1-pagrvaso)/(balanvaso-normaavaso)
    	else:
    		return (1-pagrvaso)/(balanvaso-normakvaso)
    print(alfavasop())
    def betavasop():
    	if zenklasvasop()>0:
    		return (pagrvaso*balanvaso-normaavaso)/(balanvaso-normaavaso)
    	else:
    		return (pagrvaso*balanvaso-normakvaso)/(balanvaso-normakvaso)
    print(betavasop())
    def karareiksmevasop():
    	vertevaso = float(vrpietus.value.replace(",", "."))
    	if zenklasvasop()<0:
    		return zenklasvasop()*math.log(float(alfavasop())*float(vertevaso)+float(betavasop()), pagrvaso)
    	else:
    		return zenklasvasop()*math.log(float(alfavasop())*float(vertevaso)+float(betavasop()), pagrvaso)
    vasopnew_data={'x':[0,karareiksmevasop()],'y':["vasop","vasop"]}
    sourcevasop.data.update(vasopnew_data)
    print(karareiksmevasop())
vrpietus.on_change("value", vasop_update)

def vasov_update(attr, old, new):
    def zenklasvasov():
    	def kryptisvasov():
    		if normakvaso-balanvaso < 0:
    			return 1
    		else:
    			return-1
    	vertevaso = float(vrvakaras.value.replace(",", "."))
    	if (vertevaso-balanvaso)*kryptisvasov()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasvasov())
    def alfavasov():
    	if zenklasvasov()>0:
    		return (1-pagrvaso)/(balanvaso-normaavaso)
    	else:
    		return (1-pagrvaso)/(balanvaso-normakvaso)
    print(alfavasov())
    def betavasov():
    	if zenklasvasov()>0:
    		return (pagrvaso*balanvaso-normaavaso)/(balanvaso-normaavaso)
    	else:
    		return (pagrvaso*balanvaso-normakvaso)/(balanvaso-normakvaso)
    print(betavasov())
    def karareiksmevasov():
    	vertevaso = float(vrvakaras.value.replace(",", "."))
    	if zenklasvasov()<0:
    		return zenklasvasov()*math.log(float(alfavasov())*float(vertevaso)+float(betavasov()), pagrvaso)
    	else:
    		return zenklasvasov()*math.log(float(alfavasov())*float(vertevaso)+float(betavasov()), pagrvaso)
    vasovnew_data={'x':[0,karareiksmevasov()],'y':["vasov","vasov"]}
    sourcevasov.data.update(vasovnew_data)
    print(karareiksmevasov())
vrvakaras.on_change("value", vasov_update)



normakvyzd= 1
normaavyzd = -1
balanvyzd = float((normaavyzd+normakvyzd)/2)
pagrvyzd = 1.001
def vyzdr_update(attr, old, new):
    def zenklasvyzdr():
    	def kryptisvyzdr():
    		if normakvyzd-balanvyzd < 0:
    			return 1
    		else:
    			return-1
    	vertevyzd = float(vdrytas.value.replace(",", "."))
    	if (vertevyzd-balanvyzd)*kryptisvyzdr()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasvyzdr())
    def alfavyzdr():
    	if zenklasvyzdr()>0:
    		return (1-pagrvyzd)/(balanvyzd-normaavyzd)
    	else:
    		return (1-pagrvyzd)/(balanvyzd-normakvyzd)
    print(alfavyzdr())
    def betavyzdr():
    	if zenklasvyzdr()>0:
    		return (pagrvyzd*balanvyzd-normaavyzd)/(balanvyzd-normaavyzd)
    	else:
    		return (pagrvyzd*balanvyzd-normakvyzd)/(balanvaso-normakvyzd)
    print(betavyzdr())
    def karareiksmevyzdr():
    	vertevyzd = float(vdrytas.value.replace(",", "."))
    	if zenklasvyzdr()<0:
    		return zenklasvyzdr()*math.log(float(alfavyzdr())*float(vertevyzd)+float(betavyzdr()), pagrvyzd)
    	else:
    		return zenklasvyzdr()*math.log(float(alfavyzdr())*float(vertevyzd)+float(betavyzdr()), pagrvyzd)
    vyzdrnew_data={'x':[0,karareiksmevyzdr()],'y':["vyzdr","vyzdr"]}
    sourcevyzdr.data.update(vyzdrnew_data)
    print(karareiksmevyzdr())
vdrytas.on_change("value", vyzdr_update)

def vyzdp_update(attr, old, new):
    def zenklasvyzdp():
    	def kryptisvyzdp():
    		if normakvyzd-balanvyzd < 0:
    			return 1
    		else:
    			return-1
    	vertevyzd = float(vdpietus.value.replace(",", "."))
    	if (vertevyzd-balanvyzd)*kryptisvyzdp()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasvyzdp())
    def alfavyzdp():
    	if zenklasvyzdp()>0:
    		return (1-pagrvyzd)/(balanvyzd-normaavyzd)
    	else:
    		return (1-pagrvyzd)/(balanvyzd-normakvyzd)
    print(alfavyzdp())
    def betavyzdp():
    	if zenklasvyzdp()>0:
    		return (pagrvyzd*balanvyzd-normaavyzd)/(balanvyzd-normaavyzd)
    	else:
    		return (pagrvyzd*balanvyzd-normakvyzd)/(balanvaso-normakvyzd)
    print(betavyzdp())
    def karareiksmevyzdp():
    	vertevyzd = float(vdpietus.value.replace(",", "."))
    	if zenklasvyzdp()<0:
    		return zenklasvyzdp()*math.log(float(alfavyzdp())*float(vertevyzd)+float(betavyzdp()), pagrvyzd)
    	else:
    		return zenklasvyzdp()*math.log(float(alfavyzdp())*float(vertevyzd)+float(betavyzdp()), pagrvyzd)
    vyzdpnew_data={'x':[0,karareiksmevyzdp()],'y':["vyzdp","vyzdp"]}
    sourcevyzdp.data.update(vyzdpnew_data)
    print(karareiksmevyzdp())
vdpietus.on_change("value", vyzdp_update)

def vyzdv_update(attr, old, new):
    def zenklasvyzdv():
    	def kryptisvyzdv():
    		if normakvyzd-balanvyzd < 0:
    			return 1
    		else:
    			return-1
    	vertevyzd = float(vdvakaras.value.replace(",", "."))
    	if (vertevyzd-balanvyzd)*kryptisvyzdv()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasvyzdv())
    def alfavyzdv():
    	if zenklasvyzdv()>0:
    		return (1-pagrvyzd)/(balanvyzd-normaavyzd)
    	else:
    		return (1-pagrvyzd)/(balanvyzd-normakvyzd)
    print(alfavyzdv())
    def betavyzdv():
    	if zenklasvyzdv()>0:
    		return (pagrvyzd*balanvyzd-normaavyzd)/(balanvyzd-normaavyzd)
    	else:
    		return (pagrvyzd*balanvyzd-normakvyzd)/(balanvaso-normakvyzd)
    print(betavyzdv())
    def karareiksmevyzdv():
    	vertevyzd = float(vdvakaras.value.replace(",", "."))
    	if zenklasvyzdv()<0:
    		return zenklasvyzdv()*math.log(float(alfavyzdv())*float(vertevyzd)+float(betavyzdv()), pagrvyzd)
    	else:
    		return zenklasvyzdv()*math.log(float(alfavyzdv())*float(vertevyzd)+float(betavyzdv()), pagrvyzd)
    vyzdvnew_data={'x':[0,karareiksmevyzdv()],'y':["vyzdv","vyzdv"]}
    sourcevyzdv.data.update(vyzdvnew_data)
    print(karareiksmevyzdv())
vdvakaras.on_change("value", vyzdv_update)



normaktrem= 1
normaatrem = -1
balantrem = float((normaatrem+normaktrem)/2)
pagrtrem = 1.001
def tremr_update(attr, old, new):
    def zenklastremr():
    	def kryptistremr():
    		if normaktrem-balantrem < 0:
    			return 1
    		else:
    			return-1
    	vertetrem = float(trrytas.value.replace(",", "."))
    	if (vertetrem-balantrem)*kryptistremr()>=0:
    		return 1
    	else:
    		return -1
    print(zenklastremr())
    def alfatremr():
    	if zenklastremr()>0:
    		return (1-pagrtrem)/(balantrem-normaatrem)
    	else:
    		return (1-pagrtrem)/(balantrem-normaktrem)
    print(alfatremr())
    def betatremr():
    	if zenklastremr()>0:
    		return (pagrtrem*balantrem-normaatrem)/(balantrem-normaatrem)
    	else:
    		return (pagrtrem*balantrem-normaktrem)/(balanvaso-normaktrem)
    print(betatremr())
    def karareiksmetremr():
    	vertetrem = float(trrytas.value.replace(",", "."))
    	if zenklastremr()<0:
    		return zenklastremr()*math.log(float(alfatremr())*float(vertetrem)+float(betatremr()), pagrtrem)
    	else:
    		return zenklastremr()*math.log(float(alfatremr())*float(vertetrem)+float(betatremr()), pagrtrem)
    tremrnew_data={'x':[0,karareiksmetremr()],'y':["tremr","tremr"]}
    sourcetremr.data.update(tremrnew_data)
    print(karareiksmetremr())
trrytas.on_change("value", tremr_update)

def tremp_update(attr, old, new):
    def zenklastremp():
    	def kryptistremp():
    		if normaktrem-balantrem < 0:
    			return 1
    		else:
    			return-1
    	vertetrem = float(trpietus.value.replace(",", "."))
    	if (vertetrem-balantrem)*kryptistremp()>=0:
    		return 1
    	else:
    		return -1
    print(zenklastremp())
    def alfatremp():
    	if zenklastremp()>0:
    		return (1-pagrtrem)/(balantrem-normaatrem)
    	else:
    		return (1-pagrtrem)/(balantrem-normaktrem)
    print(alfatremp())
    def betatremp():
    	if zenklastremp()>0:
    		return (pagrtrem*balantrem-normaatrem)/(balantrem-normaatrem)
    	else:
    		return (pagrtrem*balantrem-normaktrem)/(balanvaso-normaktrem)
    print(betatremp())
    def karareiksmetremp():
    	vertetrem = float(trpietus.value.replace(",", "."))
    	if zenklastremp()<0:
    		return zenklastremp()*math.log(float(alfatremp())*float(vertetrem)+float(betatremp()), pagrtrem)
    	else:
    		return zenklastremp()*math.log(float(alfatremp())*float(vertetrem)+float(betatremp()), pagrtrem)
    def karareiksmetrempriba():
    	if karareiksmetremp()>4:
    		return 4
    	elif karareiksmetremp()<-4:
    		return -4
    	else:
    		return karareiksmetremp()
    trempnew_data={'x':[0,karareiksmetrempriba()],'y':["tremp","tremp"]}
    if karareiksmetrempriba() > 0:
    	r26.glyph.line_color = "blue"
    else:
    	r26.glyph.line_color = "red"
    sourcetremp.data.update(trempnew_data)
    print(karareiksmetremp())
trpietus.on_change("value", tremp_update)

def tremv_update(attr, old, new):
    def zenklastremv():
    	def kryptistremv():
    		if normaktrem-balantrem < 0:
    			return 1
    		else:
    			return-1
    	vertetrem = float(trvakaras.value.replace(",", "."))
    	if (vertetrem-balantrem)*kryptistremv()>=0:
    		return 1
    	else:
    		return -1
    print(zenklastremv())
    def alfatremv():
    	if zenklastremv()>0:
    		return (1-pagrtrem)/(balantrem-normaatrem)
    	else:
    		return (1-pagrtrem)/(balantrem-normaktrem)
    print(alfatremv())
    def betatremv():
    	if zenklastremv()>0:
    		return (pagrtrem*balantrem-normaatrem)/(balantrem-normaatrem)
    	else:
    		return (pagrtrem*balantrem-normaktrem)/(balanvaso-normaktrem)
    print(betatremv())
    def karareiksmetremv():
    	vertetrem = float(trvakaras.value.replace(",", "."))
    	if zenklastremv()<0:
    		return zenklastremv()*math.log(float(alfatremv())*float(vertetrem)+float(betatremv()), pagrtrem)
    	else:
    		return zenklastremv()*math.log(float(alfatremv())*float(vertetrem)+float(betatremv()), pagrtrem)
    def karareiksmetremvriba():
    	if karareiksmetremv()>4:
    		return 4
    	elif karareiksmetremv()<-4:
    		return -4
    	else:
    		return karareiksmetremv()
    tremvnew_data={'x':[0,karareiksmetremvriba()],'y':["tremv","tremv"]}
    if karareiksmetremvriba() > 0:
    	r27.glyph.line_color = "blue"
    else:
    	r27.glyph.line_color = "red"
    sourcetremv.data.update(tremvnew_data)
    print(karareiksmetremv())
trvakaras.on_change("value", tremv_update)



normaknos= -1
normaanos = 1
balannos = float((normaanos+normaknos)/2)
pagrnos = 1.001
def nosr_update(attr, old, new):
    def zenklasnosr():
    	def kryptisnosr():
    		if normaknos-balannos < 0:
    			return 1
    		else:
    			return-1
    	vertenos = float(surytas.value.replace(",", "."))
    	if (vertenos-balannos)*kryptisnosr()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasnosr())
    def alfanosr():
    	if zenklasnosr()>0:
    		return (1-pagrnos)/(balannos-normaanos)
    	else:
    		return (1-pagrnos)/(balannos-normaknos)
    print(alfanosr())
    def betanosr():
    	if zenklasnosr()>0:
    		return (pagrnos*balannos-normaanos)/(balannos-normaanos)
    	else:
    		return (pagrnos*balannos-normaknos)/(balanvaso-normaknos)
    print(betanosr())
    def karareiksmenosr():
    	vertenos = float(surytas.value.replace(",", "."))
    	if zenklasnosr()<0:
    		return zenklasnosr()*math.log(float(alfanosr())*float(vertenos)+float(betanosr()), pagrnos)
    	else:
    		return zenklasnosr()*math.log(float(alfanosr())*float(vertenos)+float(betanosr()), pagrnos)
    def karareiksmenosrriba():
    	if karareiksmenosr()>4:
    		return 4
    	elif karareiksmenosr()<-4:
    		return -4
    	else:
    		return karareiksmenosr()
    nosrnew_data={'x':[0,karareiksmenosrriba()],'y':["nosr","nosr"]}
    if karareiksmenosrriba() > 0:
    	r28.glyph.line_color = "blue"
    else:
    	r28.glyph.line_color = "red"
    sourcenosr.data.update(nosrnew_data)
    print(karareiksmenosr())
surytas.on_change("value", nosr_update)

def nosp_update(attr, old, new):
    def zenklasnosp():
    	def kryptisnosp():
    		if normaknos-balannos < 0:
    			return 1
    		else:
    			return-1
    	vertenos = float(supietus.value.replace(",", "."))
    	if (vertenos-balannos)*kryptisnosp()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasnosp())
    def alfanosp():
    	if zenklasnosp()>0:
    		return (1-pagrnos)/(balannos-normaanos)
    	else:
    		return (1-pagrnos)/(balannos-normaknos)
    print(alfanosp())
    def betanosp():
    	if zenklasnosp()>0:
    		return (pagrnos*balannos-normaanos)/(balannos-normaanos)
    	else:
    		return (pagrnos*balannos-normaknos)/(balanvaso-normaknos)
    print(betanosp())
    def karareiksmenosp():
    	vertenos = float(supietus.value.replace(",", "."))
    	if zenklasnosp()<0:
    		return zenklasnosp()*math.log(float(alfanosp())*float(vertenos)+float(betanosp()), pagrnos)
    	else:
    		return zenklasnosp()*math.log(float(alfanosp())*float(vertenos)+float(betanosp()), pagrnos)
    def karareiksmenospriba():
    	if karareiksmenosp()>4:
    		return 4
    	elif karareiksmenosp()<-4:
    		return -4
    	else:
    		return karareiksmenosp()
    nospnew_data={'x':[0,karareiksmenospriba()],'y':["nosp","nosp"]}
    if karareiksmenospriba() > 0:
    	r29.glyph.line_color = "blue"
    else:
    	r29.glyph.line_color = "red"
    sourcenosp.data.update(nospnew_data)
    print(karareiksmenosp())
supietus.on_change("value", nosp_update)

def nosv_update(attr, old, new):
    def zenklasnosv():
    	def kryptisnosv():
    		if normaknos-balannos < 0:
    			return 1
    		else:
    			return-1
    	vertenos = float(suvakaras.value.replace(",", "."))
    	if (vertenos-balannos)*kryptisnosv()>=0:
    		return 1
    	else:
    		return -1
    print(zenklasnosv())
    def alfanosv():
    	if zenklasnosv()>0:
    		return (1-pagrnos)/(balannos-normaanos)
    	else:
    		return (1-pagrnos)/(balannos-normaknos)
    print(alfanosv())
    def betanosv():
    	if zenklasnosv()>0:
    		return (pagrnos*balannos-normaanos)/(balannos-normaanos)
    	else:
    		return (pagrnos*balannos-normaknos)/(balanvaso-normaknos)
    print(betanosv())
    def karareiksmenosv():
    	vertenos = float(suvakaras.value.replace(",", "."))
    	if zenklasnosv()<0:
    		return zenklasnosv()*math.log(float(alfanosv())*float(vertenos)+float(betanosv()), pagrnos)
    	else:
    		return zenklasnosv()*math.log(float(alfanosv())*float(vertenos)+float(betanosv()), pagrnos)
    def karareiksmenosvriba():
    	if karareiksmenosv()>4:
    		return 4
    	elif karareiksmenosv()<-4:
    		return -4
    	else:
    		return karareiksmenosv()
    nosvnew_data={'x':[0,karareiksmenosvriba()],'y':["nosv","nosv"]}
    if karareiksmenosvriba() > 0:
    	r30.glyph.line_color = "blue"
    else:
    	r30.glyph.line_color = "red"
    sourcenosv.data.update(nosvnew_data)
    print(karareiksmenosv())
suvakaras.on_change("value", nosv_update)



normaksarg= 1
normaasarg = -1
balansarg = float((normaasarg+normaksarg)/2)
pagrsarg = 1.001
def sargr_update(attr, old, new):
    def zenklassargr():
    	def kryptissargr():
    		if normaksarg-balansarg < 0:
    			return 1
    		else:
    			return-1
    	vertesarg = float(slrrytas.value.replace(",", "."))
    	if (vertesarg-balansarg)*kryptissargr()>=0:
    		return 1
    	else:
    		return -1
    print(zenklassargr())
    def alfasargr():
    	if zenklassargr()>0:
    		return (1-pagrsarg)/(balansarg-normaasarg)
    	else:
    		return (1-pagrsarg)/(balansarg-normaksarg)
    print(alfasargr())
    def betasargr():
    	if zenklassargr()>0:
    		return (pagrsarg*balansarg-normaasarg)/(balansarg-normaasarg)
    	else:
    		return (pagrsarg*balansarg-normaksarg)/(balanvaso-normaksarg)
    print(betasargr())
    def karareiksmesargr():
    	vertesarg = float(slrrytas.value.replace(",", "."))
    	if zenklassargr()<0:
    		return zenklassargr()*math.log(float(alfasargr())*float(vertesarg)+float(betasargr()), pagrsarg)
    	else:
    		return zenklassargr()*math.log(float(alfasargr())*float(vertesarg)+float(betasargr()), pagrsarg)
    def karareiksmesargrriba():
    	if karareiksmesargr()>4:
    		return 4
    	elif karareiksmesargr()<-4:
    		return -4
    	else:
    		return karareiksmesargr()
    sargrnew_data={'x':[0,karareiksmesargrriba()],'y':["sargr","sargr"]}
    if karareiksmesargrriba() > 0:
    	r31.glyph.line_color = "blue"
    else:
    	r31.glyph.line_color = "red"
    sourcesargr.data.update(sargrnew_data)
    print(karareiksmesargr())
slrrytas.on_change("value", sargr_update)

def sargp_update(attr, old, new):
    def zenklassargp():
    	def kryptissargp():
    		if normaksarg-balansarg < 0:
    			return 1
    		else:
    			return-1
    	vertesarg = float(slrpietus.value.replace(",", "."))
    	if (vertesarg-balansarg)*kryptissargp()>=0:
    		return 1
    	else:
    		return -1
    print(zenklassargp())
    def alfasargp():
    	if zenklassargp()>0:
    		return (1-pagrsarg)/(balansarg-normaasarg)
    	else:
    		return (1-pagrsarg)/(balansarg-normaksarg)
    print(alfasargp())
    def betasargp():
    	if zenklassargp()>0:
    		return (pagrsarg*balansarg-normaasarg)/(balansarg-normaasarg)
    	else:
    		return (pagrsarg*balansarg-normaksarg)/(balanvaso-normaksarg)
    print(betasargp())
    def karareiksmesargp():
    	vertesarg = float(slrpietus.value.replace(",", "."))
    	if zenklassargp()<0:
    		return zenklassargp()*math.log(float(alfasargp())*float(vertesarg)+float(betasargp()), pagrsarg)
    	else:
    		return zenklassargp()*math.log(float(alfasargp())*float(vertesarg)+float(betasargp()), pagrsarg)
    def karareiksmesargpriba():
    	if karareiksmesargp()>4:
    		return 4
    	elif karareiksmesargp()<-4:
    		return -4
    	else:
    		return karareiksmesargp()
    sargpnew_data={'x':[0,karareiksmesargpriba()],'y':["sargp","sargp"]}
    if karareiksmesargpriba() > 0:
    	r32.glyph.line_color = "blue"
    else:
    	r32.glyph.line_color = "red"
    sourcesargp.data.update(sargpnew_data)
    print(karareiksmesargp())
slrpietus.on_change("value", sargp_update)

def sargv_update(attr, old, new):
    def zenklassargv():
    	def kryptissargv():
    		if normaksarg-balansarg < 0:
    			return 1
    		else:
    			return-1
    	vertesarg = float(slrvakaras.value.replace(",", "."))
    	if (vertesarg-balansarg)*kryptissargv()>=0:
    		return 1
    	else:
    		return -1
    print(zenklassargv())
    def alfasargv():
    	if zenklassargv()>0:
    		return (1-pagrsarg)/(balansarg-normaasarg)
    	else:
    		return (1-pagrsarg)/(balansarg-normaksarg)
    print(alfasargv())
    def betasargv():
    	if zenklassargv()>0:
    		return (pagrsarg*balansarg-normaasarg)/(balansarg-normaasarg)
    	else:
    		return (pagrsarg*balansarg-normaksarg)/(balanvaso-normaksarg)
    print(betasargv())
    def karareiksmesargv():
    	vertesarg = float(slrvakaras.value.replace(",", "."))
    	if zenklassargv()<0:
    		return zenklassargv()*math.log(float(alfasargv())*float(vertesarg)+float(betasargv()), pagrsarg)
    	else:
    		return zenklassargv()*math.log(float(alfasargv())*float(vertesarg)+float(betasargv()), pagrsarg)
    def karareiksmesargvriba():
    	if karareiksmesargv()>4:
    		return 4
    	elif karareiksmesargv()<-4:
    		return -4
    	else:
    		return karareiksmesargv()
    sargvnew_data={'x':[0,karareiksmesargvriba()],'y':["sargv","sargv"]}
    if karareiksmesargvriba() > 0:
    	r33.glyph.line_color = "blue"
    else:
    	r33.glyph.line_color = "red"
    sourcesargv.data.update(sargvnew_data)
    print(karareiksmesargv())
slrvakaras.on_change("value", sargv_update)



normakskl= 1
normaaskl = -1
balanskl = float((normaaskl+normakskl)/2)
pagrskl = 1.001
def sklr_update(attr, old, new):
    def zenklassklr():
    	def kryptissklr():
    		if normakskl-balanskl < 0:
    			return 1
    		else:
    			return-1
    	verteskl = float(sekrytas.value.replace(",", "."))
    	if (verteskl-balanskl)*kryptissklr()>=0:
    		return 1
    	else:
    		return -1
    print(zenklassklr())
    def alfasklr():
    	if zenklassklr()>0:
    		return (1-pagrskl)/(balanskl-normaaskl)
    	else:
    		return (1-pagrskl)/(balanskl-normakskl)
    print(alfasklr())
    def betasklr():
    	if zenklassklr()>0:
    		return (pagrskl*balanskl-normaaskl)/(balanskl-normaaskl)
    	else:
    		return (pagrskl*balanskl-normakskl)/(balanvaso-normakskl)
    print(betasklr())
    def karareiksmesklr():
    	verteskl = float(sekrytas.value.replace(",", "."))
    	if zenklassklr()<0:
    		return zenklassklr()*math.log(float(alfasklr())*float(verteskl)+float(betasklr()), pagrskl)
    	else:
    		return zenklassklr()*math.log(float(alfasklr())*float(verteskl)+float(betasklr()), pagrskl)
    def karareiksmesklrriba():
    	if karareiksmesklr()>4:
    		return 4
    	elif karareiksmesklr()<-4:
    		return -4
    	else:
    		return karareiksmesklr()
    sklrnew_data={'x':[0,karareiksmesklrriba()],'y':["sklr","sklr"]}
    if karareiksmesklrriba() > 0:
    	r34.glyph.line_color = "blue"
    else:
    	r34.glyph.line_color = "red"
    sourcesklr.data.update(sklrnew_data)
    print(karareiksmesklr())
sekrytas.on_change("value", sklr_update)

def sklp_update(attr, old, new):
    def zenklassklp():
    	def kryptissklp():
    		if normakskl-balanskl < 0:
    			return 1
    		else:
    			return-1
    	verteskl = float(sekpietus.value.replace(",", "."))
    	if (verteskl-balanskl)*kryptissklp()>=0:
    		return 1
    	else:
    		return -1
    print(zenklassklp())
    def alfasklp():
    	if zenklassklp()>0:
    		return (1-pagrskl)/(balanskl-normaaskl)
    	else:
    		return (1-pagrskl)/(balanskl-normakskl)
    print(alfasklp())
    def betasklp():
    	if zenklassklp()>0:
    		return (pagrskl*balanskl-normaaskl)/(balanskl-normaaskl)
    	else:
    		return (pagrskl*balanskl-normakskl)/(balanvaso-normakskl)
    print(betasklp())
    def karareiksmesklp():
    	verteskl = float(sekpietus.value.replace(",", "."))
    	if zenklassklp()<0:
    		return zenklassklp()*math.log(float(alfasklp())*float(verteskl)+float(betasklp()), pagrskl)
    	else:
    		return zenklassklp()*math.log(float(alfasklp())*float(verteskl)+float(betasklp()), pagrskl)
    def karareiksmesklpriba():
    	if karareiksmesklp()>4:
    		return 4
    	elif karareiksmesklp()<-4:
    		return -4
    	else:
    		return karareiksmesklp()
    sklpnew_data={'x':[0,karareiksmesklpriba()],'y':["sklp","sklp"]}
    if karareiksmesklpriba() > 0:
    	r35.glyph.line_color = "blue"
    else:
    	r35.glyph.line_color = "red"
    sourcesklp.data.update(sklpnew_data)
    print(karareiksmesklp())
sekpietus.on_change("value", sklp_update)

def sklv_update(attr, old, new):
    def zenklassklv():
    	def kryptissklv():
    		if normakskl-balanskl < 0:
    			return 1
    		else:
    			return-1
    	verteskl = float(sekvakaras.value.replace(",", "."))
    	if (verteskl-balanskl)*kryptissklv()>=0:
    		return 1
    	else:
    		return -1
    print(zenklassklv())
    def alfasklv():
    	if zenklassklv()>0:
    		return (1-pagrskl)/(balanskl-normaaskl)
    	else:
    		return (1-pagrskl)/(balanskl-normakskl)
    print(alfasklv())
    def betasklv():
    	if zenklassklv()>0:
    		return (pagrskl*balanskl-normaaskl)/(balanskl-normaaskl)
    	else:
    		return (pagrskl*balanskl-normakskl)/(balanvaso-normakskl)
    print(betasklv())
    def karareiksmesklv():
    	verteskl = float(sekvakaras.value.replace(",", "."))
    	if zenklassklv()<0:
    		return zenklassklv()*math.log(float(alfasklv())*float(verteskl)+float(betasklv()), pagrskl)
    	else:
    		return zenklassklv()*math.log(float(alfasklv())*float(verteskl)+float(betasklv()), pagrskl)
    def karareiksmesklvriba():
    	if karareiksmesklv()>4:
    		return 4
    	elif karareiksmesklv()<-4:
    		return -4
    	else:
    		return karareiksmesklv()
    sklvnew_data={'x':[0,karareiksmesklvriba()],'y':["sklv","sklv"]}
    if karareiksmesklvriba() > 0:
    	r36.glyph.line_color = "blue"
    else:
    	r36.glyph.line_color = "red"
    sourcesklv.data.update(sklvnew_data)
    print(karareiksmesklvriba())
sekvakaras.on_change("value", sklv_update)




l = layout([protok(), invard , inpavard, lytis, inamz],
    [tikslus()], 
    [pav1()],
    [pav2()],
    [pav3()],
    [pav4()],
    [eiga()],
    [slapimo()],
    [aprsrugs(), srrytas, srpietus, srvakaras],
    [aprssvies(), ssrytas, sspietus, ssvakaras],
    [aprstank(), strytas, stpietus, stvakaras],
    [aprsputo(), sprytas, sppietus, spvakaras],
    [prikseil()],
    [seiliu()],
    [aprserugst(), serrytas, serpietus, servakaras],
    [aprseklamp(), sekrytas, sekpietus, sekvakaras],
    [tiriam()],
    [kraujot()],
    [aprpulsed(), psrytas, pspietus, psvakaras],
    [refleksu()],
    [aprkunotemp(), ktrytas, ktpietus, ktvakaras],
    [aprdermoref(), drrytas, drpietus, drvakaras],
    [aprvasomref(), vrrytas, vrpietus, vrvakaras],
    [aprvyzdyd(), vdrytas, vdpietus, vdvakaras],
    [aprtremoref(), trrytas, trpietus, trvakaras],
    [aprsneruzgu(), surytas, supietus, suvakaras],
    [tiriam1()],
    [aprsarglinref(), slrrytas, slrpietus, slrvakaras],
    [tiriam2()],
    [kvepparmat10()],
    [aprkvepdaz(), kdrytas, kdpietus, kdvakaras],
    [tiriam3()],
    [kraujparmat()],
    [aprpulgul(), pgrytas, pgpietus, pgvakaras],
    [aprsiskraujgul(), skgrytas, skgpietus, skgvakaras],
    [aprdiakraujgul(), dkgrytas, dkgpietus, dkgvakaras],
    [ortatest()],
    [aprpulsatsi15()],
    [atsist(), parytas, papietus, pavakaras],
    [po15(), pa15rytas, pa15pietus, pa15vakaras],
    [aprkraujpulsatsi45()],
    [siskraujatsi(), skarytas, skapietus, skavakaras],
    [diaskraujatsi(), dkarytas, dkapietus, dkavakaras],
    [pulsatsi45(), pa45rytas, pa45pietus, pa45vakaras],
    [tiriam4()],
    [kvepparmat14()],
    [aprkvepsu(), ksirytas, ksipietus, ksivakaras],
    )
l2= column(p, p1, p2, p3, p4, p5, p6)
l1 = row(l, l2)
# add the layout to curdoc
curdoc().add_root(l1)