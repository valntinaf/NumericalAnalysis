from dps import Data
from datetime import datetime
fmt = '%H:%M:%S'

class Data_3h:
	data = {"vel":0, "umi":0, "temp":0, "rad":0, "press":0, "precip":0 , "windir":0}
	hour = ""
	station = ""
	vel = 0;
	umi = 0;
	temp = 0;
	rad = 0;
	press = 0;
	precip = 0;


	def __init__(self, hour, station, vel, umi, temp, rad, press, precip, windir):
		self.hour = hour
		self.station = station
		self.vel = vel
		self.umi = umi
		self.temp = temp
		self.rad = rad
		self.press = press
		self.precip = precip
		self.windir = windir

def read_data_3h():
	all_data = {"vel":[], "umi":[], "temp":[], "rad":[], "press":[], "precip":[] , "windir":[]}
	 
	datas = []

	filepath = 'data/for_3horas.csv'
	with open(filepath) as fp:
		line = fp.readline()
		cnt = 0
		while line:
			try:
				line = fp.readline()

				print("Line {}: {}".format(cnt, line.strip()))
				comas=line.split(',')

				hour = datetime.strptime(comas[2].split(' ')[1],fmt)

				station = comas[0]
				vel=float(float(comas[3]))
				all_data["vel"].append(vel)
				line = fp.readline()
				print("Line {}: {}".format(cnt, line.strip()))
				comas=line.split(',')
				umi=float(comas[3])
				all_data["umi"].append(umi)
				line = fp.readline()
				print("Line {}: {}".format(cnt, line.strip()))
				comas=line.split(',')
				temp=float(comas[3])
				all_data["temp"].append(temp)
				line = fp.readline()
				print("Line {}: {}".format(cnt, line.strip()))
				comas=line.split(',')
				rad=float(comas[3])
				all_data["rad"].append(rad)
				line = fp.readline()
				print("Line {}: {}".format(cnt, line.strip()))
				comas=line.split(',')
				press=float(comas[3])
				all_data["press"].append(press)
				line = fp.readline()
				print("Line {}: {}".format(cnt, line.strip()))
				comas=line.split(',')
				precip=float(comas[3])
				all_data["precip"].append(precip)
				line = fp.readline()
				print("Line {}: {}".format(cnt, line.strip()))
				comas=line.split(',')
				windir=float(comas[3])
				all_data["windir"].append(windir)

				data_temp = Data_3h(hour, station, vel, umi, temp, rad, press, precip, windir)
				datas.append(data_temp)

				print("Line {} readed.".format(cnt))
				cnt += 1
			except:
				print("No se pudo leer una línea.")
	return datas

def read_data_h():
	all_data = []
	return all_data