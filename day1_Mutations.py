# Read a given string, change the character at a given index and then print the modified string.
def replace_character(string, location, character):
    l = list(string)#chuyền string vào một list
    l[location] = character #thay thế ký tự mới vào vị trí muốn thay đổi
    string = ''.join(l)  #nối các ký tự trong list 
    return string  #hàm trả về chuỗi đã được thay đổi
   
if __name__ == '__main__':
    string = input("Enter String :")
    i = input("Enter location :")
    c = input ("Enter character :")
    new_string = replace_character(string, int(i), c)
    print(new_string)