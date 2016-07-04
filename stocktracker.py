from urllib.request import urlopen
#import requests
import smtplib



def email(msg): #Send an email with the string payload 'msg'
	
	TO = 'ADD RECIPIENT EMAIL ADDRESS HERE'
	SUBJECT = 'Stock Summary'
	TEXT = msg

	# Email Sign-in
	sender_email = 'SENDER EMAIL HERE'
	sender_PW = 'SENDER PW HERE'

	server = smtplib.SMTP('mail.gmx.com', 587)
	server.ehlo()
	server.starttls()
	server.login(sender_email, sender_PW)

	BODY = '\r\n'.join(['To: %s' % TO,
						'From: %s' % sender_email,
						'Subject: %s' % SUBJECT,
						'', TEXT])

	try:
		server.sendmail(sender_email, [TO], BODY)
		print ('email sent')
	except:
		print ('error sending mail')

	server.quit()


#get the data from yahoo stock api (hsbc, vw, ftse, euro) and convert to a string
r = str(urlopen('http://finance.yahoo.com/d/quotes.csv?s=HSBA.L+VOW.DE+^FTSE+EURGBP=X&f=nghbp2').read())

#parse the data into the list stockData:

stockData=[]
datum=''

for i in r:
	datum = datum+i
	if i=="\"" or i==",":
		stockData.append(datum[:-1])
		datum=''

#print everything in the list
print ('stockData = ',stockData)

#contruct the payload
message = stockData[1] + stockData[5] + "\n" + \
          stockData[9] + stockData[13] + "\n" + \
          stockData[17] + stockData[21] + "\n" + \
          stockData[25] + stockData[29]

print("Payload :\n", message)


#email(message)

