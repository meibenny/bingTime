"""
Create GUI for BingTime.
"""

from tkinter import *
import audioPlay
import images
from dictionaries import *
import turtle

#set coordinates for turtle movement
lotT = (-240, 0)
C4 = (-300, -50)
dickinsonDining = (-125, 55)
UU = (-25, 75)
EB = (50, 80)
EBBartle = (110, 80)
BartleParking = (235, 70)
BartleLH = (300, 50)
LH = (340, 40)
lotL = (410, 0)
ConnectorRd = (450, -40)
AA = (460, -70)
AB = (465, -140)
PhysFac = (440, -230)
sciIIIV = (375, -285)
lotF1 = (335, -315)
sciIV = (305, -325)
sci = (275, -275)
iroquois = (-25, 150)
app1 = (135, 160)
app2 = (130, 190)
app3 = (160, 195)
app4 = (190, 210)
h1 = (395, 70)
h2 = (395, 130)
FABartle = (110, 0)
Bartle = (140, 0)
EBFA = (90, 0)
FA = (90, -80)

#initiate GUI code
class bingTimeGui:
    def __init__(self):

        #create instance variables
        self.__sCor = "" #start coordinate
        self.__eCor = "" #end coordinate
        self.__t = "" #dummy variable for turtle object
        self.__s = "" #dummy variable for turtle screen method

        #create main window
        self.__root = Toplevel()
        self.__win = Tk()
        (self.__win).title("bingTime") #set name for window


        #Turtle Test
        #**************************************************************
        canvas1 = Canvas(self.__root, background = "black", width = 1024, height = 768)
        photo = PhotoImage(file = "BUBRAIN.gif") #set photo 
        canvas1.create_image((514,386),image = photo) #set canvas background
        canvas1.pack()#pack canvas

        #create turtle screen
        self.__t1 = turtle.TurtleScreen(canvas1)
        self.__t1.bgpic("BUBRAIN.gif")
##        self.__t = turtle.RawTurtle(self.__t1)
##        self.__t.color("red")

        #**************************************************************

        #create label to display travel time
        #travel time static label
        self.__travelTimeLabel = Label(self.__win, text = 'Travel Time:')
        self.__travelTimeLabel.grid(row = 5, column = 1)
        self.__travelTime = StringVar(self.__win)
        self.__travelTimeText = Message(self.__win, textvariable = self.__travelTime,\
                                      width = 20)
        self.__travelTimeText.grid(row = 5, column = 2)
        
        #dropdown menu box creation
        #*******************************************************
        #create dropdown menu
        menubar = Menu(self.__win)
        (self.__win).config(menu = menubar)
        
        optionsMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Options", menu = optionsMenu)
        #**********************************************************
        #show map on event from dropdown menu
        #invokes showMap method
        #*******************************************************
        
        optionsMenu.add_command(label = "Show Map", command = (self.showMap))


        #create option menu of starting points
        #**************************************************************
        variableStart = StringVar(self.__win)
        variableStart.set("From") # default value
        start = OptionMenu(self.__win, variableStart, "C4", "Appalachian", "CIW Dining Hall",\
                     "Hinman Dining Hall", "Lecture Hall", "Science Buildings",\
                     "Bartle Library", "Fine Arts", "Union(Old)", command = self.startVar)
        start.grid(row = 2, column = 1)

        #create option menu of ending points
        #****************************************************************
        variableEnd = StringVar(self.__win)
        variableEnd.set("To") # default value
        end = OptionMenu(self.__win, variableEnd, "C4", "Appalachian", "CIW Dining Hall",\
                     "Hinman Dining Hall", "Lecture Hall", "Science Buildings",\
                     "Bartle Library", "Fine Arts", "Union(Old)", command = self.endVar)  
        end.grid(row = 2, column = 2)

        #*******************************************************
        #create combobox to play music
        musicVariable = StringVar(self.__win)
        musicVariable.set("Music") #default value of musicOptionMenu
        musicOptionMenu = OptionMenu(self.__win, musicVariable , \
                                         "simpsons.wav", "capt_midnight.wav", "herewego.wav",\
                                     "highscore.wav", "mario_01.wav", "mario_08.wav",\
                                     "scooby_hello.wav", "wumbo.wav", command = self.playAudio)
        musicOptionMenu.grid(row = 1, column = 1)

        #*******************************************************
        #create button to submit locations
        submitButton = Button(self.__win, text = "Submit", command = \
                              self.moveTurtle)
        submitButton.grid(row = 2, column = 3)
        
        mainloop()

        

    #create method to display messagebox
    #pops up messagebox
    def message(self):
        messagebox.showinfo("BingTime", "BingTime MuthaFuckers")

    #create method to display map
    #invokes Image from images module
    #invokes draw method in Image module
    def showMap(self):
        self.message()
        brainMap = images.Image("BUBRAIN.gif")
        images.Image.draw(brainMap)

    #create method to play audio
    #invokes playAudio from audioPlayTest module
    def playAudio(self, fileName):
        audioPlay.playAudio(fileName)

    #set start variable for movement
    def startVar(self, var):
        self.__sCor = var
        #print(sVar)
        
    #set end variable for movement
    def endVar(self, var):
        self.__eCor = var
        #print(eVar)

    # define move turtle function
    def moveTurtle(self):
        #print("You've entered moveTurtle")
