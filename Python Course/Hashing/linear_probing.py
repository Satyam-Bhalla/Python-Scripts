from collections import defaultdict

def hash_function(s):
    global mod
    return len(s)%mod

def insert(string,table):
    global mod
    index=hash_function(string)
    while(table[index]!=""):
        index=(index+1)%mod
    table[index]=string

def search(string,table):
    global mod
    index = hash_function(string)
    while(table[index] != ''):
        if(table[index] == string):
            print('Found')
            return
        index = (index + 1) % mod
    print('Not Found')
    
table=defaultdict(str)
mod=26
insert('delhi',table)
insert('mumbai',table)
insert('kolkata',table)
insert('chennai',table)
insert('jalandhar',table)
insert('abcdefgh', table)

print(table)
search('mumbai',table)
search('varanasi',table)
search('abcdefgh',table)
