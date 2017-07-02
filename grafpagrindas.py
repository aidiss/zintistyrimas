from bokeh.plotting import figure, ColumnDataSource, show
from bokeh.layouts import column, row, layout
from bokeh.models import Span, BoxAnnotation, FixedTicker, FuncTickFormatter
from bokeh.models.ranges import FactorRange
from bokeh.models.widgets import TextInput, Div, Select
import logging
import math


# grafikų pavadinimų sąrašas
pavadin =   [
            "<-Simpatinis|Parasimpatinis->",
            "<-Katogeniniss|Gliukogeninis->",
            "<-Disaerobinis|Anaerobinis->",
            "<-Rūgščių trūkumas|Rūgščių perteklius->",
            "<-Elektrolitų trūkumas|Elektrolitų perteklius->",
            "<-Kalio trūkumas|Kalio perteklius->",
            "<-Anglies dvideginio trūkumas|Anglies dvideginio perteklius->"
            ]
# generuojamų grafikų sąrašas
plist = ["p1", "p2", "p3", "p4", "p5", "p6", "p7"]

# tuščias list į kurį pridedami sugeneruoti grafikai atvaizdavimui
# naudojant column(grafikai.make_graf())
L = []


# categorical tipo duomenys, kad būtų galima atvaziduoti grafike, atitinaktys kiekvieno tyrimo ryto, pietų ir vakaro (kol kas tik 2)
factorssp = [
			"sklv", "sargv", "nosv", "tremv", "vyzdv", "vasov", "dermv", "tempv", "kriv", "ppv", "sdv", "ps1v", "bla1",
			"sklp", "sargp", "nosp", "tremp", "vyzdp", "vasop", "dermp", "tempp", "krip", "ppp", "sdp", "ps1p", "bla2",
			"sklr", "sargr", "nosr", "tremr", "vyzdr", "vasor", "dermr", "tempr", "krir", "ppr", "sdr", "ps1r", "bla3"
			]

factorskg = [
			"uputv", "usvv", "d2p4v", "kphiv", "p4v", "tankv", "kdv", "sphkv", "bla1",
			"uputp", "usvp", "d2p4p", "kphip", "p4p", "tankp", "kdp", "sphkp", "bla2",
			"uputr", "usvr", "d2p4r", "kphir", "p4r", "tankr", "kdr", "sphkr", "bla3"
			]

# skaičiuojam atitinakamų categorical skaičių, kad
# 1) automatiškai grafike nusistatytų ribos tarp ryto, pietų ir vakaro
# 2) tekstas atskiriantis juos
# 3) y categorical axis range'as
countsp = len(factorssp)
countkg = len(factorskg)

invard = TextInput(name="vard", value="", title="Vardas", width=130)
inpavard = TextInput(name="pavard", value="", title="Pavardė", width=160)
lytis = Select(title="Lytis:", value="", options=["Vyras", "Moteris"], width=130)
inamz = TextInput(name="amz", value="", title="Amžius", width=80)

srrytas = TextInput(name="rytas1", value="", title="Rytas", width=60)
srpietus = TextInput(name="pietus1", value="", title="Pietūs", width=60)
srvakaras = TextInput(name="vakaras1", value="", title="Vakaras", width=60)

ssrytas = TextInput(name="rytas2", value="", title="Rytas", width=60)
sspietus = TextInput(name="pietus2", value="", title="Pietūs", width=60)
ssvakaras = TextInput(name="vakaras2", value="", title="Vakaras", width=60)

strytas = TextInput(name="rytas3", value="", title="Rytas", width=60)
stpietus = TextInput(name="pietus3", value="", title="Pietūs", width=60)
stvakaras = TextInput(name="vakaras3", value="", title="Vakaras", width=60)

sprytas = TextInput(name="rytas4", value="", title="Rytas", width=60)
sppietus = TextInput(name="pietus4", value="", title="Pietūs", width=60)
spvakaras = TextInput(name="vakaras4", value="", title="Vakaras", width=60)

serrytas = TextInput(name="rytas5", value="", title="Rytas", width=60)
serpietus = TextInput(name="pietus5", value="", title="Pietūs", width=60)
servakaras = TextInput(name="vakaras5", value="", title="Vakaras", width=60)

sekrytas = TextInput(name="rytas6", value="", title="Rytas", width=60)
sekpietus = TextInput(name="pietus6", value="", title="Pietūs", width=60)
sekvakaras = TextInput(name="vakaras6", value="", title="Vakaras", width=60)

psrytas = TextInput(name="rytas7", value="", title="Rytas", width=60)
pspietus = TextInput(name="pietus7", value="", title="Pietūs", width=60)
psvakaras = TextInput(name="vakaras7", value="", title="Vakaras", width=60)

ktrytas = TextInput(name="rytas8", value="", title="Rytas", width=60)
ktpietus = TextInput(name="pietus8", value="", title="Pietūs", width=60)
ktvakaras = TextInput(name="vakaras8", value="", title="Vakaras", width=60)

drrytas = TextInput(name="rytas9", value="", title="Rytas", width=60)
drpietus = TextInput(name="pietus9", value="", title="Pietūs", width=60)
drvakaras = TextInput(name="vakaras9", value="", title="Vakaras", width=60)

vrrytas = TextInput(name="rytas10", value="", title="Rytas", width=60)
vrpietus = TextInput(name="pietus10", value="", title="Pietūs", width=60)
vrvakaras = TextInput(name="vakaras10", value="", title="Vakaras", width=60)

vdrytas = TextInput(name="rytas11", value="", title="Rytas", width=60)
vdpietus = TextInput(name="pietus11", value="", title="Pietūs", width=60)
vdvakaras = TextInput(name="vakaras11", value="", title="Vakaras", width=60)

trrytas = TextInput(name="rytas12", value="", title="Rytas", width=60)
trpietus = TextInput(name="pietus12", value="", title="Pietūs", width=60)
trvakaras = TextInput(name="vakaras12", value="", title="Vakaras", width=60)

surytas = TextInput(name="rytas13", value="", title="Rytas", width=60)
supietus = TextInput(name="pietus13", value="", title="Pietūs", width=60)
suvakaras = TextInput(name="vakaras13", value="", title="Vakaras", width=60)

slrrytas = TextInput(name="rytas14", value="", title="Rytas", width=60)
slrpietus = TextInput(name="pietus14", value="", title="Pietūs", width=60)
slrvakaras = TextInput(name="vakaras14", value="", title="Vakaras", width=60)

kdrytas = TextInput(name="rytas15", value="", title="Rytas", width=60)
kdpietus = TextInput(name="pietus15", value="", title="Pietūs", width=60)
kdvakaras = TextInput(name="vakaras15", value="", title="Vakaras", width=60)

pgrytas = TextInput(name="rytas16", value="", title="Rytas", width=60)
pgpietus = TextInput(name="pietus16", value="", title="Pietūs", width=60)
pgvakaras = TextInput(name="vakaras16", value="", title="Vakaras", width=60)

skgrytas = TextInput(name="rytas17", value="", title="Rytas", width=60)
skgpietus = TextInput(name="pietus17", value="", title="Pietūs", width=60)
skgvakaras = TextInput(name="vakaras17", value="", title="Vakaras", width=60)

dkgrytas = TextInput(name="rytas18", value="", title="Rytas", width=60)
dkgpietus = TextInput(name="pietus18", value="", title="Pietūs", width=60)
dkgvakaras = TextInput(name="vakaras18", value="", title="Vakaras", width=60)

parytas = TextInput(name="rytas19", value="", title="Rytas", width=60)
papietus = TextInput(name="pietus19", value="", title="Pietūs", width=60)
pavakaras = TextInput(name="vakaras19", value="", title="Vakaras", width=60)

pa15rytas = TextInput(name="rytas20", value="", title="Rytas", width=60)
pa15pietus = TextInput(name="pietus20", value="", title="Pietūs", width=60)
pa15vakaras = TextInput(name="vakaras20", value="", title="Vakaras", width=60)

skarytas = TextInput(name="rytas21", value="", title="Rytas", width=60)
skapietus = TextInput(name="pietus21", value="", title="Pietūs", width=60)
skavakaras = TextInput(name="vakaras21", value="", title="Vakaras", width=60)

dkarytas = TextInput(name="rytas22", value="", title="Rytas", width=60)
dkapietus = TextInput(name="pietus22", value="", title="Pietūs", width=60)
dkavakaras = TextInput(name="vakaras22", value="", title="Vakaras", width=60)

pa45rytas = TextInput(name="rytas23", value="", title="Rytas", width=60)
pa45pietus = TextInput(name="pietus23", value="", title="Pietūs", width=60)
pa45vakaras = TextInput(name="vakaras23", value="", title="Vakaras", width=60)

ksirytas = TextInput(name="rytas24", value="", title="Rytas", width=60)
ksipietus = TextInput(name="pietus24", value="", title="Pietūs", width=60)
ksivakaras = TextInput(name="vakaras24", value="", title="Vakaras", width=60)


# ši dalims tam, kad suvedus duomenis į atitinakmą TextInput, grafike atsispindėtų
# simpatinis/parasimpatinis
sourceps1r = ColumnDataSource(data=dict(x=[], y=[]))
sourceps1p = ColumnDataSource(data=dict(x=[], y=[]))
sourceps1v = ColumnDataSource(data=dict(x=[], y=[]))

sourcesdr = ColumnDataSource(data=dict(x=[], y=[]))
sourcesdp = ColumnDataSource(data=dict(x=[], y=[]))
sourcesdv = ColumnDataSource(data=dict(x=[], y=[]))

sourceppr = ColumnDataSource(data=dict(x=[], y=[]))
sourceppp = ColumnDataSource(data=dict(x=[], y=[]))
sourceppv = ColumnDataSource(data=dict(x=[], y=[]))

sourcekrir = ColumnDataSource(data=dict(x=[], y=[]))
sourcekrip = ColumnDataSource(data=dict(x=[], y=[]))
sourcekriv = ColumnDataSource(data=dict(x=[], y=[]))

sourcetempr = ColumnDataSource(data=dict(x=[], y=[]))
sourcetempp = ColumnDataSource(data=dict(x=[], y=[]))
sourcetempv = ColumnDataSource(data=dict(x=[], y=[]))

sourcedermr = ColumnDataSource(data=dict(x=[], y=[]))
sourcedermp = ColumnDataSource(data=dict(x=[], y=[]))
sourcedermv = ColumnDataSource(data=dict(x=[], y=[]))

sourcevasor = ColumnDataSource(data=dict(x=[], y=[]))
sourcevasop = ColumnDataSource(data=dict(x=[], y=[]))
sourcevasov = ColumnDataSource(data=dict(x=[], y=[]))

sourcevyzdr = ColumnDataSource(data=dict(x=[], y=[]))
sourcevyzdp = ColumnDataSource(data=dict(x=[], y=[]))
sourcevyzdv = ColumnDataSource(data=dict(x=[], y=[]))

sourcetremr = ColumnDataSource(data=dict(x=[], y=[]))
sourcetremp = ColumnDataSource(data=dict(x=[], y=[]))
sourcetremv = ColumnDataSource(data=dict(x=[], y=[]))

sourcenosr = ColumnDataSource(data=dict(x=[], y=[]))
sourcenosp = ColumnDataSource(data=dict(x=[], y=[]))
sourcenosv = ColumnDataSource(data=dict(x=[], y=[]))