##        print("The sVar is", self.__sCor)
##        print("The eVar is", self.__eCor)
        time = getTime((self.__sCor), (self.__eCor))
##        print(time)
        self.__travelTime.set(time)
##        print(getTime(self.__sCor, self.__eCor))
##        print(self.__travelTime)
       
        #if self.__sCor == start point, then use function for that start point
        #use function to route to end point
        if self.__sCor == "C4":
            print("Entered C4 Path")
            self.fromC4(self.__eCor)
        elif self.__sCor == "Appalachian":
            self.fromApp(self.__eCor)
        elif self.__sCor == "CIW Dining Hall":
            self.fromCIW(self.__eCor)
        elif self.__sCor == "Hinman Dining Hall":
            self.fromHin(self.__eCor)
        elif self.__sCor == "Lecture Hall":
            self.fromLH(self.__eCor)
        elif self.__sCor == "Science Buildings":
            self.fromSci(self.__eCor)
        elif self.__sCor == "Bartle Library":
            self.fromBartle(self.__eCor)
        elif self.__sCor == "Fine Arts":
            self.fromFA(self.__eCor)
        elif self.__sCor == "Union(Old)":
            self.fromUU(self.__eCor)
        else:
            t = turtle.RawTurtle(self.__t1)
            t.shape("turtle")
            t.color("red")
            t.pensize(3)
            t.speed(1) #lowest speed
            t.circle(20)
            turtle.done()
   




