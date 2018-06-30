from tkinter import *
from urllib.request import urlopen
import urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error, json,tkinter.messagebox,sys,io,base64

class Application(object):
    """ Application class """

    _Version,_Name,_Usage=1.0,"weather","Usage : python3 weathers.py \"city or country name\" \npython3 weather.py\nwith no city name the program starts with Paris\nsample :\npython3 weather.py \"Paris\""
    _WIDTH,_HEIGHT,_MapWidth,_MapHeight,_MapZoom=320,400,320,300,9
    _TITLE_FONT,_STANDARD_FONT="Lucida 13 bold","Lucida 13"

    """
        init UI
    """
    def __init__(self):

        self._tk = Tk()
        self._tk.title(self._Name)
        self._tk.minsize(width=self._WIDTH,height=self._HEIGHT)
        self._tk.resizable(width=False, height=False)
        self._tk.bind_all('<Command-q>',self.quit)
        self._tk.bind_all('<Command-Q>',self.quit)

        self.menubar = Menu(self._tk)
        self.appmenu = Menu(self.menubar, tearoff=0)
        self.appmenu.add_command(label="Quit", command=self.quit)
        self.menubar.add_cascade(label=self._Name, menu=self.appmenu)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about)
        self.helpmenu.add_command(label="Help & How-To", command=self.help)
        self.helpmenu.add_command(label="Version", command=self.version)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self._tk.config(menu=self.menubar)

        self.LOCATION_VALUE = StringVar()
        self.CONDITION_VALUE = StringVar()
        self.WIND_VALUE = StringVar()
        self.ATMOSPHERE_VALUE = StringVar()
        self.ASTRONOMY_VALUE = StringVar()
        self.LAST_UPDATE_VALUE = StringVar()

        self.upperBlock = Frame(self._tk)
        self.locationInput = Entry(self.upperBlock,font = "Ar")
        self.locationInput.grid(row=0, column=0, sticky=W+E)
        self.buttonSearch = Button(self.upperBlock,text='search / update',command=self.update)
        self.buttonSearch.grid(row=0, column=1)
        self.upperBlock.pack(side = TOP,fill=X)

        self.weatherBlock = Frame(self._tk)
        self.locationLabel = Label(self.weatherBlock, text = "Location : " ,font = self._TITLE_FONT)
        self.locationLabel.grid(row=0, column=0, sticky=W)
        self.locationValue = Label(self.weatherBlock, textvariable=self.LOCATION_VALUE, font=self._STANDARD_FONT)
        self.locationValue.grid(row=0, column=1, sticky=W)
        self.conditionLabel = Label(self.weatherBlock, text = "Condition : ",font = self._TITLE_FONT)
        self.conditionLabel.grid(row=1, column=0, sticky=W)
        self.conditionValue = Label(self.weatherBlock, textvariable=self.CONDITION_VALUE, font=self._STANDARD_FONT)
        self.conditionValue.grid(row=1, column=1, sticky=W)
        self.windLabel = Label(self.weatherBlock, text = "wind : ",font = self._TITLE_FONT)
        self.windLabel.grid(row=2, column=0, sticky=W)
        self.windValue = Label(self.weatherBlock, textvariable=self.WIND_VALUE, font=self._STANDARD_FONT)
        self.windValue.grid(row=2, column=1, sticky=W)
        self.atmosphereLabel = Label(self.weatherBlock, text = "Atmosphere : ",font = self._TITLE_FONT)
        self.atmosphereLabel.grid(row=3, column=0, sticky=W)
        self.atmosphereValue = Label(self.weatherBlock, textvariable=self.ATMOSPHERE_VALUE, font=self._STANDARD_FONT)
        self.atmosphereValue.grid(row=3, column=1, sticky=W)
        self.astronomyLabel = Label(self.weatherBlock, text = "Astronomy : ",font = self._TITLE_FONT)
        self.astronomyLabel.grid(row=4, column=0, sticky=W)
        self.astronomyValue = Label(self.weatherBlock, textvariable=self.ASTRONOMY_VALUE, font=self._STANDARD_FONT)
        self.astronomyValue.grid(row=4, column=1, sticky=W)
        self.forecastLabel = Label(self.weatherBlock, text = "Forecast : ",font = self._TITLE_FONT)
        self.forecastLabel.grid(row=5, column=0, sticky=W)
        self.lastupdateLabel = Label(self.weatherBlock, textvariable=self.LAST_UPDATE_VALUE, font=self._STANDARD_FONT)
        self.lastupdateLabel.grid(row=5, column=1, sticky=W)
        self.forecastList = Listbox(self.weatherBlock, height=4)
        self.forecastList.grid(row=6, columnspan=2, sticky=W+E)
        self.mapView = Canvas(self.weatherBlock, bg='grey',width=self._MapWidth, height=self._MapHeight)
        self.mapView.grid(row=7, columnspan=2)
        self.weatherBlock.pack(side = BOTTOM, fill='both')

        self.checkArgs()

    def checkArgs(self):
        if(len(sys.argv)==2):
            if(len(sys.argv[0])!=0):
                self.updateWith(str(sys.argv[1]));
        elif(len(sys.argv)>2):
            print(self._Usage)
            self.quit()
        else:
            self.updateWith("Amritsar");

    def retrieveData(self,name):
        try:
            #query
            baseurl = "https://query.yahooapis.com/v1/public/yql?"
            yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=\""+name+"\") and u=\"c\""
            yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
            result = urllib.request.urlopen(yql_url).read()
            data = json.loads(result.decode())

            #data retrieve
            city = data['query']['results']['channel']['location']['city']
            country = data['query']['results']['channel']['location']['country']
            region = data['query']['results']['channel']['location']['region']
            self.LOCATION_VALUE.set(city+" "+country+" "+region)

            temp = data['query']['results']['channel']['item']['condition']['temp']
            tempU = data['query']['results']['channel']['units']['temperature']
            if(tempU=='C'):
                tempU='°'
            text = data['query']['results']['channel']['item']['condition']['text']
            low = data['query']['results']['channel']['item']['forecast'][0]['low']
            high = data['query']['results']['channel']['item']['forecast'][0]['high']
            self.CONDITION_VALUE.set(temp+tempU +" "+ text + " Min "+low+tempU+" Max "+high+tempU)

            speed = data['query']['results']['channel']['wind']['speed']
            speedU = data['query']['results']['channel']['units']['speed']
            self.WIND_VALUE.set(speed+speedU)

            humidity = data['query']['results']['channel']['atmosphere']['humidity']
            pressure = data['query']['results']['channel']['atmosphere']['pressure']
            pressureU = data['query']['results']['channel']['units']['pressure']
            self.ATMOSPHERE_VALUE.set("Humidity "+humidity+"% Pressure "+pressure+pressureU)

            sunrise = data['query']['results']['channel']['astronomy']['sunrise']
            sunset = data['query']['results']['channel']['astronomy']['sunset']
            self.ASTRONOMY_VALUE.set("Sunset "+sunrise+" Sunrise "+sunset)

            lastUptate = data['query']['results']['channel']['item']['pubDate']
            self.LAST_UPDATE_VALUE.set(lastUptate)

            self.forecastList.delete(0, END)
            for i in range(1,len(data['query']['results']['channel']['item']['forecast']),1):
                forecast = data['query']['results']['channel']['item']['forecast'][i]
                self.forecastList.insert(END,forecast['day']+" "+forecast['date']+" "+forecast['text']+" Min "+forecast['low']+tempU+" Max "+ forecast['high']+tempU)
            
            coord = self.retrieveGeoData(name)
            self.image_url = "http://maps.google.com/maps/api/staticmap?center="+str(coord['latitude'])+","+str(coord['longitude'])+"&zoom="+str(self._MapZoom)+"&size="+str(self._MapWidth)+"x"+str(self._MapHeight)+"&format=gif&maptype=terrain&markers=size:mid%7Ccolor:red%7C"+str(coord['latitude'])+","+str(coord['longitude'])+"&sensor=false&"
            self.image_byt = urlopen(self.image_url).read()
            self.image_b64 = base64.encodestring(self.image_byt)
            self.photo = PhotoImage(data=self.image_b64)
            self.mapView.delete(ALL)
            self.mapView.create_image(0,0,image=self.photo, anchor="nw")
        except urllib.error.URLError :
            self.showInternetErrorMsg()
            self.quit()
        except TypeError:
            self.showBadCityMessage()
            self.LOCATION_VALUE.set("- - -")
            self.CONDITION_VALUE.set("- - -")
            self.WIND_VALUE.set("- - -")
            self.ATMOSPHERE_VALUE.set("- - -")
            self.ASTRONOMY_VALUE.set("- - -")
            self.LAST_UPDATE_VALUE.set("- - -")
            self.mapView.delete(ALL)
            self.forecastList.delete(0, END)
        else:
            pass
        finally:
            pass

    def retrieveGeoData(self,name):
        try:
            baseurl = "https://query.yahooapis.com/v1/public/yql?"
            yql_query = "select * from geo.places(1) where text=\""+name+"\""
            yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
            result = urllib.request.urlopen(yql_url).read()
            data = json.loads(result.decode())
            coord = {}
            coord['latitude'] = data['query']['results']['place']['centroid']['latitude']
            coord['longitude'] = data['query']['results']['place']['centroid']['longitude']
            return coord  
        except urllib.error.URLError :
            pass
        except TypeError:
            pass
        else:
            pass
        finally:
            pass

    def quit(self):
        self._tk.destroy()

    def about(self):
        tkinter.messagebox.showinfo("About", "Developed by\n\nTushar Malhotra\n\nmalhotra1995tushar@gmail.com")
    
    def help(self):
        tkinter.messagebox.showinfo("Help","Type a city or a country name then press search/update.")

    def version(self):
        tkinter.messagebox.showinfo("Version", "Version "+str(self._Version))

    def showInternetErrorMsg(self):
        print("Error no internet connection available")

    def showBadCityMessage(self):
        tkinter.messagebox.showinfo("Error","City not found")


    def updateWith(self,name):
        self.locationInput.insert(0,name)
        self.update();

    def update(self):
        if(len(self.locationInput.get())!=0):
            self.retrieveData(self.locationInput.get())

    def mainloop(self):
        self._tk.mainloop()

if __name__ == '__main__':
    Application().mainloop()
