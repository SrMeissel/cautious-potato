import GUI

def main(): 
    GUI.init()

    for i in range(500):
        GUI.update(i)

    GUI.shutdown()


if __name__=="__main__": 
    main() 