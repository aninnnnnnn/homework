# 1. ვიქტორინა
# შეადგინე ვიქტორინის პროგრამა. მომხმარებელს უნდა დავუსვათ კითხვა: “რომელი
# იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს
# დღესაც?”
# სავარაუდო პასუხები:
# 1. შუმერთა
# 2. სელჩუკთა
# 3. რომის
# 4. მონღოლთა
# მომხმარებელმა უნდა შეიყვანოს სწორი პასუხის ნომერი ან თავად სწორი პასუხი.
# შეცდომის შემთხვევაში იბეჭდება:
# „არა! სწორი პასუხია რომის!“
# სწორი პასუხის შემთხვევაში იბეჭდება:
# „სწორია!“

answers = ["1. შუმერთა",
           "2. სელჩუკთა",
           "3. რომის",
           "4. მონღოლთა"]
question = ("“რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?” სავარაუდო პასუხები:")

print(question)

for choice in answers:
    print(choice)

guess = input("შეიყვანეთ თქვენი პასუხი: ")

while guess != "3" and guess != "რომის":
    print("არა! სწორი პასუხია რომის!")
    break

else:
    print("სწორია!")

# 3. თუთიყუშის პროგრამა
# დაწერე პროგრამა _ თუთიყუში. პროგრამამ უნდა გაიმეოროს რასაც ეტყვი მანამ სანამ არ
# შეიყვან სიტყვას quit, თუმცა წინ დაურთოს კითხვა „User Said Whaaat!?”
# თუ შევიყვანეთ სიტყვა Hello დაიბეჭდება
# „User Said Whaaat!?”
# “User Said Hello”

while True:
    word = input("User Said Whaaat: ").lower()

    if word == "quit":
        break


    else:
        print(f"User Said {word}")

# 2. გამრავლების ტაბულა

a = int(input("Enter number till I have to give you multiplication table: "))

for i in range(1, a+1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")
    print()

# 1. ონლაინ მაღაზია
# პროგრამა გთავაზობს პროდუქტის სამ კატეგორიას.
# მაგ.
# 1. ლეპტოპები
# 2. პერსონალური კომპიუტერები
# 3. მობილურები
# მომხმარებელი ირჩევს ერთ-ერთს.
# პროგრამა ითხოვს მაქსიმალურ ბიუჯეტს და ბიუჯეტის მიხედვით სთავაზობს
# მომხმარებელს კონკრეტულ მოდელს არჩეულ კატეგორიაში.
# (თითო კატეგორიაში მინიმუმ 3 პროდუქტი მაინც უნდა იყოს)


a = ["laptop", "pc", "phone"]
phone = ["Motorolla", "Pixel", "Iphone"]
pc = ["Dell", "HP", "Sony"]
laptop = ["Leonovo", "Mac", "Acer"]


while True:
    user_choice = input(f"please choose desired product {a}: ").lower()
    if user_choice in a:
        break
    print(f"WARNING! you have to choose from the list: {a} ")

budget = int(input("Please enter your budget: "))

if budget < 500:
    print("Sorry We have no product for this budget.")
else:
    if user_choice == "phone":
        if 500 <= budget <= 1100:
            print(f"We suggest {phone[0]}")
        elif 1100 < budget <= 1500:
            print(f"We suggest {phone[1]}")
        else:
            print(f"We suggest {phone[2]}")

    elif user_choice == "pc":
        if 500 <= budget <= 1100:
            print(f"We suggest {pc[0]}")
        elif 1100 < budget <= 1500:
            print(f"We suggest {pc[1]}")
        else:
            print(f"We suggest {pc[2]}")

    elif user_choice == "laptop":
        if 500 <= budget <= 1100:
            print(f"We suggest {laptop[0]}")
        elif 1100 < budget <= 1500:
            print(f"We suggest {laptop[1]}")
        else:
            print(f"We suggest {laptop[2]}")

# 2. ქუესთის შედგენა (Text Based Adventure Game)

# !!! მეტი ვერ მოვიფიქრე :დდ და კიდევ X და O -ს გარდა სხვა რამის შეყვანაზეც არმაქვს არაფერი დაწერილი და დავამთავრებ მაგასაც.
# თამაში: სიკვდილი ან სიცოცხლე
# - გამარჯობა, თქვენ შედიხართ კვადრატულ ოთახში, სადაც ორი კარია (შესასვლელის გარდა)
# უნდა აირჩიოთ რომელ კარში შეხვალთ, არასწორი კარის გაღების შემთხვევაში you are drop dead. კარები მონიშნულია O და X ნიშნებით.
# - არჩევანი 1: O ან X
# - თქვენ აირჩიეთ O და გადახვედით შემდეგ ოთახში
# - თქვენ აირჩიეთ X და მოკვდით Game Over!
# - არჩევანი 2: O ან X
# - თქვენ აირჩიეთ O და მოკვდით Game Over!
# - თქვენ აირჩიეთ X და გადახვედით შემდეგ ოთახში
# - არჩევანი 3: O ან X
# - თქვენ აირჩიეთ O და მოკვდით Game Over!
# - თქვენ აირჩიეთ X და გადახვედით შემდეგ ოთახში
# - არჩევანი 4: O ან X
# - თქვენ აირჩიეთ X და მოკვდით Game Over!
# - თქვენ აირჩიეთ O და გადახვედით შემდეგ ოთახში
# - არჩევანი 5: O ან X
# - თქვენ აირჩიეთ X და მოკვდით Game Over!
# - თქვენ აირჩიეთ O ! გილოცავთ თქვენ გააღწიეთ შენობიდან!
#
#
a = ["O", "X"]

intro = print("გამარჯობა, თქვენ შედიხართ კვადრატულ ოთახში, სადაც ორი კარია (შესასვლელის გარდა) 1 წუთში თქვენ უნდა აირჩიოთ რომელ კარში შეხვალთ, არასწორი კარის გაღების შემთხვევაში you are drop dead :P, დროსი ამოწურვის შემთხვევაშიც you are drop dead, კარები მონიშნულია O და X ნიშნებით.")
choice = input(f"გთხოვთ აირჩიოთ ოთახის კარი [a]:")

if choice not in a:
    print("Error, please choose from [a]")

if choice == "O":
    print("- თქვენ აირჩიეთ O და გადახვედით მეორე ოთახში")
    choice = input(f"გთხოვთ აირჩიოთ ოთახის კარი [a]:")
    if choice == "X":
        print("- თქვენ აირჩიეთ X და გადახვედით მესამე ოთახში")
        choice = input(f"გთხოვთ აირჩიოთ ოთახის კარი [a]:")
        if choice == "X":
            print("- თქვენ აირჩიეთ X და გადახვედით მეოთხე ოთახში")
            choice = input(f"გთხოვთ აირჩიოთ ოთახის კარი [a]:")
            if choice == "O":
                print("- თქვენ აირჩიეთ O და გადახვედით ბოლო ოთახში")
                choice = input(f"გთცოვთ აირჩიოთ ოთახის კარი [a]")
                if choice == "O":
                    print("გილოცავთ თქვენ გააღწიეთ შენობიდან!")
                elif choice == "O":
                    print("Game Over!")
            elif choice == "X":
                print("- თქვენ აირჩიეთ X და მოკვდით Game Over")
        elif choice == "O":
            print("- თქვენ აირჩიეთ O და მოკვდით Game Over!")
    elif choice == "O":
        print("- თქვენ აირჩიეთ O და მოკვდით Game Over!")
elif choice == "X":
    print("- თქვენ აირჩიეთ X და მოკვდით. Game Over!")