#Everything below this point are instructions for turtle movement
#See coordinates as defined above bingTimeGUI
#*******************************************************************************
    def fromC4(self, destination):
        t = turtle.RawTurtle(self.__t1)
        t.shape("turtle")
        t.color("red")
        t.pensize(3)
        t.speed(1) #lowest speed
        t.up() #pen up
        t.goto(C4)
        t.down()
        if destination == "C4":
            t.circle(5)
            ##print("C4 - Success")
            s.bgpic("BUBRAIN.gif")
            turtle.done()
        elif destination == "Appalachian":
            t.goto(lotT)
            t.goto(dickinsonDining)
            t.goto(UU)
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(app1)
            t.goto(app2)
            t.goto(app3)
            t.goto(app4)
            t.circle(5)
            ##print("App - Success")
            turtle.done()
        elif destination == "CIW Dining Hall":
            t.goto(lotT)
            t.goto(dickinsonDining)
            t.goto(UU)
            t.goto(iroquois)
            t.circle(5)
            ##print("CIW - Success")
            turtle.done()
        elif destination == "Union(Old)":
            t.goto(lotT)
            t.goto(dickinsonDining)
            t.goto(UU)
            t.circle(5)
            ##print("Union(Old) - Success")
            turtle.done()
        elif destination == "Bartle Library":
            t.goto(lotT)
            t.goto(dickinsonDining)
            t.goto(UU)
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(FABartle)
            t.goto(Bartle)
            t.circle(5)
            ##print("Bartle - Success")
            turtle.done()
        elif destination == "Fine Arts":
            t.goto(lotT)
            t.goto(dickinsonDining)
            t.goto(UU)
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(FABartle)
            t.goto(EBFA)
            t.goto(FA)
            t.circle(5)
            ##print("Fine Arts - Success")
            turtle.done()
        elif destination == "Lecture Hall":
            t.goto(lotT)
            t.goto(dickinsonDining)
            t.goto(UU)
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.circle(5)
            ##print("LH - Success")
            turtle.done()
        elif destination == "Hinman Dining Hall":
            t.goto(lotT)
            t.goto(dickinsonDining)
            t.goto(UU)
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.goto(h1)
            t.goto(h2)
            t.circle(5)
            ##print("Hinman - Success")
            turtle.done()
        elif destination == "Science Buildings":
            t.goto(lotT)
            t.goto(dickinsonDining)
            t.goto(UU)
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.goto(lotL)
            t.goto(ConnectorRd)
            t.goto(AA)
            t.goto(AB)
            t.goto(PhysFac)
            t.goto(sciIIIV)
            t.goto(lotF1)
            t.goto(sciIV)
            t.goto(sci)
            t.circle(5)
            ##print("Sci - Success")
            turtle.done()
        else:
            t.circle(20)
            ##print("Error")
            turtle.done()

#*************************************************************
    def fromApp(self, destination):
        t = turtle.RawTurtle(self.__t1)
        t.shape("turtle")
        t.color("red")
        t.pensize(3)
        t.speed(1) #lowest speed
        t.up() #pen up
        t.goto(app4)
        t.down()
        if destination == "C4":
            t.goto(app3)
            t.goto(app2)
            t.goto(app1)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.goto(dickinsonDining)
            t.goto(lotT)
            t.goto(C4)
            t.circle(5)
            ##print("C4 - Success")
            turtle.done()
        elif destination == "Applachian":
            t.circle(5)
            #print("App - Success")
            turtle.done()
        elif destination == "CIW Dining Hall":
            t.goto(app3)
            t.goto(app2)
            t.goto(app1)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.goto(iroquois)
            t.circle(5)
            ##print("CIW - Success")
            turtle.done()
        elif destination == "Hinman Dining Hall":
            t.goto(app3)
            t.goto(app2)
            t.goto(app1)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(LH)
            t.goto(h1)
            t.goto(h2)
            t.circle(5)
            ##print("Hinman - Success")
            turtle.done()
        elif destination == "Lecture Hall":
            t.goto(app3)
            t.goto(app2)
            t.goto(app1)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(LH)
            t.circle(5)
            ##print("LH - Success")
            turtle.done()
        elif destination == "Science Buildings":
            t.goto(app3)
            t.goto(app2)
            t.goto(app1)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(LH)
            t.goto(lotL)
            t.goto(ConnectorRd)
            t.goto(AA)
            t.goto(AB)
            t.goto(PhysFac)
            t.goto(sciIIIV)
            t.goto(lotF1)
            t.goto(sciIV)
            t.goto(sci)
            t.circle(5)
            ##print("Sci - Success")
            turtle.done()
        elif destination == "Bartle Library":
            t.goto(app3)
            t.goto(app2)
            t.goto(app1)
            t.goto(EBBartle)
            t.goto(FABartle)
            t.goto(Bartle)
            t.circle(5)
            ##print("Bartle - Success")
            turtle.done()
        elif destination == "Fine Arts":
            t.goto(app3)
            t.goto(app2)
            t.goto(app1)
            t.goto(EBBartle)
            t.goto(FABartle)
            t.goto(EBFA)
            t.goto(FA)
            t.circle(5)
            ##print("Fine Arts - Success")
            turtle.done()
        elif destination == "Union(Old)":
            t.goto(app3)
            t.goto(app2)
            t.goto(app1)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.circle(5)
            ##print("Union(Old) - Success")
            turtle.done()
        else:
            t.circle(20)
            ##print("Error")
            turtle.done()


