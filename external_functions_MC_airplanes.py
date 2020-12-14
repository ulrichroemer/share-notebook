from math import *
from random import gauss
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
#from scipy.optimize import curve_fit
import numpy as np

def linspace(lo, hi, n):
    x = [(hi - lo) / n * i + lo for i in range(n)]
    
    return x


def norm_pdf(x, mu, sigma):
    f = []
    for i in range(100):
        f.append(1/sqrt(2 * pi * sigma**2) * exp(-(x[i] - mu)**2 / (2 * sigma**2)))
    
    return f


def plot_crew_distribution(mu, sigma):
    x = linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    plt.plot(x, norm_pdf(x, mu, sigma))
    plt.xlabel('$ m_{Crew} $ in [kg]')
    plt.ylabel('Wahrscheinlichkeitsdichte')
    plt.show()

def fit_weight_distribution():
    plt.figure()
    data_x=np.arange(44.5, 110, 10)
    data_y=np.array([1.2, 10.7, 20.1, 24.5, 21, 11.7, 10.8])/100
    k=plt.bar(data_x, data_y, width=9)
    for rect, label in zip(k.patches, ['<50','50-59', '60-69', '70-79', '80-89', '90-99', '>=100']):
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height/2-0.008, label, ha='center', va='bottom')

    # Data for Least-Square Fit with (rescaled) normal distribution
    data_x[-1]=109
    plt.plot(data_x, data_y, 'kx')

    def gaussian(x, a, mean, sigma):
        return a * np.exp(-((x - mean)**2 / (2 * sigma**2)))

    #popt,pcov = curve_fit(gaussian, data_x, data_y, [0.1, 80, 20]) 
    popt = array([ 0.23589765, 77.29540412, 18.2463603 ]) #(mybinder does not support scipy packages..)

    mu = popt[1]
    sigma = popt[2]

    xi = np.linspace(40, 110)
    plt.plot(xi,gaussian(xi,popt[0], mu, sigma), 'r')
    plt.xlim([40, 110])
    plt.show()

    return mu,sigma


def visualization_MC_airplanes():
    r = linspace(2.5, 5, 8)
    fig = plt.figure()
    ax = fig.gca()
    earth = plt.Circle((0, 0), 1, color='deepskyblue')
    earth_arc = Arc((0, 0), 2, 2, angle=0.0, theta1=0.0, theta2=360.0, edgecolor='navy', lw=1.5)
    erfolg_visulaisierung = 0

    for i in range(8):
        rand = gauss(mu=370, sigma=20)
        rand_arc = rand
        if rand > 360:
            erfolg_visulaisierung += 1
            rand_arc = 360
        flight = Arc((0, 0), r[i], r[i], angle=90.0, theta1=0.0, theta2=rand_arc)
        ax.add_artist(flight)
        plt.scatter(r[i] / 2 * sin(- radians(rand)), r[i] / 2 * cos(- radians(rand)), marker="<",
                    edgecolors='k', zorder=10)

    ax.add_artist(earth)
    ax.add_artist(earth_arc)
    ax.set_aspect(1.0)
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.vlines(0, 1, 3, colors='r', linestyles='dashed')
    plt.axis('off')

    plt.show()

    if erfolg_visulaisierung == 0 or (1 < erfolg_visulaisierung < 7) or erfolg_visulaisierung == 8:
        print(str(erfolg_visulaisierung) + " Erfolge und " + str(8 - erfolg_visulaisierung) + " Misserfolge")
    elif erfolg_visulaisierung == 1:
        print(str(erfolg_visulaisierung) + " Erfolg und " + str(8 - erfolg_visulaisierung) + " Misserfolge")
    else:
        print(str(erfolg_visulaisierung) + " Erfolge und " + str(8 - erfolg_visulaisierung) + " Misserfolg")

    print("Relative Häufigkeit eines Erfolges: " + str(erfolg_visulaisierung / 8))


def print_results(N, H_Erfolg, h_Erfolg):
    # Anzeigen der Ergebnisse
    if H_Erfolg == 0 or (1 < H_Erfolg < N - 1) or H_Erfolg == N:
        print(str(H_Erfolg) + " Erfolge und " + str(N - H_Erfolg) + " Misserfolge")
    elif H_Erfolg == 1:
        print(str(H_Erfolg) + " Erfolg und " + str(N - H_Erfolg) + " Misserfolge")
    else:
        print(str(H_Erfolg) + " Erfolge und " + str(N - H_Erfolg) + " Misserfolg")

    print("Relative Häufigkeit eines Erfolges: " + str(h_Erfolg))
