import reader_wewe as r_wewe
from scipy.interpolate import BarycentricInterpolator, interp1d

import numpy as np
import matplotlib.pyplot as plt 
import math

from scipy.interpolate import griddata

from datetime import datetime
fmt = '%H:%M:%S'

datas = r_wewe.read_data_3h()
all_data_h = r_wewe.read_data_h()

round = 10000

grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]

methods_names = {
	0: "BarycentricInterpolator",
	1: "interp1d"
	}
methods = {
	"BarycentricInterpolator": BarycentricInterpolator,
	"interp1d": interp1d
	}

print(" Estaciones displonibles: ")
print(" ITATIRA, SANTANA DO CARIRI, AIUABA, MARANGUAPE, PEDRA BRANCA, ETC... ")


print("Escriba la estación: ")
station = input()

data_station = []

for data in datas:
	if data.station == station:
		data_station.append(data)

print("Escriba la hora, ejemplo: 18:21:12 : ")
hour_f = input()
hour = datetime.strptime(hour_f,fmt).timestamp()//round

# hour, station, vel, umi, temp, rad, press, precip, windir
hours = []
vels = []
umis = []
temps = []
rads = []
presses = []
precips = []
windirs = []

for data in data_station:
	hours.append(data.hour.timestamp()//round)
	vels.append(data.vel)
	umis.append(data.umi)
	temps.append(data.temp)
	rads.append(data.rad)
	presses.append(data.press)
	precips.append(data.precip)
	windirs.append(data.windir)

print("Hallando la informaación a las {}".format(hour))

method_i=0

interpolated=False

print(hours)
print(temps)

# Getting functions

f_vel = interp1d(hours , vels)
# Getting value y in x point 
estimated_vel = f_vel(hour)
# Checking if it worked
if not math.isnan(estimated_vel):
	print("Obteniendo valor...")
	print("Estimated vel:")
	print(estimated_vel)
	interpolated=True

f_umi = interp1d(hours , umis)
# Getting value y in x point 
estimated_umi = f_umi(hour)
# Checking if it worked
if not math.isnan(estimated_umi):
	print("Obteniendo valor...")
	print("Estimated umi:")
	print(estimated_umi)
	interpolated=True

f_temp = interp1d(hours , temps)
# Getting value y in x point 
estimated_temp = f_temp(hour)
# Checking if it worked
if not math.isnan(estimated_temp):
	print("Obteniendo valor...")
	print("Estimated temp:")
	print(estimated_temp)
	interpolated=True


f_rad = interp1d(hours , rads)
# Getting value y in x point 
estimated_rad = f_rad(hour)
# Checking if it worked
if not math.isnan(estimated_rad):
	print("Obteniendo valor...")
	print("Estimated rad:")
	print(estimated_rad)
	interpolated=True

f_press = interp1d(hours , presses)
# Getting value y in x point 
estimated_press = f_press(hour)
# Checking if it worked
if not math.isnan(estimated_press):
	print("Obteniendo valor...")
	print("Estimated press:")
	print(estimated_press)
	interpolated=True

f_precip = interp1d(hours , precips)
# Getting value y in x point 
estimated_precip = f_precip(hour)
# Checking if it worked
if not math.isnan(estimated_precip):
	print("Obteniendo valor...")
	print("Estimated precip:")
	print(estimated_precip)
	interpolated=True

f_windir = interp1d(hours , windirs)
# Getting value y in x point 
estimated_windir = f_windir(hour)
# Checking if it worked
if not math.isnan(estimated_windir):
	print("Obteniendo valor...")
	print("Estimated windir:")
	print(estimated_windir)
	interpolated=True

plt.plot(hours,vels,'x', mew=2, label='Datos')
# Datos de plot
plt.xlabel("hours")
plt.ylabel("vels")
plt.legend()
plt.show()

plt.plot(hours,umis,'x', mew=2, label='Datos')
# Datos de plot
plt.xlabel("hours")
plt.ylabel("umis")
plt.legend()
plt.show()

plt.plot(hours,temps,'x', mew=2, label='Datos')
# Datos de plot
plt.xlabel("hours")
plt.ylabel("temps")
plt.legend()
plt.show()

plt.plot(hours,rads,'x', mew=2, label='Datos')
# Datos de plot
plt.xlabel("hours")
plt.ylabel("rads")
plt.legend()
plt.show()

plt.plot(hours,presses,'x', mew=2, label='Datos')
# Datos de plot
plt.xlabel("hours")
plt.ylabel("press")
plt.legend()
plt.show()

plt.plot(hours,precips,'x', mew=2, label='Datos')
# Datos de plot
plt.xlabel("hours")
plt.ylabel("Precipitación")
plt.legend()
plt.show()

plt.plot(hours,windirs,'x', mew=2, label='Datos')
# Datos de plot
plt.xlabel("hours")
plt.ylabel("Dirección del viento")
plt.legend()
plt.show()