#*************************************************************
    def fromCIW(self, destination):
        t = turtle.RawTurtle(self.__t1)
        t.shape("turtle")
        t.color("red")
        t.pensize(3)
        t.speed(1) #lowest speed
        t.up() #pen up
        t.goto(iroquois)
        t.down()
        if destination == "C4":
            t.goto(UU)
            t.goto(dickinsonDining)
            t.goto(lotT)
            t.goto(C4)
            t.circle(5)
            ##print("C4 - Success")
            turtle.done()
        elif destination == "Appalachian":
            t.goto(UU)
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(app1)
            t.goto(app2)
            t.goto(app3)
            t.goto(app4)
            t.circle(5)
            ##print("App - Success")
            turtle.done()
        elif destination == "CIW Dining Hall":
            t.circle(5)
            ##print("CIW - Success")
            turtle.done()
        elif destination == "Hinman Dining Hall":
            t.goto(UU)
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.goto(h1)
            t.goto(h2)
            t.circle(5)
            ##print("Hinman - Success")
            turtle.done()
        elif destination == "Lecture Hall":
            t.goto(UU)
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.circle(5)
            ##print("LH - Success")
            turtle.done()
        elif destination == "Science Buildings":
            t.goto(UU)
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(LH)
            t.goto(lotL)
            t.goto(ConnectorRd)
            t.goto(AA)
            t.goto(AB)
            t.goto(PhysFac)
            t.goto(sciIIIV)
            t.goto(lotF1)
            t.goto(sciIV)
            t.goto(sci)
            t.circle(5)
            ##print("Sci - Success")
            turtle.done()
        elif destination == "Bartle Library":
            t.goto(UU)
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(FABartle)
            t.goto(Bartle)
            t.circle(5)
            ##print("Bartle - Success")
            turtle.done()
        elif destination == "Fine Arts":
            t.goto(UU)
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(FABartle)
            t.goto(EBFA)
            t.goto(FA)
            t.circle(5)
            ##print("FA - Success")
            turtle.done()
        elif destination == "Union(Old)":
            t.goto(UU)
            t.circle(5)
            ##print("Union(Old) - Success")
            turtle.done()
        else:
            t.circle(20)
            ##print("Error")
            turtle.done()

#*******************************************************************
    def fromHin(self, destination):
        t = turtle.RawTurtle(self.__t1)
        t.shape("turtle")
        t.color("red")
        t.pensize(3)
        t.speed(1) #lowest speed
        t.up() #pen up
        t.goto(h2)
        t.down()
        if destination == "C4":
            t.goto(h1)
            t.goto(LH)
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.goto(dickinsonDining)
            t.goto(lotT)
            t.goto(C4)
            t.circle(5)
            #print("C4 - Success")
            turtle.done()
        elif destination == "Appalachian":
            t.goto(h1)
            t.goto(LH)
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(app1)
            t.goto(app2)
            t.goto(app3)
            t.goto(app4)
            t.circle(5)
            #print("App - Success")
            turtle.done()
        elif destination == "CIW Dining Hall":
            t.goto(h1)
            t.goto(LH)
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.goto(iroquois)
            t.circle(5)
            #print("CIW - Success")
            turtle.done()
        elif destination == "Hinman Dining Hall":
            t.circle(5)
            #print("Hinman - Success")
            turtle.done()
        elif destination == "Lecture Hall":
            t.goto(h1)
            t.goto(LH)
            t.circle(5)
            #print("LH - Success")
            turtle.done()
        elif destination == "Science Buildings":
            t.goto(h1)
            t.goto(LH)
            t.goto(lotL)
            t.goto(ConnectorRd)
            t.goto(AA)
            t.goto(AB)
            t.goto(PhysFac)
            t.goto(sciIIIV)
            t.goto(lotF1)
            t.goto(sciIV)
            t.goto(sci)
            t.circle(5)
            #print("Sci - Success")
            turtle.done()
        elif destination == "Bartle Library":
            t.goto(h1)
            t.goto(LH)
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(FABartle)
            t.goto(Bartle)
            t.circle(5)
            #print("Bartle - Success")
            turtle.done()
        elif destination == "Fine Arts":
            t.goto(h1)
            t.goto(LH)
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(FABartle)
            t.goto(EBFA)
            t.goto(FA)
            t.circle(5)
            #print("FA - Success")
            turtle.done()
        elif destination == "Union(Old)":
            t.goto(h1)
            t.goto(LH)
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.circle(5)
            #print("UU - Success")
            turtle.done()
        else:
            t.circle(20)
            #print("Error")
            turtle.done()

