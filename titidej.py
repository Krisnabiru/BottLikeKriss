# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit


#client = LineClient()
#client = LINE(id='EMAIL HERE', passwd='PASSWORD HERE')
client = LINE("Et9CTYSOU8Wu0Ye9zM2b.ggNCLqZ5irfKOvdzgQfq2W.X0K5obTzBtTVY3/ZxoZCvDziMFPx79rhxXHpY8BQ6m4=")
clientMid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
client.log("Auth Token : " + str(client.authToken))

botStart = time.time()

msg_dict = {}

# Initialize OEPoll with LINE instance
oepoll = OEPoll(client)

mode='self'
cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

keyMessage = """╔═══════════════
║┏━━ೋ• ❄ •ೋ━━━┓
║ ❁ 🛡  кєи кαиєкι! ＢＯＴ  🛡 ❁    
║┗━━ೋ• ❄ •ೋ━━━┛
╠═══════════════
║「ĸeyword」
╠═══════════════
║╔❂͜͡➣「/ѕιderѕ」
║╠❂͜͡➣「/pυвlιc」
║╠❂͜͡➣「/ѕearcнιng」
║╠❂͜͡➣「/newғιтυre」
║╠❂͜͡➣「/cancel」
║╠❂͜͡➣「/aвoυт」
║╚❂͜͡➣「/ĸelυar」
╚═══════════════ """

newMessage ="""⚘ 🐯 new fiture area 🐯 ⚚
❂͜͡☆➣ https://tinyurl.com/newfiture (cek disini)
❂͜͡☆➣ https://tinyurl.com/newfiture2 (cek disini)
❂͜͡☆➣ cυaca「naмa ĸoтa」= cek cuaca kota
❂͜͡☆➣ ѕнolaт「naмa ĸoтa」= cek jadwal sholat di kota
❂͜͡☆➣ cpoѕт 「υѕernaмe ιg ĸaмυ」= untuk cek post terakhir mu yang berupa foto
❂͜͡☆➣ cvιd「υѕernaмe ιg ĸaмυ」= untuk cek post terakhir mu yang berupa video
❂͜͡☆➣ ѕcreen 「υѕernaмe ιg ĸaмυ」= untuk screenshoot ig kamu
❂͜͡☆➣ loĸaѕι「yang ιngιn ĸaмυ carι」= υnтυĸ мencarι loĸaѕι
❂͜͡☆➣ /lιrιĸ「jυdυl lagυ」= υnтυĸ мencarι lιrιĸ lagυ
❂͜͡☆➣ /lagυ「jυdυl lagυ」= untuk mencari lagu joox
❂͜͡☆➣ ιnғo ѕaya = вυaт lυcυ lυcυ an

ada ιngιn мenyaranĸan ғιтυre? cнaт ĸe http://line.me/ti/p/%40ish7215m"""

sidersMessage =""" 🛡  кєи кαиєкι v2! ＢＯＴ  🛡

⚘ 🐯 cнecĸ ѕιderѕ area 🐯 ⚚
❂͜͡☆➣ ѕeтlaѕтpoιnт = cнecĸ ѕιderѕ
❂͜͡☆➣ vιewlaѕтѕeen = cнecĸ ѕιderѕ
❂͜͡☆➣ ѕeтpoιnт = cнecĸ ѕιderѕ
❂͜͡☆➣ read = cнecĸ ѕιderѕ"""

publicMessage =""" ⚘ 🐯 pυвlιc area 🐯 ⚚
❂͜͡☆➣ creaтor = conтacт peмвυaт вoт
❂͜͡☆➣ apaĸaн 「тeхт yang ιngιn ĸaмυ тanyaĸan」 (ѕeperтι ĸerang ajaιв)
❂͜͡☆➣ ĸedapĸedιp「тeхт yang ιngιn dιĸedap ĸedιpĸan」 = coвa aja
❂͜͡☆➣ doѕa @「naмe」 = вυaт lυcυ2an
❂͜͡☆➣ paнala @「naмe」 = вυaт lυcυ2an
❂͜͡☆➣ gcreaтor = мenυnjυĸĸan peмвυaт grυp
❂͜͡☆➣ gιnғo = ιnғo grυp
❂͜͡☆➣ ѕpaмтag @ 「naмe」= ѕpaм yang dιтag
❂͜͡☆➣ /ѕpaм: on/oғғ + jυмlaн + ĸaтa = ѕpaм dengan jυмlaн ĸaтa
❂͜͡☆➣ мenтιon all = мenтιon ѕeмυa
❂͜͡☆➣ мenтιon = мenтιon ѕeмυa
❂͜͡☆➣ тag all = мenтιon ѕeмυa
❂͜͡☆➣ тagall = мenтιon ѕeмυa
❂͜͡☆➣ ѕay = coвa aja ĸeтιĸ ѕay"""

