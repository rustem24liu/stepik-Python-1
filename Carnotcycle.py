import numpy as np
import matplotlib.pyplot as plt

# Define temperature limits and number of points to plot
T_L = 273.15    # Lower temperature limit (in Kelvin)
T_H = 1273.15   # Upper temperature limit (in Kelvin)
npoints = 100   # Number of points to plot

# Define pressure limits and number of points to plot
P_L = 1e5       # Lower pressure limit (in Pascal)
P_H = 10e5      # Upper pressure limit (in Pascal)

# Define the temperature and pressure values for the four stages of the Carnot cycle
T1 = T_L
P1 = P_H
T2 = T_H
P2 = P_H
T3 = T_H
P3 = P_L
T4 = T_L
P4 = P_L

# Define the temperature and pressure values for the adiabatic expansion and compression curves
T_ad = np.linspace(T_H, T_L, npoints)
P_ad_exp = P_H * (T_ad / T_H) ** (5/2)
P_ad_comp = P_L * (T_ad / T_L) ** (5/2)

# Define the temperature and pressure values for the isothermal expansion and compression curves
T_iso = np.linspace(T1, T2, npoints)
P_iso_exp = P1 * (T_iso / T1)
P_iso_comp = P2 * (T_iso / T2)

# Plot the Carnot cycle on a P-T graph
fig, ax = plt.subplots()
ax.plot([T1, T2], [P1, P2], 'r', label='Isotherms')
ax.plot([T2, T3], [P2, P3], 'g', label='Adiabats')
ax.plot([T3, T4], [P3, P4], 'r')
ax.plot([T4, T1], [P4, P1], 'g')
ax.plot(T_ad, P_ad_exp, 'b', label='Adiabats')
ax.plot(T_ad, P_ad_comp, 'b')
ax.plot(T_iso, P_iso_exp, 'k', label='Isotherms')
ax.plot(T_iso, P_iso_comp, 'k')
ax.set_xlabel('Temperature (K)')
ax.set_ylabel('Pressure (Pa)')
ax.set_xlim([T_L, T_H])
ax.set_ylim([P_L, P_H])
ax.legend(loc='best')
plt.show()
