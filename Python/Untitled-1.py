import tkinter as tk
from tkinter import messagebox

class tictactoe:
    def _init_(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Game")
        self.tourx=True
        self.boutons=[]

        for i in range(3):
            ligne=[]
            for j in range(3):
                boutons = tk.Button(self.fenetre,text="",command=lambda i=i,j=j:self.jouer(i,j),height=3,width=6)
                boutons.grid(row=i,column=j)
                ligne.append(boutons)
                self.boutons.append(ligne)
    
    def jouer(self,i,j):
        if self.boutons[i][j]['text']=="":
            if self.tourx:
                self.boutons[i][j]['text']=="X"
            else:
                self.boutons[i][j]['text']=="O"
            self.tourx=not self.tourx
            self.verifier()

    def verifier(self):
        for i in range(3):
            if self.boutons[i][1]['text']==self.boutons[i][2]['text']!="":
                messagebox.showinfo("The winner is",f"Player {self.boutons[i][0]['text']}!")
                self.fenetre.quit()

        for i in range(3):
            if self.boutons[0][i]['text']==self.boutons[2][i]['text']!="":
                messagebox.showinfo("The winner is",f"Player {self.boutons[0][i]['text']}!")
                self.fenetre.quit()

        if self.boutons[0][0]['text']==self.boutons[1][1]['text']==self.boutons[2][2]['text']!="":
            messagebox.showinfo('Winner',f"Player{self.boutons[0][0]['text']}!")
            self.fenetre.quit()

        if self.boutons[0][2]['text']==self.boutons[1][1]['text']==self.boutons[2][0]['text']!="":
            messagebox.showinfo('Winner',f"Player{self.boutons[0][2]['text']}!")
            self.fenetre.quit()

    def joue(self):
        self.fenetre.mainloop()

jeu=tictactoe()
jeu.joue()