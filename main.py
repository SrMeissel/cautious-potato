import GUI

def main(): 
    GUI.init()

    for i in range(450):
        #effective range 0-350
        GUI.update(i)

    GUI.shutdown()


if __name__=="__main__": 
    main() 