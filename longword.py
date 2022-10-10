def longest_word(filename):
    with open(filename) as file_name:
        longword = ''
        for line in my_file:
            stripped_line = line.strip()
            tokens = stripped_line.split()
            for word in tokens:
                if len(word) > len(longword):
                    longword = word     
    return longword
            
print(longest_word(input("please enter file name: ")))