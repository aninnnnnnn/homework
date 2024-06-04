# # 1. დაწერე პროგრამა რომელიც გეკითხება ჯერ სახელს, შემდეგ გვარს და ინფორმაციის მიღების
# # შემდეგ ტერმინალში ბეჭდავს ერთმანეთის გვერდით.
#
# a = input("What's your name?: ")
# b = input("What's your surname?: ")
# print(a, b)
#
# #2. დაწერე პროგრამა რომელიც ითხოვს ორ რიცხვს, პირველი რიცხვი აჰყავს მეორის ხარისხში
# #და შედეგი იბეჭდება ტერმინალში.
#
# a = int(input("Number 1: "))
# b = int(input("Number 2: "))
#
# print(a**b)

# 3. დაწერე პროგრამა რომელიც გეკითხება სახელს, გვარს, ასაკს და ქალაქს და ბეჭდავს
# ინფორმაციას შემდეგი სახით:
# Name: Lia
# Surname: Kebadze
# Age: 20
# City: Tbilisi

# name = input("Whats your name?: ")
# surname = input("Whats your surname?: ")
# age = input("Whats your age?: ")
# city = input("Whats your city?: ")
#
# print(f"""Name: {name}
# Surname: {surname}
# Age: {age}
# City: {city}""")

# 4. დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ნებისმიერი სამი სხვადასხვა ხილის
# დასახელება ცალცალკე. რეზულტატი კი იბეჭდება შემდეგი სახით:
# Apple//Peach%%Orange

# fruit1 = input("Name fruit number one: ")
# fruit2 = input("Name fruit number two: ")
# fruit3 = input("Name fruit number three: ")
#
# print(f"{fruit1}//{fruit2}%%{fruit3}")

# 5. დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ტექსტი, დათვლის მასში არსებული
# სიმბოლოების რაოდენობას და გამოიტანს შედეგს შემდეგნაირად:
# Number of symbols: 50

# txt = input("Please enter text: ")
#
# a = int(len(txt))
# print("Number of symbols:", a)