print("----Калькулятор----")
a = input("Вкажіть значення а = ")
b = input("Вкажіть значення b = ")
intA = int(a)
intB = int(b)
c = intA // intB # цілосне ділення
print(f"a // b = {c}")
c = intA ** intB # піднесення до степеня
print(f"a ** b = {c}")
c = intA % intB # % остача від ділення
print(f"a % b = {c}")
intA += intB # це скорочена форма запису intA = intA + intB ( перезаписує змінну intA )
print(f"a += b = {intA}")
intA -= intB # це скорочена форма запису intA = intA - intB ( перезаписує змінну intA )
print(f"a -= b = {intA}")
intA *= intB # це скорочена форма запису intA = intA * intB ( перезаписує змінну intA )
print(f"a *= b = {intA}")
intA //= intB # це скорочена форма запису intA = intA // intB ( перезаписує змінну intA )
print(f"a //= b = {intA}")
intA **= intB # це скорочена форма запису intA = intA ** intB ( перезаписує змінну intA )
print(f"a **= b = {intA}")
intA %= intB # це скорочена форма запису intA = intA % intB ( перезаписує змінну intA )
print(f"a %= b = {intA}")

intA /= intB # це скорочена форма запису intA = intA / intB ( перезаписує змінну intA )
# / перетворює int на float
print(f"a /= b = {intA}")




'''
+=  те саме, що  c = a + b
-=  те саме, що  c = a - b
*=  те саме, що  c = a * b
/=  те саме, що  c = a / b
/ перетворює int на float
//=  те саме, що  c = a // b
**=  те саме, що  c = a ** b
%=  те саме, що  c = a % b
'''