searchingMessage =""" ⚘ 🐯 ѕearcнιng area 🐯 ⚚
❂͜͡☆➣ proғιleιg 「υѕernaмe」
❂͜͡☆➣ ιnѕтagraм 「υѕernaмe」
❂͜͡☆➣ .ιnѕтagraм 「υѕernaмe」
❂͜͡☆➣ wιĸιpedιa 「тeхт」
❂͜͡☆➣ gιмage「тeхт」
❂͜͡☆➣ тr-en 「тeхт」
❂͜͡☆➣ тr-ιd 「тeхт」
❂͜͡☆➣ ιd@en
❂͜͡☆➣ en@ιd
❂͜͡☆➣ ιd@jp
❂͜͡☆➣ jp@ιd
❂͜͡☆➣ ιd@тн
❂͜͡☆➣ тн@ιd
❂͜͡☆➣ ιd@jp
❂͜͡☆➣ ιd@ar
❂͜͡☆➣ ar@ιd
❂͜͡☆➣ ιd@ĸo
❂͜͡☆➣ ĸo@ιd
❂͜͡☆➣ yт: [jυdυl]
❂͜͡☆➣ ceĸ (тanggal)-(вυlan)-(тaнυn)
❂͜͡☆➣ /ιg 「υѕernaмe」
❂͜͡☆➣ ѕearcнιd: 「ιd lιne」"""

cancelMessage ="""ғιтυr вerѕтaтυѕ oғғlιne!"""

welcomeMessage="""тerιмa ĸaѕιн тelaн мengυndang вoт ιnι! 
ιnvιтe aĸυ ĸe grυp ĸalιan ya :)
⭐ υnтυĸ мengeтaнυι adмιn ĸeтιĸ "creaтor"!
⭐ υnтυĸ мengeтaнυι ғιтυre apa ѕaja darι вoт ιnι ĸeтιĸ "нelp"
⭐ υnтυĸ вoт вeĸerja ѕecara мaхιмal ѕιlaнĸan ιnvιтe creaтor вoт! тнanĸyoυ!❤
"""

meMessage="""⭐ нow тo υѕe ιт::
- !say 「тeхт」
- @say 「тeхт」
- #say 「тeхт」
- $say 「тeхт」
- %say 「тeхт」
- ^say 「тeхт」
- &say 「тeхт」
- *say 「тeхт」
- (say 「тeхт」
- )say 「тeхт」
"""

sayMessage ="""⭐ Kode Baнaѕa ⭐
aғ : Aғrιĸaanѕ
ѕq : Alвanιan
ar : Araвιc
нy : Arмenιan
zн : Cнιneѕe
nl : Dυтcн
ғr : Frencн
de : Gerмan
en : Englιѕн
ιd : Indoneѕιan
ja : Japaneѕe
ĸo : Korean
ιт : Iтalιan
la : Laтιn
pт : Porтυgυeѕe
ro : Roмanιan
rυ : Rυѕѕιan
eѕ : Spanιѕн
тн : Tнaι
vι : Vιeтnaмeѕe
ѕυ : ѕυи∂α 
נω : נαωα
⭐ Tнanĸ Yoυ ⭐
"""

mulai = time.time()
KAC=[client]
mid = client.getProfile().mid

Bots=[mid]
admin=["ub8530f15ff4020c3cc2d1ad2f066aa4b","u5601bdfbc2c67e7adcb95f790127b193"]
owner=["ub8530f15ff4020c3cc2d1ad2f066aa4b","u5601bdfbc2c67e7adcb95f790127b193"]
protectname=[]

