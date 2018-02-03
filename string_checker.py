#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

strings = ['abc', 'xyz', 'aba', '1221']

def main():
    print(check_string(strings))

def check_string(str):
    count = 0
    for str_item in str:
        if len(str_item) >= 2 and str_item[0] == str_item[-1]:
            count += 1
        else:
            pass
    return count


if __name__ == "__main__":
    main()
