#!/usr/bin/python3

from detectEnglish import isEnglish as isEnglish
from transpositionEncrypt import decrypt as decrypt

def main():
    myMessage = """L
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

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print(hackedMessage)

def hackTransposition(message):
    print('Hacking...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))

        decryptedText = decrypt(message, key)

        if isEnglish(decryptedText):
            print()
            print('Possible encryption hack:')
            print('Key #%s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D for done, or just press Enter for continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return(decryptedText)

    return(None)


if __name__ == '__main__':
    main()
