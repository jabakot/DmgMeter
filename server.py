#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import socket
UDP_IP="192.168.1.2"
UDP_PORT=5005
sock = socket.socket( socket.AF_INET,socket.SOCK_DGRAM ) # UDP
sock.bind( (UDP_IP,UDP_PORT) )
i=0
MemberList={}
ML_values=[]
def DpsSpam():
    s_msg='D>'
    ML_values = list(MemberList.values())
    for x in range(len(ML_values)):
        if ML_values[x].active==1:
            s_msg+='%s:%s;' %(str(ML_values[x].id),str(ML_values[x].dps))
    print(s_msg)
    for y in range(len(ML_values)):
        if ML_values[y].active==1:
            sock.sendto(bytes(s_msg,'ascii'),(ML_values[y].ip,ML_values[y].port))
    ML_values.clear()
def reset():
    ML_values = list(MemberList.values())
    for x in range(len(MemberList)):ML_values[x].dps=0
    ML_values.clear()
def NickSpam():
    s_msg='N>'
    ML_values = list(MemberList.values())
    for x in range(len(ML_values)):
        if ML_values[x].active==1:
            s_msg+='%s:%s;' %(ML_values[x].id,ML_values[x].nick)
    print(s_msg)
    for y in range(len(ML_values)):
        if ML_values[y].active==1:
            sock.sendto(bytes(s_msg,'ascii'),(ML_values[y].ip,ML_values[y].port))
    ML_values.clear()
def DpsUpdate(id,dps):
    #MemberList[int(s_id)].dps=int(s_dps)
    ML_values = list(MemberList.values())
    for x in range(len(ML_values)):
        if ML_values[x].id==int(id):
            ML_values[x].dps=str(dps)
            break
def SetInactive(id):
    ML_values = list(MemberList.values())
    s_msg='R>%d' %(int(id))
    print (s_msg)
    for x in range(len(ML_values)):
        if ML_values[x].id==int(id):
            ML_values[x].active=0
            break
    for y in range(len(ML_values)):
        if ML_values[y].active==1:
            sock.sendto(bytes(s_msg,'ascii'),(ML_values[y].ip,ML_values[y].port))
    ML_values.clear()
def SetActive(id):
    ML_values = list(MemberList.values())
    s_msg='R>%d' %(int(id))
    print (s_msg)
    for x in range(len(ML_values)):
        if ML_values[x].id==int(id):
            ML_values[x].active=1
            break
def DmgUpdate(id,dmg):
    ML_values = list(MemberList.values())
    for x in range(len(ML_values)):
        if ML_values[x].id==int(id):
            ML_values[x].dmg=str(dmg)
            break
def DmgSpam():
    s_msg='T>'
    ML_values = list(MemberList.values())
    for x in range(len(ML_values)):
        if ML_values[x].active==1:
            s_msg+='%s:%s;' %(str(ML_values[x].id),str(ML_values[x].dmg))
    print(s_msg)
    for y in range(len(ML_values)):
        if ML_values[y].active==1:
            sock.sendto(bytes(s_msg,'ascii'),(ML_values[y].ip,ML_values[y].port))
    ML_values.clear()
class Raid:
    def __init__(self,nick,ip,port,id,active=0,dps=0,dmg=0):
        self.nick=nick
        self.ip=ip
        self.port=port
        self.dps=dps
        self.id=id
        self.active=active
        self.dmg=dmg
try:
    while True:
        data,addr = sock.recvfrom( 1024 ) # buffer size is 1024 bytes
        command=data[0:5];
        if command==b'Ping!':
            NickName=data[6:]
            Nick=str(NickName)
            if str(NickName) in list(MemberList.keys()):
                #print (bytes(str(MemberList[Nick].id),'ascii'))
                msg=b'P>%b' %(bytes(str(MemberList[Nick].id),'ascii'))
                print ("Welcome back", NickName)
                sock.sendto(msg,(addr[0],addr[1]))
                SetActive(MemberList[Nick].id)
            else:
                #i+=1
                print(i)
                L={Nick:Raid(Nick,addr[0],addr[1],i,1)}
                MemberList.update(L)
                print("Hello ,",MemberList[Nick].nick,MemberList[Nick].ip,MemberList[Nick].port,i)
                msg=b'P>%b' %(bytes(str(i),'ascii'))
                sock.sendto(msg,(addr[0],addr[1]))
                i+=1
            NickSpam()    
        elif command==b'Spam!':DpsSpam()
        elif command==b'DPSU!':
            g_msg=data[6:]
            (s_id,s_dps) = g_msg.split(b':')
            DpsUpdate(s_id,s_dps)
            DpsSpam()
        elif command==b'RESE!':reset()
        elif command==b'NSPM!':NickSpam()
        elif command==b'BBYE!':
            g_msg=data[6:]
            print("Bye bye", g_msg)
            SetInactive(int(g_msg))
        elif command==b'DMGU!':
            g_msg=data[6:]
            (s_id,s_dmg) = g_msg.split(b':')
            DmgUpdate(s_id,s_dmg)
            DmgSpam()
        
except KeyboardInterrupt:
    print ('interrupted!')

