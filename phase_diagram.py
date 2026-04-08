import numpy as np
import matplotlib.pyplot as plt

def plot_phase(s,alpha,delta,n,g):

    k = np.linspace(0.01,10,200)

    investment = s*(k**alpha)
    break_even = (n+g+delta)*k

    fig,ax = plt.subplots()

    ax.plot(k,investment,label="s f(k)")
    ax.plot(k,break_even,label="(n+g+δ)k")

    ax.legend()

    return fig
