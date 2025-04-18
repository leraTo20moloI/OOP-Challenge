class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.energy = 5 
        self.tricks = []

        def eat(self):
            self.hunger =max(0, self.hunger - 3)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} is eating.")

            def sleep(self):
                self.energy = min(10, self.energy + 5)
                print(f"{self.name} is sleeping.")
                
                def play(self):
                    if self.energy >= 2:
                        self.energy -= 2 
                        self.happiness = min(10, self.happiness + 2)
                        self.hunger = min(10, self.hunger + 1)
                        print(f"{self.name} is playing.")
                    else:
                        print(f"{self.name} is tired to play.")

                        def get_status(self):
                            print(f"\n{self.name} Status:")
                            print(f"Hunger: {self.hunger}")
                            print(f"Happiness: {self.happiness}")
                            print(f"Energy: {self.energy}")
                            print(f"Tricks: {','.join(self.tricks) if self.tricks else 'None'}")

                            def train(self, trick):
                                self.tricks.append(trick)
                                print(f"{self.name} learned how to {trick}!")

                                def show_tricks(self):
                                    if self.tricks:
                                        print(f"{self.name} knows these tricks: {','}")
                                    else:
                                        print(f"{self.name} hasn't learned ant trick.")



                            



