from appointment_class import *
from pet_class import *
from human_class import *

# creating 3 pets
pet1 = Pet('Mr.Mitten', 'Persian', 'Cat')
pet2 = Pet('Cookie', 'Husky', 'Dog')
pet3 = Pet('Mike', 'Labrador', 'Dog')


# creating 3 clients
client1 = Client('Card', 'Potts', '75119346471', 'jpotts@hotmail.com')
client2 = Client('Card', 'Jones', '75549446471', 'jjones@hotmail.com')
client3 = Client('Card', 'Mars', '75159746471', 'bmars@hotmail.com')


# creating 2 veterinarian
vet1 = Veterinarian( 'Rick', '7983838708', 'rick@barrowhill.com', 'Cat')
vet2 = Veterinarian( 'Nisa', '7983838708', 'nisa@barrowhill.com', 'Dog')


#creating 3 appointments
app1 = Appointment('bad stomach', '19-01-2019', '165')
app2 = Appointment('broken leg', '19-01-2019', '165')
app3 = Appointment('tail', '19-01-2019', '165')
app = []
app.append(app1)
app.append(app2)
app.append(app3)


# Adding pets and vets to appointment
app1.adding_pet(pet1)
app2.adding_pet(pet2)
app3.adding_pet(pet3)

app1.adding_vet(vet1)
app2.adding_vet(vet2)
app3.adding_vet(vet2)

# As a user i can list all appointments /
print('/////////////////////////APPOINTMENT LIST///////////////////')
for appointment in app:
    print('(Disease: ', appointment.disease, '(PetName: ', appointment.get_pet().identify_name(), '(Appointment Date: ', appointment.date, '(VET: ',  appointment.get_vet().identify_name(), '(Price: £', appointment.price)


# as a user i can get pet and owner details for one pet/
print('///////////////////////PET OWNER DETAIL////////////////////////')
pet1.add_owner(client1)
print(f" Owner: {pet1.owner.identify_name()}, (Pet: {pet1.name}, (Breed : {pet1.breed}, (Species: {pet1.species}")