sourcesargr = ColumnDataSource(data=dict(x=[], y=[]))
sourcesargp = ColumnDataSource(data=dict(x=[], y=[]))
sourcesargv = ColumnDataSource(data=dict(x=[], y=[]))

sourcesklr = ColumnDataSource(data=dict(x=[], y=[]))
sourcesklp = ColumnDataSource(data=dict(x=[], y=[]))
sourcesklv = ColumnDataSource(data=dict(x=[], y=[]))

# kiekvineo grafiko kiekvieno TextInput duomenų skaičiavimo formulė, kuri nėra vienoda visiems ir kuri gali įtraukti ir kitų TextInput duomenis t.y. kiekvienam categorical yra nubrėžiama linija pagal skaičavimo formulę.
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
        if (verteps1r-balanps1)*kryptisps1r() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasps1r())

    def alfaps1r():
        if zenklasps1r() > 0:
            return (1-pagrps1)/(balanps1-normaaps1)
        else:
            return (1-pagrps1)/(balanps1-normakps1)
    logging.info(alfaps1r())

    def betaps1r():
        if zenklasps1r() > 0:
            return (pagrps1*balanps1-normaaps1)/(balanps1-normaaps1)
        else:
            return (pagrps1*balanps1-normakps1)/(balanps1-normakps1)
    logging.info(betaps1r())

    def karareiksmeps1r():
        psr = float(psrytas.value.replace(",", "."))
        pgr = float(pgrytas.value.replace(",", "."))
        verteps1 = psr-pgr
        if zenklasps1r() < 0:
            return zenklasps1r()*math.log(alfaps1r()*verteps1+betaps1r(), pagrps1)
        else:
            return zenklasps1r()*math.log(alfaps1r()*verteps1+betaps1r(), pagrps1)

    def karareiksmeps1rriba():
        if karareiksmeps1r() > 4:
            return 4
        elif karareiksmeps1r() < -4:
            return -4
        else:
            return karareiksmeps1r()
    ps1rnew_data = {'x': [0, karareiksmeps1rriba()], 'y': ["ps1r", "ps1r"]}
    if karareiksmeps1rriba() > 0:
        sp1.glyph.line_color = "blue"
    else:
        sp1.glyph.line_color = "red"
    sourceps1r.data.update(ps1rnew_data)
    logging.info(karareiksmeps1r())
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
        if (verteps1p-balanps1)*kryptisps1p() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasps1p())

    def alfaps1p():
        if zenklasps1p() > 0:
            return (1-pagrps1)/(balanps1-normaaps1)
        else:
            return (1-pagrps1)/(balanps1-normakps1)
    logging.info(alfaps1p())

    def betaps1p():
        if zenklasps1p() > 0:
            return (pagrps1*balanps1-normaaps1)/(balanps1-normaaps1)
        else:
            return (pagrps1*balanps1-normakps1)/(balanps1-normakps1)
    logging.info(betaps1p())

    def karareiksmeps1p():
        psp = float(pspietus.value.replace(",", "."))
        pgp = float(pgpietus.value.replace(",", "."))
        verteps1 = psp-pgp
        if zenklasps1p() < 0:
            return zenklasps1p()*math.log(alfaps1p()*verteps1+betaps1p(), pagrps1)
        else:
            return zenklasps1p()*math.log(alfaps1p()*verteps1+betaps1p(), pagrps1)

    def karareiksmeps1priba():
        if karareiksmeps1p() > 4:
            return 4
        elif karareiksmeps1p() < -4:
            return -4
        else:
            return karareiksmeps1p()
    ps1pnew_data = {'x': [0, karareiksmeps1priba()], 'y': ["ps1p", "ps1p"]}
    sourceps1p.data.update(ps1pnew_data)
    if karareiksmeps1priba() > 0:
        sp2.glyph.line_color = "blue"
    else:
        sp2.glyph.line_color = "red"
    logging.info(karareiksmeps1p())
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
        if (verteps1v-balanps1)*kryptisps1v() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasps1v())

    def alfaps1v():
        if zenklasps1v() > 0:
            return (1-pagrps1)/(balanps1-normaaps1)
        else:
            return (1-pagrps1)/(balanps1-normakps1)
    logging.info(alfaps1v())

    def betaps1v():
        if zenklasps1v() > 0:
            return (pagrps1*balanps1-normaaps1)/(balanps1-normaaps1)
        else:
            return (pagrps1*balanps1-normakps1)/(balanps1-normakps1)
    logging.info(betaps1v())

    def karareiksmeps1v():
        psv = float(psvakaras.value.replace(",", "."))
        pgv = float(pgvakaras.value.replace(",", "."))
        verteps1 = psv-pgv
        if zenklasps1v() < 0:
            return zenklasps1v()*math.log(alfaps1v()*verteps1+betaps1v(), pagrps1)
        else:
            return zenklasps1v()*math.log(alfaps1v()*verteps1+betaps1v(), pagrps1)

    def karareiksmeps1vriba():
        if karareiksmeps1v() > 4:
            return 4
        elif karareiksmeps1v() < -4:
            return -4
        else:
            return karareiksmeps1v()
    ps1vnew_data = {'x': [0, karareiksmeps1vriba()], 'y': ["ps1v", "ps1v"]}
    if karareiksmeps1vriba() > 0:
        sp3.glyph.line_color = "blue"
    else:
        sp3.glyph.line_color = "red"
    sourceps1v.data.update(ps1vnew_data)
    logging.info(karareiksmeps1v())
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
        if (vertesd-balansd)*kryptissdr() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklassdr())

    def alfasdr():
        if zenklassdr() > 0:
            return (1-pagrsd)/(balansd-normaasd)
        else:
            return (1-pagrsd)/(balansd-normaksd)
    logging.info(alfasdr())

    def betasdr():
        if zenklassdr() > 0:
            return (pagrsd*balansd-normaasd)/(balansd-normaasd)
        else:
            return (pagrsd*balansd-normaksd)/(balansd-normaksd)
    logging.info(betasdr())

    def karareiksmesdr():
        skar = float(skarytas.value.replace(",", "."))
        skgr = float(skgrytas.value.replace(",", "."))
        dkar = float(dkarytas.value.replace(",", "."))
        dkgr = float(dkgrytas.value.replace(",", "."))
        vertesd = skar-skgr+dkar-dkgr
        if zenklassdr() < 0:
            return zenklassdr()*math.log(alfasdr()*vertesd+betasdr(), pagrsd)
        else:
            return zenklassdr()*math.log(alfasdr()*vertesd+betasdr(), pagrsd)

    def karareiksmesdrriba():
        if karareiksmesdr() > 4:
            return 4
        elif karareiksmesdr() < -4:
            return -4
        else:
            return karareiksmesdr()
    sdrnew_data = {'x': [0, karareiksmesdrriba()], 'y': ["sdr", "sdr"]}
    if karareiksmesdrriba() > 0:
        sp4.glyph.line_color = "blue"
    else:
        sp4.glyph.line_color = "red"
    sourcesdr.data.update(sdrnew_data)
    logging.info(karareiksmesdr())
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
        if (vertesd-balansd)*kryptissdp() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklassdp())

    def alfasdp():
        if zenklassdp() > 0:
            return (1-pagrsd)/(balansd-normaasd)
        else:
            return (1-pagrsd)/(balansd-normaksd)
    logging.info(alfasdp())

    def betasdp():
        if zenklassdp() > 0:
            return (pagrsd*balansd-normaasd)/(balansd-normaasd)
        else:
            return (pagrsd*balansd-normaksd)/(balansd-normaksd)
    logging.info(betasdp())

    def karareiksmesdp():
        skap = float(skapietus.value.replace(",", "."))
        skgp = float(skgpietus.value.replace(",", "."))
        dkap = float(dkapietus.value.replace(",", "."))
        dkgp = float(dkgpietus.value.replace(",", "."))
        vertesd = (skap-skgp)+(dkap-dkgp)
        if zenklassdp() < 0:
            return zenklassdp()*math.log(alfasdp()*vertesd+betasdp(), pagrsd)
        else:
            return zenklassdp()*math.log(alfasdp()*vertesd+betasdp(), pagrsd)

    def karareiksmesdpriba():
        if karareiksmesdp() > 4:
            return 4
        elif karareiksmesdp() < -4:
            return -4
        else:
            return karareiksmesdp()
    sdpnew_data = {'x': [0, karareiksmesdpriba()], 'y': ["sdp", "sdp"]}
    if karareiksmesdpriba() > 0:
        sp5.glyph.line_color = "blue"
    else:
        sp5.glyph.line_color = "red"
    sourcesdp.data.update(sdpnew_data)
    logging.info(karareiksmesdp())
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
        if (vertesd-balansd)*kryptissdv() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklassdv())

    def alfasdv():
        if zenklassdv() > 0:
            return (1-pagrsd)/(balansd-normaasd)
        else:
            return (1-pagrsd)/(balansd-normaksd)
    logging.info(alfasdv())

    def betasdv():
        if zenklassdv() > 0:
            return (pagrsd*balansd-normaasd)/(balansd-normaasd)
        else:
            return (pagrsd*balansd-normaksd)/(balansd-normaksd)
    logging.info(betasdv())

    def karareiksmesdv():
        skav = float(skavakaras.value.replace(",", "."))
        skgv = float(skgvakaras.value.replace(",", "."))
        dkav = float(dkavakaras.value.replace(",", "."))
        dkgv = float(dkgvakaras.value.replace(",", "."))
        vertesd = (skav-skgv)+(dkav-dkgv)
        if zenklassdv() < 0:
            return zenklassdv()*math.log(alfasdv()*vertesd+betasdv(), pagrsd)
        else:
            return zenklassdv()*math.log(alfasdv()*vertesd+betasdv(), pagrsd)

    def karareiksmesdvriba():
        if karareiksmesdv() > 4:
            return 4
        elif karareiksmesdv() < -4:
            return -4
        else:
            return karareiksmesdv()
    sdvnew_data = {'x': [0, karareiksmesdvriba()], 'y': ["sdv", "sdv"]}
    if karareiksmesdvriba() > 0:
        sp6.glyph.line_color = "blue"
    else:
        sp6.glyph.line_color = "red"
    sourcesdv.data.update(sdvnew_data)
    logging.info(karareiksmesdv())
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
        pp2 = max(pgr, par, pa15r, pa45r)-pa45r
        vertepp = pp1+pp2
        if (vertepp-balanpp)*kryptisppr() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasppr())

    def alfappr():
        if zenklasppr() > 0:
            return (1-pagrpp)/(balanpp-normaapp)
        else:
            return (1-pagrpp)/(balanpp-normakpp)
    logging.info(alfappr())

    def betappr():
        if zenklasppr() > 0:
            return (pagrpp*balanpp-normaapp)/(balanpp-normaapp)
        else:
            return (pagrpp*balanpp-normakpp)/(balanpp-normakpp)
    logging.info(betappr())

    def karareiksmeppr():
        pgr = float(pgrytas.value.replace(",", "."))
        par = float(parytas.value.replace(",", "."))
        pa15r = float(pa15rytas.value.replace(",", "."))
        pa45r = float(pa45rytas.value.replace(",", "."))
        pp1 = max(pgr, par, pa15r, pa45r)-pgr
        pp2 = max(pgr, par, pa15r, pa45r)-pa45r
        vertepp = pp1+pp2
        if zenklasppr() < 0:
            return zenklasppr()*math.log(alfappr()*vertepp+betappr(), pagrpp)
        else:
            return zenklasppr()*math.log(alfappr()*vertepp+betappr(), pagrpp)

    def karareiksmepprriba():
        if karareiksmeppr() > 4:
            return 4
        elif karareiksmeppr() < -4:
            return -4
        else:
            return karareiksmeppr()
    pprnew_data = {'x': [0, karareiksmepprriba()], 'y': ["ppr", "ppr"]}
    if karareiksmepprriba() > 0:
        sp7.glyph.line_color = "blue"
    else:
        sp7.glyph.line_color = "red"
    sourceppr.data.update(pprnew_data)
    logging.info(karareiksmeppr())
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
        pp2 = max(pgp, pap, pa15p, pa45p)-pa45p
        vertepp = pp1+pp2
        if (vertepp-balanpp)*kryptisppp() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasppp())

    def alfappp():
        if zenklasppp() > 0:
            return (1-pagrpp)/(balanpp-normaapp)
        else:
            return (1-pagrpp)/(balanpp-normakpp)
    logging.info(alfappp())

    def betappp():
        if zenklasppp() > 0:
            return (pagrpp*balanpp-normaapp)/(balanpp-normaapp)
        else:
            return (pagrpp*balanpp-normakpp)/(balanpp-normakpp)
    logging.info(betappp())

    def karareiksmeppp():
        pgp = float(pgpietus.value.replace(",", "."))
        pap = float(papietus.value.replace(",", "."))
        pa15p = float(pa15pietus.value.replace(",", "."))
        pa45p = float(pa45pietus.value.replace(",", "."))
        pp1 = max(pgp, pap, pa15p, pa45p)-pgp
        pp2 = max(pgp, pap, pa15p, pa45p)-pa45p
        vertepp = pp1+pp2
        if zenklasppp() < 0:
            return zenklasppp()*math.log(alfappp()*vertepp+betappp(), pagrpp)
        else:
            return zenklasppp()*math.log(alfappp()*vertepp+betappp(), pagrpp)

    def karareiksmepppriba():
        if karareiksmeppp() > 4:
            return 4
        elif karareiksmeppp() < -4:
            return -4
        else:
            return karareiksmeppp()
    pppnew_data = {'x': [0, karareiksmepppriba()], 'y': ["ppp", "ppp"]}
    if karareiksmepppriba() > 0:
        sp8.glyph.line_color = "blue"
    else:
        sp8.glyph.line_color = "red"
    sourceppp.data.update(pppnew_data)
    logging.info(karareiksmeppp())
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
        pp2 = max(pgv, pav, pa15v, pa45v)-pa45v
        vertepp = pp1+pp2
        if (vertepp-balanpp)*kryptisppv() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasppv())

    def alfappv():
        if zenklasppv() > 0:
            return (1-pagrpp)/(balanpp-normaapp)
        else:
            return (1-pagrpp)/(balanpp-normakpp)
    logging.info(alfappv())

    def betappv():
        if zenklasppv() > 0:
            return (pagrpp*balanpp-normaapp)/(balanpp-normaapp)
        else:
            return (pagrpp*balanpp-normakpp)/(balanpp-normakpp)
    logging.info(betappv())

    def karareiksmeppv():
        pgv = float(pgvakaras.value.replace(",", "."))
        pav = float(pavakaras.value.replace(",", "."))
        pa15v = float(pa15vakaras.value.replace(",", "."))
        pa45v = float(pa45vakaras.value.replace(",", "."))
        pp1 = max(pgv, pav, pa15v, pa45v)-pgv
        pp2 = max(pgv, pav, pa15v, pa45v)-pa45v
        vertepp = pp1+pp2
        if zenklasppv() < 0:
            return zenklasppv()*math.log(alfappv()*vertepp+betappv(), pagrpp)
        else:
            return zenklasppv()*math.log(alfappv()*vertepp+betappv(), pagrpp)

    def karareiksmeppvriba():
        if karareiksmeppv() > 4:
            return 4
        elif karareiksmeppv() < -4:
            return -4
        else:
            return karareiksmeppv()
    ppvnew_data = {'x': [0, karareiksmeppvriba()], 'y': ["ppv", "ppv"]}
    if karareiksmeppvriba() > 0:
        sp9.glyph.line_color = "blue"
    else:
        sp9.glyph.line_color = "red"
    sourceppv.data.update(ppvnew_data)
    logging.info(karareiksmeppv())
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
        if (vertekri-balankri)*kryptiskrir() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklaskrir())

    def alfakrir():
        if zenklaskrir() > 0:
            return (1-pagrkri)/(balankri-normaakri)
        else:
            return (1-pagrkri)/(balankri-normakkri)
    logging.info(alfakrir())

    def betakrir():
        if zenklaskrir() > 0:
            return (pagrkri*balankri-normaakri)/(balankri-normaakri)
        else:
            return (pagrkri*balankri-normakkri)/(balankri-normakkri)
    logging.info(betakrir())

    def karareiksmekrir():
        psr = float(psrytas.value.replace(",", "."))
        kdr = float(kdrytas.value.replace(",", "."))
        vertekri = psr/kdr
        if zenklaskrir() < 0:
            return zenklaskrir()*math.log(alfakrir()*vertekri+betakrir(), pagrkri)
        else:
            return zenklaskrir()*math.log(alfakrir()*vertekri+betakrir(), pagrkri)

    def karareiksmekrirriba():
        if karareiksmekrir() > 4:
            return 4
        elif karareiksmekrir() < -4:
            return -4
        else:
            return karareiksmekrir()
    krirnew_data = {'x': [0, karareiksmekrirriba()], 'y': ["krir", "krir"]}
    if karareiksmekrirriba() > 0:
        sp10.glyph.line_color = "blue"
    else:
        sp10.glyph.line_color = "red"
    sourcekrir.data.update(krirnew_data)
    logging.info(karareiksmekrir())
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
        if (vertekri-balankri)*kryptiskrip() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklaskrip())

    def alfakrip():
        if zenklaskrip() > 0:
            return (1-pagrkri)/(balankri-normaakri)
        else:
            return (1-pagrkri)/(balankri-normakkri)
    logging.info(alfakrip())

    def betakrip():
        if zenklaskrip() > 0:
            return (pagrkri*balankri-normaakri)/(balankri-normaakri)
        else:
            return (pagrkri*balankri-normakkri)/(balankri-normakkri)
    logging.info(betakrip())

    def karareiksmekrip():
        psp = float(pspietus.value.replace(",", "."))
        kdp = float(kdpietus.value.replace(",", "."))
        vertekri = psp/kdp
        if zenklaskrip() < 0:
            return zenklaskrip()*math.log(alfakrip()*vertekri+betakrip(), pagrkri)
        else:
            return zenklaskrip()*math.log(alfakrip()*vertekri+betakrip(), pagrkri)

    def karareiksmekripriba():
        if karareiksmekrip() > 4:
            return 4
        elif karareiksmekrip() < -4:
            return -4
        else:
            return karareiksmekrip()
    kripnew_data = {'x': [0, karareiksmekripriba()], 'y': ["krip", "krip"]}
    if karareiksmekripriba() > 0:
        sp11.glyph.line_color = "blue"
    else:
        sp11.glyph.line_color = "red"
    sourcekrip.data.update(kripnew_data)
    logging.info(karareiksmekrip())
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
        if (vertekri-balankri)*kryptiskriv() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklaskriv())

    def alfakriv():
        if zenklaskriv() > 0:
            return (1-pagrkri)/(balankri-normaakri)
        else:
            return (1-pagrkri)/(balankri-normakkri)
    logging.info(alfakriv())

    def betakriv():
        if zenklaskriv() > 0:
            return (pagrkri*balankri-normaakri)/(balankri-normaakri)
        else:
            return (pagrkri*balankri-normakkri)/(balankri-normakkri)
    logging.info(betakriv())

    def karareiksmekriv():
        psv = float(psvakaras.value.replace(",", "."))
        kdv = float(kdvakaras.value.replace(",", "."))
        vertekri = psv/kdv
        if zenklaskriv() < 0:
            return zenklaskriv()*math.log(alfakriv()*vertekri+betakriv(), pagrkri)
        else:
            return zenklaskriv()*math.log(alfakriv()*vertekri+betakriv(), pagrkri)

    def karareiksmekrivriba():
        if karareiksmekriv() > 4:
            return 4
        elif karareiksmekriv() < -4:
            return -4
        else:
            return karareiksmekriv()
    krivnew_data = {'x': [0, karareiksmekrivriba()], 'y': ["kriv", "kriv"]}
    if karareiksmekrivriba() > 0:
        sp12.glyph.line_color = "blue"
    else:
        sp12.glyph.line_color = "red"
    sourcekriv.data.update(krivnew_data)
    logging.info(karareiksmekriv())
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
        if (vertetemp-balantemp)*kryptistempr() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklastempr())

    def alfatempr():
        if zenklastempr() > 0:
            return (1-pagrtemp)/(balantemp-normaatemp)
        else:
            return (1-pagrtemp)/(balantemp-normaktemp)
    logging.info(alfatempr())

    def betatempr():
        if zenklastempr() > 0:
            return (pagrtemp*balantemp-normaatemp)/(balantemp-normaatemp)
        else:
            return (pagrtemp*balantemp-normaktemp)/(balantemp-normaktemp)
    logging.info(betatempr())

    def karareiksmetempr():
        vertetemp = float(ktrytas.value.replace(",", "."))
        if zenklastempr() < 0:
            return zenklastempr()*math.log(float(alfatempr())*float(vertetemp)+float(betatempr()), pagrtemp)
        else:
            return zenklastempr()*math.log(float(alfatempr())*float(vertetemp)+float(betatempr()), pagrtemp)

    def karareiksmetemprriba():
        if karareiksmetempr() > 4:
            return 4
        elif karareiksmetempr() < -4:
            return -4
        else:
            return karareiksmetempr()
    temprnew_data = {'x': [0, karareiksmetemprriba()], 'y': ["tempr", "tempr"]}
    if karareiksmetemprriba() > 0:
        sp13.glyph.line_color = "blue"
    else:
        sp13.glyph.line_color = "red"
    sourcetempr.data.update(temprnew_data)
    logging.info(karareiksmetempr())