#*******************************************************************
    def fromLH(self, destination):
        t = turtle.RawTurtle(self.__t1)
        t.shape("turtle")
        t.color("red")
        t.pensize(3)
        t.speed(1) #lowest speed
        t.up() #pen up
        t.goto(LH)
        t.down()
        if destination == "C4":
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.goto(dickinsonDining)
            t.goto(lotT)
            t.goto(C4)
            t.circle(5)
            ##print("C4 - Success")
            turtle.done()
        elif destination == "Appalachian":
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(app1)
            t.goto(app2)
            t.goto(app3)
            t.goto(app4)
            t.circle(5)
            ##print("App - Success")
            turtle.done()
        elif destination == "CIW Dining Hall":
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.goto(iroquois)
            t.circle(5)
            ##print("CIW - Success")
            turtle.done()
        elif destination == "Hinman Dining Hall":
            t.goto(h1)
            t.goto(h2)
            t.circle(5)
            ##print("Hinman - Success")
            turtle.done()
        elif destination == "Lecture Hall":
            t.circle(5)
            ##print("LH - Success")
            turtle.done()
        elif destination == "Science Buildings":
            t.goto(lotL)
            t.goto(ConnectorRd)
            t.goto(AA)
            t.goto(AB)
            t.goto(PhysFac)
            t.goto(sciIIIV)
            t.goto(lotF1)
            t.goto(sciIV)
            t.goto(sci)
            t.circle(5)
            #print("Sci - Success")
            turtle.done()
        elif destination == "Bartle Library":
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(FABartle)
            t.goto(Bartle)
            t.circle(5)
            #print("Bartle - Success")
            turtle.done()
        elif destination == "Fine Arts":
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(FABartle)
            t.goto(EBFA)
            t.goto(FA)
            t.circle(5)
            #print("FA - Success")
            turtle.done()
        elif destination == "Union(Old)":
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.circle(5)
            #print("UU - Success")
            turtle.done()
        else:
            t.circle(20)
            #print("Error")
            turtle.done()

