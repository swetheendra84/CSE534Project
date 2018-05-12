import os
import sys
import subprocess

data = {}
def parse_hping():
    f = open('hping.out','r')
    g = open('parse_hping.out','w+')
    data_enable = False
    for line in f.readlines():
        if line.startswith('--- ') and not data_enable:
            line = line.rstrip('\n')
            line = line.lstrip('--- ')
            line = line[:-20]
            #line = line.rstrip(' hping statistic ---')
            website = line
            g.write(website+',')
            data_enable = True
        elif line.startswith('Unable to resolve ') and not data_enable:
            line = line.rstrip('\n')
            line = line.split('\'')
            website = line[1]
            g.write(website+','+'0,0,0,')
            data_enable = True
        elif data_enable and line.startswith('round-trip '):
            line = line.rstrip('\n')
            line = line.lstrip('round-trip min/avg/max = ')
            line = line.rstrip(' ms')
            min_rtt,avg_rtt,max_rtt = line.split('/')
            g.write(min_rtt+','+avg_rtt+','+max_rtt+',')
        elif data_enable and line.startswith('len='):
            line = line.strip('\n')
            line = line.split('=')
            line = line[3]
            ttl = line.rstrip(' DF id')
            g.write(ttl+'\n')
            data_enable = False   
        elif data_enable and line.startswith('Return Code: 1'):
            g.write(str(0)+'\n')
            data_enable = False 
    f.close()
    g.close()
            
def parse_traceroute():
    f = open('traceroute.out','r')
    g = open('parse_traceroute.out','w+')
    data_enable = False
    hop_count = 0
    for line in f.readlines():
        if not data_enable and line.startswith('***sudo tcptraceroute'):
            line = line.rstrip('\n')
            #print line
            line = line[28:]
            #print line
            line = line.rstrip(' 80***')
            #print line
            website = line
            g.write(website+',')
            data_enable = True
            hop_count=0
        elif data_enable and line.startswith('Return Code'):
            hop_count-=2
            g.write(str(hop_count)+'\n')
            data_enable = False
        elif data_enable:
            hop_count+=1
    f.close()
    g.close()
    
def new_parse_hping():
    f = open('hping.out','r')
    g = open('parse_hping.out','w+')
    data_enable = False
    for line in f.readlines():
        if line.startswith('***sudo hping3'):
            line = line.rstrip('\n')
            #line = line.lstrip('--- ')
            line = line[40:]
            line = line[:-3]
            #line = line.rstrip(' hping statistic ---')
            website = line
            g.write(website+',')
            data_enable = True
        elif line.startswith('Unable to resolve ') and not data_enable:
            line = line.rstrip('\n')
            line = line.split('\'')
            website = line[1]
            g.write(website+','+'0,0,0,')
            data_enable = True
        elif data_enable and line.startswith('round-trip '):
            line = line.rstrip('\n')
            line = line.lstrip('round-trip min/avg/max = ')
            line = line.rstrip(' ms')
            min_rtt,avg_rtt,max_rtt = line.split('/')
            g.write(min_rtt+','+avg_rtt+','+max_rtt+',')
        elif data_enable and line.startswith('len='):
            line = line.strip('\n')
            line = line.split('=')
            line = line[3]
            ttl = line.rstrip(' DF id')
            g.write(ttl+'\n')
            data_enable = False   
        elif data_enable and line.startswith('Return Code: 1'):
            g.write(str(0)+'\n')
            data_enable = False 
    f.close()
    g.close()
    
parse_traceroute()
parse_hping()
        
        
        
        
        
        
        
        
        
        
        