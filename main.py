def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words_count = len(file_contents.split())
        map_char_frankestein ={}
        file_contents_arr = list(file_contents)
        for char in file_contents_arr:
            lower_char = char.lower()
            if not lower_char.isalpha():
                continue
            num_char= map_char_frankestein.get(lower_char,0)
            map_char_frankestein[lower_char]= num_char +1    

        result ='--- Begin report of books/frankenstein.txt ---\n'
        result+=f'{words_count} words found in the document \n\n'
        for key in map_char_frankestein:
            num_times_char = map_char_frankestein.get(key)
            result+=f"The '{key}' character was found {num_times_char} times\n"
        result+='--- End report ---'

        print(result)
       


main()
#print(f"the number of p is {new_dict.get('p')},the number of c is {new_dict.get('c')}, the number of whitespaces is {new_dict.get(' ')}")
#print(new_dict)

def countChar():
    string_test='hi pip'
    #string_test_char = string_test.split('')
    string_test_char=list(string_test)
    return len(string_test_char)

#print(f"la lunghezza della stringa hi pip is {len('hi pip')}, il numero di caratteri sono {countChar()}")