#*******************************************************************
    def fromSci(self, destination):
        t = turtle.RawTurtle(self.__t1)
        t.shape("turtle")
        t.color("red")
        t.pensize(3)
        t.speed(1) #lowest speed
        t.up() #pen up
        t.goto(sci)
        t.down()
        if destination == "C4":
            t.goto(sciIV)
            t.goto(sciIIIV)
            t.goto(PhysFac)
            t.goto(AB)
            t.goto(AA)
            t.goto(ConnectorRd)
            t.goto(lotL)
            t.goto(LH)
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.goto(dickinsonDining)
            t.goto(lotT)
            t.goto(C4)
            t.circle(5)
            #print("C4 - Success")
            turtle.done()
        elif destination == "Appalachian":
            t.goto(sciIV)
            t.goto(sciIIIV)
            t.goto(PhysFac)
            t.goto(AB)
            t.goto(AA)
            t.goto(ConnectorRd)
            t.goto(lotL)
            t.goto(LH)
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(app1)
            t.goto(app2)
            t.goto(app3)
            t.goto(app4)
            t.circle(5)
            #print("App - Success")
            turtle.done()
        elif destination == "CIW Dining Hall":
            t.goto(sciIV)
            t.goto(sciIIIV)
            t.goto(PhysFac)
            t.goto(AB)
            t.goto(AA)
            t.goto(ConnectorRd)
            t.goto(lotL)
            t.goto(LH)
            t.goto(BartleLH)
            t.goto(BartleParking)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.goto(iroquois)
            t.circle(5)
            #print("CIW - Success")
            turtle.done()
        elif destination == "Hinman Dining Hall":
            t.goto(sciIV)
            t.goto(sciIIIV)
            t.goto(PhysFac)
            t.goto(AB)
            t.goto(AA)
            t.goto(ConnectorRd)
            t.goto(lotL)
            t.goto(LH)
            t.goto(h1)
            t.goto(h2)
            t.circle(5)
            #print("Hinman - Success")
            turtle.done()
        elif destination == "Lecture Hall":
            t.goto(sciIV)
            t.goto(sciIIIV)
            t.goto(PhysFac)
            t.goto(AB)
            t.goto(AA)
            t.goto(ConnectorRd)
            t.goto(lotL)
            t.goto(LH)
            t.circle(5)
            #print("LH - Success")
            turtle.done()
        elif destination == "Science Buildings":
            t.circle(5)
            #print("Sci - Success")
            turtle.done()
        else:
            t.circle(20)
            #print("Error")
            turtle.done()

#*******************************************************************
    def fromBartle(self, destination):
        t = turtle.RawTurtle(self.__t1)
        t.shape("turtle")
        t.color("red")
        t.pensize(3)
        t.speed(1) #lowest speed
        t.up() #pen up
        t.goto(Bartle)
        t.down()
        if destination == "C4":
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.goto(dickinsonDining)
            t.goto(lotT)
            t.goto(C4)
            t.circle(5)
            ##print("C4 - Success")
            turtle.done()
        elif destination == "Appalachian":
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(app1)
            t.goto(app2)
            t.goto(app3)
            t.goto(app4)
            t.circle(5)
            ##print("App - Success")
            turtle.done()
        elif destination == "CIW Dining Hall":
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(UU)
            t.goto(iroquois)
            t.circle(5)
            ##print("CIW - Success")
            turtle.done()
        elif destination == "Hinman Dining Hall":
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.goto(h1)
            t.goto(h2)
            t.circle(5)
            ##print("Hinman - Success")
            turtle.done()
        elif destination == "Lecture Hall":
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.circle(5)
            ##print("LH - Success")
            turtle.done()
        elif destination == "Science Buildings":
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.goto(lotL)
            t.goto(ConnectorRd)
            t.goto(AA)
            t.goto(AB)
            t.goto(PhysFac)
            t.goto(sciIIIV)
            t.goto(lotF1)
            t.goto(sciIV)
            t.goto(sci)
            t.circle(5)
            ##print("Sci - Success")
            turtle.done()
        elif destination == "Bartle Library":
            t.circle(5)
            ##print("Bartle - Success")
            turtle.done()
        elif destination == "Fine Arts":
            t.goto(FABartle)
            t.goto(EBFA)
            t.goto(FA)
            t.circle(5)
            ##print("FA - Success")
            turtle.done()
        elif destination == "Union(Old)":
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.circle(5)
            ##print("UU - Success")
            turtle.done()
        else:
            t.circle(20)
            ##print("Error")
            turtle.done()

