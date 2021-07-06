from collections import defaultdict

def hash_function(s):
    mod=26
    return len(s)%mod

def insert(string,table):
    index=hash_function(string)
    table[index].append(string)

def search(string,table):
    index=hash_function(string)
    for i in table[index]:
        if i==string:
            print("Found")
            return
    print("Not Found")
                  
    
    
table=defaultdict(list)
insert('delhi',table)
insert('mumbai',table)
insert('kolkata',table)
insert('chennai',table)
insert('jalandhar',table)

print(table)
search('kolkata',table)
search('varanasi',table)


