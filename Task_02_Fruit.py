def print_task_condition():
    print("\nЗадача 2. В списке находятся названия фруктов.\n"
          " Выведите все фрукты, названия которых начинаются на заданную букву.\n"
          "а –> абрикос, авокадо, апельсин, айва.\n")

def create_fruits_list():
    fruits_list = ["абрикос", "авокадо", "апельсин", "айва",
                   "банан", "бергамот", "бабако", "бакупари",
                   "виноград", "вишня", "вампи", "восковница",
                   "гранат", "груша", "грейпфрут", "гуава",
                   "дыня", "дуриан", "джамбу", "джекфрут",
                   "жердела", "зизифис", "инжир", "имбу",
                   "кокос", "киви", "канталупа", "климентин",
                   "лайм", "лимон", "манго", "маракуйя",
                   "нектарин", "нони", "опунция", "персик",
                   "помело", "рамбутан", "слива", "сапота",
                   "тамаринд", "танжело", "учува", "угни",
                   "финик", "фейхоа", "хурма", "хеномелес",
                   "цитрон", "цабр", "эвтерпа", "яблоко"]
    return fruits_list

def get_first_letter(message):
    first_letter = input(message)[0].lower()
    print(f'Вы ввели букву "{first_letter}"')
    return first_letter

def get_fruits(first_letter, fruits_list):
    fined_fruits_list = []
    for i in range(len(fruits_list)):
        if fruits_list[i][0] == first_letter:
            fined_fruits_list.append(fruits_list[i])
    if len(fined_fruits_list) == 0:
        fined_fruits_list.append('фрукты в списке не найдены')
    return fined_fruits_list

print_task_condition()
fruits_list = create_fruits_list()
first_letter = get_first_letter("Введите первую букву: ")
fined_fruits_list = get_fruits(first_letter, fruits_list)
print(f'{first_letter} -> ', end= '')
print(*fined_fruits_list)
