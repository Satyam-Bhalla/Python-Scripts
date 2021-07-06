from collections import defaultdict

def hash_function(s):
    global mod
    return len(s)%mod

def insert(string,table):
    global mod
    index=hash_function(string)
    i=1
    while(table[index]!=""):
        index=(index+(i*i))%mod
        i+=1
    table[index]=string

def search(string,table):
    global mod
    index = hash_function(string)
    i=1
    while(table[index] != ''):
        if(table[index] == string):
            print('Found')
            return
        index = (index + i*i) % mod
        i+=1
    print('Not Found')
    
table=defaultdict(str)
mod=26
insert('delhi',table)
insert('mumbai',table)
insert('kolkata',table)
insert('chennai',table)
insert('jalandhar',table)
insert('lucknow',table)
print(table)
search('mumbai',table)
search('varanasi',table)
search('lucknow',table)
