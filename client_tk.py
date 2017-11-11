# coding: utf-8

import tkinter as tk
from Population import Population
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


class ClientTK(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        # CheckBoxes
        self.elitism = tk.IntVar()
        self.cb_elitism = tk.Checkbutton(
            self, variable=self.elitism, text="elitisme")
        self.cb_benchmark = tk.Checkbutton(self, text="benchmark")
        # Labels
        self.l_nbinds = tk.Label(self, text="Nombre d'individus")
        self.l_mut = tk.Label(self, text="Fréquence mutation")
        self.l_gen = tk.Label(self, text="Nombre générations cible")
        # Text fields
        self.f_nbinds = tk.Entry(self)
        self.f_mut = tk.Entry(self)
        self.f_gen = tk.Entry(self)
        # Option menu
        select_meth_list = ['roulette', 'tournoi']
        self.select_meth = tk.StringVar()
        self.select_meth.set('tournoi')
        self.menu_meth = tk.OptionMenu(
            self, self.select_meth, *select_meth_list)

        # Buttons
        self.btn_exit = tk.Button(self, text="Quitter", command=exit)
        self.btn_go = tk.Button(self, text="Lancer", command=self.run)
        # Pack
        self.l_nbinds.pack()
        self.f_nbinds.pack()
        self.l_mut.pack()
        self.f_mut.pack()
        self.l_gen.pack()
        self.f_gen.pack()
        self.cb_elitism.pack()
        self.cb_benchmark.pack()
        self.menu_meth.pack()
        self.btn_exit.pack()
        self.btn_go.pack()

    def animer(self, i):
        if self.select_meth.get() == 'tournoi':
            if self.elitism.get():
                self.p1.evoluer_tournoi_garder_parent(
                    10, int(self.f_mut.get()))
            else:
                self.p1.evoluer_tournoi(int(self.f_mut.get()))
        else:
            if self.elitism.get():
                self.p1.evoluer_roulette_garder_parent(
                    10, int(self.f_mut.get()))
            else:
                self.p1.evoluer_roulette(self.f_mut.get())
        nx1, ny1 = self.p1.meilleurChemin.to_plot()
        plt.title('Génération: ' + str(self.p1.generation))
        self.graph1.set_data(nx1, ny1)

    def run(self):
        self.p1 = Population(int(self.f_nbinds.get()), 0, 'cercle.csv')
        init_dist = self.p1.meilleurFitness
        x1, y1 = self.p1.meilleurChemin.to_plot()
        fi = plt.figure()
        plt.title('Génération: 1')
        plt.axes().set_aspect('equal', 'datalim')
        plt.scatter(x1, y1)
        self.graph1, = plt.plot(x1, y1, 'r')
        ani = FuncAnimation(fi, self.animer, interval=10, repeat=False,
                            frames=int(self.f_gen.get()) - 2)
        plt.show()
        plt.close()
        end_dist = self.p1.meilleurFitness


app = ClientTK()
app.mainloop()
