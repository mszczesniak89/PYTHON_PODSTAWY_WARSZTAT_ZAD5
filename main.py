import random

actual_dice = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']

intro = """
Wprowadź dane w postaci:

xDy+z

gdzie:
x - liczba rzutów kośćmi
Dy - rodzaj kości (np.D6,D10)
z - liczba, którą należy dodać do wyniku rzutów

Typy kostek występujące w grach: D3, D4, D6, D8, D10, D12, D20, D100
"""


def dice_sim(num1, num2, num3=0):
    result = 0
    for _ in range(num1):
        r = random.randint(1, num2)
        result += r
    result += num3
    return result


def input_analysis():
    while True:
        try:
            global x2
            global y2
            global z2
            user_choice = input("Wprowadź dane: ")
            user_choice = [char for char in user_choice]
            y1 = []
            if not ("+" in user_choice) or ("-" in user_choice):
                y1 = user_choice[user_choice.index('D') + 1:]
            elif ("+" in user_choice):
                y1 = user_choice[user_choice.index('D') + 1:user_choice.index('+')]
            elif ("-" in user_choice):
                y1 = user_choice[user_choice.index('D') + 1:user_choice.index('-')]
            y2 = ""
            for num_y in y1:
                y2 += num_y
            y2 = int(y2)

            if not (f"D{y2}" in actual_dice):
                print("Nie występuje taki typ kostki!")
                raise ValueError

            x1 = user_choice[:user_choice.index('D')]
            if not x1:
                x1 = ['1']
            x2 = ""
            for num_x in x1:
                x2 += num_x
            x2 = int(x2)

            z1 = []
            if ("+" in user_choice):
                z1 = user_choice[user_choice.index('+'):]
            elif ("-" in user_choice):
                z1 = user_choice[user_choice.index('-'):]
            z2 = ""
            if not z1:
                z1 = ['0']
            for num_z in z1:
                z2 += num_z
            z2 = int(z2)
            break
        except:
            print("Wprowadź odpowiednie dane!")


print(intro)

input_analysis()

print(f"Wynik to {dice_sim(x2, y2, z2)}")
