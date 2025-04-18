from Pet import Pet

def main():
    Pet = Pet("Snoppy")

    Pet.get_status()

    Pet.eat()
    Pet.sleep()
    Pet.play()
    Pet.train("roll over")
    Pet.train("fetch")

    Pet.get_status()
    Pet.show_tricks()

    if __name__ == "__main__":
        main()
