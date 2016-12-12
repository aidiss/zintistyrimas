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
            text-align: justify;
            text-justify: inter-word;
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


 #outer-circle {
   background: white;
   border-radius: 50%;
   border: 1px solid;
   height: 40px;
   width: 40px;
   position: relative;
   /* 
    Child elements with absolute positioning will be 
    positioned relative to this div 
   */
 }
 #inner-circle {
   position: absolute;
   background: black;
   border-radius: 50%;
   height: 25px;
   width: 25px;
   /*
    Put top edge and left edge in the center
   */
   top: 19%;
   left: 19%;
   margin: 50x 50px 50px 50x;
   /* 
    Offset the position correctly with
    minus half of the width and minus half of the height 
   */
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
  transition: opacity 1ms;
  visibility: hidden;
  opacity: 1;
  overflow-y:scroll;
  z-index: 10;
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
  transition: all 5s ease-in-out;
}

.popup h2 {
  margin-top: 0;
  color: #333;
  font-family: Verdana, Arial, sans-serif;
}
.popup .close {
  position: absolute;
  top: 20px;
  right: 30px;
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
  max-height: 30%;
  overflow: auto;
  text-align: justify;
  text-justify: inter-word;
}

@media screen and (max-width: 1000px){
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

aprugis = Div(text = "<br>Ūgis (Stovint išsitiesus, centimetrais)" , width=250)
inugis = TextInput(name = "ugis", value="", width=220, height=None)

aprkrut = Div(text = "<br>Krūtinės ląstos apimtis (Pažąstų aukštyje, nuleidus rankas, centimetrais)", width=250)
inkrut = TextInput(name = "krut", value="", width=220, height=None)

aprjuos = Div(text = "<br>Juosmens apimtis (Per siauriausią vietą, centimetrais)", width=250)
injuos = TextInput(name = "juos", value="", width=220, height=None)

aprklub = Div(text = "<br>Klubų apimtis (Per plačiausią vietą, maždaug genitalijų aukštyje, centimetrais)", width=250)
inklub= TextInput(name = "klub", value="", width=220, height=None)

aprmase = Div(text = "<br>Masė (Ryte, išsituštinus, pasišlapinus, nusirengus, kg)", width=250)
inmase= TextInput(name = "mase", value="", width=220, height=None)


factors = ["a", "b", "c", "d", "e", "f", "g", "h"]

source = ColumnDataSource(data=dict(x=[], y=[]))
source1 = ColumnDataSource(data=dict(x=[], y=[]))
source2 = ColumnDataSource(data=dict(x=[], y=[]))
sourcet = ColumnDataSource(data=dict(x=[], y=[]))

p = figure(x_axis_label='kh', y_axis_label='ph', x_range = [-60, 60], y_range = factors, width=350,
            plot_height=150, toolbar_location = None)
p.title.text = "<-Katabolizmas|Anabolizmas->"
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
def protok():
    return Div(text="""<br><b>ORGANIZMO BŪKLĖS TYRIMO PROTOKOLAS</b>""", width=330, height=None)

invard = TextInput(name = "vard", value="", title = "Vardas", width = 130)
inpavard = TextInput(name = "pavard", value="", title = "Pavardė", width = 160)
lytis = Select(title="Lytis:", value="", options=["Vyras", "Moteris"], width = 110)
inamz = TextInput(name = "amz", value="", title = "Amžius", width = 80) 
# indata = TextInput(value="", title = "Data")

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




def pav1():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup1">3 - 2 SAVAITĖS IKI TYRIMŲ DIENOS</a>
</div>

<div id="popup1" class="overlay">
    <div class="popup">
        <h2>3-2 SAVAITĖS IKI TYRIMŲ DIENOS</h2>
        <a class="close" href="#">&times;</a>
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
    <div class="popup">
        <h2>MAŽIAUSIAI 2 DIENOS IKI TYRIMŲ DIENOS</h2>
        <a class="close" href="#">&times;</a>
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
    <div class="popup">
        <h2>TYRIMŲ DIENOS IŠVAKARĖSE</h2>
        <a class="close" href="#">&times;</a>
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
    <div class="popup">
        <h2>TYRIMŲ DIENĄ</h2>
        <a class="close" href="#">&times;</a>
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
    <div class="popup">
        <h2>Rūgštingumas</h2>
        <a class="close" href="#">&times;</a>
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
    <div class="popup">
        <h2>Šviesumas</h2>
        <a class="close" href="#">&times;</a>
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
    <div class="popup">
        <h2>Tankis</h2>
        <a class="close" href="#">&times;</a>
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
    <div class="popup">
        <h2>Putojimas</h2>
        <a class="close" href="#">&times;</a>
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
      <td><b>putos prasiskiria per 1 min.>/b></td>
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
    <div class="popup">
        <h2>Rūgštingumas</h2>
        <a class="close" href="#">&times;</a>
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
        <a class="close" href="#">&times;</a>
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
    <a class="button" href="#popup11"><br>Pulsas sėdint</a>
</div>

<div id="popup11" class="overlay">
    <div class="popup">
        <h2>Pulsas sėdint</h2>
        <a class="close" href="#">&times;</a>
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

def kunotemp():
    return Div(text="""
<div class="box">
    <a class="button" href="#popup12"><br>Kūno temperatūra</a>
</div>

<div id="popup12" class="overlay">
    <div class="popup">
        <h2>Kūno temperatūra</h2>
        <a class="close" href="#">&times;</a>
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
    <div class="popup">
        <h2>Dermografinis refleksas</h2>
        <a class="close" href="#">&times;</a>
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
    <div class="popup">
        <h2>Vasomotorinis refleksas</h2>
        <a class="close" href="#">&times;</a>
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

# 
vrrytas = TextInput(name = "rytas10", value="", title = "Rytas", width = 60)
vrpietus = TextInput(name = "pietus10", value="", title = "Pietūs", width = 60)
vrvakaras = TextInput(name = "vakaras10", value="", title = "Vakaras", width = 60)


# tr>
#       <td>-4</td>
#       <td><div id="outer-circle">
#             <div id="inner-circle">
#               </div>
#                     </div></td>
#     </tr>
    



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


l = layout(children=[[protok(), invard , inpavard, lytis, inamz],
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
    [aprdermoref(), drrytas, drpietus, drvakaras],
    [aprvasomref(), vrrytas, vrpietus, vrvakaras],



    # [input2],
    ])

# add the layout to curdoc
curdoc().add_root(l)