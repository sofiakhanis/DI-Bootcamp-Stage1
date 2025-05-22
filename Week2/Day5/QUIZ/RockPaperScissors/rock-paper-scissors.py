from game import Game
   
def print_results(results):
    print (f"Wins: {results['win']}, Losses: {results['loss']}, Draws: {results['draw']}")
    print ("Thank for playing!")

def main ():
    results = {"win" : 0, "loss" : 0, "draw" : 0}
    while True:
        choice = input("1. Play a new game / 2. Show scores / 3. Quit (write the number of your choice): ")
        if choice  == "1":
            player = Game()
            result = player.play()
            if result in results:
                results[result] +=1 
        elif choice == "3":
            print_results(results)
            print ("Stopping the game.")
            break
        elif choice == "2":
            print_results(results)
        else: 
            print("Invalid input. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
