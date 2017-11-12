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
            self, variable=self.elitism, text="Elitisme")
        self.keep_benchmark = tk.IntVar()
        self.cb_benchmark = tk.Checkbutton(
            self, variable=self.keep_benchmark, text="Enregistrer les données")
        # Labels
        self.l_title = tk.Label(self, text="Choisir les paramètres")
        self.l_nbinds = tk.Label(self, text="Nombre d'individus")
        self.l_mut = tk.Label(self, text="Fréquence mutation")
        self.l_gen = tk.Label(self, text="Générations")
        self.l_meth = tk.Label(self, text="Méthode de selection")
        self.l_mut_meth = tk.Label(self, text="Méthode de mutation")
        self.l_carte = tk.Label(self, text="Carte")
        self.l_result = tk.Label(self)
        # Text fields
        self.f_nbinds = tk.Entry(self)
        self.f_mut = tk.Entry(self)
        self.f_gen = tk.Entry(self)
        # Option menu
        select_mut_list = ['swap', 'scramble']
        self.select_mut = tk.StringVar()
        self.select_mut.set('swap')
        self.menu_mut = tk.OptionMenu(
            self, self.select_mut, *select_mut_list)
        select_meth_list = ['roulette', 'tournoi']
        self.select_meth = tk.StringVar()
        self.select_meth.set('tournoi')
        self.menu_meth = tk.OptionMenu(
            self, self.select_meth, *select_meth_list)
        # Buttons
        self.btn_carte = tk.Button(
            self, text='Choisir carte', command=self.openfile)
        self.btn_exit = tk.Button(self, text="Quitter", command=exit)
        self.btn_go = tk.Button(self, text="Lancer", command=self.run)
        self.place_elements()

    def openfile(self):
        self.carte_name = tk.filedialog.askopenfilename(
            filetypes=[('CSV files', '*.csv')])

    def place_elements(self):
        """
        Organise tous les éléments sur la fenetre
        """
        self.l_title.grid(row=0, column=1)
        self.l_nbinds.grid(row=1, column=0)
        self.f_nbinds.grid(row=1, column=1)
        self.l_mut.grid(row=2, column=0)
        self.f_mut.grid(row=2, column=1)
        self.l_gen.grid(row=3, column=0)
        self.f_gen.grid(row=3, column=1)
        self.l_meth.grid(row=4, column=0)
        self.menu_meth.grid(row=4, column=1)
        self.l_mut_meth.grid(row=5, column=0)
        self.menu_mut.grid(row=5, column=1)
        self.l_carte.grid(row=6, column=0)
        self.btn_carte.grid(row=6, column=1)
        self.cb_elitism.grid(row=7, column=0)
        self.cb_benchmark.grid(row=7, column=1)
        self.btn_go.grid(row=8, column=0, pady=5)
        self.btn_exit.grid(row=8, column=1, pady=5)
        self.l_result.grid(row=9, column=0)

    def animer(self, i):
        """
        Fonction d'animation
        """
        # Evolution en fonction des paramètres
        elitism = True if self.elitism == 1 else False
        self.p1.evoluer(int(self.f_mut.get()),
                        self.select_meth.get(), self.select_mut.get(), elitism, 5)
        nx1, ny1 = self.p1.meilleurChemin.to_plot()
        plt.title('Génération: ' + str(self.p1.generation))
        self.graph1.set_data(nx1, ny1)
        # Longueur du chemin courant
        curr_best = self.p1.meilleurFitness
        # Si on a atteint la generation cible
        if self.p1.generation == int(self.f_gen.get()):
            # Calculer le taux d'amélioration
            self.pct_imp = round((1 - (curr_best / self.init_dist)) * 100, 2)
            # L'afficher
            self.l_result.config(
                text="Taux d'amélioration: " + str(self.pct_imp) + '%')
            if self.keep_benchmark.get() == 1:
                self.benchmark()

    def benchmark(self):
        """
        Ecrit le taux d'amélioration
        en fonction des paramètres courants
        dans un fichier
        """
        opts = '{0}, {1}, {2}, {3}, {4}, {5}, {6}\n'.format(
            self.f_nbinds.get(),
            self.f_gen.get(),
            self.f_mut.get(),
            self.select_meth.get(),
            self.select_mut.get(),
            self.elitism.get(),
            self.pct_imp
        )
        with open('data.csv', 'a') as f:
            f.write(opts)

    def run(self):
        """
        Initialise une population et lance
        l'animation.
        """
        self.p1 = Population(int(self.f_nbinds.get()), 0, self.carte_name)
        self.init_dist = self.p1.meilleurFitness
        x1, y1 = self.p1.meilleurChemin.to_plot()
        fi = plt.figure()
        plt.title('Génération: 1')
        plt.axes().set_aspect('equal', 'datalim')
        plt.scatter(x1, y1)
        self.graph1, = plt.plot(x1, y1, 'r')
        ani = FuncAnimation(fi, self.animer, interval=10, repeat=False,
                            frames=int(self.f_gen.get()) - 2)
        plt.show()


app = ClientTK()
app.mainloop()
