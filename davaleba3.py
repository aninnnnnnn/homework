# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს
# და დაბეჭდავს შემდეგნაირად:
# input: “word”
# Output: „Tripled: wordwordword“

a = input("Enter a word: ")

def return_tripled(a):
    print(f"Input: '{a}'")
    print(f"Output: 'Tripled: {3*a}'")

return_tripled(3)

# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას
# მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)

mase = float(input("please enter your mase: "))

def mase_on_moon():
    return mase / 6

# 3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას
# მომხმარებლისგან input() ფუნქციის დახმარებით (სამ მონაცემს _ პირველ რიცხვს,
# მოქმედებას (+ - * / ^), მეორე რიცხვს)
# მაგ. „2 * 6“ დათვლის და დააბრუნებს შედეგს. გაითვალისწინე რომ რიცხვის შეყვანის
# მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი
# მესიჯი. ასევე ნულზე გაყოფა არ შეიძ₾ება, ამ შემთხვევაშიც უნდა დააბრუნოს
# შესაბამისი მესიჯი. (დააბრუნოს და არა დაპრინტოს)


def calculator():
    try:
        a = float(input("a: "))
        op = input("operation: ")
        b = float(input("c: "))
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                return "invalid input"
            else:
                return a / b
        elif op == "^":
            return a ** b
    except ValueError:
        return "Invalid operation"


print(calculator())
