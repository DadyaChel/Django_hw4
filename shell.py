from DadyaFood.models import *

# cl = Client(user=User.objects.create(email='vin_diesil_family_forever@gmail.com', password='family'), name='vin_diesel', card_number=91327489379038475)

cl2 = Client(user=User.objects.create(
    email='nikname21@gmail.com',
    password='defender42'),
    name='Азат Соколов',
    card_number=4147565798789009)
wr = Worker(user=User.objects.create(
    email='altywa1998@gmail.com',
    password='nono34'),
    name='Алтынай Алиева',
    position='Оператор кассы')

# cl.save()
cl2.save()
wr.save()


F = Food.objects.create(name='Шаурма', start_price=50)
F2 = Food.objects.create(name='Гамбургер', start_price=25)

D1 = Ingredient.objects.create(name='сыр', extra_price=10)
D2 = Ingredient.objects.create(name='курица', extra_price=70)
D3 = Ingredient.objects.create(name='говядина', extra_price=80)
D4 = Ingredient.objects.create(name='салат', extra_price=15)
D5 = Ingredient.objects.create(name='фри', extra_price=15)


F.save()
F2.save()
D1.save()
D2.save()
D3.save()
D4.save()
D5.save()


F.ingredient.set([D1, D4, D5], through_defaults={'client': cl2, 'worker': wr})
F2.ingredient.set([D2, D4], through_defaults={'client': cl2, 'worker': wr})


F.ingredient.all()
F2.ingredient.all()

res = (F.start_price + D1.extra_price+D4.extra_price+D5.extra_price)
res

res1 = (F2.start_price + D4.extra_price+D2.extra_price)
res1

sss = (F.start_price + D1.extra_price+D4.extra_price + D5.extra_price + F2.start_price + D4.extra_price + D2.extra_price)
sss







