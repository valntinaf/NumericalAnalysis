# Data per station

class Sensor():
	vel = "velocidad"
	pres = "velocidad"
	e = "velocidad"
	we = "velocidad"
	po = "velocidad"


class Data:
	vel = ""
	umi = "0"
	temp = ""
	rad = ""
	press = ""
	precip = ""
	windir = ""

	def __init__(self, vel, umi, temp, rad, press, precip, windir): 
		self.vel = vel 
		self.umi = umi
		self.temp = temp 
		self.rad = rad 
		self.press = press
		self.precip = precip 
		self.windir = windir 