ktrytas.on_change("value", tempr_update)


def tempp_update(attr, old, new):
    def zenklastempp():
        def kryptistempp():
            if normaktemp-balantemp < 0:
                return 1
            else:
                return-1
        vertetemp = float(ktpietus.value.replace(",", "."))
        if (vertetemp-balantemp)*kryptistempp() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklastempp())

    def alfatempp():
        if zenklastempp() > 0:
            return (1-pagrtemp)/(balantemp-normaatemp)
        else:
            return (1-pagrtemp)/(balantemp-normaktemp)
    logging.info(alfatempp())

    def betatempp():
        if zenklastempp() > 0:
            return (pagrtemp*balantemp-normaatemp)/(balantemp-normaatemp)
        else:
            return (pagrtemp*balantemp-normaktemp)/(balantemp-normaktemp)
    logging.info(betatempp())

    def karareiksmetempp():
        vertetemp = float(ktpietus.value.replace(",", "."))
        if zenklastempp() < 0:
            return zenklastempp()*math.log(float(alfatempp())*float(vertetemp)+float(betatempp()), pagrtemp)
        else:
            return zenklastempp()*math.log(float(alfatempp())*float(vertetemp)+float(betatempp()), pagrtemp)

    def karareiksmetemppriba():
        if karareiksmetempp() > 4:
            return 4
        elif karareiksmetempp() < -4:
            return -4
        else:
            return karareiksmetempp()
    temppnew_data = {'x': [0, karareiksmetemppriba()], 'y': ["tempp", "tempp"]}
    if karareiksmetemppriba() > 0:
        sp14.glyph.line_color = "blue"
    else:
        sp14.glyph.line_color = "red"
    sourcetempp.data.update(temppnew_data)
    logging.info(karareiksmetempp())
