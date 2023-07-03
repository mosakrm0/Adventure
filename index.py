import time


#introduction

print("Whats Your Name ?\t")
UserName = input("> ")
time.sleep(1)
print(f"Welcome {UserName} to This Adventure!\n")


#Page 1

time.sleep(1)
print("You find yourself stranded on a deserted island after a shipwreck. You are surrounded by dense jungle and the sound of waves crashing against the shore. You have no idea where you are or how you will get back home. The sun is setting, and you need to make a decision. What do you do? ")
time.sleep(1)
print("\tType 'Explore the Jungle' Or 'Build a Shelter on the Beach' to continue")
UserChoice = input("> ").lower()


#Page 2

if UserChoice == "explore the jungle": 
    time.sleep(1)
    print("\nYou decide to explore the jungle in search of any signs of civilization. As you venture deeper, the foliage becomes thicker, making it hard to see. Suddenly, you hear a rustling sound behind you. What do you do?")
    time.sleep(1)
    print("\tType 'Investigate the Sound' Or 'Hide and Observe' to continue")
    UserChoice = input("> ").lower()

#Page 4

    if UserChoice == "investigate the sound":
        time.sleep(1)
        print("\nCuriosity gets the better of you, and you decide to investigate the sound. As you approach, you come across a group of friendly natives who have been living on the island for generations. They welcome you and offer you food and shelter. You have found a new home! The natives teach you their ways, and you live happily on the island for the rest of your days.")
        time.sleep(1)
        print("\t THE END !")


#Page 5

    elif UserChoice == "hide and observe":
        time.sleep(1)
        print("\nYou quickly hide behind a bush and observe the area. Soon, a group of unfriendly natives pass by, unaware of your presence. Realizing the danger, you decide to quietly make your way back to the beach. With newfound caution, you survive on the island, eventually finding a way to signal for help and get rescued.")
        time.sleep(1)
        print("\t THE END !")


    else:
        time.sleep(1)
        print("\nThats Not a Vaild Choice , You Lost !")
        print("\t THE END !")


#Page 3

elif UserChoice == "build a shelter on the beach":
    time.sleep(1)
    print("\nYou choose to build a shelter on the beach to protect yourself from the elements. Using the wreckage from the ship, you construct a sturdy shelter and gather some firewood. As night falls, you hear strange noises coming from the jungle. What do you do?")
    time.sleep(1)
    print("\tType 'Stay in the Shelter' Or 'Investigate the Noises' to continue")
    UserChoice = input("> ").lower()
    
#Page 6

    if UserChoice == 'stay in the shelter':
        print("\nYou choose to stay in the shelter, hoping that the noises will go away. Unfortunately, the noises grow louder and more intense throughout the night. Suddenly, a pack of wild animals attacks your shelter. You manage to fend them off but suffer injuries. The next morning, you decide it's too risky to stay and venture into the jungle to find help.")
        time.sleep(1)
    
    #Page 2 (Again)

        print("You decide to explore the jungle in search of any signs of civilization. As you venture deeper, the foliage becomes thicker, making it hard to see. Suddenly, you hear a rustling sound behind you. What do you do?")
        time.sleep(1)
        print("\tType 'Investigate the Sound' Or 'Hide and Observe' to continue")
        UserChoice = input("> ").lower()

        if UserChoice == "investigate the sound":
            time.sleep(1)
            print("\nCuriosity gets the better of you, and you decide to investigate the sound. As you approach, you come across a group of friendly natives who have been living on the island for generations. They welcome you and offer you food and shelter. You have found a new home! The natives teach you their ways, and you live happily on the island for the rest of your days.")
            time.sleep(1)
            print("\n\t THE END !")

#Page 7

        elif UserChoice == "hide and observe":
            time.sleep(1)
            print("\nYou quickly hide behind a bush and observe the area. Soon, a group of unfriendly natives pass by, unaware of your presence. Realizing the danger, you decide to quietly make your way back to the beach. With newfound caution, you survive on the island, eventually finding a way to signal for help and get rescued.")
            time.sleep(1)
            print("\n\t THE END !")


        else:
            time.sleep(1)
            print("\nThats Not a Vaild Choice , You Lost !")
            print("\n\t THE END !")



    elif UserChoice == 'investigate the noises':
        time.sleep(1)
        print("\nDriven by curiosity, you decide to investigate the noises in the jungle. As you approach, you stumble upon an ancient temple hidden among the trees. The temple is filled with treasure and artifacts from a lost civilization. You become rich beyond your wildest dreams and find a way to leave the island with your newfound wealth.")
        print("\n\t THE END !")
    
    else:
        time.sleep(1)
        print("\nThats Not a Vaild Choice , You Lost !")
        print("\n\t THE END !")


else:
    time.sleep(1)
    print("\nThats Not a Vaild Choice , You Lost !")
    print("\n\t THE END !")
