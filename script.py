from linked_list import Node, LinkedList
from JPNames import pokemon_jpnames, digimon_jpnames

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self, key):
    return sum(key.encode())
  
  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if key == item[0]:
        item[1] = value
        return
    
    list_at_array.insert(payload)
  
  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    
    return None
  
  def get_all_items(self):
        items = []
        for bucket in self.array:
            items.extend(bucket)
        return items

pokedex = HashMap(len(pokemon_jpnames))
digidex = HashMap(len(digimon_jpnames))

for pokemon in pokemon_jpnames:
  pokedex.assign(pokemon[0], pokemon[1])

charizard_name = pokedex.retrieve('Charizard')
print("Charizard's Japanese name is:", charizard_name)

#Add a new Pokemon to the hash map
pokedex.assign('Infernape', 'ゴウカザル')
infernape_name = pokedex.retrieve('Infernape')
print("A new Pokemon called Infernape has been added with the Japanese name:", infernape_name)

for digimon in digimon_jpnames:
  digidex.assign(digimon[0], digimon[1])

agumon_name = digidex.retrieve('Agumon')
print("Agumon's Japanese name is:", agumon_name)

#Add a new Digimon to the hash map
digidex.assign('WarGreymon', 'ウォーグレイモン')
wargreymon_name = digidex.retrieve('WarGreymon')
print("A new Digimon called WarGreymon has been added with the Japanese name:", wargreymon_name)

# Print all items in the pokedex
all_pokemon = pokedex.get_all_items()
print("Full Pokemon Hashmap:")
for pokemon in all_pokemon:
    print(f"{pokemon[0]}: {pokemon[1]}")

print("\n")

# Print all items in the digidex
all_digimon = digidex.get_all_items()
print("Full Digimon Hashmap:")
for digimon in all_digimon:
    print(f"{digimon[0]}: {digimon[1]}")
