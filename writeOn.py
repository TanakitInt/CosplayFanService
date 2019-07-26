import os
import time

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from datetime import datetime

def inputErrorMessage():
    #print an error message

    print(
"""
!!!   Please input a valid number.  !!!
"""
        )
    
def fileView():
    #user prompt view file
    print(
"""
To Cancel please type "9"
"""
    )

    while True:
        viewSelection = input("Picture to PREVIEW (1-3): ")

        if viewSelection == "1":
            os.startfile("1_placeholder.jpg")

        elif viewSelection == "2":
            os.startfile("2_placeholder.jpg")

        elif viewSelection == "3":
            os.startfile("3_placeholder.jpg")

        elif viewSelection == "9":
            menu()

        else:
            inputErrorMessage()

def imageManage():

    def fontSelect():
        #font selection
        print(
"""
(1) New Tanakitkun *[My hand write]* 
(2) Inkfree
(3) Roboto Light
(4) Segoe UI Light
"""
            )
        while True:
            fontSelection = input("Select a FONT to draw on (1-4) : ")

            if fontSelection == "1":
                font = ImageFont.truetype(r'font/New_Tanakitkun.ttf', 72)
                return font

            elif fontSelection == "2":
                font = ImageFont.truetype(r'font/Inkfree.ttf', 72)
                return font

            elif fontSelection == "3":
                font = ImageFont.truetype(r'font/Roboto-Light.ttf', 72)
                return font

            elif fontSelection == "4":
                font = ImageFont.truetype(r'font/segoeuil.ttf', 72)
                return font

            else:
                inputErrorMessage()

    def colorSelect():
        #color selection
        print(
"""
(1) Night Black *[Recommended]*
(2) Material Red
(3) Material Blue
(4) Colorful Pink
(5) Nature Green
"""
            )
        while True:
            colorSelection = input("Select a COLOR for a text (1-5) : ")
            
            if colorSelection == "1":
                color = (0, 0, 0) #Black
                return color

            elif colorSelection == "2":
                color = (211, 47, 47) #Red
                return color

            elif colorSelection == "3":
                color = (48, 63, 159) #Blue
                return color

            elif colorSelection == "4":
                color = (240, 98, 146) #Pink
                return color

            elif colorSelection == "5":
                color = (102, 187, 106) #Green
                return color

            else:
                inputErrorMessage()


    def imageSelect():
        #user propmt file selection
        while True:
            drawSelection = input("Picture to PROCESS (1-3) : ")
            selection = [] 
            #[picture number, x coordiniation, y coordiniation]

            if drawSelection == "1":
                selection = [1, 250, 250]
                
                return selection

            elif drawSelection == "2":
                selection = [2, 500, 500]
                
                return selection

            elif drawSelection == "3":
                selection = [3, 1000, 1000]

                return selection

            else:
                inputErrorMessage()

    def completeNotify():
        print("Done!")
        print("Your Fan Service is now completed, please see at the \"output\" folder!")
        print("...")

    def process(selection, font, color):
        #image processing

        if selection[0] == 1:
            image = "1_placeholder.jpg"

        elif selection[0] == 2:
            image = "2_placeholder.jpg" 

        elif selection[0] == 3:
            image = "3_placeholder.jpg" 

        imageIn = Image.open(image)
        drawIn = ImageDraw.Draw(imageIn)

        #text input
        userText = str(input("Your name : "))

        #current date
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')        

        #draw on picture
        drawIn.text((selection[1], selection[2]), userText, color, font = font)

        #draw a Timestamp (Fixed Settings)
        drawIn.text((10, 10), str(date), (255, 255, 255), font = ImageFont.truetype(r'font/segoeuil.ttf', 36)) #white

        #create output folder
        if not os.path.exists("output"):
            os.makedirs("output")

        imageIn.save("output/Your fan service here.jpg")

        #Notify user the process was completed
        completeNotify()

    def selectionTransfer():
        #transfer a variable

        font = fontSelect()
        selection = imageSelect()
        color = colorSelect()
        
        process(selection, font, color)

    selectionTransfer()


def credits():
    #creator credits

    creditsFile = open('Credits.txt', 'r')
    print(creditsFile.read())
    creditsFile.close()

def exit():
    #edit program

    print("Press ENTER key to quit..." '\n')

    userExit = input()

    quit()

def introduction():
    #intro to the program
    introFile = open('Introduction.txt', 'r')
    print(introFile.read())
    introFile.close()

def menu():
    #main menu
    print(
"""
Menu :
(1) Preview file
(2) Start processing
(3) Credits
(9) Exit
"""
    )
    while True:
        print("For help, type : \"help\"")
        menuSelection = input("Menu selection : ")

        if menuSelection == "1":
            fileView()

        elif menuSelection == "2":
            imageManage()

        elif menuSelection == "3":
            credits()

        elif menuSelection == "9":
            exit()

        elif menuSelection == "help":
            menu()

        else:
            inputErrorMessage()

introduction()
menu()
