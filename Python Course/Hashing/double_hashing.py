from collections import defaultdict

def hash_function(s):
    global mod
    return len(s)%mod

def hash_function2(s):
    mod1=15
    return 2*len(s)%mod1

def insert(string,table):
    global mod
    index=hash_function(string)
    while(table[index]!=""):
        index=(index+hash_function2(string))%mod
    table[index]=string

def search(string,table):
    global mod
    index = hash_function(string)
    while(table[index] != ''):
        if(table[index] == string):
            print('Found')
            return
        index = (index + hash_function2(string)) % mod
    print('Not Found')
    
table=defaultdict(str)
mod=26
insert('delhi',table)
insert('mumbai',table)
insert('kolkata',table)
insert('chennai',table)
insert('jalandhar',table)
insert('lucknow',table)
insert('dhanbad',table)
print(table)
search('dhanbad',table)
search('varanasi',table)