ktpietus.on_change("value", tempp_update)


def tempv_update(attr, old, new):
    def zenklastempv():
        def kryptistempv():
            if normaktemp-balantemp < 0:
                return 1
            else:
                return-1
        vertetemp = float(ktvakaras.value.replace(",", "."))
        if (vertetemp-balantemp)*kryptistempv() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklastempv())

    def alfatempv():
        if zenklastempv() > 0:
            return (1-pagrtemp)/(balantemp-normaatemp)
        else:
            return (1-pagrtemp)/(balantemp-normaktemp)
    logging.info(alfatempv())

    def betatempv():
        if zenklastempv() > 0:
            return (pagrtemp*balantemp-normaatemp)/(balantemp-normaatemp)
        else:
            return (pagrtemp*balantemp-normaktemp)/(balantemp-normaktemp)
    logging.info(betatempv())

    def karareiksmetempv():
        vertetemp = float(ktvakaras.value.replace(",", "."))
        if zenklastempv() < 0:
            return zenklastempv()*math.log(float(alfatempv())*float(vertetemp)+float(betatempv()), pagrtemp)
        else:
            return zenklastempv()*math.log(float(alfatempv())*float(vertetemp)+float(betatempv()), pagrtemp)

    def karareiksmetempvriba():
        if karareiksmetempv() > 4:
            return 4
        elif karareiksmetempv() < -4:
            return -4
        else:
            return karareiksmetempv()
    tempvnew_data = {'x': [0, karareiksmetempvriba()], 'y': ["tempv", "tempv"]}
    if karareiksmetempvriba() > 0:
        sp15.glyph.line_color = "blue"
    else:
        sp15.glyph.line_color = "red"
    sourcetempv.data.update(tempvnew_data)
    logging.info(karareiksmetempv())
ktvakaras.on_change("value", tempv_update)


normakderm = 1
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
        if (vertederm-balanderm)*kryptisdermr() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasdermr())

    def alfadermr():
        if zenklasdermr() > 0:
            return (1-pagrderm)/(balanderm-normaaderm)
        else:
            return (1-pagrderm)/(balanderm-normakderm)
    logging.info(alfadermr())

    def betadermr():
        if zenklasdermr() > 0:
            return (pagrderm*balanderm-normaaderm)/(balanderm-normaaderm)
        else:
            return (pagrderm*balanderm-normakderm)/(balanderm-normakderm)
    logging.info(betadermr())

    def karareiksmedermr():
        vertederm = float(drrytas.value.replace(",", "."))
        if zenklasdermr() < 0:
            return zenklasdermr()*math.log(float(alfadermr())*float(vertederm)+float(betadermr()), pagrderm)
        else:
            return zenklasdermr()*math.log(float(alfadermr())*float(vertederm)+float(betadermr()), pagrderm)

    def karareiksmedermrriba():
        if karareiksmedermr() > 4:
            return 4
        elif karareiksmedermr() < -4:
            return -4
        else:
            return karareiksmedermr()
    dermrnew_data = {'x': [0, karareiksmedermrriba()], 'y': ["dermr", "dermr"]}
    if karareiksmedermrriba() > 0:
        sp16.glyph.line_color = "blue"
    else:
        sp16.glyph.line_color = "red"
    sourcedermr.data.update(dermrnew_data)
    logging.info(karareiksmedermr())
drrytas.on_change("value", dermr_update)


def dermp_update(attr, old, new):
    def zenklasdermp():
        def kryptisdermp():
            if normakderm-balanderm < 0:
                return 1
            else:
                return-1
        vertederm = float(drpietus.value.replace(",", "."))
        if (vertederm-balanderm)*kryptisdermp() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasdermp())

    def alfadermp():
        if zenklasdermp() > 0:
            return (1-pagrderm)/(balanderm-normaaderm)
        else:
            return (1-pagrderm)/(balanderm-normakderm)
    logging.info(alfadermp())

    def betadermp():
        if zenklasdermp() > 0:
            return (pagrderm*balanderm-normaaderm)/(balanderm-normaaderm)
        else:
            return (pagrderm*balanderm-normakderm)/(balanderm-normakderm)
    logging.info(betadermp())

    def karareiksmedermp():
        vertederm = float(drpietus.value.replace(",", "."))
        if zenklasdermp() < 0:
            return zenklasdermp()*math.log(float(alfadermp())*float(vertederm)+float(betadermp()), pagrderm)
        else:
            return zenklasdermp()*math.log(float(alfadermp())*float(vertederm)+float(betadermp()), pagrderm)

    def karareiksmedermpriba():
        if karareiksmedermp() > 4:
            return 4
        elif karareiksmedermp() < -4:
            return -4
        else:
            return karareiksmedermp()
    dermpnew_data = {'x': [0, karareiksmedermpriba()], 'y': ["dermp", "dermp"]}
    if karareiksmedermpriba() > 0:
        sp17.glyph.line_color = "blue"
    else:
        sp17.glyph.line_color = "red"
    sourcedermp.data.update(dermpnew_data)
    logging.info(karareiksmedermp())
drpietus.on_change("value", dermp_update)


def dermv_update(attr, old, new):
    def zenklasdermv():
        def kryptisdermv():
            if normakderm-balanderm < 0:
                return 1
            else:
                return-1
        vertederm = float(drvakaras.value.replace(",", "."))
        if (vertederm-balanderm)*kryptisdermv() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasdermv())

    def alfadermv():
        if zenklasdermv() > 0:
            return (1-pagrderm)/(balanderm-normaaderm)
        else:
            return (1-pagrderm)/(balanderm-normakderm)
    logging.info(alfadermv())

    def betadermv():
        if zenklasdermv() > 0:
            return (pagrderm*balanderm-normaaderm)/(balanderm-normaaderm)
        else:
            return (pagrderm*balanderm-normakderm)/(balanderm-normakderm)
    logging.info(betadermv())

    def karareiksmedermv():
        vertederm = float(drvakaras.value.replace(",", "."))
        if zenklasdermv() < 0:
            return zenklasdermv()*math.log(float(alfadermv())*float(vertederm)+float(betadermv()), pagrderm)
        else:
            return zenklasdermv()*math.log(float(alfadermv())*float(vertederm)+float(betadermv()), pagrderm)

    def karareiksmedermvriba():
        if karareiksmedermv() > 4:
            return 4
        elif karareiksmedermv() < -4:
            return -4
        else:
            return karareiksmedermv()
    dermvnew_data = {'x': [0, karareiksmedermvriba()], 'y': ["dermv", "dermv"]}
    if karareiksmedermvriba() > 0:
        sp18.glyph.line_color = "blue"
    else:
        sp18.glyph.line_color = "red"
    sourcedermv.data.update(dermvnew_data)
    logging.info(karareiksmedermv())
drvakaras.on_change("value", dermv_update)


normakvaso = -1
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
        if (vertevaso-balanvaso)*kryptisvasor() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasvasor())

    def alfavasor():
        if zenklasvasor() > 0:
            return (1-pagrvaso)/(balanvaso-normaavaso)
        else:
            return (1-pagrvaso)/(balanvaso-normakvaso)
    logging.info(alfavasor())

    def betavasor():
        if zenklasvasor() > 0:
            return (pagrvaso*balanvaso-normaavaso)/(balanvaso-normaavaso)
        else:
            return (pagrvaso*balanvaso-normakvaso)/(balanvaso-normakvaso)
    logging.info(betavasor())

    def karareiksmevasor():
        vertevaso = float(vrrytas.value.replace(",", "."))
        if zenklasvasor() < 0:
            return zenklasvasor()*math.log(float(alfavasor())*float(vertevaso)+float(betavasor()), pagrvaso)
        else:
            return zenklasvasor()*math.log(float(alfavasor())*float(vertevaso)+float(betavasor()), pagrvaso)

    def karareiksmevasorriba():
        if karareiksmevasor() > 4:
            return 4
        elif karareiksmevasor() < -4:
            return -4
        else:
            return karareiksmevasor()
    vasornew_data = {'x': [0, karareiksmevasorriba()], 'y': ["vasor", "vasor"]}
    if karareiksmevasorriba() > 0:
        sp19.glyph.line_color = "blue"
    else:
        sp19.glyph.line_color = "red"
    sourcevasor.data.update(vasornew_data)
    logging.info(karareiksmevasor())
vrrytas.on_change("value", vasor_update)


def vasop_update(attr, old, new):
    def zenklasvasop():
        def kryptisvasop():
            if normakvaso-balanvaso < 0:
                return 1
            else:
                return-1
        vertevaso = float(vrpietus.value.replace(",", "."))
        if (vertevaso-balanvaso)*kryptisvasop() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasvasop())

    def alfavasop():
        if zenklasvasop() > 0:
            return (1-pagrvaso)/(balanvaso-normaavaso)
        else:
            return (1-pagrvaso)/(balanvaso-normakvaso)
    logging.info(alfavasop())

    def betavasop():
        if zenklasvasop() > 0:
            return (pagrvaso*balanvaso-normaavaso)/(balanvaso-normaavaso)
        else:
            return (pagrvaso*balanvaso-normakvaso)/(balanvaso-normakvaso)
    logging.info(betavasop())

    def karareiksmevasop():
        vertevaso = float(vrpietus.value.replace(",", "."))
        if zenklasvasop() < 0:
            return zenklasvasop()*math.log(float(alfavasop())*float(vertevaso)+float(betavasop()), pagrvaso)
        else:
            return zenklasvasop()*math.log(float(alfavasop())*float(vertevaso)+float(betavasop()), pagrvaso)

    def karareiksmevasopriba():
        if karareiksmevasop() > 4:
            return 4
        elif karareiksmevasop() < -4:
            return -4
        else:
            return karareiksmevasop()
    vasopnew_data = {'x': [0, karareiksmevasopriba()], 'y': ["vasop", "vasop"]}
    if karareiksmevasopriba() > 0:
        sp20.glyph.line_color = "blue"
    else:
        sp20.glyph.line_color = "red"
    sourcevasop.data.update(vasopnew_data)
    logging.info(karareiksmevasop())
vrpietus.on_change("value", vasop_update)


