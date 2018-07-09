import webbrowser, sys, pyperclip

#sys.argv is a list of the commands passed through the terminal

#For linux users, download the script, go to the download directory and type:
		# python map.py "Address" in terminal or
		# copy the address of the place and run the script python map.py in terminal

sys.argv

if len(sys.argv)>1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

