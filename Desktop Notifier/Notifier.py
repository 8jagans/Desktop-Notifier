from win10toast import ToastNotifier 
import datetime

n = ToastNotifier() 

title = "Good Morning, Jos"

messages = " Today is {} ".format(datetime.date.today())

n.show_toast(
	title,
	messages,
	icon_path ="cal.ico",
	duration = 5) 