wait = {
    'contact':False,
    'autoJoin':True,
    'sticker':False,
    'autoCancel':{"on":True,"members":10},
    "spam":{},
    "detectMention":False,
    "Members":1,
    "wordban":{},
    'leaveRoom':True,
    'likeOn':True,
    'comment1':"Auto Like By http://line.me/ti/p/%40ish7215m",
    'timeline':True,
    'autoAdd':True,
    'atjointicket':True,
    "alwaysRead":True,
    "linkticket":False,
    "cpp":False,
    "cpg":False,
    'message':"тнαикѕ fσя α∂∂ мє! му ¢яєαтσя ιѕ http://line.me/ti/p/%40ish7215m",
    "lang":"JP",
    "comment":"тнαикѕ fσя α∂∂ мє! му ¢яєαтσя ιѕ http://line.me/ti/p/%40ish7215m",
    "commenty":"Auto Like by кєи кαиєкι\n\nhttp://line.me/ti/p/%40ish7215m",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":" ",
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "teman":{},
    "winvite":False,
    "likeOn":True,
    "protection":False,
    "welcomemsg":True,
    "welmsg":" welcome to ",
    "pname":{},
    "pro_name":{},
    "Pap":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

settings = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "timeRestart": "18000",
    "simiSimi":{},
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    
   
hasil = {
    "result":False,
    "posts":False,
    "postInfo":False,
    "liked":{}
    }
    
wordban = {
    "kontol":{},
    "kontl":{},
    "kntl":{},
    "memek":{},
    "anjing":{},
    "njing":{},
    "anjeng":{}
}

setTime = {}
setTime = wait2['setTime']

contact = client.getProfile()
backup = client.getProfile()
profile = client.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendKontok(self, HelloWorld, midUrang):
      msg = Message()
      msg.contentMetadata = {'mid': midUrang}
      msg.to = HelloWorld
      msg.contentType = 13
      return self.Talk.client.sendMessage(0, msg)
    
def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    
def NOTIFIED_READ_MESSAGE(op):
   # print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = client.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print "[Command] Tag All"
    try:
       client.sendMessage(msg)
    except Exception as error:
       pass
   #    print error

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        msg = Message()
        msg.contentType = 0
        msg.text = text_
        msg.contentMetada = {'MENTION':'{"MENTIONEES":['+aa+']}'}
        client.sendMessage(msg)
    except Exception as error:
        pass
        
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print "[Command] Tag All"
    try:
       client.sendMessage(msg)
    except Exception as error:
       pass

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "• @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         client.sendMessage(msg)
    except Exception as error:
        pass

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def yt(query):
    with requests.session() as s:
        isi = []
        if query == "":
            query = "S1B nrik"
        s.headers['user-agent'] = 'Mozilla/5.0'
                     
        url    = 'http://www.youtube.com/results'
        params = {'search_query': query}
                     
        r    = s.get(url, params=params)
        soup = BeautifulSoup(r.content, 'html5lib')
                     
        for a in soup.select('.yt-lockup-title > a[title]'):
            if '&List' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=','')
                    isi += ['youtu.be' + b]
        return isi

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

while True:
    try:
        ops=oepoll.singleTrace(count=50)
        if ops != None:
          for op in ops:
#=========================================================================================================================================#
            #if op.type in OpType._VALUES_TO_NAMES:
            #    print("[ {} ] {}".format(str(op.type), str(OpType._VALUES_TO_NAMES[op.type])))
#=========================================================================================================================================#
            if op.type == 5:
                if wait["autoAdd"] == True:
                    client.findAndAddContactsByMid(op.param1)
                    if (wait["message"] in [""," ","\n",None]):
                        pass
                    else:
                        client.sendMessage(op.param1,str(wait["message"]))
		
            if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        client.sendMessage(op.param1, "Haii " + "☞ " + nick[0] + " ☜" + "\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-)   ")
                                    else:
                                        client.sendMessage(op.param1, "Haii " + "☞ " + nick[1] + " ☜" + "\nBetah Banget Jadi Penonton. . .\nChat Napa (-__-)   ")
                                else:
                                    client.sendMessage(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja?\nSini Gabung Chat...   ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
	
            if op.type == 13:
                #print op.param1
                #print op.param2
                #print op.param3
                if mid in op.param3:
                    G = client.getGroup(op.param1)
                    if wait["autoJoin"] == True:
                        if wait["autoCancel"]["on"] == True:
                            if len(G.members) <= wait["autoCancel"]["members"]:
                                client.acceptGroupInvitation(op.param1)
                                Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                client.sendContact(op.param1, Oa)
                                sendMentionV2(op.param1,"мaaғ @! ! мeмвer anda вelυм мencυĸυpι😊 ѕιlaнĸan нυвυngι oa dιaтaѕ!", [op.param2])
                                client.leaveGroup(op.param1)
                            else:
                                client.acceptGroupInvitation(op.param1)
                                xname = client.getContact(op.param2).displayName
                                Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                client.sendContact(op.param1, Oa)
                                sendMentionV2(op.param1, "тerιмa ĸaѕιн @! тelaн мengυndang вoт ιnι!\n\nwajιв add oa dιaтaѕ! \nĸeтιĸ нelp υnтυĸ мelιнaт ғιтυre вoт ιnι!", [op.param2])                                                        
                        else:
                            client.acceptGroupInvitation(op.param1)
                            Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                            client.sendContact(op.param1, Oa)
                            client.sendMessage(op.param1, "wajιв add oa dιaтaѕ! \nĸeтιĸ нelp υnтυĸ мelιнaт ғιтυre вoт ιnι!")
                    elif wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            client.acceptGroupInvitation(op.param1)
                            Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                            client.sendContact(op.param1, Oa)
                            sendMentionV2(op.param1,"мaaғ @! ! мeмвer anda вelυм мencυĸυpι😊 ѕιlaнĸan нυвυngι oa dιaтaѕ!", [op.param2])
                            client.leaveGroup(op.param1)
                else:
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, InviterX)
                    if matched_list == []:
                        pass
                    else:
                        client.cancelGroupInvitation(op.param1, matched_list)

            if op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            client.sendChatChecked(receiver, msg_id)
                            contact = client.getContact(sender)
                            if text.lower() == 'me':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() == 'speed':
                                start = time.time()
                                client.sendMessage(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                client.sendMessage(receiver, "%sdetik" % (elapsed_time))
                            elif '/curidp' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    if client.getContact(u).videoProfile != None:
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
                            elif '/curicover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getProfileCoverURL(mid=u)
                                    client.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    client.sendMessage(receiver, str(e))
                            elif text.lower() == 'mention':
                                group = client.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//100
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*100 : (a+1)*100]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Alin \n'
                                    client.sendMessage(receiver, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    client.sendMessage(receiver, "Total {} Mention".format(str(len(nama))))    
					
                            elif text.lower() == 'tag all':
                                group = client.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//100
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*100 : (a+1)*100]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Alin \n'
                                    client.sendMessage(receiver, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    client.sendMessage(receiver, "Total {} Mention".format(str(len(nama))))    
					
                            elif text.lower() == "oa": 
                              if msg._from in admin:
                                Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                client.sendContact(msg.to, Oa)
				
                            elif "Ayat:" in msg.text:
                              try:
                                 sep = text.split(" ")
                                 ayat = text.replace(sep[0] + " ","")
                                 path = "http://islamcdn.com/quran/media/audio/ayah/ar.alafasy/" + ayat
                                 sendMentionV2(msg.to, "@! ini ayat yang kamu cari..", [sender])
                                 client.sendAudioWithURL(msg.to, path)
                              except Exception as error:
                                 client.sendMessage(msg.to, str(error))
					
                            elif "Jadwal: " in msg.text:
                                    try:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.replace("Jadwal: "+txt[1]+" ","")
                                        response = requests.get("https://farzain.xyz/api/premium/acaratv.php?apikey=kanekipubot&id="+txt[1]+"")
                                        data = response.json()
                                        pictig = str(data['status'])
                                        hasil = str(data['url'])
                                        text = "Status : "+pictig+"\n"+hasil+""
                                        client.sendMessage(msg.to, text)
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))
   
                            elif "Call: " in msg.text:
                                no = msg.text.replace("Call: ","")
                                r = requests.get("http://apisora.herokuapp.com/prank/call/?no="+str(no))
                                data = r.json()
                                result = data["result"].replace('</br>', '\n')
                                tgb = "[ Prank Call ]\n\n"
                                tgb += "Status: "+str(data["status"])+"\n"
                                tgb += "Result "+str(result)+"\n\n[ Finish ]"
                                client.sendMessage(msg.to,str(tgb))
                                Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                client.sendContact(msg.to, Oa)
		
                            elif "Sms: " in msg.text:
                                    try:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.replace("Sms: "+txt[1]+" ","")
                                        response = requests.get("http://leert.corrykalam.gq/sms.php?no="+txt[1]+"&text="+teks+"")
                                        data = response.json()
                                        pictig = str(data['status'])
                                        hasil = str(data['detail'])
                                        text = "Status : "+pictig+"\n\n"+hasil+""
                                        client.sendMessage(msg.to, text)
                                        Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                        client.sendContact(msg.to, Oa)
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))
           
                            elif msg.text in ["Result"]:
                                    mE = client.getProfile()
                                    gT = client.getGroupIdsJoined()
                                    fT = client.getAllContactIds()
                                    ginv = client.getGroupIdsInvited()
                                    client.sendMessage(msg.to,"「"+mE.displayName+"」 \n\nGroup total : " + str(len(gT))+ "\nFriend total: " +str(len(fT))+ "\nPending Group: " + str(len(ginv)))       
                    
                            elif "detectout" in msg.text:
                               if msg._from in admin:
                                groups = client.getGroupIdsJoined()
                                for group in groups:               	
                                    G = client.getGroup(group)
                                    if len(G.members) <= wait["autoCancel"]["members"]:
                                        Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                        owner = 'u5601bdfbc2c67e7adcb95f790127b193'
                                        client.sendContact(group, Oa)
                                        client.sendMessage(group,"мaaғ! мeмвer anda вelυм мencυĸυpι😊 ѕιlaнĸan нυвυngι oa dιaтaѕ!")
                                        client.leaveGroup(group)
					
                            elif "meme: " in msg.text.lower():
                                    try:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.lower().replace("meme: "+txt[1]+" ","")
                                        data = []
                                        r = requests.get("http://ofckaneki.dynu.net/bot.php")
                                        r = eval(r.text)
                                        for a in r:
                                            data.append(a)
                                        c = random.choice(data)
                                        foto = "https://memegen.link/"+c+"/"+txt[1]+"/"+teks+".jpg"
                                        client.sendImageWithURL(msg.to, foto)
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))
			
                            elif "Retro: " in msg.text:
                                    try:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.replace("Retro: "+txt[1]+" ","")
                                        satu = ["1","2","3","4","5"]
                                        dua = ["1","2","3","4"]
                                        k = random.choice(satu)
                                        w = random.choice(dua)
                                        response = requests.get("http://leert.corrykalam.gq/retrowave.php?text1="+txt[1]+"&text2="+teks+"&text3=&btype="+k+"&ttype="+w+"")
                                        data = response.json()
                                        hasil = str(data['image'])
                                        download = str(data['image'])                      
                                        client.sendMessage(receiver, download)
                                        client.sendImageWithURL(receiver, hasil)
                                        Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                        client.sendContact(receiver, Oa)
                                    except Exception as e:
                                        client.sendMessage(receiver, str(e))
			
                            elif "Pcid: " in msg.text:
                                txt = msg.text.split(" ")
                                teks = msg.text.replace("Pcid: "+txt[1]+" ","")
                                x = client.findContactsByUserid(txt[1])
                                a = client.getContact(msg._from)
                                sendMentionV2(x.mid,"Anda mendapatkan pesan dari @!\n\n "+teks+"", [a.mid])
                                sendMentionV2(msg.to,"Sukses mengirim pesan ke @!\nDari: "+a.displayName+"\nPesan: "+teks+"", [x.mid])
                                Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                client.sendContact(msg.to, Oa)

                            elif "Gbcon: " in msg.text:
                              if msg._from in admin:
                                n = client.getGroupIdsJoined()   
                                y = msg.text.split(" ")
                                k = msg.text.replace("Gbcon: "+y[1]+" ","")
                                Oa = y[1]
                                for people in n:                	
                                	client.sendContact(people, Oa)

                            elif "Fs: " in msg.text:
                                    try:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.replace("Fs: "+txt[1]+" ","")
                                        response = requests.get("https://farzain.com/api/premium/fs.php?apikey=kanekipubot&id="+txt[1]+"")
                                        data = response.json()
                                        pictig = str(data['status'])
                                        hasil = str(data['url'])
                                        text = "Status : "+pictig+""
                                        client.sendMessage(msg.to, text)
                                        client.sendImageWithURL(msg.to, hasil)
                                        Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                        client.sendContact(msg.to, Oa)
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))

                            elif msg.text in ["Gcreator"]:
                              if msg.toType == 2:
                                    msg.contentType = 13
                                    ginfo = client.getGroup(msg.to)
                                    gCreator = ginfo.creator.mid
                                    try:
                                        msg.contentMetadata = {'mid': gCreator}
                                        gCreator1 = ginfo.creator.displayName
                        
                                    except:
                                        gCreator = "Error"
                                    client.sendMessage(msg.to, "Group Creator : " + gCreator1)
                                    client.sendContact(msg.to, gCreator)

                            elif "Gimage " in msg.text:
                                      googl = msg.text.replace("Gimage ","")
                                      url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + googl
                                      raw_html = (download_page(url))
                                      items = []
                                      items = items + (_images_get_all_items(raw_html))
                                      path = random.choice(items)
                                      try:
                                          start = time.time()
                                          client.sendImageWithURL(msg.to,random.choice(items))
                                          client.sendImageWithURL(msg.to,random.choice(items))
                                          client.sendImageWithURL(msg.to,random.choice(items))
                                          client.sendMessage(msg.to,"Total Image Links ="+str(len(items)))
                                      except Exception as njer:
                                            client.sendMessage(msg.to, str(njer))
				
                            elif "Info saya" in msg.text:
                              kelamin = ("Waria","Laki-laki","Perempuan","Tidak Diketahui","Bencong")
                              wajah = ("Standar","Ganteng","Cantik","Beruk","Hancur")
                              status = ("Menikah","Pacaran","Jones")
                              k = random.choice(kelamin)
                              w = random.choice(wajah)
                              s = random.choice(status)
                              client.sendMessage(msg.to,"• Nama : "+client.getContact(msg._from).displayName+"\n• Kelamin : "+k+"\n• Wajah : "+w+"\n• Status Kehidupan : "+s)
