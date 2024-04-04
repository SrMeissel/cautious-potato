import GUI
import math

def printHello():
    print("Hello")

def printBye():
    print("Bye")

def main(): 
    GUI.init(10, 450)

    GUI.setStartButtonCallback(printHello)          
    GUI.setStopButtonCallback(printBye)

    for i in range(450):
        GUI.update([i, 450-i, math.sin(i/15)*200+200, math.cos(i/15)*200+200])

    GUI.shutdown()


if __name__=="__main__": 
    main()