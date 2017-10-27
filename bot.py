# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,base64

cl = LINETCR.LINE()
cl.login(qr=True)
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
farzain = "I1RvbG9uZyBLZXJqYXNhbWEtbnlhIHVudHVrIHRpZGFrIG1lcnViYWgga29tZW4gc2VjYXJhIGtlc2VsdXJ1aGFuIHRlcnV0YW1hIHBhZGEgVVJMIENoYW5uZWwgWW91dHViZSBTYXlhLCBrYWxhdSBtYXUgZGl0YW1iYWggZGlraXQgc2lsYWhrYW4KZGVmIGF1dG9saWtlKCk6I1RvbG9uZyBLZXJqYXNhbWEtbnlhIHVudHVrIHRpZGFrIG1lcnViYWgga29tZW4gc2VjYXJhIGtlc2VsdXJ1aGFuIHRlcnV0YW1hIHBhZGEgVVJMIENoYW5uZWwgWW91dHViZSBTYXlhLCBrYWxhdSBtYXUgZGl0YW1iYWggZGlraXQgc2lsYWhrYW4KICAgICBmb3IgenggaW4gcmFuZ2UoMCwxMDApOiNUb2xvbmcgS2VyamFzYW1hLW55YSB1bnR1ayB0aWRhayBtZXJ1YmFoIGtvbWVuIHNlY2FyYSBrZXNlbHVydWhhbiB0ZXJ1dGFtYSBwYWRhIFVSTCBDaGFubmVsIFlvdXR1YmUgU2F5YSwga2FsYXUgbWF1IGRpdGFtYmFoIGRpa2l0IHNpbGFoa2FuCiAgICAgICAgaGFzaWwgPSBjbC5hY3Rpdml0eShsaW1pdD0xMDApI1RvbG9uZyBLZXJqYXNhbWEtbnlhIHVudHVrIHRpZGFrIG1lcnViYWgga29tZW4gc2VjYXJhIGtlc2VsdXJ1aGFuIHRlcnV0YW1hIHBhZGEgVVJMIENoYW5uZWwgWW91dHViZSBTYXlhLCBrYWxhdSBtYXUgZGl0YW1iYWggZGlraXQgc2lsYWhrYW4KICAgICAgICBpZiBoYXNpbFsncmVzdWx0J11bJ3Bvc3RzJ11benhdWydwb3N0SW5mbyddWydsaWtlZCddID09IEZhbHNlOiNUb2xvbmcgS2VyamFzYW1hLW55YSB1bnR1ayB0aWRhayBtZXJ1YmFoIGtvbWVuIHNlY2FyYSBrZXNlbHVydWhhbiB0ZXJ1dGFtYSBwYWRhIFVSTCBDaGFubmVsIFlvdXR1YmUgU2F5YSwga2FsYXUgbWF1IGRpdGFtYmFoIGRpa2l0IHNpbGFoa2FuCiAgICAgICAgICB0cnk6ICAgICNUb2xvbmcgS2VyamFzYW1hLW55YSB1bnR1ayB0aWRhayBtZXJ1YmFoIGtvbWVuIHNlY2FyYSBrZXNlbHVydWhhbiB0ZXJ1dGFtYSBwYWRhIFVSTCBDaGFubmVsIFlvdXR1YmUgU2F5YSwga2FsYXUgbWF1IGRpdGFtYmFoIGRpa2l0IHNpbGFoa2FuCiAgICAgICAgICAgIGNsLmxpa2UoaGFzaWxbJ3Jlc3VsdCddWydwb3N0cyddW3p4XVsndXNlckluZm8nXVsnbWlkJ10saGFzaWxbJ3Jlc3VsdCddWydwb3N0cyddW3p4XVsncG9zdEluZm8nXVsncG9zdElkJ10sbGlrZVR5cGU9MTAwMikjVG9sb25nIEtlcmphc2FtYS1ueWEgdW50dWsgdGlkYWsgbWVydWJhaCBrb21lbiBzZWNhcmEga2VzZWx1cnVoYW4gdGVydXRhbWEgcGFkYSBVUkwgQ2hhbm5lbCBZb3V0dWJlIFNheWEsIGthbGF1IG1hdSBkaXRhbWJhaCBkaWtpdCBzaWxhaGthbgogICAgICAgICAgICBjbC5jb21tZW50KGhhc2lsWydyZXN1bHQnXVsncG9zdHMnXVt6eF1bJ3VzZXJJbmZvJ11bJ21pZCddLGhhc2lsWydyZXN1bHQnXVsncG9zdHMnXVt6eF1bJ3Bvc3RJbmZvJ11bJ3Bvc3RJZCddLCJBdXRvbGlrZSBCeSBGYXJ6YWluIC0gekZ6XG5cblN1YnNjcmliZSBDaGFubmVsIFNheWEgeWFrIGthbGF1IG1hdSBiaXNhIGtheWFrIGdpbmlcbmh0dHBzOi8veW91dHViZS5jb20vYy96Zno0OCIpI1RvbG9uZyBLZXJqYXNhbWEtbnlhIHVudHVrIHRpZGFrIG1lcnViYWgga29tZW4gc2VjYXJhIGtlc2VsdXJ1aGFuIHRlcnV0YW1hIHBhZGEgVVJMIENoYW5uZWwgWW91dHViZSBTYXlhLCBrYWxhdSBtYXUgZGl0YW1iYWggZGlraXQgc2lsYWhrYW4KICAgICAgICAgICAgcHJpbnQgIkxpa2UiI1RvbG9uZyBLZXJqYXNhbWEtbnlhIHVudHVrIHRpZGFrIG1lcnViYWgga29tZW4gc2VjYXJhIGtlc2VsdXJ1aGFuIHRlcnV0YW1hIHBhZGEgVVJMIENoYW5uZWwgWW91dHViZSBTYXlhLCBrYWxhdSBtYXUgZGl0YW1iYWggZGlraXQgc2lsYWhrYW4KICAgICAgICAgIGV4Y2VwdDojVG9sb25nIEtlcmphc2FtYS1ueWEgdW50dWsgdGlkYWsgbWVydWJhaCBrb21lbiBzZWNhcmEga2VzZWx1cnVoYW4gdGVydXRhbWEgcGFkYSBVUkwgQ2hhbm5lbCBZb3V0dWJlIFNheWEsIGthbGF1IG1hdSBkaXRhbWJhaCBkaWtpdCBzaWxhaGthbgogICAgICAgICAgICBwYXNzI1RvbG9uZyBLZXJqYXNhbWEtbnlhIHVudHVrIHRpZGFrIG1lcnViYWgga29tZW4gc2VjYXJhIGtlc2VsdXJ1aGFuIHRlcnV0YW1hIHBhZGEgVVJMIENoYW5uZWwgWW91dHViZSBTYXlhLCBrYWxhdSBtYXUgZGl0YW1iYWggZGlraXQgc2lsYWhrYW4KICAgICAgICBlbHNlOiNUb2xvbmcgS2VyamFzYW1hLW55YSB1bnR1ayB0aWRhayBtZXJ1YmFoIGtvbWVuIHNlY2FyYSBrZXNlbHVydWhhbiB0ZXJ1dGFtYSBwYWRhIFVSTCBDaGFubmVsIFlvdXR1YmUgU2F5YSwga2FsYXUgbWF1IGRpdGFtYmFoIGRpa2l0IHNpbGFoa2FuCiAgICAgICAgICAgIHByaW50ICJBbHJlYWR5IExpa2VkIiNUb2xvbmcgS2VyamFzYW1hLW55YSB1bnR1ayB0aWRhayBtZXJ1YmFoIGtvbWVuIHNlY2FyYSBrZXNlbHVydWhhbiB0ZXJ1dGFtYSBwYWRhIFVSTCBDaGFubmVsIFlvdXR1YmUgU2F5YSwga2FsYXUgbWF1IGRpdGFtYmFoIGRpa2l0IHNpbGFoa2FuCiAgICAgdGltZS5zbGVlcCg1MDApI1RvbG9uZyBLZXJqYXNhbWEtbnlhIHVudHVrIHRpZGFrIG1lcnViYWgga29tZW4gc2VjYXJhIGtlc2VsdXJ1aGFuIHRlcnV0YW1hIHBhZGEgVVJMIENoYW5uZWwgWW91dHViZSBTYXlhLCBrYWxhdSBtYXUgZGl0YW1iYWggZGlraXQgc2lsYWhrYW4KdGhyZWFkMiA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWF1dG9saWtlKSNUb2xvbmcgS2VyamFzYW1hLW55YSB1bnR1ayB0aWRhayBtZXJ1YmFoIGtvbWVuIHNlY2FyYSBrZXNlbHVydWhhbiB0ZXJ1dGFtYSBwYWRhIFVSTCBDaGFubmVsIFlvdXR1YmUgU2F5YSwga2FsYXUgbWF1IGRpdGFtYmFoIGRpa2l0IHNpbGFoa2FuCnRocmVhZDIuZGFlbW9uID0gVHJ1ZSNUb2xvbmcgS2VyamFzYW1hLW55YSB1bnR1ayB0aWRhayBtZXJ1YmFoIGtvbWVuIHNlY2FyYSBrZXNlbHVydWhhbiB0ZXJ1dGFtYSBwYWRhIFVSTCBDaGFubmVsIFlvdXR1YmUgU2F5YSwga2FsYXUgbWF1IGRpdGFtYmFoIGRpa2l0IHNpbGFoa2FuCnRocmVhZDIuc3RhcnQoKSNUb2xvbmcgS2VyamFzYW1hLW55YSB1bnR1ayB0aWRhayBtZXJ1YmFoIGtvbWVuIHNlY2FyYSBrZXNlbHVydWhhbiB0ZXJ1dGFtYSBwYWRhIFVSTCBDaGFubmVsIFlvdXR1YmUgU2F5YSwga2FsYXUgbWF1IGRpdGFtYmFoIGRpa2l0IHNpbGFoa2FuCiNUb2xvbmcgS2VyamFzYW1hLW55YSB1bnR1ayB0aWRhayBtZXJ1YmFoIGtvbWVuIHNlY2FyYSBrZXNlbHVydWhhbiB0ZXJ1dGFtYSBwYWRhIFVSTCBDaGFubmVsIFlvdXR1YmUgU2F5YSwga2FsYXUgbWF1IGRpdGFtYmFoIGRpa2l0IHNpbGFoa2Fu"
exec(base64.b64decode(farzain))
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

#----------------------[Masukin Semua SC Yang Ente Pengen Disini]----------------------#
        if op.type == 25:
            msg = op.message
            if msg.text in ["Speed","speed"]:
                    start = time.time()
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
#----------------------[Masukin Semua SC Yang Ente Pengen Disini]----------------------#

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
