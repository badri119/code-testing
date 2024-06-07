with open('test.txt', 'r') as reader:
    list = reader.readlines()
    # print(list)
    reversed = reversed(list)
    print(reversed)
    with open('test.txt', 'w') as writer:
        for line in reversed:
            writer.write(line)