#*******************************************************************
    def fromFA(self, destination):
        t = turtle.RawTurtle(self.__t1)
        t.shape("turtle")
        t.color("red")
        t.pensize(3)
        t.speed(1) #lowest speed
        t.up() #pen up
        t.goto(FA)
        t.down()
        if destination == "C4":
            t.goto(EBFA)
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.goto(dickinsonDining)
            t.goto(lotT)
            t.goto(C4)
            t.circle(5)
            ##print("C4 - Success")
            turtle.done()
        elif destination == "Appalachian":
            t.goto(EBFA)
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(app1)
            t.goto(app2)
            t.goto(app3)
            t.goto(app4)
            t.circle(5)
            ##print("App - Success")
            turtle.done()
        elif destination == "CIW Dining Hall":
            t.goto(EBFA)
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.goto(iroquois)
            t.circle(5)
            ##print("CIW - Success")
            turtle.done()
        elif destination == "Hinman Dining Hall":
            t.goto(EBFA)
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.goto(h1)
            t.goto(h2)
            t.circle(5)
            ##print("Hinman - Success")
            turtle.done()
        elif destination == "Lecture Hall":
            t.goto(EBFA)
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.circle(5)
            ##print("LH - Success")
            turtle.done()
        elif destination == "Science Buildings":
            t.goto(EBFA)
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.goto(lotL)
            t.goto(ConnectorRd)
            t.goto(AA)
            t.goto(AB)
            t.goto(PhysFac)
            t.goto(sciIIIV)
            t.goto(lotF1)
            t.goto(sciIV)
            t.goto(sci)
            t.circle(5)
            ##print("Sci - Success")
            turtle.done()
        elif destination == "Bartle Library":
            t.goto(EBFA)
            t.goto(FABartle)
            t.goto(Bartle)
            t.circle(5)
            ##print("Bartle - Success")
            turtle.done()
        elif destination == "Fine Arts":
            t.circle(5)
            ##print("FA - Success")
            turtle.done()
        elif destination == "Union(Old)":
            t.goto(EBFA)
            t.goto(FABartle)
            t.goto(EBBartle)
            t.goto(EB)
            t.goto(UU)
            t.circle(5)
            ##print("UU - Success")
            turtle.done()
        else:
            t.circle(20)
            ##print("Error")
            turtle.done()

#*******************************************************************
    def fromUU(self, destination):
        t = turtle.RawTurtle(self.__t1)
        t.shape("turtle")
        t.color("red")
        t.pensize(3)
        t.speed(1) #lowest speed
        t.up() #pen up
        t.goto(UU)
        t.down()
        if destination == "C4":
            t.goto(dickinsonDining)
            t.goto(lotT)
            t.goto(C4)
            t.circle(5)
            ##print("C4 - Success")
            turtle.done()
        elif destination == "Appalachian":
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(app1)
            t.goto(app2)
            t.goto(app3)
            t.goto(app4)
            t.circle(5)
            ##print("App - Success")
            turtle.done()
        elif destination == "CIW Dining Hall":
            t.goto(iroquois)
            t.circle(5)
            ##print("CIW - Success")
            turtle.done()
        elif destination == "Hinman Dining Hall":
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.goto(h1)
            t.goto(h2)
            t.circle(5)
            ##print("Hinman - Success")
            turtle.done()
        elif destination == "Lecture Hall":
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.circle(5)
            ##print("LH - Success")
            turtle.done()
        elif destination == "Science Buildings":
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(BartleParking)
            t.goto(BartleLH)
            t.goto(LH)
            t.goto(lotL)
            t.goto(ConnectorRd)
            t.goto(AA)
            t.goto(AB)
            t.goto(PhysFac)
            t.goto(sciIIIV)
            t.goto(lotF1)
            t.goto(sciIV)
            t.goto(sci)
            t.circle(5)
            ##print("Sci - Success")
            turtle.done()
        elif destination == "Bartle Library":
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(FABartle)
            t.goto(Bartle)
            t.circle(5)
            ##print("Bartle - Success")
            turtle.done()
        elif destination == "Fine Arts":
            t.goto(EB)
            t.goto(EBBartle)
            t.goto(FABartle)
            t.goto(EBFA)
            t.goto(FA)
            t.circle(5)
            ##print("FA - Success")
            turtle.done()
        elif destination == "Union(Old)":
            t.circle(5)
            ##print("Union(Old) - Success")
            turtle.done()
        else:
            t.circle(20)
            ##print("Error")
            turtle.done()


#*******************************************************************
bingTimeGui()
        
