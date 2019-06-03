import time

pout = [1, 2, 3, 4]

counter = 0

def to_binary(value):
    binary = []
    while value != 0:
        bit = int(value % 2)
        binary.append(bit)
        value = int(value / 2)
    binary.reverse()
    for dummy in range(4-len(binary)):
        binary.insert(0, 0)
    return binary

while True:
    if counter == 11:
        counter = 0
        binary = to_binary(counter)
        for i in range(0, 4):
            print(pout[i], binary[i])
        time.sleep(1)
        counter += 1
        print(" ")
    else:
        binary = to_binary(counter)
        for i in range(0, 4):
            print(pout[i], binary[i])
        time.sleep(1)
        counter += 1
        print(" ")    
