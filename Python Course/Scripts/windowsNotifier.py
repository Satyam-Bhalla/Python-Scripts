from win10toast import ToastNotifier
toaster = ToastNotifier()
for i in range(10):
	toaster.show_toast("Virus Warning","Stealing data",icon_path="favicon.ico",duration=2)

toaster.show_toast("Example two","This notification is in it's own thread!",icon_path=None,duration=2,threaded=True)