#-------------Fungsi Pap-----------------------------#
                            elif "!say " in msg.text.lower():
                                    query = msg.text.replace("!say ","")
                                    with requests.session() as s:
                                        s.headers['user-agent'] = 'Mozilla/5.0'
                                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                                        params = {'language': 'af', 'speed': '1', 'query': query}
                                        r = s.get(url, params=params)
                                        mp3 = r.url
                                        client.sendAudioWithURL(msg.to, mp3)

                            elif "Surat:" in msg.text.lower():
                               try:
                                  sep = msg.text.split(" ")
                                  surah = int(text.lower().replace(sep[0] + " ",""))
                                  if 0 < surah < 115:
                                      if surah not in [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 16, 17, 18, 20, 21, 23, 26, 37]:
                                          if len(str(surah)) == 1:
                                              audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-00" + str(surah) + "-muslimcentral.com.mp3"
                                              sendMentionV2(msg.to, "@! ini surat yang kamu minta..", [msg._from])
                                              client.sendAudioWithURL(msg.to, audionya)
                                          elif len(str(surah)) == 2:
                                              audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-0" + str(surah) + "-muslimcentral.com.mp3"
                                              sendMentionV2(msg.to, "@! ini surat yang kamu minta..", [msg._from])
                                              client.sendAudioWithURL(msg.to, audionya)
                                          else:
                                              audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-" + str(surah) + "-muslimcentral.com.mp3"
                                              sendMentionV2(msg.to, "@! ini surat yang kamu minta..", [msg._from])
                                              client.sendAudioWithURL(msg.to, audionya)
                                      else:
                                          sendMentionV2(msg.to, "@! Surah yang kamu minta terlalu panjang", [msg._from])
                                  else:
                                      sendMentionV2(msg.to, "@! Quran hanya 114 surah", [msg._from])
                               except Exception as error:
                                   client.sendMessage(msg.to, "error\n"+str(error))

                            elif "neon: " in msg.text.lower():
                                    try:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.lower().replace("neon: ","")
                                        color = ["red","yellow","green","purple","violet","blue"]
                                        k = random.choice(color)
                                        foto = "https://ari-api.herokuapp.com/neon?text="+teks+"&color="+k+""
                                        sendMentionV2(msg.to, "@! ini foto neon pesanan kamu..", [msg._from])
                                        client.sendImageWithURL(msg.to, foto)
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))

                            elif msg.text in ["restart"]:
                                        if msg._from in admin:
                                            client.sendMessage(msg.to, "Tunggu Sebentar..")
                                            client.sendMessage(msg.to, "Bot has been restarted")
                                            restart_program()
                                        else:
                                            client.sendMessage(msg.to, "No Access")
			
                            elif "Cek " in msg.text:
                                tanggal = msg.text.replace("Cek ","")
                                r=requests.get('http://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                lahir = data["data"]["lahir"]
                                usia = data["data"]["usia"]
                                ultah = data["data"]["ultah"]
                                zodiak = data["data"]["zodiak"]
                                client.sendMessage(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
                
                            elif "Pict group " in msg.text:
                                saya = msg.text.replace('Pict group ','')
                                gid = client.getGroupIdsJoined()
                                for i in gid:
                                    h = client.getGroup(i).name
                                    gna = client.getGroup(i)
                                    if h == saya:
                                        client.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
                        
#------------------------CHECK SYSTEM------------------------#    
                         
                            elif msg.text.lower().startswith("story "):
                                            sep = msg.text.replace("story ","")
                                            url = "http://rahandiapi.herokuapp.com/instastory/"+sep+"?key=betakey"
                                            with requests.session() as web:
                                                web.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                r = web.get(url)
                                                data = r.text
                                                data = json.loads(data)
                                                if data["url"] != []:
                                                    items = data["url"]["link"]
                                                    client.sendImageWithURL(msg.to, items)
                                    
                            elif msg.text.lower().startswith("sholat "):
                                location = msg.text.replace("sholat ","")
                                params = {'lokasi':location}
                                with requests.session() as web:
                                    r = requests.get("http://api.corrykalam.net/apisholat.php?" + urllib.urlencode(params))                      
                                    data = r.text
                                    data = json.loads(data)
                                    if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashr : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                        ret_ = "[ Prayer Schedule ]"
                                        ret_ += "\n\nLocation : " + data[0]
                                        ret_ += "\n" + data[1]
                                        ret_ += "\n" + data[2]
                                        ret_ += "\n" + data[3]               
                                        ret_ += "\n" + data[4]
                                        ret_ += "\n" + data[5]
                                    else:
                                           ret_ = "[ Prayer Schedule ] Error : Location not found" 
                                    client.sendMessage(msg.to, str(ret_))
            
                            elif msg.text.lower().startswith("lokasi "):
                                location = msg.text.lower().replace("lokasi ","")
                                params = {'lokasi':location}
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    r = requests.get("http://api.corrykalam.net/apiloc.php?"+ urllib.urlencode(params))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "[ Details Location ]"
                                        ret_ += "\n\nLocation : " + data[0]
                                        ret_ += "\nGoogle Maps : " + link
                                    else:
                                           ret_ = "[ Details Location ] Error : Location not found"
                                    client.sendMessage(msg.to, str(ret_))
            
                            elif msg.text.lower().startswith("twitter "):               
                                       user = msg.text.lower().replace("twitter ","")
                                       with requests.session() as s: 
                                            s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0' 
                                            url    = 'https://twitter.com/'+user
                                            r    = s.get(url)
                                            soup = BeautifulSoup(r.content, 'html5lib')
                                            hasil = soup.select_one('.ProfileHeaderCard')
                                            hasil = hasil.findAll(msg.text)
                                            tweet = soup.find('span', class_ = 'ProfileNav-value').get_text()
                                            fllwng = soup.find('li', class_ = 'ProfileNav-item ProfileNav-item--following').get_text()
                                            fllwr = soup.find('li', class_ = 'ProfileNav-item ProfileNav-item--followers').get_text()
                                            fav = soup.find('li', class_ = 'ProfileNav-item ProfileNav-item--favorites').get_text()
                                            img = soup.find('img', class_ = 'ProfileAvatar-image')
                                            client.sendImageWithURL(msg.to,img['src'])
                                            client.sendMessage(msg.to,'Name: '+hasil[2]+'\nUsername: '+hasil[7]+hasil[8]+'\nBio: '+hasil[12]+hasil[13]+' '+hasil[15]+hasil[16]+'\nLoc: '+hasil[20]+'\nWeb: '+hasil[26]+'\nJoined: '+hasil[32]+'\nBorn: '+hasil[37])
                                            client.sendMessage(msg.to,'Tweets: '+tweet+'\nFollowing: '+fllwng.replace('Following','')+'\nFollowers: '+fllwr.replace('Followers','')+'\nLikes:'+fav.replace('Likes',''))
                            
                            elif msg.text.lower().startswith("image "):
                                            sep = msg.text.replace("image ","")
                                            url = "http://rahandiapi.herokuapp.com/imageapi?key=betakey&q="+sep+""
                                            with requests.session() as web:
                                                web.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                r = web.get(url)
                                                data = r.text
                                                data = json.loads(data)
                                                if data["result"] != []:
                                                    items = data["result"]
                                                    path = random.choice(items)
                                                    a = items.index(path)
                                                    b = len(items)
                                                    client.sendImageWithURL(msg.to, str(path))
        
                            elif msg.text.lower() == "cfotogroup":
                                if msg._from in admin:
                                  wait["cpg"] = True
                                  client.sendMessage(msg.to,"please send an image for group profile.")
                                else:
                                	 client.sendMessage(msg.to,"command denied")
                                	 client.sendMessage(msg.to,"creator permission recuired")
					
                            elif msg.text.lower() == "changepict":
                                if msg._from in admin:
                                   wait["cpp"] = True
                                   client.sendMessage(msg.to,"please send an image")
                                else:
                                	 client.sendMessage(msg.to,"command denied")
                                	 client.sendMessage(msg.to,"creator permission recuired")
			
                            elif 'ytmp3: ' in text:
                               url_= text.replace('ytmp3: ','')
                               params = {'key':'betakey','q':url_}
                               path = 'http://rahandiapi.herokuapp.com/youtubeapi?'
                               r = requests.get(path,params=params).json()
                               client.sendMessage(msg.to, r['result']['audiolist'][4]['url'])

                            elif "/lirik " in msg.text:
                                    try:
                                        instagram = msg.text.replace("/lirik ","")
                                        response = requests.get("http://rahandiapi.herokuapp.com/lyricapi?key=betakey&q="+instagram+"")
                                        data = response.json()
                                        pictig = str(data['title'])
                                        hasil = str(data['lyric'])
                                        text = "Judul : "+pictig+"\n\n"+hasil+""
                                        client.sendMessage(msg.to, text)
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))
           
                            elif "Screen " in msg.text:
                                    try:
                                        instagram = msg.text.replace("Screen ","")
                                        response = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link=www.instagram.com/"+instagram+"")
                                        data = response.json()
                                        pictig = data['result']
                                        client.sendImageWithURL(msg.to, pictig)
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))

                            elif "/ti/g/" in msg.text.lower():
                                  if wait["atjointicket"] == True:
                                      link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                      links = link_re.findall(text)
                                      n_links = []
                                      for l in links:
                                          if l not in n_links:
                                              n_links.append(l)
                                      for ticket_id in n_links:
                                          group = client.findGroupByTicket(ticket_id)
                                          client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                          client.sendMessage(msg.to, "Berhasil masuk ke group %s" % str(group.name))
                                              
                            elif msg.text.lower().startswith("cuaca "):
                                location = msg.text.lower().replace("cuaca ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib2.quote(location)))
                                    data = r.text
                                    data = json.loads(data)
                                    if "result" not in data:
                                        ret_ = "╔══『 Status Cuaca 』"
                                        ret_ += "\n╠ ⌬.「 Lokasi 」 : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\n╠ ⌬.「 Suhu 」 : " + data[1].replace("Suhu : ","")
                                        ret_ += "\n╠ ⌬.「 Kelembaban 」: " + data[2].replace("Kelembaban : ","")
                                        ret_ += "\n╠ ⌬.「 Tekanan Udara 」 : " + data[3].replace("Tekanan udara : ","")
                                        ret_ += "\n╠ ⌬.「 Kecepatan Angin」 : " + data[4].replace("Kecepatan angin : ","")
                                        ret_ += "\n╚══『 Status Cuaca 』"
                                    else:
                                        ret_ = "[ Weather Status ] Error : Lokasi tidak ditemukan"
                                    client.sendMessage(msg.to, str(ret_))
				
                            elif text.lower() == 'tagall':
                                group = client.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//100
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*100 : (a+1)*100]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Alin \n'
                                    client.sendMessage(receiver, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    client.sendMessage(receiver, "Total {} Mention".format(str(len(nama))))      
		           
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
	
#=================================================================================================================#
            if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        sendMentionV2(op.param1, "Haii ☞ @! ☜\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-)", [op.param2])
                                    else:
                                        sendMentionV2(op.param1, "Haii ☞ @! ☜\nBetah Banget Jadi Penonton. . .\nChat Napa (-__-)", [op.param2])
                                else:
                                    sendMentionV2(op.param1, "Haii ☞ @! ☜\nNgapain Kak Ngintip Aja?\nSini Gabung Chat...", [op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
 
            if op.type == 55:
                try:
                    if op.param1 in wait2['readPoint']:
                        Name = client.getContact(op.param2).displayName
                        if Name in wait2['readMember'][op.param1]:
                            pass
                        else:
                            wait2['readMember'][op.param1] += "\n・ " + Name + datetime.today().strftime(' [%d - %H:%M:%S]')
                            wait2['ROM'][op.param1][op.param2] = "・ " + Name
                            wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    else:
                        pass
                except:
                    pass
		
            if op.type == 17:
                    if wait["welcomemsg"] == True:
                       if op.param2 not in Bots:
                             ginfo = client.getGroup(op.param1)
                             client.sendContact(op.param1, op.param2)
                             sendMentionV2(op.param1,"Hallo @! \nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini (ﾉ*>∀<)ﾉ♡", [op.param2])  
			
            if op.type == 24:
                if wait["leaveRoom"] == True:
                    client.leaveRoom(op.param1)
        
            if op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.contentType == 13:
                   if wait["wblack"] == True:
                        if msg.contentMetadata["mid"] in wait["commentBlack"]:
                            client.sendMessage(msg.to,"already")
                            wait["wblack"] = False
                        else:
                            wait["commentBlack"][msg.contentMetadata["mid"]] = True
                            wait["wblack"] = False
                            client.sendMessage(msg.to,"decided not to comment")
                              
                   elif wait["dblack"] == True:
                       if msg.contentMetadata["mid"] in wait["commentBlack"]:
                            del wait["commentBlack"][msg.contentMetadata["mid"]]
                            client.sendMessage(msg.to,"deleted")
                            wait["dblack"] = False

                       else:
                            wait["dblack"] = False
                            client.sendMessage(msg.to,"It is not in the black list")
                        
                   elif wait["wblacklist"] == True:
                       if msg.contentMetadata["mid"] in wait["blacklist"]:
                            client.sendMessage(msg.to,"already")
                            client.sendMessage(msg.to,"already")
                            wait["wblacklist"] = False
                       else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            client.sendMessage(msg.to,"aded")

                   elif wait["dblacklist"] == True:
                       if msg.contentMetadata["mid"] in wait["blacklist"]:
                            del wait["blacklist"][msg.contentMetadata["mid"]]
                            client.sendMessage(msg.to,"deleted")
                            wait["dblacklist"] = False

                       else:
                            wait["dblacklist"] = False
                            client.sendMessage(msg.to,"It is not in the black list")
                        
                   elif wait["contact"] == True:
                        msg.contentType = 0
                        client.sendMessage(msg.to,msg.contentMetadata["mid"])
                        if 'displayName' in msg.contentMetadata:
                            contact = client.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = client.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            client.sendMessage(msg.to,"⎈ Profile Name :\n" + msg.contentMetadata["displayName"] + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Message :\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu))
                        else:
                            contact = client.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = client.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            client.sendMessage(msg.to,"⎈ Profile Name :\n" + msg.contentMetadata["displayName"] + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Message :\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu))
                        
                elif msg.contentType == 7:
                    if wait['sticker'] == True:
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                        client.sendMessage(msg.to, filler)
                    else:
                        pass
                    
                elif msg.contentType == 1:
                    if msg._from in admin:
                         if msg.toType == 2:
                                if wait["cpg"] == True:
                                    path = client.downloadObjectMsgId(msg.id)
                                    wait["cpg"] = False
                                    client.updateGroupPicture(msg.to, path)
                                    client.sendMessage(msg.to,"Foto grup telah di perbaharui !")
                                if wait["cpp"] == True:
                                    path = client.downloadObjectMsgId(msg.id)
                                    wait["cpp"] = False
                                    client.updateProfilePicture(path)
                                    client.sendMessage(msg.to, "success change profile picture")
            
			
#-----------INFO GROUP CREATOR---------------#
                elif msg.text in ["Accept invite"]:
                    if msg._from in admin:
                        gid = client.getGroupIdsInvited()
                        _list = ""
                        for i in gid:
                            if i is not None:
                                gids = client.getGroup(i)
                                _list += gids.name
                                client.acceptGroupInvitation(i)
                            else:
                                break
                        if gid is not None:
                            client.sendMessage(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                        else:
                            client.sendMessage(msg.to,"Tidak ada grup yang tertunda saat ini")
			
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            oepoll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
        
# Add function to OEPoll
oepoll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE
})

while True:
    oepoll.trace()
