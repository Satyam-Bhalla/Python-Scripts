import webbrowser
import time

total_breaks = 3
break_count = 0
#To take a break after 1 hour
while(break_count < total_breaks):
    print("This program started on "+time.ctime())
    time.sleep(1*60*60)  
    webbrowser.open("https://www.youtube.com/channel/UCwjdb9MdYI0VqUlz8UdCTYw")
    break_count += 1
