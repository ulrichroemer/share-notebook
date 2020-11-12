import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from matplotlib.patches import Arc


def plot_crew_distribution(mu, sigma):
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma))
    plt.xlabel('$ m_{Crew} $ in [kg]')
    plt.ylabel('Wahrscheinlichkeit')
    plt.show()


def visualization_MC_airplanes():
    r = np.linspace(2.5, 5, 8)
    step = np.zeros(10)

    fig = plt.figure()
    ax = fig.gca()
    earth = plt.Circle((0, 0), 1, color='deepskyblue')
    earth_arc = Arc((0, 0), 2, 2, angle=0.0, theta1=0.0, theta2=360.0, edgecolor='navy', lw=1.5)
    erfolg_visulaisierung = 0

    for i in range(8):
        rand = 370 + 20 * np.random.randn()
        rand_arc = rand
        if rand > 360:
            erfolg_visulaisierung += 1
            rand_arc = 360
        flight = Arc((0, 0), r[i], r[i], angle=90.0, theta1=0.0, theta2=rand_arc)
        ax.add_artist(flight)
        plt.scatter(r[i] / 2 * np.sin(- np.deg2rad(rand)), r[i] / 2 * np.cos(- np.deg2rad(rand)), marker="<",
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
