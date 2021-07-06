from requests import get
n = int(input("How many quotes do you want to fetch:\n"))

for i in range(n):
    try:
        r = get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&json=?")
        print(r.json())
        d = r.json()
        for key in d.keys():
            if key=="quoteAuthor":
                print("Author :",d['quoteAuthor'])
                print("Quote :",d['quoteText'])
        print("-"*50)
    except Exception as e:
        d['quoteText'] = d['quoteText'].replace('//','/')
        print("Author :",d['quoteAuthor'])
        print("Quote :",d['quoteText'])
        print("-"*50)
