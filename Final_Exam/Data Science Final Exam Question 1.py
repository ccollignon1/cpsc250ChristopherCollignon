#Christopher Collignon
#06/30/2023
#CPSC250 Final Exam Data Science Question 1

import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def fitting_function(t,y0,v0,g):
    return(y0+(v0*t)-(0.5*g*(t**2)))
#Initialize numpy arrays
time = np.array([])
height = np.array([])
dtime = np.array([])
dheight = np.array([])

#Read data from csv
with open('Projectile.csv', 'r') as file:
    reader=csv.reader(file)
    #Skip header line
    next(reader)
    #place data in respective arrays
    for row in reader:
        time=np.append(time,float(row[0]))
        height=np.append(height,float(row[1]))
        dtime=np.append(dtime,float(row[2]))
        dheight=np.append(dheight,float(row[3]))


#Use SciPi to find statistics
popt,pcov=curve_fit(fitting_function,time,height,sigma=dheight,absolute_sigma=True)

#Find and print error
error=np.sqrt(np.diag(pcov))
print(f'y0 = {popt[0]:.3f} +/- {error[0]:.3f} m')
print(f'v0 = {popt[1]:.3f} +/- {error[1]:.3f} m/s')
print(f'g = {popt[2]:.3f} +/- {error[2]:.3f} m/s^2')
#Choose print statement based on calculated value of gravit
grav=9.81
if np.abs(popt[2] -grav)<=error[2]:
    print("The extracted value of g agrees with the expected value.")
else:
    print("The extracted value of g disagrees with the expected value.")

#Create a figure and plot data points with formatted errorbars,
#plot best fit line, plot error bound lines,
#and format legend properly
plt.figure(figsize=(10,6))
plt.title("Projectile Motion Experiment")

data=plt.errorbar(time,height,xerr=dtime,yerr=dheight,fmt='o', capsize=4,elinewidth=1,markeredgewidth=1,label='Data')

t_fit=np.linspace(time.min(),time.max(),1000)
fit, =plt.plot(t_fit,fitting_function(t_fit,*popt),'r--')

bound, =plt.plot(t_fit, fitting_function(t_fit, *(popt - error)), 'g--')
plt.plot(t_fit, fitting_function(t_fit, *(popt + error)), 'g--')

plt.xlabel('Time (s)')
plt.ylabel('Height (m)')

legend_fit = f'Quadratic fit:\ny = - 0.5 * ({popt[2]:.3f} +/- {error[2]:.3f} m/s^2) * t^2 + \n({popt[1]:.3f} +/- {error[1]:.3f} m/s) * t + \n{popt[0]:.3f} +/- {error[0]:.3f} m'
plt.legend(handles=[fit,bound,data],labels=[legend_fit, 'One sigma error','Data'])

plt.show()


print("Completed")