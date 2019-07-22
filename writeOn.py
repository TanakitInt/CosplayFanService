import os

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def fileView():
    #user prompt view file

    while True:
        viewSelection = input("Picture to PREVIEW (1-3): ")

        if viewSelection == "1":
            os.startfile("1_placeholder.jpg")

        elif viewSelection == "2":
            os.startfile("2_placeholder.jpg")

        elif viewSelection == "3":
            os.startfile("3_placeholder.jpg")

        else:
            print(
        """
        Please input a valid number.
    """
            )

def imangeManage():

    def select():
        #user propmt file selection

        while True:
            drawSelection = input("Picture to PROCESS (1-3) : ")

            if drawSelection == "1":
                selection = 1
                return selection

            elif drawSelection == "2":
                selection = 2
                return selection

            elif drawSelection == "3":
                selection = 3
                return selection

            else:
                print(
            """
        Please input a valid number.
            """
                    )

    def process(selection):
        #image processing

        if selection == 1:
            image = "1_placeholder.jpg"

        elif selection == 2:
            image = "2_placeholder.jpg" 

        elif selection == 3:
            image = "3_placeholder.jpg" 

        imageIn = Image.open(image)
        drawIn = ImageDraw.Draw(imageIn)

        #print("OK!")


    def selectionTransfer():
        #
        selection = select()
        process(selection)
    selectionTransfer()


def credits():
    #creator credits

    print(
        """
    blah blah blah credits here.
        """
        )


def exit():
    #edit program

    print("Press any key to quit..." '\n')

    userExit = input()

    quit()

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
        menuSelection = input("Menu selection : ")

        if menuSelection == "1":
            fileView()

        elif menuSelection == "2":
            imangeManage()

        elif menuSelection == "3":
            credits()

        elif menuSelection == "9":
            exit()

menu()
