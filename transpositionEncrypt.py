#!/usr/bin/python

import math

def main():
    action = 'decrypt'
    key = 10
    if action == 'encrypt':
        text = """Letter 1


St. Petersburgh, Dec. 11th, 17--

TO Mrs. Saville, England

You will rejoice to hear that no disaster has accompanied the
commencement of an enterprise which you have regarded with such evil
forebodings.  I arrived here yesterday, and my first task is to assure
my dear sister of my welfare and increasing confidence in the success
of my undertaking.

I am already far north of London, and as I walk in the streets of
Petersburgh, I feel a cold northern breeze play upon my cheeks, which
braces my nerves and fills me with delight.  Do you understand this
feeling?  This breeze, which has travelled from the regions towards
which I am advancing, gives me a foretaste of those icy climes.
Inspirited by this wind of promise, my daydreams become more fervent
and vivid.  I try in vain to be persuaded that the pole is the seat of
frost and desolation; it ever presents itself to my imagination as the
region of beauty and delight.  There, Margaret, the sun is forever
visible, its broad disk just skirting the horizon and diffusing a
perpetual splendour.  There--for with your leave, my sister, I will put
some trust in preceding navigators--there snow and frost are banished;
and, sailing over a calm sea, we may be wafted to a land surpassing in
wonders and in beauty every region hitherto discovered on the habitable
globe.  Its productions and features may be without example, as the
phenomena of the heavenly bodies undoubtedly are in those undiscovered
solitudes.  What may not be expected in a country of eternal light?  I
may there discover the wondrous power which attracts the needle and may
regulate a thousand celestial observations that require only this
voyage to render their seeming eccentricities consistent forever.  I
shall satiate my ardent curiosity with the sight of a part of the world
never before visited, and may tread a land never before imprinted by
the foot of man. These are my enticements, and they are sufficient to
conquer all fear of danger or death and to induce me to commence this
laborious voyage with the joy a child feels when he embarks in a little
boat, with his holiday mates, on an expedition of discovery up his
native river. But supposing all these conjectures to be false, you
cannot contest the inestimable benefit which I shall confer on all
mankind, to the last generation, by discovering a passage near the pole
to those countries, to reach which at present so many months are
requisite; or by ascertaining the secret of the magnet, which, if at
all possible, can only be effected by an undertaking such as mine."""
        print(encrypt(text, key))
    elif action == 'decrypt':
        text = """L
sc7s,
r  eohensoghlnr ,iir  eef sn.rno  re, hensrefit dlswtfea ner  nbniycfdIapto re rs orb  reoib to  au- ee tra-wts v aenidnvn dal ntb antluyhclWocc iaie csl
a  oeyadsceerlmcwipev ae ot aaiareqegtiteoahh maohyniipvBieteocebtsemo nopae , p hu a  tipce eueeSb.-. Yehnrmem eua 
giy rsesm aitsd
eonaiet ce  ,arit.u i hrrgrIcsetcsydsdoe  iehlsosieeineedTg rbrjirdalr-y,rprevt  hsesyddne e d bopsueesohyn ooihttoegys ph er conq geeesn. yuiga evnanrefnrcnenuaehno rgeiwb ai  ts eunsu uo l hra g,var
c wrmsibist,foa brc.ttu - Eojeo p
ee  rsfsveas 
iyasdh
e
ardsneeIorpm cvlh ntnbiaoid i thlp  ermrvtnraeesotslm gaehaselounii
 .fo ,uucihaaeare   grbrhioibr r x me dasvta euth cwo t etebsuteren t s rthrwriddeedo.eed terr d tie lhaltsmaich tgerf
niewa nte es tothea syneh  sneytht.r1
Snuoa hacnnwhduo.esnttms nieeorIdto  tr lnlyweel  dhgrcvmosanmaoiito,eevir st atl efaaiuleruveasgzfps oum tsegenrdi abts seyisnteoaewate boreeutbdnettoowahaghls ih  mtc  aaihtto s  v  o  m s r  aucho jderi, anooir   eactn hlokhnbrstouoisnai icewas f a e g1
ag irdanotthaecr dtd oytwdnn ft yhnItssfd a hsssdDei?ehe n
mgessmrhf a evytu it aen gsotirene,dt ofep rryI
tdarde;la,eoui a tc a.dnsimhnhoue rd e tr?hvnetenuoeetrittirofItro   rbimaeibtTmetut ooncoiuwo nkt ht nvsisacslaeebilnieeyiah n ceyrtanr htiofakarPhtTvlwc isim eivdhe  e t  ee gcs aa  , h be byci   eors e ltsw , teeii mmmni oats atvtti nyget r   tnurlT    s ite  
i    rnaurhotb ud tpeaedb ueem irn eedrt dlusrhesohnino
idstooleta rmy hynhfoafrdemssiyf stwoee e
vulo snssec  n r ngettrhn eesgemi
bnenis e,hOiaiets emorce  bIhrmaadrli eumkmfo weouenr hcmaml s
 zhlh ha ae stspysotdi dh oniesont  h,,i
idsh spehwlswoino fbancwwap
nteevhl c mhl
 aitindsaenya rrr rn astva 
 egcsrsaeihffdfeyl p
oe tef
l    m
 t eh lilsxorneplntenttnhcadladge hre tm
;c tacallc n 1t , lnl haadefph weo edysse fnc cyi afaa frloeuehyneiytfTeaeetidg  i.e r  r
.nbeetfdor  ahoat  svtikeaieneieiimngrsrangaea awdygreeeItfaoepoveend
.yx  lIe owaemtaiatovri iiehtnte  
od abrtfsesyiclddtmelvhaeeieti,pfyarp jo,o ie ol,ati  poiaa or et ghleytugm
eD Mldltasc n r rivdara ksaoacoic nar nls
g repe
 d goaeh,sd ocvifoc
dwodbea  ed h
 n imtefn.Mt issi nntdrtasle  snond l flso  itr 
tieyu,hfesd is  pao 
 tuhceaenat noeretsvaety atnr,tneih en, co aeoenao  l n
hd e  t.ote  ttmfInl sisanosectsneorhon,l, en i
re1re
 ottctcaiyetiireyf urfrrnneugl LdktPhatzokbn whunei   rwhavofyI imae n v  pefd;ptyi
 d ahfs krhdguoehvtl pn-osi,ommtasnieooehgsoa t e n ltso ne flmdhsitdy dlirlyn citel   s hee rdfnem t ainfna  cbytcse b aoddui shcby hai f
ttoc elesh otqrtefe   bddsn"""
        print(decrypt(text, key))
    else:
        exit()



def encrypt(text, key):
    length = len(text)
    matrix = [''] * key

    col = 0
    for letter in text:
        matrix[col] += letter
        col += 1
        if col == key:
            col = 0

    return(''.join(matrix))



def numOfRows(text, key):
    # get number of columns
    columns = math.ceil(len(text) / float(key))
    unused = key * columns - len(text)
    return(int(columns), int(unused))



def decrypt(text, key):
    columns = numOfRows(text, key)[0]
    unused = numOfRows(text, key)[1]
    col, row = 0, 0
    matrix = [''] * columns
    for char in text:
        matrix[col] += char
        col += 1
        if col == columns or (col == columns - 1 and row >= key - unused ):
            row += 1
            col = 0

    text = ''.join(matrix)

    return(text)



if __name__ == '__main__':
    main()



# >>> import transpositionEncrypt as crypt
# >>> crypt.encrypt(text,key)
# >>> crypt.decrypt(text,key)
