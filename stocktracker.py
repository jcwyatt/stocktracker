import requests
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



#get the data from yahoo stock api
r = requests.get('http://finance.yahoo.com/d/quotes.csv?s=HSBA.L+VOW.DE&f=nghbp2')



#parse the data into a list stockData
stockData=[]
datum=''

for i in r.text:
	datum = datum+i
	if i=="\"" or i==",":
		stockData.append(datum[:-1])
		datum=''


#contruct the payload
message = "HSBC " + stockData[5] + "\n" + "VW " + stockData[13]

print(message)

email(message)

