import GUI

def main(): 
    GUI.init(10, 4500)

    for i in range(450):
        GUI.update(i*10)

    GUI.shutdown()


if __name__=="__main__": 
    main()