from faker import Faker
fake = Faker()
for i in fake.profile():
    print(i.upper(), ':', fake.profile()[i])