def vasov_update(attr, old, new):
    def zenklasvasov():
        def kryptisvasov():
            if normakvaso-balanvaso < 0:
                return 1
            else:
                return-1
        vertevaso = float(vrvakaras.value.replace(",", "."))
        if (vertevaso-balanvaso)*kryptisvasov() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasvasov())

    def alfavasov():
        if zenklasvasov() > 0:
            return (1-pagrvaso)/(balanvaso-normaavaso)
        else:
            return (1-pagrvaso)/(balanvaso-normakvaso)
    logging.info(alfavasov())

    def betavasov():
        if zenklasvasov() > 0:
            return (pagrvaso*balanvaso-normaavaso)/(balanvaso-normaavaso)
        else:
            return (pagrvaso*balanvaso-normakvaso)/(balanvaso-normakvaso)
    logging.info(betavasov())

    def karareiksmevasov():
        vertevaso = float(vrvakaras.value.replace(",", "."))
        if zenklasvasov() < 0:
            return zenklasvasov()*math.log(float(alfavasov())*float(vertevaso)+float(betavasov()), pagrvaso)
        else:
            return zenklasvasov()*math.log(float(alfavasov())*float(vertevaso)+float(betavasov()), pagrvaso)

    def karareiksmevasovriba():
        if karareiksmevasov() > 4:
            return 4
        elif karareiksmevasov() < -4:
            return -4
        else:
            return karareiksmevasov()
    vasovnew_data = {'x': [0, karareiksmevasovriba()], 'y': ["vasov", "vasov"]}
    if karareiksmevasovriba() > 0:
        sp21.glyph.line_color = "blue"
    else:
        sp21.glyph.line_color = "red"
    sourcevasov.data.update(vasovnew_data)
    logging.info(karareiksmevasov())
vrvakaras.on_change("value", vasov_update)


normakvyzd = 1
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
        if (vertevyzd-balanvyzd)*kryptisvyzdr() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasvyzdr())

    def alfavyzdr():
        if zenklasvyzdr() > 0:
            return (1-pagrvyzd)/(balanvyzd-normaavyzd)
        else:
            return (1-pagrvyzd)/(balanvyzd-normakvyzd)
    logging.info(alfavyzdr())

    def betavyzdr():
        if zenklasvyzdr() > 0:
            return (pagrvyzd*balanvyzd-normaavyzd)/(balanvyzd-normaavyzd)
        else:
            return (pagrvyzd*balanvyzd-normakvyzd)/(balanvyzd-normakvyzd)
    logging.info(betavyzdr())

    def karareiksmevyzdr():
        vertevyzd = float(vdrytas.value.replace(",", "."))
        if zenklasvyzdr() < 0:
            return zenklasvyzdr()*math.log(float(alfavyzdr())*float(vertevyzd)+float(betavyzdr()), pagrvyzd)
        else:
            return zenklasvyzdr()*math.log(float(alfavyzdr())*float(vertevyzd)+float(betavyzdr()), pagrvyzd)

    def karareiksmevyzdrriba():
        if karareiksmevyzdr() > 4:
            return 4
        elif karareiksmevyzdr() < -4:
            return -4
        else:
            return karareiksmevyzdr()
    vyzdrnew_data = {'x': [0, karareiksmevyzdrriba()], 'y': ["vyzdr", "vyzdr"]}
    if karareiksmevyzdrriba() > 0:
        sp22.glyph.line_color = "blue"
    else:
        sp22.glyph.line_color = "red"
    sourcevyzdr.data.update(vyzdrnew_data)
    logging.info(karareiksmevyzdr())
vdrytas.on_change("value", vyzdr_update)


def vyzdp_update(attr, old, new):
    def zenklasvyzdp():
        def kryptisvyzdp():
            if normakvyzd-balanvyzd < 0:
                return 1
            else:
                return-1
        vertevyzd = float(vdpietus.value.replace(",", "."))
        if (vertevyzd-balanvyzd)*kryptisvyzdp() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasvyzdp())

    def alfavyzdp():
        if zenklasvyzdp() > 0:
            return (1-pagrvyzd)/(balanvyzd-normaavyzd)
        else:
            return (1-pagrvyzd)/(balanvyzd-normakvyzd)
    logging.info(alfavyzdp())

    def betavyzdp():
        if zenklasvyzdp() > 0:
            return (pagrvyzd*balanvyzd-normaavyzd)/(balanvyzd-normaavyzd)
        else:
            return (pagrvyzd*balanvyzd-normakvyzd)/(balanvyzd-normakvyzd)
    logging.info(betavyzdp())

    def karareiksmevyzdp():
        vertevyzd = float(vdpietus.value.replace(",", "."))
        if zenklasvyzdp() < 0:
            return zenklasvyzdp()*math.log(float(alfavyzdp())*float(vertevyzd)+float(betavyzdp()), pagrvyzd)
        else:
            return zenklasvyzdp()*math.log(float(alfavyzdp())*float(vertevyzd)+float(betavyzdp()), pagrvyzd)

    def karareiksmevyzdpriba():
        if karareiksmevyzdp() > 4:
            return 4
        elif karareiksmevyzdp() < -4:
            return -4
        else:
            return karareiksmevyzdp()
    vyzdpnew_data = {'x': [0, karareiksmevyzdpriba()], 'y': ["vyzdp", "vyzdp"]}
    if karareiksmevyzdpriba() > 0:
        sp23.glyph.line_color = "blue"
    else:
        sp23.glyph.line_color = "red"
    sourcevyzdp.data.update(vyzdpnew_data)
    logging.info(karareiksmevyzdp())
vdpietus.on_change("value", vyzdp_update)


def vyzdv_update(attr, old, new):
    def zenklasvyzdv():
        def kryptisvyzdv():
            if normakvyzd-balanvyzd < 0:
                return 1
            else:
                return-1
        vertevyzd = float(vdvakaras.value.replace(",", "."))
        if (vertevyzd-balanvyzd)*kryptisvyzdv() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasvyzdv())

    def alfavyzdv():
        if zenklasvyzdv() > 0:
            return (1-pagrvyzd)/(balanvyzd-normaavyzd)
        else:
            return (1-pagrvyzd)/(balanvyzd-normakvyzd)
    logging.info(alfavyzdv())

    def betavyzdv():
        if zenklasvyzdv() > 0:
            return (pagrvyzd*balanvyzd-normaavyzd)/(balanvyzd-normaavyzd)
        else:
            return (pagrvyzd*balanvyzd-normakvyzd)/(balanvyzd-normakvyzd)
    logging.info(betavyzdv())

    def karareiksmevyzdv():
        vertevyzd = float(vdvakaras.value.replace(",", "."))
        if zenklasvyzdv() < 0:
            return zenklasvyzdv()*math.log(float(alfavyzdv())*float(vertevyzd)+float(betavyzdv()), pagrvyzd)
        else:
            return zenklasvyzdv()*math.log(float(alfavyzdv())*float(vertevyzd)+float(betavyzdv()), pagrvyzd)

    def karareiksmevyzdvriba():
        if karareiksmevyzdv() > 4:
            return 4
        elif karareiksmevyzdv() < -4:
            return -4
        else:
            return karareiksmevyzdv()
    vyzdvnew_data = {'x': [0, karareiksmevyzdvriba()], 'y': ["vyzdv", "vyzdv"]}
    if karareiksmevyzdvriba() > 0:
        sp24.glyph.line_color = "blue"
    else:
        sp24.glyph.line_color = "red"
    sourcevyzdv.data.update(vyzdvnew_data)
    logging.info(karareiksmevyzdv())
vdvakaras.on_change("value", vyzdv_update)


normaktrem = 1
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
        if (vertetrem-balantrem)*kryptistremr() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklastremr())

    def alfatremr():
        if zenklastremr() > 0:
            return (1-pagrtrem)/(balantrem-normaatrem)
        else:
            return (1-pagrtrem)/(balantrem-normaktrem)
    logging.info(alfatremr())

    def betatremr():
        if zenklastremr() > 0:
            return (pagrtrem*balantrem-normaatrem)/(balantrem-normaatrem)
        else:
            return (pagrtrem*balantrem-normaktrem)/(balantrem-normaktrem)
    logging.info(betatremr())

    def karareiksmetremr():
        vertetrem = float(trrytas.value.replace(",", "."))
        if zenklastremr() < 0:
            return zenklastremr()*math.log(float(alfatremr())*float(vertetrem)+float(betatremr()), pagrtrem)
        else:
            return zenklastremr()*math.log(float(alfatremr())*float(vertetrem)+float(betatremr()), pagrtrem)

    def karareiksmetremrriba():
        if karareiksmetremr() > 4:
            return 4
        elif karareiksmetremr() < -4:
            return -4
        else:
            return karareiksmetremr()
    tremrnew_data = {'x': [0, karareiksmetremrriba()], 'y': ["tremr", "tremr"]}
    if karareiksmetremrriba() > 0:
        sp25.glyph.line_color = "blue"
    else:
        sp25.glyph.line_color = "red"
    sourcetremr.data.update(tremrnew_data)
    logging.info(karareiksmetremr())
trrytas.on_change("value", tremr_update)


def tremp_update(attr, old, new):
    def zenklastremp():
        def kryptistremp():
            if normaktrem-balantrem < 0:
                return 1
            else:
                return-1
        vertetrem = float(trpietus.value.replace(",", "."))
        if (vertetrem-balantrem)*kryptistremp() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklastremp())

    def alfatremp():
        if zenklastremp() > 0:
            return (1-pagrtrem)/(balantrem-normaatrem)
        else:
            return (1-pagrtrem)/(balantrem-normaktrem)
    logging.info(alfatremp())

    def betatremp():
        if zenklastremp() > 0:
            return (pagrtrem*balantrem-normaatrem)/(balantrem-normaatrem)
        else:
            return (pagrtrem*balantrem-normaktrem)/(balantrem-normaktrem)
    logging.info(betatremp())

    def karareiksmetremp():
        vertetrem = float(trpietus.value.replace(",", "."))
        if zenklastremp() < 0:
            return zenklastremp()*math.log(float(alfatremp())*float(vertetrem)+float(betatremp()), pagrtrem)
        else:
            return zenklastremp()*math.log(float(alfatremp())*float(vertetrem)+float(betatremp()), pagrtrem)

    def karareiksmetrempriba():
        if karareiksmetremp() > 4:
            return 4
        elif karareiksmetremp() < -4:
            return -4
        else:
            return karareiksmetremp()
    trempnew_data = {'x': [0, karareiksmetrempriba()], 'y': ["tremp", "tremp"]}
    if karareiksmetrempriba() > 0:
        sp26.glyph.line_color = "blue"
    else:
        sp26.glyph.line_color = "red"
    sourcetremp.data.update(trempnew_data)
    logging.info(karareiksmetremp())
trpietus.on_change("value", tremp_update)


def tremv_update(attr, old, new):
    def zenklastremv():
        def kryptistremv():
            if normaktrem-balantrem < 0:
                return 1
            else:
                return-1
        vertetrem = float(trvakaras.value.replace(",", "."))
        if (vertetrem-balantrem)*kryptistremv() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklastremv())

    def alfatremv():
        if zenklastremv() > 0:
            return (1-pagrtrem)/(balantrem-normaatrem)
        else:
            return (1-pagrtrem)/(balantrem-normaktrem)
    logging.info(alfatremv())

    def betatremv():
        if zenklastremv() > 0:
            return (pagrtrem*balantrem-normaatrem)/(balantrem-normaatrem)
        else:
            return (pagrtrem*balantrem-normaktrem)/(balantrem-normaktrem)
    logging.info(betatremv())

    def karareiksmetremv():
        vertetrem = float(trvakaras.value.replace(",", "."))
        if zenklastremv() < 0:
            return zenklastremv()*math.log(float(alfatremv())*float(vertetrem)+float(betatremv()), pagrtrem)
        else:
            return zenklastremv()*math.log(float(alfatremv())*float(vertetrem)+float(betatremv()), pagrtrem)

    def karareiksmetremvriba():
        if karareiksmetremv() > 4:
            return 4
        elif karareiksmetremv() < -4:
            return -4
        else:
            return karareiksmetremv()
    tremvnew_data = {'x': [0, karareiksmetremvriba()], 'y': ["tremv", "tremv"]}
    if karareiksmetremvriba() > 0:
        sp27.glyph.line_color = "blue"
    else:
        sp27.glyph.line_color = "red"
    sourcetremv.data.update(tremvnew_data)
    logging.info(karareiksmetremv())
