#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
import json 
# json ist für das Speichern zuständig

def studium_daten():
    name = eingabe_name.get()
    studiengang = eingabe_studiengang.get()
    modul = eingabe_modul.get()
    prüfungsleistung = eingabe_prüfungsleistung.get()
    semester = eingabe_semester.get()
    
    if name or studiengang or modul or semester or prüfungsleistung:
        ausgabe.config(text=f"Name: {name}, Studiengang: {studiengang} , Modul: {modul} , Semester: {semester} , Prüfungsleistung: {prüfungsleistung} !")
   
    else:
        messagebox.showwarning("Eingabefehler", "Bitte füllen Sie die Felder aus.")

#klassen: Studiengang, Semester. Modul, Prüfungsleistungen(klausurnote)

class Pruefungsleistung:
    """Abstrakte Basisklasse: Jede Prüfung kann eine Note berechnen"""
#docstrings für help commands

class Klausur(Pruefungsleistung):
    """Note wird aus den erreichten Punkten berechnet."""

    def __init__(self, datum=None, dauer_min=90, punkte=None, max_punkte=100):
        super().__init__(datum) #super ruft methoden von anderen klassen auf
        self.dauer_min = dauer_min
        self.punkte = punkte
        self.max_punkte = max_punkte
#standardmäßges klausurformat mit datum integriert, dauer 90min
    def berechne_note(self):
        if self.punkte is None:
            return None
        prozent = self.punkte / self.max_punkte * 100
#einfache berechnung für die berechnung der noten, beispielpunkte:
        if prozent >= 90:
            return 1.0
        if prozent >= 80:
            return 2.0
        if prozent >= 70:
            return 3.0
        if prozent >= 50:
            return 4.0
        return 5.0
#sagt einem ob man bestanden hat oder nicht
    def note_prüfen(prozent):
        if prozent >= 50:
            print("Sie haben bestanden!")
        else:
            print("Sie sind durchgefallen")


class Modul:
    def __init__(self, name, ects, pruefung):
        self.name = name
        self.ects = ects
        self.pruefung = pruefung  # genau eine Prüfungsleistung

class Semester:
    def __init__(self, nummer):
        self.nummer = nummer
        self.module = []

    def modul_hinzufuegen(self, modul):
        self.module.append(modul)

class Studiengang:
    def __init__(self, name, ects_gesamt, ziel_note):
        self.name = name
        self.ects_gesamt = ects_gesamt
        self.ziel_note = ziel_note
        self.semester = [] #leere liste



# Hauptfenster erstellen
fenster = tk.Tk()
fenster.title("Studium UI - Dein Studium! (Name / M.nummer)")
fenster.geometry("700x600")

#Beispiele, wie es am ende aussehen kann
tk.Label(fenster, text="Studiengang: Informatik").pack(pady=5)
tk.Label(fenster, text="Semester: 1 ").pack(pady=5)
tk.Label(fenster, text="Module: - - - - - Note:").pack(pady=5)
tk.Label(fenster, text="Mathematik - Klausur1: 3.5 ").pack(pady=5)
tk.Label(fenster, text="Python - Portfolio1: 2.6 ").pack(pady=5)
tk.Label(fenster, text="Prüfungen: (P1,...) - Note:").pack(pady=5)
tk.Label(fenster, text="Notenschnitt: 2.5 - Ziel: 2.0 ").pack(pady=5)

# ausgabeeee
ausgabe = tk.Label(fenster, text="")
ausgabe.pack()

# GUI starten
fenster.mainloop()


# In[ ]:




