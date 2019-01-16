import copy;
from listepriorite import ListePriorite;


class listeDePriorite():
    def __init__(self):
        self.__dalton = []
    
    def __str__(self):
        return f"{self.__dalton}"
        # facon plus complexe
        # res = "["
        # for i in range(len(self.__dalton)):
        #     res += self.__dalton[i].__str__()
        #     res += ','
        # res += "]"
        # return res;

    def empty(self):
        if len(self.__dalton) == 0:
            return True
        else:
            return False
    
    def add(self, priorité, obj):
        tuple = (priorité, obj)
        self.__dalton.append(tuple)
        self.__dalton.sort()

    def contains(self, obj):
        for val in range(len(self.__dalton)):
            tuple = self.__dalton[val]
            if tuple[1] == obj:
                return True
        return False
    
    def priorities_of(self, obj):
        liste = []
        for i in self.__dalton:
            if obj == i[1]:
                liste.append(i[0])
        return liste        
    
    def pop(self):
        supp = self.__dalton.pop()
        return supp

  
    @property
    def prio_min(self):
        return self.__dalton[1][0]

    @property
    def prio_max(self):
        return self.__dalton[-1][0]
    
    def items(self):
        for i in self.__dalton: yield i
    
    def vals(self):
        for i in self.__dalton:
            yield i[1]
    
    @property
    def length(self):
        return len(self.__dalton)
    
    def at(self, indice):
        return self.__dalton[indice ]
    
    def delete(self, indice):
        return self.__dalton.pop(indice)

    def __iadd__(self, tuple):
        x = tuple[0]
        y = tuple[1]
        self.add(x,y)
        return self
    

daltons = listeDePriorite()
print(daltons.empty())
# print(f"priorite min = {daltons.prio_min}, priorite max = {daltons.prio_max}")  # None, None
daltons.add(5, "Joe")
daltons.add(1, "Jack")
daltons.add(3, "Averell")
daltons.add(4, "William")
daltons.add(1, "Ma")
daltons.add(10, "Jack")

print(daltons.contains("Lucky Luke"))  # False
print(daltons.contains("Averell"))  # True
print(daltons.priorities_of("Jack")) 

print(daltons.pop())
print(daltons)
print(f"priorite min = {daltons.prio_min}, priorite max = {daltons.prio_max}")

for elt in daltons.items():
    print(elt, end=", ")  # ((1, 'Jack'), (1, 'Ma'), (3, 'Averell'),
    #  (4, 'William'), (5, 'Joe'),
print()

for val in daltons.vals():
        print(val, end=", ")  # Jack, Ma, Averell, William, Joe,
print()

print(daltons.length)  # 5
print(daltons.at(0))  # (1, "Jack")

val = daltons.pop()
print(daltons)  # [(1, 'Jack'), (1, 'Ma'), (3, 'Averell'), (4, 'William')]
print(val)  # (5, 'Joe')
print(f"priorite min = {daltons.prio_min}, priorite max = {daltons.prio_max}")  # 1, 4

outlaws = copy.deepcopy(daltons)
daltons.delete(0)
print(daltons)    # [(1, 'Ma'), (3, 'Averell'), (4, 'William')]
print(outlaws)    # [(1, 'Jack'), (1, 'Ma'), (3, 'Averell'), (4, 'William')]
