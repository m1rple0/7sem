def chastotniy_analiz():

    answer = input("Ввести алфавит  +/-  : ")
    if answer == "+":
        alphabet = input("Alphabet: ")
        alphabet_set = set(alphabet.lower())
    else:
        print("Алфавит не выбран")
        alphabet_set = None

    text = input("Введите текст для анализа: ")
    totallen = len(text)
    char_counts = {}  # словарь 

    for char in text:
        char_l = char.lower() 
        
        if alphabet_set is None or char_l in alphabet_set:
            char_counts[char_l] = char_counts.get(char_l, 0) + 1
            
    
    sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    
    print(f"Общее количество символов: {totallen}")

    for char, count in sorted_chars:
        percentage = (count / totallen) * 100
        display_char = "пробел" if char == ' ' else char
        print(f"{display_char} | {count} | {percentage:.2f}%")

chastotniy_analiz()