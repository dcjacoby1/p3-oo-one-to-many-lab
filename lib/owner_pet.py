class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner = None):
    #checks to see if the pet_type is in the PET_TYPES list    
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        #adds the pet object to the all list
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        #loops through each object of the all list
        #if the owner property of the object is equal to the owner name, includes the pet
        #format owner1.pets() to see all pets for owner1
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
    #checks if the pet was already created, if so, adds the owner as the pet owner
    #would add in the format owner1.add_pet(pet1), where pet1 was already created (pet1 = Pet("Wheezy", "dog"))
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class")
        pet.owner = self

    def get_sorted_pets(self):
    #runs the pets() function for self (the owner) and sorts it based on the criteria pet.name
    #lamda used an an anonymous function, key is used to set the criteria
        return sorted(self.pets(), key = lambda pet: pet.name)
