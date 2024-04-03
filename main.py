import GUI
import math

def main(): 
    GUI.init(10, 450)

    for i in range(45000):
        GUI.update([i, 450-i, math.sin(i/15)*200+200, math.cos(i/15)*200+200])

    GUI.shutdown()


if __name__=="__main__": 
    main()