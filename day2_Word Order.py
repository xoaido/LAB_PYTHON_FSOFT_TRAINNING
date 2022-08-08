#You are given  words. Some words may repeat. For each word, output its number of occurrences. 
#The output order should correspond with the input order of appearance of the word. 
# See the sample input/output for clarification.
from collections import Counter

if __name__ == '__main__':
    n = int(input("Nhập số phần tử trong mảng : "))
    LIST = []
    for i in range(n):
        LIST.append(input().strip())#thêm đối tượng vào cuối list bỏ khoảng trắng ở đầu cuối
    count = Counter(LIST)
    print(len(count))# in ra số lượng phần tử duy nhất trong mảng
    print(*count.values())#Phương thức Counter.Values ​​() giúp thấy tần số của từng phần tử duy nhất.




#print(Counter(LIST))
#print(list(count.elements()))
#print(LIST)