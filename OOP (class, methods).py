class Dog:
    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name=name
        self.age=age

    # instance method
    def descitpion(self):
        return print("{} is {}".format(self.name,self.age))

    # instance method
    def speaks(self,sound):
        return print("{} speaks {}".format(self.name,sound))

# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print ( "{} is {} ,{} is {}".format(philo.name,philo.age,mikey.name,mikey.age))

# Is Philo a mammal?
print(philo.species =='mammal')

# Determine the oldest dog
def get_oldest_dog(*args):
    return max(args)

# Output
print (get_oldest_dog(philo.age, mikey.age))

print(philo.descitpion(), philo.speaks("wouf wouf"))

class Email:
    def __init__(self):
        self.is_sent = False
    def send_email(self):
        self.is_sent = True

my_email = Email()
my_email.is_sent

my_email.send_email()
my_email.is_sent
