# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:32:13 2020

@author: m58527
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:10:56 2020

@author: m58527
"""

from tkinter import *
from tkinter import ttk
from functools import partial
import numpy as np


class DiceRoller:

    def __init__(self,root):
        
        self.root=root
         
        #%% MENU BAR 
        
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
                
        #%% CREATE FRAMES
        self.topFrame = ttk.Frame(root)
        self.topFrame.config(relief=RIDGE,
                             height=300,
                             width=300)
        self.topFrame.pack(fill=X)
        
        self.bottomFrame = ttk.Frame(root)
        self.bottomFrame.pack()
        self.bottomFrame.config(relief=FLAT,
                                height=500,
                                width=350)    

        #%% CREATE THE WINDOW LABEL
        #FRAME FOR LABELS        
        self.label = ttk.Label(self.topFrame, text = 'Welcome')
        self.label.pack()
        
        #%% CREATE DICE BUTTONS
        #DEFINE VARIABLES FOR DICE BUTTONS
        #ROWS AND COLUMNS
        self.rollCol = 2
        self.rollRowStart = 2
        self.entryCol = self.rollCol-1
        self.answerCol = self.rollCol+1
        self.descCol = self.entryCol-1

        
        #FRAMES
        self.rollButtonFrame = self.bottomFrame

        #BUTTON AND LABEL VARIABLES
        self.entryWidth = 6

#CREATE BUTTONS, LABELS, AND DESCRIPTIONS
        self.diceEntries = []
        self.diceButtons = []
        self.diceLabels = []
        self.diceDescs = []
        
        #DICE
        self.diceNames = ['D4','D6','D8','D10','D12','D20','D100']
        #pictures of dice
        self.dicePics = ['button icons/d4pic.png',
                         'button icons/d6pic.png',
                         'button icons/d8pic.png',
                         'button icons/d10pic.png',
                         'button icons/d12pic.png',
                         'button icons/d20pic.png',
                         'button icons/d100pic.png']
        
        for i in range(len(self.diceNames)):
                        
            #CREATE TEXT FOR DESC
            self.buttonText = 'Roll '+self.diceNames[i]
            self.descText = 'Number of '+self.diceNames[i]+' dice: '
            
            #GET ROW
            self.currentRow = self.rollRowStart+i
            
            #CREATE ENTRY BOX
            self.diceEntry = ttk.Entry(self.rollButtonFrame, 
                                       width=self.entryWidth)
            self.diceEntry.grid(row=self.currentRow,
                                    column=self.entryCol)
    
            
            #CREATE LABELS FOR ANSWERS
            self.diceLabel = ttk.Label(self.rollButtonFrame, 
                                            text = 'Total: 0')
            self.diceLabel.grid(row=self.currentRow,
                                    column=self.answerCol)
            
            #CREATE LABELS FOR DESCRIPTIONS
            self.diceDesc = ttk.Label(self.rollButtonFrame, 
                                      text = self.descText,
                                      width = 22)
            self.diceDesc.grid(row=self.currentRow,
                                   column=self.descCol)
            
            #CREATE BUTTONS
            self.diceButton = ttk.Button(self.rollButtonFrame, 
                                         text = self.buttonText,
                                         command = partial(self.rollDX,i))
            self.diceButton.grid(row=self.currentRow,
                                     column=self.rollCol)
            
            #ADD THINGS TO LISTS
            self.diceEntries.append(self.diceEntry)
            self.diceButtons.append(self.diceButton)
            self.diceLabels.append(self.diceLabel)
            self.diceDescs.append(self.diceDesc)
            
        #OTHER BUTTONS AND STUFF
        #TOTAL
        self.totalRow = len(self.diceNames)+2
        
        self.TotalButton = ttk.Button(self.rollButtonFrame, text = '          Roll All          ',
                                                            command = self.rollAll)     
        self.TotalButton.grid(row=self.totalRow, column = self.rollCol-1, columnspan=2,)
        
        self.TotalLabel = ttk.Label(self.rollButtonFrame, text = 'Total: 0')
        self.TotalLabel.grid(row=self.totalRow, column = self.answerCol)
        
        #RESET
        self.resetCol = self.descCol
        self.resetRow = self.totalRow
        
        self.ResetButton = ttk.Button(self.rollButtonFrame, text = 'RESET FIELDS',
                                                            command = self.resetFields)     
        self.ResetButton.grid(row=self.resetRow, column = self.resetCol)
        
        #RANDOM
        self.randCol = self.resetCol
        self.randRow = self.resetRow+1
        
        self.RandButton = ttk.Button(self.rollButtonFrame, text = 'Random Numbers',
                                                            command = self.fillRandom)     
        self.RandButton.grid(row=self.randRow, column = self.randCol)    

        self.randRow2 = self.randRow+1
        
        self.RandButton2 = ttk.Button(self.rollButtonFrame, text = 'Random Numbers Between:',
                                                            command = self.fillRandomBetween) 
        self.RandButton2.grid(row=self.randRow2, column = self.randCol)  
        
        #entries for random limits
        self.lowerRanLimEntry = ttk.Entry(self.rollButtonFrame, 
                                       width=self.entryWidth)
        self.lowerRanLimEntry.grid(row=self.randRow2,
                                    column=self.randCol+1)
        
        self.upperRanLimEntry = ttk.Entry(self.rollButtonFrame, 
                                        width=self.entryWidth)
        self.upperRanLimEntry.grid(row=self.randRow2,
                                    column=self.randCol+2)
    #%% DICE ROLLER METHODS    
        
    def rollDX(self,i,output=None):
                
        self.currentDiceName = self.diceNames[i]
        self.diceLabel = self.diceLabels[i]
        self.diceEntry = self.diceEntries[i]
        
        #max roll of dice
        max_sides=int(self.currentDiceName.strip('D'))
        #get number of dice from input
        numDice = self.diceEntry.get()
        #check if dice number is blank
        if numDice=='':
            numDice=0
        else:
            numDice = int(numDice)
        #initiate dice total    
        self.diceTotal = 0
        
        #roll each dice, add up total
        for eachDice in range(numDice):
            diceRoll = np.random.randint(1,max_sides+1)
            self.diceTotal = self.diceTotal+diceRoll
        
        if output==None:
            #update label saying you have rolled dice            
            rollText = 'You have rolled '+str(numDice)+' '+ self.currentDiceName +'s.'
            self.label.config(text=rollText)
            self.label.config(wraplength = 250,
                              justify = CENTER,
                              foreground = 'black',
                              background = 'white',
                              font = ('Courier',18))
            
            dicePhoto = PhotoImage(file = self.dicePics[i])
            dicePhoto = dicePhoto.subsample(5,5)
            self.label.img = dicePhoto
            self.label.config(image=dicePhoto,
                              compound = 'left')
        
        #update label with result
        answerText = 'Answer: '+str(self.diceTotal)
        self.diceLabel.config(text = answerText)
        
        if output==1:
            return self.diceTotal
        
    def rollAll(self):
        
        self.totals = []
        
        for die in range(len(self.diceNames)):
            self.totals.append(self.rollDX(die,output=1))
            
        diceTotal = sum(self.totals)
        
        #update label saying you have rolled dice            
        rollText = 'You have rolled all the dice.'
        self.label.config(text=rollText)
        self.label.config(wraplength = 250,
                          justify = CENTER,
                          foreground = 'black',
                          background = 'white',
                          font = ('Courier',18))
        dicePhoto = PhotoImage(file = r'C:\Users\M58527\Documents\Training\GUI\button icons\dice.gif')
        dicePhoto = dicePhoto.subsample(5,5)
        self.label.img = dicePhoto
        self.label.config(image=dicePhoto,
                          compound = 'left')
        
        #update label with result
        answerText = 'Total of all dice: '+str(diceTotal)
        self.TotalLabel.config(text = answerText) 
        
    def resetFields(self):
        for i in range(len(self.diceNames)):
            self.diceEntry = self.diceEntries[i]
            self.diceEntry.delete(0,END)
            
    def fillRandom(self):
            
        for i in range(len(self.diceNames)):
            self.diceEntry = self.diceEntries[i]
            self.diceEntry.delete(0,END)
            self.diceEntry.insert(0,np.random.randint(0,20))
            
    def fillRandomBetween(self):
        self.upperRanLim = self.upperRanLimEntry.get()
        self.lowerRanLim = self.lowerRanLimEntry.get()
        
        if self.upperRanLim == '':
            self.upperRanLim = 10
        if self.lowerRanLim == '':
            self.lowerRanLim = 1 
            
        for i in range(len(self.diceNames)):
            self.diceEntry = self.diceEntries[i]
            self.diceEntry.delete(0,END)
            self.diceEntry.insert(0,np.random.randint(self.lowerRanLim,self.upperRanLim))
            
    #%% MENU BAR FUNCTIONS, ETC
    # Defining Exit Funtion
    def exit(self):
        self.root.destroy()

        
#%% MAIN FUNCTION
        
def main():
    #create parent window
    root = Tk()
    app = DiceRoller(root)
    root.mainloop()
  
#%% CALL MAIN
if __name__ == "__main__": main()