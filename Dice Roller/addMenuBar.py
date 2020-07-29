# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:20:34 2020

@author: m58527
"""
from tkinter import * 

#%% MENU BAR 
def CreateMenuBar(self,root):
        # CREATE MENU BAR
        self.menubar = Menu(root,font=("times new roman",15,"bold"),activebackground="skyblue")
        # PUT MENU BAR ON ROOT WINDOW
        root.config(menu=self.menubar)
        
        # CREATE FILE MENU
        self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        # ADD A 'RESET' COMMAND
        self.filemenu.add_command(label="Reset fields",accelerator="Ctrl+R",command=self.resetFields)
        # ADD A SEPARATOR BETWEEN EXIT AND THE REST
        self.filemenu.add_separator()
        # ADD EXIT COMMAND
        self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
        # ADD FILE MENU TO MENU BAR
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        
        # CREATE EDIT MENU
        self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        # ADD A 'EXAMPLE' COMMAND
        self.filemenu.add_command(label="Example",accelerator="Ctrl+E")
        # ADD FILE MENU TO MENU BAR
        self.menubar.add_cascade(label="Edit", menu=self.filemenu)
        
        # CREATE VIEW MENU
        self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        # ADD A 'EXAMPLE' COMMAND
        self.filemenu.add_command(label="Example",accelerator="Ctrl+E")
        # ADD FILE MENU TO MENU BAR
        self.menubar.add_cascade(label="View", menu=self.filemenu)
        
        # CREATE DICE WINDOW
        self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        # ADD A 'EXAMPLE' COMMAND
        self.filemenu.add_command(label="Example",accelerator="Ctrl+E")
        # ADD FILE MENU TO MENU BAR
        self.menubar.add_cascade(label="Dice", menu=self.filemenu)
        
        # CREATE SETTINGS WINDOW
        self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
        # ADD A 'EXAMPLE' COMMAND
        self.filemenu.add_command(label="Example",accelerator="Ctrl+E")
        # ADD FILE MENU TO MENU BAR
        self.menubar.add_cascade(label="Settings", menu=self.filemenu)