# python3
# Linards Tomass Beķeris 221RDB161 10.grupa

def build_heap(data):
    swaps = []  # swaps liste tuksha
    n = len(data)  # ievades datu garums

    # (n // 2 - 1)  0, -1
    for i in range(n // 2 - 1, -1, -1):
        swaps = sift_down(data, i, swaps) 

    return swaps  #atgriezh swaps

def sift_down(data, i, swaps):
    n = len(data)  # garums
    minimalaisIndx = i  # minimalais index ka index i

    kreisais = 2 * i + 1  # izrekina index
    # parbauda vai eksiste
    if kreisais < n and data[kreisais] < data[minimalaisIndx]:
        minimalaisIndx = kreisais  # updato

    labais = 2 * i + 2  # izrekina
    # parbauda vai eksiste
    if labais < n and data[labais] < data[minimalaisIndx]:
        minimalaisIndx = labais  # updeito

    # ja indekss no minimala elementa ir nomainijies no esosa i indeksa
    if i != minimalaisIndx:
        swaps.append((i, minimalaisIndx)) 
        data[i], data[minimalaisIndx] = data[minimalaisIndx], data[i]
        swaps = sift_down(data, minimalaisIndx, swaps)

    return swaps  # atgriezh swaps

def read_input_from_file(file_path):
    try:
        with open(f"tests/{file_path}", "r") as f:
            text = f.read().strip()
        return text.split('\n')
    except FileNotFoundError:
        print("Neatbilstošs faila path")
        return None
    except:
        print("Kļūda nolasot failu")
        return None


def main():
    input_veids = input(
        "Ievadi 'F' lai nolasītu inputu no faila, vai arī 'I' lai nolasītu input no klaviatūras: ").strip()

    if input_veids == 'F':
        file_name = input(
            "Ievadi faila nosaukumu. (Tie faila nosaukumi kuros būs burts 'a' nedarbosies: ")

        if 'a' in file_name:
            print("Neatbilstošs faila nosaukums")
            return

        file_path = f"{file_name.zfill(2)}"
        input_lines = read_input_from_file(file_path)

        if input_lines:
            n = int(input_lines[0])
            data = list(map(int, input_lines[1].split()))
            assert len(data) == n 

            swaps = build_heap(data)

            print(len(swaps)) 

    elif input_veids == 'I':
        try:
            n = int(input())  
            data = list(map(int, input("Ievade: ").split())) 

            assert len(data) == n 

            swaps = build_heap(data)  

            print(len(swaps)) 
            
            for i, j in swaps:
                print(i, j)

        except:
            print("Neatbilstoša ievade")
    else:
        print("Neatbilstošs ievades veids")
if __name__ == "__main__":
    main()