trvakaras.on_change("value", tremv_update)


normaknos = -1
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
        if (vertenos-balannos)*kryptisnosr() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasnosr())

    def alfanosr():
        if zenklasnosr() > 0:
            return (1-pagrnos)/(balannos-normaanos)
        else:
            return (1-pagrnos)/(balannos-normaknos)
    logging.info(alfanosr())

    def betanosr():
        if zenklasnosr() > 0:
            return (pagrnos*balannos-normaanos)/(balannos-normaanos)
        else:
            return (pagrnos*balannos-normaknos)/(balannos-normaknos)
    logging.info(betanosr())

    def karareiksmenosr():
        vertenos = float(surytas.value.replace(",", "."))
        if zenklasnosr() < 0:
            return zenklasnosr()*math.log(float(alfanosr())*float(vertenos)+float(betanosr()), pagrnos)
        else:
            return zenklasnosr()*math.log(float(alfanosr())*float(vertenos)+float(betanosr()), pagrnos)

    def karareiksmenosrriba():
        if karareiksmenosr() > 4:
            return 4
        elif karareiksmenosr() < -4:
            return -4
        else:
            return karareiksmenosr()
    nosrnew_data = {'x': [0, karareiksmenosrriba()], 'y': ["nosr", "nosr"]}
    if karareiksmenosrriba() > 0:
        sp28.glyph.line_color = "blue"
    else:
        sp28.glyph.line_color = "red"
    sourcenosr.data.update(nosrnew_data)
    logging.info(karareiksmenosr())
surytas.on_change("value", nosr_update)


def nosp_update(attr, old, new):
    def zenklasnosp():
        def kryptisnosp():
            if normaknos-balannos < 0:
                return 1
            else:
                return-1
        vertenos = float(supietus.value.replace(",", "."))
        if (vertenos-balannos)*kryptisnosp() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasnosp())

    def alfanosp():
        if zenklasnosp() > 0:
            return (1-pagrnos)/(balannos-normaanos)
        else:
            return (1-pagrnos)/(balannos-normaknos)
    logging.info(alfanosp())

    def betanosp():
        if zenklasnosp() > 0:
            return (pagrnos*balannos-normaanos)/(balannos-normaanos)
        else:
            return (pagrnos*balannos-normaknos)/(balannos-normaknos)
    logging.info(betanosp())

    def karareiksmenosp():
        vertenos = float(supietus.value.replace(",", "."))
        if zenklasnosp() < 0:
            return zenklasnosp()*math.log(float(alfanosp())*float(vertenos)+float(betanosp()), pagrnos)
        else:
            return zenklasnosp()*math.log(float(alfanosp())*float(vertenos)+float(betanosp()), pagrnos)

    def karareiksmenospriba():
        if karareiksmenosp() > 4:
            return 4
        elif karareiksmenosp() < -4:
            return -4
        else:
            return karareiksmenosp()
    nospnew_data = {'x': [0, karareiksmenospriba()], 'y': ["nosp", "nosp"]}
    if karareiksmenospriba() > 0:
        sp29.glyph.line_color = "blue"
    else:
        sp29.glyph.line_color = "red"
    sourcenosp.data.update(nospnew_data)
    logging.info(karareiksmenosp())
supietus.on_change("value", nosp_update)


def nosv_update(attr, old, new):
    def zenklasnosv():
        def kryptisnosv():
            if normaknos-balannos < 0:
                return 1
            else:
                return-1
        vertenos = float(suvakaras.value.replace(",", "."))
        if (vertenos-balannos)*kryptisnosv() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklasnosv())

    def alfanosv():
        if zenklasnosv() > 0:
            return (1-pagrnos)/(balannos-normaanos)
        else:
            return (1-pagrnos)/(balannos-normaknos)
    logging.info(alfanosv())

    def betanosv():
        if zenklasnosv() > 0:
            return (pagrnos*balannos-normaanos)/(balannos-normaanos)
        else:
            return (pagrnos*balannos-normaknos)/(balannos-normaknos)
    logging.info(betanosv())

    def karareiksmenosv():
        vertenos = float(suvakaras.value.replace(",", "."))
        if zenklasnosv() < 0:
            return zenklasnosv()*math.log(float(alfanosv())*float(vertenos)+float(betanosv()), pagrnos)
        else:
            return zenklasnosv()*math.log(float(alfanosv())*float(vertenos)+float(betanosv()), pagrnos)

    def karareiksmenosvriba():
        if karareiksmenosv() > 4:
            return 4
        elif karareiksmenosv() < -4:
            return -4
        else:
            return karareiksmenosv()
    nosvnew_data = {'x': [0, karareiksmenosvriba()], 'y': ["nosv", "nosv"]}
    if karareiksmenosvriba() > 0:
        sp30.glyph.line_color = "blue"
    else:
        sp30.glyph.line_color = "red"
    sourcenosv.data.update(nosvnew_data)
    logging.info(karareiksmenosv())
suvakaras.on_change("value", nosv_update)


normaksarg = 1
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
        if (vertesarg-balansarg)*kryptissargr() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklassargr())

    def alfasargr():
        if zenklassargr() > 0:
            return (1-pagrsarg)/(balansarg-normaasarg)
        else:
            return (1-pagrsarg)/(balansarg-normaksarg)
    logging.info(alfasargr())

    def betasargr():
        if zenklassargr() > 0:
            return (pagrsarg*balansarg-normaasarg)/(balansarg-normaasarg)
        else:
            return (pagrsarg*balansarg-normaksarg)/(balansarg-normaksarg)
    logging.info(betasargr())

    def karareiksmesargr():
        vertesarg = float(slrrytas.value.replace(",", "."))
        if zenklassargr() < 0:
            return zenklassargr()*math.log(float(alfasargr())*float(vertesarg)+float(betasargr()), pagrsarg)
        else:
            return zenklassargr()*math.log(float(alfasargr())*float(vertesarg)+float(betasargr()), pagrsarg)

    def karareiksmesargrriba():
        if karareiksmesargr() > 4:
            return 4
        elif karareiksmesargr() < -4:
            return -4
        else:
            return karareiksmesargr()
    sargrnew_data = {'x': [0, karareiksmesargrriba()], 'y': ["sargr", "sargr"]}
    if karareiksmesargrriba() > 0:
        sp31.glyph.line_color = "blue"
    else:
        sp31.glyph.line_color = "red"
    sourcesargr.data.update(sargrnew_data)
    logging.info(karareiksmesargr())
slrrytas.on_change("value", sargr_update)


def sargp_update(attr, old, new):
    def zenklassargp():
        def kryptissargp():
            if normaksarg-balansarg < 0:
                return 1
            else:
                return-1
        vertesarg = float(slrpietus.value.replace(",", "."))
        if (vertesarg-balansarg)*kryptissargp() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklassargp())

    def alfasargp():
        if zenklassargp() > 0:
            return (1-pagrsarg)/(balansarg-normaasarg)
        else:
            return (1-pagrsarg)/(balansarg-normaksarg)
    logging.info(alfasargp())

    def betasargp():
        if zenklassargp() > 0:
            return (pagrsarg*balansarg-normaasarg)/(balansarg-normaasarg)
        else:
            return (pagrsarg*balansarg-normaksarg)/(balansarg-normaksarg)
    logging.info(betasargp())

    def karareiksmesargp():
        vertesarg = float(slrpietus.value.replace(",", "."))
        if zenklassargp() < 0:
            return zenklassargp()*math.log(float(alfasargp())*float(vertesarg)+float(betasargp()), pagrsarg)
        else:
            return zenklassargp()*math.log(float(alfasargp())*float(vertesarg)+float(betasargp()), pagrsarg)

    def karareiksmesargpriba():
        if karareiksmesargp() > 4:
            return 4
        elif karareiksmesargp() < -4:
            return -4
        else:
            return karareiksmesargp()
    sargpnew_data = {'x': [0, karareiksmesargpriba()], 'y': ["sargp", "sargp"]}
    if karareiksmesargpriba() > 0:
        sp32.glyph.line_color = "blue"
    else:
        sp32.glyph.line_color = "red"
    sourcesargp.data.update(sargpnew_data)
    logging.info(karareiksmesargp())
slrpietus.on_change("value", sargp_update)


def sargv_update(attr, old, new):
    def zenklassargv():
        def kryptissargv():
            if normaksarg-balansarg < 0:
                return 1
            else:
                return-1
        vertesarg = float(slrvakaras.value.replace(",", "."))
        if (vertesarg-balansarg)*kryptissargv() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklassargv())

    def alfasargv():
        if zenklassargv() > 0:
            return (1-pagrsarg)/(balansarg-normaasarg)
        else:
            return (1-pagrsarg)/(balansarg-normaksarg)
    logging.info(alfasargv())

    def betasargv():
        if zenklassargv() > 0:
            return (pagrsarg*balansarg-normaasarg)/(balansarg-normaasarg)
        else:
            return (pagrsarg*balansarg-normaksarg)/(balansarg-normaksarg)
    logging.info(betasargv())

    def karareiksmesargv():
        vertesarg = float(slrvakaras.value.replace(",", "."))
        if zenklassargv() < 0:
            return zenklassargv()*math.log(float(alfasargv())*float(vertesarg)+float(betasargv()), pagrsarg)
        else:
            return zenklassargv()*math.log(float(alfasargv())*float(vertesarg)+float(betasargv()), pagrsarg)

    def karareiksmesargvriba():
        if karareiksmesargv() > 4:
            return 4
        elif karareiksmesargv() < -4:
            return -4
        else:
            return karareiksmesargv()
    sargvnew_data = {'x': [0, karareiksmesargvriba()], 'y': ["sargv", "sargv"]}
    if karareiksmesargvriba() > 0:
        sp33.glyph.line_color = "blue"
    else:
        sp33.glyph.line_color = "red"
    sourcesargv.data.update(sargvnew_data)
    logging.info(karareiksmesargv())
slrvakaras.on_change("value", sargv_update)


normakskl = 1
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
        if (verteskl-balanskl)*kryptissklr() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklassklr())

    def alfasklr():
        if zenklassklr() > 0:
            return (1-pagrskl)/(balanskl-normaaskl)
        else:
            return (1-pagrskl)/(balanskl-normakskl)
    logging.info(alfasklr())

    def betasklr():
        if zenklassklr() > 0:
            return (pagrskl*balanskl-normaaskl)/(balanskl-normaaskl)
        else:
            return (pagrskl*balanskl-normakskl)/(balanskl-normakskl)
    logging.info(betasklr())

    def karareiksmesklr():
        verteskl = float(sekrytas.value.replace(",", "."))
        if zenklassklr() < 0:
            return zenklassklr()*math.log(float(alfasklr())*float(verteskl)+float(betasklr()), pagrskl)
        else:
            return zenklassklr()*math.log(float(alfasklr())*float(verteskl)+float(betasklr()), pagrskl)

    def karareiksmesklrriba():
        if karareiksmesklr() > 4:
            return 4
        elif karareiksmesklr() < -4:
            return -4
        else:
            return karareiksmesklr()
    sklrnew_data = {'x': [0, karareiksmesklrriba()], 'y': ["sklr", "sklr"]}
    if karareiksmesklrriba() > 0:
        sp34.glyph.line_color = "blue"
    else:
        sp34.glyph.line_color = "red"
    sourcesklr.data.update(sklrnew_data)
    logging.info(karareiksmesklr())
