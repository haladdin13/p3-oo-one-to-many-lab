class Pet:

#     Define a class variable PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"] and validate that the pet_type is one of those types in the __init__ method.
# raise Exception if this check fails.

    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception("pet_type must be one of {}".format(Pet.PET_TYPES))
    

    

class Owner:
    
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("pet must be an instance of Pet")
        
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda x: x.name)