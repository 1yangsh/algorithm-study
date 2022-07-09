n = int(input())
string = str()

for _ in range(n):
    string = str()
    while True:
        try:
            input_str = input()
            if input_str == "":
                break
            string += input_str
        except:
            break

    
    length = len(string)
    ratio = round(((length - string.count("#")) / length) * 100, 1)

    if ratio == int(ratio):
        ratio = int(ratio)

    print(f"Efficiency ratio is {ratio}%.")
    



    