sekrytas.on_change("value", sklr_update)


def sklp_update(attr, old, new):
    def zenklassklp():
        def kryptissklp():
            if normakskl-balanskl < 0:
                return 1
            else:
                return-1
        verteskl = float(sekpietus.value.replace(",", "."))
        if (verteskl-balanskl)*kryptissklp() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklassklp())

    def alfasklp():
        if zenklassklp() > 0:
            return (1-pagrskl)/(balanskl-normaaskl)
        else:
            return (1-pagrskl)/(balanskl-normakskl)
    logging.info(alfasklp())

    def betasklp():
        if zenklassklp() > 0:
            return (pagrskl*balanskl-normaaskl)/(balanskl-normaaskl)
        else:
            return (pagrskl*balanskl-normakskl)/(balanskl-normakskl)
    logging.info(betasklp())

    def karareiksmesklp():
        verteskl = float(sekpietus.value.replace(",", "."))
        if zenklassklp() < 0:
            return zenklassklp()*math.log(float(alfasklp())*float(verteskl)+float(betasklp()), pagrskl)
        else:
            return zenklassklp()*math.log(float(alfasklp())*float(verteskl)+float(betasklp()), pagrskl)

    def karareiksmesklpriba():
        if karareiksmesklp() > 4:
            return 4
        elif karareiksmesklp() < -4:
            return -4
        else:
            return karareiksmesklp()
    sklpnew_data = {'x': [0, karareiksmesklpriba()], 'y': ["sklp", "sklp"]}
    if karareiksmesklpriba() > 0:
        sp35.glyph.line_color = "blue"
    else:
        sp35.glyph.line_color = "red"
    sourcesklp.data.update(sklpnew_data)
    logging.info(karareiksmesklp())
sekpietus.on_change("value", sklp_update)


def sklv_update(attr, old, new):
    def zenklassklv():
        def kryptissklv():
            if normakskl-balanskl < 0:
                return 1
            else:
                return-1
        verteskl = float(sekvakaras.value.replace(",", "."))
        if (verteskl-balanskl)*kryptissklv() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklassklv())

    def alfasklv():
        if zenklassklv() > 0:
            return (1-pagrskl)/(balanskl-normaaskl)
        else:
            return (1-pagrskl)/(balanskl-normakskl)
    logging.info(alfasklv())

    def betasklv():
        if zenklassklv() > 0:
            return (pagrskl*balanskl-normaaskl)/(balanskl-normaaskl)
        else:
            return (pagrskl*balanskl-normakskl)/(balanskl-normakskl)
    logging.info(betasklv())

    def karareiksmesklv():
        verteskl = float(sekvakaras.value.replace(",", "."))
        if zenklassklv() < 0:
            return zenklassklv()*math.log(float(alfasklv())*float(verteskl)+float(betasklv()), pagrskl)
        else:
            return zenklassklv()*math.log(float(alfasklv())*float(verteskl)+float(betasklv()), pagrskl)

    def karareiksmesklvriba():
        if karareiksmesklv() > 4:
            return 4
        elif karareiksmesklv() < -4:
            return -4
        else:
            return karareiksmesklv()
    sklvnew_data = {'x': [0, karareiksmesklvriba()], 'y': ["sklv", "sklv"]}
    if karareiksmesklvriba() > 0:
        sp36.glyph.line_color = "blue"
    else:
        sp36.glyph.line_color = "red"
    sourcesklv.data.update(sklvnew_data)
    logging.info(karareiksmesklvriba())
sekvakaras.on_change("value", sklv_update)

# katogeninis/gliukogeninis
# S-pHK
# KD
# t
# P4
# KpHi
# D2-P4
# U-šv
# U-put

sourcesphkr = ColumnDataSource(data=dict(x=[], y=[]))
sourcesphkp = ColumnDataSource(data=dict(x=[], y=[]))
sourcesphkv = ColumnDataSource(data=dict(x=[], y=[]))

sourcekdr = ColumnDataSource(data=dict(x=[], y=[]))
sourcekdp = ColumnDataSource(data=dict(x=[], y=[]))
sourcekdv = ColumnDataSource(data=dict(x=[], y=[]))

sourcetankr = ColumnDataSource(data=dict(x=[], y=[]))
sourcetankp = ColumnDataSource(data=dict(x=[], y=[]))
sourcetankv = ColumnDataSource(data=dict(x=[], y=[]))


def sphkr_update(attr, old, new):
    def sphkr():
        tank = float(strytas.value.replace(",", "."))
        vertetank = tank*1000-1000
        serug = float(serrytas.value.replace(",", "."))
        return serug+0.033333*vertetank-0.533333

    def sphkrriba():
        if sphkr() > 4:
            return 4
        elif sphkr() < -4:
            return -4
        else:
            return sphkr()
    sphkrnew_data = {'x': [0, sphkrriba()], 'y': ["sphkr", "sphkr"]}
    if sphkrriba() > 0:
        kg1.glyph.line_color = "blue"
    else:
        kg1.glyph.line_color = "red"
    sourcesphkr.data.update(sphkrnew_data)
    return float(sphkrriba())
strytas.on_change("value", sphkr_update)
serrytas.on_change("value", sphkr_update)


def sphkp_update(attr, old, new):
    def sphkp():
        tank = float(stpietus.value.replace(",", "."))
        vertetank = tank*1000-1000
        serug = float(serpietus.value.replace(",", "."))
        return serug+0.033333*vertetank-0.533333

    def sphkpriba():
        if sphkp() > 4:
            return 4
        elif sphkp() < -4:
            return -4
        else:
            return sphkp()
    sphkpnew_data = {'x': [0, sphkpriba()], 'y': ["sphkp", "sphkp"]}
    if sphkpriba() > 0:
        kg2.glyph.line_color = "blue"
    else:
        kg2.glyph.line_color = "red"
    sourcesphkp.data.update(sphkpnew_data)
    return float(sphkpriba())
stpietus.on_change("value", sphkp_update)
serpietus.on_change("value", sphkp_update)


def sphkv_update(attr, old, new):
    def sphkv():
        tank = float(stvakaras.value.replace(",", "."))
        vertetank = tank*1000-1000
        serug = float(servakaras.value.replace(",", "."))
        return serug+0.033333*vertetank-0.533333

    def sphkvriba():
        if sphkv() > 4:
            return 4
        elif sphkv() < -4:
            return -4
        else:
            return sphkv()
    sphkvnew_data = {'x': [0, sphkvriba()], 'y': ["sphkv", "sphkv"]}
    if sphkvriba() > 0:
        kg3.glyph.line_color = "blue"
    else:
        kg3.glyph.line_color = "red"
    sourcesphkv.data.update(sphkvnew_data)
    return float(sphkvriba())
stvakaras.on_change("value", sphkv_update)
servakaras.on_change("value", sphkv_update)


normakkd = 15
pagrkd = 2


def kdr_update(attr, old, new):
    def normaakdr():
        if sphkr_update(attr, old, new) >= 6.8 and sphkr_update(attr, old, new) < 7:
            return 16
        else:
            return 17
    logging.info(normaakdr())
    balankd = float((normaakdr()+normakkd)/2)

    def zenklaskdr():
        def kryptiskdr():
            if normakkd-balankd < 0:
                return 1
            else:
                return-1
        vertekd = float(kdrytas.value.replace(",", "."))
        if (vertekd-balankd)*kryptiskdr() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklaskdr())

    def alfakdr():
        if zenklaskdr() > 0:
            return (1-pagrkd)/(balankd-normaakdr())
        else:
            return (1-pagrkd)/(balankd-normakkd)
    logging.info(alfakdr())

    def betakdr():
        if zenklaskdr() > 0:
            return (pagrkd*balankd-normaakdr())/(balankd-normaakdr())
        else:
            return (pagrkd*balankd-normakkd)/(balankd-normakkd)
    logging.info(betakdr())

    def karareiksmekdr():
        vertekd = float(kdrytas.value.replace(",", "."))
        if zenklaskdr() < 0:
            return zenklaskdr()*math.log(float(alfakdr())*float(vertekd)+float(betakdr()), pagrkd)
        else:
            return zenklaskdr()*math.log(float(alfakdr())*float(vertekd)+float(betakdr()), pagrkd)

    def karareiksmekdrriba():
        if karareiksmekdr() > 4:
            return 4
        elif karareiksmekdr() < -4:
            return -4
        else:
            return karareiksmekdr()
    kdrnew_data = {'x': [0, karareiksmekdrriba()], 'y': ["kdr", "kdr"]}
    if karareiksmekdrriba() > 0:
        kg4.glyph.line_color = "blue"
    else:
        kg4.glyph.line_color = "red"
    sourcekdr.data.update(kdrnew_data)
    logging.info(karareiksmekdr())
kdrytas.on_change("value", kdr_update)


def kdp_update(attr, old, new):
    def normaakdp():
        if sphkp_update(attr, old, new) >= 6.8 and sphkp_update(attr, old, new) < 7:
            return 16
        else:
            return 17
    logging.info(normaakdp())
    balankd = float((normaakdp()+normakkd)/2)

    def zenklaskdp():
        def kryptiskdp():
            if normakkd-balankd < 0:
                return 1
            else:
                return-1
        vertekd = float(kdpietus.value.replace(",", "."))
        if (vertekd-balankd)*kryptiskdp() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklaskdp())

    def alfakdp():
        if zenklaskdp() > 0:
            return (1-pagrkd)/(balankd-normaakdp())
        else:
            return (1-pagrkd)/(balankd-normakkd)
    logging.info(alfakdp())

    def betakdp():
        if zenklaskdp() > 0:
            return (pagrkd*balankd-normaakdp())/(balankd-normaakdp())
        else:
            return (pagrkd*balankd-normakkd)/(balankd-normakkd)
    logging.info(betakdp())

    def karareiksmekdp():
        vertekd = float(kdpietus.value.replace(",", "."))
        if zenklaskdp() < 0:
            return zenklaskdp()*math.log(float(alfakdp())*float(vertekd)+float(betakdp()), pagrkd)
        else:
            return zenklaskdp()*math.log(float(alfakdp())*float(vertekd)+float(betakdp()), pagrkd)

    def karareiksmekdpriba():
        if karareiksmekdp() > 4:
            return 4
        elif karareiksmekdp() < -4:
            return -4
        else:
            return karareiksmekdp()
    kdpnew_data = {'x': [0, karareiksmekdpriba()], 'y': ["kdp", "kdp"]}
    if karareiksmekdpriba() > 0:
        kg5.glyph.line_color = "blue"
    else:
        kg5.glyph.line_color = "red"
    sourcekdp.data.update(kdpnew_data)
    logging.info(karareiksmekdp())
kdpietus.on_change("value", kdp_update)


