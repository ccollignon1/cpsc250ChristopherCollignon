#Christopher Collignon
#06/30/2023
#CPSC250 Final Exam Data Science Question 2

import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

#Read data from CSV into dataframe
df=pd.read_csv("EmissionsData.csv")

#Create plots/subplots with given parameters
fig,axs=plt.subplots(2,2,figsize=(9,9))
fig.tight_layout(pad=2.5)

#Add title
fig.suptitle("Dependency of CO2 Emissions on Car Engine Volume and Weight", fontsize=16)

#Top left plot
axs[0, 0].scatter(df['Volume'], df['CO2'])
axs[0, 0].set_xlabel('Engine Volume (mL)')
axs[0, 0].set_ylabel('CO2 Emissions')

#Top right plot
axs[0, 1].scatter(df['Weight'], df['CO2'])
axs[0, 1].set_xlabel('Weight (kg)')
axs[0, 1].set_ylabel('CO2 Emissions')

#Linear regression 1
model1 = smf.ols(formula='CO2 ~ Volume', data=df).fit()
print(model1.summary())

#Calculate residuals for the first model
df['CO2VolumeResiduals'] = df['CO2'] - model1.fittedvalues

#Bottom left plot
axs[1, 0].scatter(df['Volume'], df['CO2'],label='Data')
axs[1, 0].plot(df['Volume'], model1.fittedvalues, color='orange', label='Prediction',linewidth=3)
axs[1, 0].set_xlabel('Engine Volume (mL)')
axs[1, 0].set_ylabel('CO2 Emissions')
axs[1, 0].legend()

#Linear regression 2
model2 = smf.ols(formula='CO2VolumeResiduals ~ Weight', data=df).fit()
print(model2.summary())

#Calculate residuals for the second model
df['Residuals'] = df['CO2VolumeResiduals'] - model2.fittedvalues

#Bottom right plot
axs[1, 1].scatter(df['Weight'], df['CO2VolumeResiduals'], label='Data')
axs[1, 1].plot(df['Weight'], model2.fittedvalues, color='orange', label='Prediction',linewidth=3)
axs[1, 1].set_xlabel('Weight (kg)')
axs[1, 1].set_ylabel('CO2 Emissions vs Volume Residuals')
axs[1, 1].legend()


plt.show()

print("Completed")