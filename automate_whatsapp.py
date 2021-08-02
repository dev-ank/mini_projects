from pywhatkit import sendwhatmsg_to_group


def send_mssg(group_id,mssg,hour,minute):

	

	try:
		sendwhatmsg_to_group(group_id,mssg,hour,minute,30,True,5)

	except Exception as e:
		print(e)


send_mssg('group id','Test Message',23,50)