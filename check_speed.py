import speedtest
from prettytable import PrettyTable


def speed_details():


	s=speedtest.Speedtest()
	

	mytable=PrettyTable(['Network Provider','Download Speed(Mb/s)','Upload Speed(Mb/s)','Ping(ms)'])

	mytable.add_row([s.get_best_server()['sponsor'],f'{(s.download()/10e+5):.2f}',f'{(s.upload()/10e+5):.2f}',s.results.ping])


	return mytable



print(speed_details())