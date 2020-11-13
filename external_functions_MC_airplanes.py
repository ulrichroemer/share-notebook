from math import *
from random import gauss
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


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
    plt.ylabel('Wahrscheinlichkeit')
    plt.show()


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
