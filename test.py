def dog_to_human(age_dog):
    if age_dog<=1:
       age_human=age_dog*15
    elif age_dog<=2:
       age_human=age_dog*12
    elif age_dog<=3:
       age_human=age_dog*9.3
    elif age_dog<=4:
       age_human=age_dog*8
    elif age_dog<=5:
       age_human=age_dog*7.2
    else:
       age_human=5*7.2+(age_dog-5)*7
    return age_human

age_dog=input('inserisci eta cane :')
age_dog=float(age_dog)
age_human=dog_to_human(age_dog)
print(round(age_human,2))


          