def kdv_update(attr, old, new):
    def normaakdv():
        if sphkv_update(attr, old, new) >= 6.8 and sphkv_update(attr, old, new) < 7:
            return 16
        else:
            return 17
    logging.info(normaakdv())
    balankd = float((normaakdv()+normakkd)/2)

    def zenklaskdv():
        def kryptiskdv():
            if normakkd-balankd < 0:
                return 1
            else:
                return-1
        vertekd = float(kdvakaras.value.replace(",", "."))
        if (vertekd-balankd)*kryptiskdv() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklaskdv())

    def alfakdv():
        if zenklaskdv() > 0:
            return (1-pagrkd)/(balankd-normaakdv())
        else:
            return (1-pagrkd)/(balankd-normakkd)
    logging.info(alfakdv())

    def betakdv():
        if zenklaskdv() > 0:
            return (pagrkd*balankd-normaakdv())/(balankd-normaakdv())
        else:
            return (pagrkd*balankd-normakkd)/(balankd-normakkd)
    logging.info(betakdv())

    def karareiksmekdv():
        vertekd = float(kdvakaras.value.replace(",", "."))
        if zenklaskdv() < 0:
            return zenklaskdv()*math.log(float(alfakdv())*float(vertekd)+float(betakdv()), pagrkd)
        else:
            return zenklaskdv()*math.log(float(alfakdv())*float(vertekd)+float(betakdv()), pagrkd)

    def karareiksmekdvriba():
        if karareiksmekdv() > 4:
            return 4
        elif karareiksmekdv() < -4:
            return -4
        else:
            return karareiksmekdv()
    kdvnew_data = {'x': [0, karareiksmekdvriba()], 'y': ["kdv", "kdv"]}
    if karareiksmekdvriba() > 0:
        kg6.glyph.line_color = "blue"
    else:
        kg6.glyph.line_color = "red"
    sourcekdv.data.update(kdvnew_data)
    logging.info(karareiksmekdv())
kdvakaras.on_change("value", kdv_update)


pagrtank = 1.2


def tankr_update(attr, old, new):
    def normaktankr():
        if sphkr_update(attr, old, new) < 6.4:
            return 67
        elif sphkr_update(attr, old, new) > 7.1:
            return 46
        else:
            return float(sphkr_update(attr, old, new)*(-30)+259)
    logging.info(normaktankr())

    def normaatank():
        if sphkr_update(attr, old, new) < 6.4:
            return 52
        elif sphkr_update(attr, old, new) > 7.1:
            return 31
        else:
            return float(sphkr_update(attr, old, new)*(-30)+244)
    logging.info(normaatank())
    balantank = float((normaatank()+normaktankr())/2)
    logging.info(balantank)

    def zenklastankr():
        def kryptistankr():
            if normaktankr()-balantank < 0:
                return 1
            else:
                return-1
        vertetank = float(ksirytas.value.replace(",", "."))
        if (vertetank-balantank)*kryptistankr() >= 0:
            return 1
        else:
            return -1
    logging.info(zenklastankr())

    def alfatankr():
        if zenklastankr() > 0:
            return (1-pagrtank)/(balantank-normaatank())
        else:
            return (1-pagrtank)/(balantank-normaktankr())
    logging.info(alfatankr())

    def betatankr():
        if zenklastankr() > 0:
            return (pagrtank*balantank-normaatank())/(balantank-normaatank())
        else:
            return (pagrtank*balantank-normaktankr())/(balantank-normaktankr())
    logging.info(betatankr())

    def karareiksmetankr():
        vertetank = float(ksirytas.value.replace(",", "."))
        if zenklastankr() < 0:
            return zenklastankr()*math.log(float(alfatankr())*float(vertetank)+float(betatankr()), pagrtank)
        else:
            return zenklastankr()*math.log(float(alfatankr())*float(vertetank)+float(betatankr()), pagrtank)

    def karareiksmetankrriba():
        if karareiksmetankr() > 4:
            return 4
        elif karareiksmetankr() < -4:
            return -4
        else:
            return karareiksmetankr()
    tankrnew_data = {'x': [0, karareiksmetankrriba()], 'y': ["tankr", "tankr"]}
    if karareiksmetankrriba() > 0:
        kg7.glyph.line_color = "blue"
    else:
        kg7.glyph.line_color = "red"
    sourcetankr.data.update(tankrnew_data)
    logging.info(karareiksmetankr())
ksirytas.on_change("value", tankr_update)

# grafikai
def make_graf():
    for i, n in zip(plist, pavadin):
        i = figure(x_range=[-5, 5], y_range=FactorRange(factors=factorssp), height=350, tools="")
        i.title.text = "<-Katabolizmas|Anabolizmas->"
        i.title.align = "center"
        i.text(x=[-4.7], y=[(countsp-(countsp-3)/3-1)], text=["Rytas"], text_font_size='10pt', text_font_style="bold", angle=1.56)
        i.text(x=[-4.7], y=[(countsp-(countsp-3)/3*2-2)], text=["Pietūs"], text_font_size='10pt', text_font_style="bold", angle=1.56)
        i.text(x=[-4.7], y=[(countsp-(countsp-1))], text=["Vakaras"], text_font_size='10pt', text_font_style="bold", angle=1.56)
        i.x_range.bounds = 'auto'
        i.y_range.bounds = 'auto'
        i.xaxis.axis_label = n
        i.yaxis.visible = False
        i.xaxis.ticker = FixedTicker(ticks=[-4, -3, -2, -1, 1, 2, 3, 4])
        i.xaxis.formatter = FuncTickFormatter(code="""
            data = {"-4": "Didelis", "-3": "Vidutinis", "-2": 'Mažas', "-1": "Norma", 1: 'Norma', 2: 'Mažas', 3: 'Vidutinis', 4: 'Didelis'}
            return data[tick]
            """)
        i.add_layout(Span(location=0, dimension='height', line_color='black', line_dash='solid', line_width=4))
        i.add_layout(Span(location=1, dimension='height', line_color='green', line_dash='dashed', line_width=4))
        i.add_layout(Span(location=-1, dimension='height', line_color='green', line_dash='dashed', line_width=4))
        i.add_layout(Span(location=2, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
        i.add_layout(Span(location=-2, dimension='height', line_color='orange', line_dash='dashed', line_width=4))
        i.add_layout(Span(location=3, dimension='height', line_color='red', line_dash='dashed', line_width=4))
        i.add_layout(Span(location=-3, dimension='height', line_color='red', line_dash='dashed', line_width=4))
        i.add_layout(Span(location=4, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
        i.add_layout(Span(location=-4, dimension='height', line_color='darkred', line_dash='dashed', line_width=4))
        i.add_layout(BoxAnnotation(top=(countsp-3)/3+1, fill_alpha=0.1, fill_color='black'))
        i.add_layout(BoxAnnotation(bottom=(countsp-3)/3+1, top=(countsp-3)/3*2+2, fill_alpha=0.1, fill_color='cyan'))
        i.add_layout(BoxAnnotation(top=countsp, fill_alpha=0.1, fill_color='yellow'))
        # simpatinis/parasimpatinis
        # if i == "p1":
        #     sp1 = i.line('x', 'y', source=sourceps1r, line_color="blue", line_width=5)
        #     sp2 = i.line('x', 'y', source=sourceps1p, line_color="blue", line_width=5)
        #     sp3 = i.line('x', 'y', source=sourceps1v, line_color="blue", line_width=5)
        #     sp4 = i.line('x', 'y', source=sourcesdr, line_color="blue", line_width=5)
        #     sp5 = i.line('x', 'y', source=sourcesdp, line_color="blue", line_width=5)
        #     sp6 = i.line('x', 'y', source=sourcesdv, line_color="blue", line_width=5)
        #     sp7 = i.line('x', 'y', source=sourceppr, line_color="blue", line_width=5)
        #     sp8 = i.line('x', 'y', source=sourceppp, line_color="blue", line_width=5)
        #     sp9 = i.line('x', 'y', source=sourceppv, line_color="blue", line_width=5)
        #     sp10 = i.line('x', 'y', source=sourcekrir, line_color="blue", line_width=5)
        #     sp11 = i.line('x', 'y', source=sourcekrip, line_color="blue", line_width=5)
        #     sp12 = i.line('x', 'y', source=sourcekriv, line_color="blue", line_width=5)
        #     sp13 = i.line('x', 'y', source=sourcetempr, line_color="blue", line_width=5)
        #     sp14 = i.line('x', 'y', source=sourcetempp, line_color="blue", line_width=5)
        #     sp15 = i.line('x', 'y', source=sourcetempv, line_color="blue", line_width=5)
        #     sp16 = i.line('x', 'y', source=sourcedermr, line_color="blue", line_width=5)
        #     sp17 = i.line('x', 'y', source=sourcedermp, line_color="blue", line_width=5)
        #     sp18 = i.line('x', 'y', source=sourcedermv, line_color="blue", line_width=5)
        #     sp19 = i.line('x', 'y', source=sourcevasor, line_color="blue", line_width=5)
        #     sp20 = i.line('x', 'y', source=sourcevasop, line_color="blue", line_width=5)
        #     sp21 = i.line('x', 'y', source=sourcevasov, line_color="blue", line_width=5)
        #     sp22 = i.line('x', 'y', source=sourcevyzdr, line_color="blue", line_width=5)
        #     sp23 = i.line('x', 'y', source=sourcevyzdp, line_color="blue", line_width=5)
        #     sp24 = i.line('x', 'y', source=sourcevyzdv, line_color="blue", line_width=5)
        #     sp25 = i.line('x', 'y', source=sourcetremr, line_color="blue", line_width=5)
        #     sp26 = i.line('x', 'y', source=sourcetremp, line_color="blue", line_width=5)
        #     sp27 = i.line('x', 'y', source=sourcetremv, line_color="blue", line_width=5)
        #     sp28 = i.line('x', 'y', source=sourcenosr, line_color="blue", line_width=5)
        #     sp29 = i.line('x', 'y', source=sourcenosp, line_color="blue", line_width=5)
        #     sp30 = i.line('x', 'y', source=sourcenosv, line_color="blue", line_width=5)
        #     sp31 = i.line('x', 'y', source=sourcesargr, line_color="blue", line_width=5)
        #     sp32 = i.line('x', 'y', source=sourcesargp, line_color="blue", line_width=5)
        #     sp33 = i.line('x', 'y', source=sourcesargv, line_color="blue", line_width=5)
        #     sp34 = i.line('x', 'y', source=sourcesklr, line_color="blue", line_width=5)
        #     sp35 = i.line('x', 'y', source=sourcesklp, line_color="blue", line_width=5)
        #     sp36 = i.line('x', 'y', source=sourcesklv, line_color="blue", line_width=5)
        # # katogeninis|gliukogeninis
        # elif i == "p2":
        #     kg1 = i.line('x', 'y', source=sourcesphkr, line_color="blue", line_width=5)
        #     kg2 = i.line('x', 'y', source=sourcesphkp, line_color="blue", line_width=5)
        #     kg3 = i.line('x', 'y', source=sourcesphkv, line_color="blue", line_width=5)
        #     kg4 = i.line('x', 'y', source=sourcekdr, line_color="blue", line_width=5)
        #     kg5 = i.line('x', 'y', source=sourcekdp, line_color="blue", line_width=5)
        #     kg6 = i.line('x', 'y', source=sourcekdv, line_color="blue", line_width=5)
        #     kg7 = i.line('x', 'y', source=sourcetankr, line_color="blue", line_width=5)
        #     kg8 = i.line('x', 'y', source=sourcetankp, line_color="blue", line_width=5)
        #     kg9 = i.line('x', 'y', source=sourcetankv, line_color="blue", line_width=5)
        L.append(i)
    return L

if __name__ == '__main__':
	main()