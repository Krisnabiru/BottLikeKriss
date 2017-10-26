# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(qr=True)
#cl.login(token="authtoken-ente")
cl.loginResult()

ki = kk = kc = cl 

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=[""]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

#---------------------------[AutoLike-nya]---------------------------#
#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
def autolike():#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
     for zx in range(0,100):#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
        hasil = cl.activity(limit=100)#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
          try:    #Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Autolike By Farzain - zFz\n\nSubscribe Channel Saya yak kalau mau bisa kayak gini\nhttps://youtube.com/c/zfz48")#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
            print "Like"#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
          except:#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
            pass#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
        else:#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
            print "Already Liked"#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
     time.sleep(500)#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
thread2 = threading.Thread(target=autolike)#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
thread2.daemon = True#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
thread2.start()#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
#Tolong Kerjasama-nya untuk tidak merubah komen secara keseluruhan terutama pada URL Channel Youtube Saya, kalau mau ditambah dikit silahkan
#---------------------------[AutoLike-nya]---------------------------#

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

#-------------------------[Jangan Dihapus]------------------------#

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
            
#-------------------------[Jangan Dihapus]------------------------#            
