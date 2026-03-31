import random
numrange_bottom = 1
numrange_upper = 20

def rand_numbers():
    rand_list = []
    for x in range(0,9):
        rand_list.append(random.randint(numrange_bottom,numrange_upper))
    # print(rand_list) 
    return(rand_list)

def player_choice(x):
    try:
        num_choice = int(input(f"Zadejte své {x+1}. číslo. Od {numrange_bottom} do {numrange_upper}: "))
        if num_choice > numrange_upper or num_choice < numrange_bottom:
            print(f"Prosím jen čísla od {numrange_bottom} do {numrange_upper}.")
            return player_choice(x)
    except ValueError:
        print(f"Prosím jen čísla od {numrange_bottom} do {numrange_upper}.")
        return player_choice(x)
        # return player_choice
        # num_choice = player_choice
    # elif num_choice < 10:
    return num_choice

while True:
    rand_numbers()
    final_agreement = []
    # print(my_numbers)

    # print(player_choice(1))

    print("Vítejte ve Sportce.")
    choice = input("Chcete si zvolit vlastní čísla nebo chcete zvolit náhodné? V-vlastní / N-náhodné: ").lower()
    machine_choice_machine = rand_numbers()

    if choice == "v":
        machine_choice_player = []
        for x in range(0,10):
            machine_choice_player.append(player_choice(x))


    elif choice == "n":
        machine_choice_player = rand_numbers()

    print("Výherní čísla:")
    print(machine_choice_machine)
    print("Vaše čísla:")
    print(machine_choice_player)
    count = 0
    for x in range(0,9):
        try:
            position = machine_choice_player.index(machine_choice_machine[x])
            final_agreement.append(machine_choice_player[position])
            count +=  1
        except ValueError:
            final_agreement.append("N")

    print("Konečná shoda:")
    print(final_agreement)
    if count <= 1:
        finished_sentence = f"v {count} případu"
    elif count >=5:
        finished_sentence = f"v {count} případech"
    else:
        finished_sentence = f"ve {count} případech"
    print(f"Máte shodu {finished_sentence}.")
