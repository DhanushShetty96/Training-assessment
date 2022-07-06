class Mobile() :
    phones={'iPhone':[],'Samsung':[],'Nokia':[],'Mi':[],'Realme':[]}
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price

class iPhone(Mobile):
    iPhone_count=0
    pass

class Samsung(Mobile):
    Samsung_count = 0
    pass

class Nokia(Mobile):
    Nokia_count = 0
    pass

class Mi(Mobile):
    Mi_count = 0
    pass

class Realme(Mobile):
    Realme_count = 0
    pass

def add_mobile():
    brand=input('Enter mobile brand\n')
    mob_name=input('Enter mobile name\n')
    mob_model=input("Enter mobile model\n")
    mob_price=input('Enter mobile price\n')

    if brand=='iPhone':
        mob = iPhone(mob_name,mob_model,mob_price)
        Mobile.phones['iPhone'].append([mob_name,mob_model,mob_price])
        mob.iPhone_count +=1

    elif brand=='Samsung':
        mob=Samsung(mob_name,mob_model,mob_price)
        Mobile.phones['Samsung'].append([mob_name,mob_model,mob_price])
        mob.Samsung_count += 1

    elif brand=='Nokia':
        mob=Nokia(mob_name,mob_model,mob_price)
        Mobile.phones['Nokia'].append([mob_name,mob_model,mob_price])
        mob.Nokia_count += 1

    elif brand=='Mi':
        mob=Mi(mob_name,mob_model,mob_price)
        Mobile.phones['Mi'].append([mob_name,mob_model,mob_price])
        mob.Mi_count += 1

    elif brand == 'Realme':
        mob = Realme(mob_name, mob_model, mob_price)
        Mobile.phones['Realme'].append([mob_name, mob_model, mob_price])
        mob.Realme_count += 1
    else:
        print("Invalid input cannot able to add")
def delete_mobile():
    brand=input('Enter mobile brand\n')
    mob_name=input("Enter mobile name\n")
    mob_model=input("Enter mobile model\n")
    mob_price=input('Enter mobile price\n')
    print('*****************************')

    if brand == 'iPhone': #and mob_model in Mobile.phones['iPhone'] :
        Mobile.phones['iPhone'].remove([mob_name, mob_model, mob_price])
        mob = iPhone(mob_name, mob_model, mob_price)
        mob.iPhone_count -= 1

    elif brand == 'Samsung' :#and mob_model in Mobile.phones['Samsung'] :
        Mobile.phones['Samsung'].remove([mob_name, mob_model, mob_price])
        mob = Samsung(mob_name, mob_model, mob_price)
        mob.Samsung_count -= 1

    elif brand == 'Nokia' :#and mob_model in Mobile.phones['Nokia'] :
        mob = Nokia(mob_name, mob_model, mob_price)
        Mobile.phones['Nokia'].remove([mob_name, mob_model, mob_price])
        mob.Nokia_count -= 1

    elif brand == 'Mi' :#and mob_model in Mobile.phones['Mi'] :
        mob = Mi(mob_name, mob_model, mob_price)
        Mobile.phones['Mi'].remove([mob_name, mob_model, mob_price])
        mob.Mi_count -= 1

    elif brand == 'Realme' :#and mob_model in Mobile.phones['Realme'] :
        mob = Realme(mob_name, mob_model, mob_price)
        Mobile.phones['Realme'].remove([mob_name, mob_model, mob_price])
        mob.Realme_count-= 1

    else:
        print("Cannot able to delete")
def list():
    print(Mobile.phones)

def count_list():
    print("iPhone-->"+str(len(Mobile.phones['iPhone']))+"\nSamsung-->"+str(len(Mobile.phones['Samsung']))+"\nNokia-->"+str(len(Mobile.phones['Nokia']))+"\nMi-->"+str(len(Mobile.phones['Mi']))+"\nRealme-->"+str(len(Mobile.phones['Realme']))+"\n")

while True:
    print("Welcome to namma Mobile shop")
    print('*****************************')
    op=0
    print('Enter 1 to add mobiles')
    print('Enter 2 Delete Mobiles')
    print('Enter 3 to list mobiles')
    print("Enter 4 to see count based on brands")
    op=int(input())
    if op==1:
        add_mobile()
    elif op==2 :
        delete_mobile()
    elif op==3:
        list()
    elif op==4 :
        count_list()
    else:
        exit()