# DAY – 1 

## Topic Covered: 
***1. Numeric Types:*** - Int, float 

***2. Sequential Types:*** - Str, List, Tuple 

***3. Dictionary***

***4. Set Types***

***5. Conditional Statements:*** - If, If-else, Nested If 

***6. Loop:*** - For, while 

   ***Problems***

 

 

### 1. Numeric Types:

***int:*** Represents integer values (whole numbers). 

```
a = 10 
Print(a) 
```
Output: 10 


***float:*** Represents floating-point numbers (decimal values). 
```
b = 3.14 
Print(b) 
```
Output: 3.14 

 

### 2. Sequential Types:

***Str:*** Represents sequences of characters (text). 
```
str1 = "Hello, World!" 
```

#### Basic Operations:

***Concatenation:*** Using + 
```
str1 = "Hi"  
str2 = "hello"  
result = str1 + " " + str2  
print(result) 
```
Output: "Hi hello" 

 
***Repetition:*** Using * 
```
str = "a" 
n = 3 
result = str * n 
print(result)   
```
Output: "aaa" 

 

***Slicing:*** Accessing parts of a string. 
```
str = "Hello, World!" 
substr = str[7:12]   
print(substr)   
```
Output: "World" 

***String Functions:*** 

***len():*** Returns the length of the string. 
```
str = "yes!" 
length = len(str) 
print(length)  
```
Output: 3 

 

 

#### Common String Methods:

 

***lower():*** Converts to lowercase. 
```
str = "Hello" 
lowercase = str.lower() 
print(lowercase)   
```
Output: "hello" 

 

***upper():*** Converts to uppercase. 
```
str = "Good" 
uppercase = str.upper() 
print(uppercase)   
```
Output: "GOOD" 

 

***islower():*** Checks if all characters are lowercase. 
```
str = "hello" 
is_lower = str.islower() 
print(is_lower)   
```
Output: True 

 

***isupper():*** Checks if all characters are uppercase. 
```
str = "AAA" 
is_upper = str.isupper() 
print(is_upper)   
```
Output: True 

  

***index():*** Like find(), but raises a ValueError if not found. 
```
str = "yes, no" 
index = str.index("no") 
print(index)   
```
Output: 5 

 

***replace():*** Replaces a substring with another. 
```
str = "Hlo, Bro" 
replaced = str.replace("Bro", "Sir") 
print(replaced)   
```
Output: "Hlo, sir" 

 

***count():*** Counts occurrences of a substring 
```
str = "Hello, World! Hello!" 
count = str.count("Hello") 
print(count)  
```
Output: 2 

 

***List:*** An ordered, mutable collection of items. 

Ex: - Alph = ["a", "b", "c"]  

or  

Num= [1,2,3] 


#### List Operations:

***Concatenation:*** Use + to combine lists. 
```
Alph = ["a", "b", "c"] 
Num= [1,2,3]  
combined_list = Alph + Num 
print(combined_list)  
```
Output: ["a", "b", "c", 1, 2, 3] 

***Repetition:*** Use * to repeat lists. 
```
Alph = ["a", "b", "c"] 
repeated_list = Alph * 2  
print(repeated_list)  
```
Output: ["a", "b", "c", "a", "b", "c"] 

***Slicing:*** Access a subset of the list. 
```
Alph = ["a", "b", "c"]  
sublist = Alph[1:3] 
print(sublist) 
```
Output: ["b", "c"] 

 

***List Functions:*** 

 

***len():*** Returns the number of elements in the list. 
```
Alph = ["a", "b", "c"]  
length = len(Alph)  
print(length) 
```
Output: 3 

***max():*** Returns the largest item in the list. 
```
Num= [1,2,3]  
largest = max(Num) 
print(largest)  
```
Output: 3 

***min():*** Returns the smallest item in the list. 
```
Num= [1,2,3]  
smallest = min(Num)  
print(smallest)  
```
Output: 1 

***sum():*** Returns the sum of all items in the list (if numeric). 
```
Num= [1,2,3]  
total = sum(Num)  
print(total) 
```
Output: 6 

 

 

##### Common List Methods: 

 

***append():*** Adds an item to the end of the list. 
```
Alph = ["a", "b", "c"]  
Alph.append("d")  
print(Alph)  
```
Output: ["a", "b", "c", "d"] 

***insert():*** Inserts an item at a specified index. 
```
Alph = ["a", "b", "c", "d"]  
Alph.insert(1, "z")  
print(fruits)  
```
Output: ["a", "z", "b", "c", "d"] 

***remove():*** Removes the first occurrence of a value. 
```
Alph = ["a", "b", "c", "d"]  
Alph.remove("b")  
print(fruits)  
```
Output: ["a", "z", "c", "d"] 

***pop():*** Removes and returns an item at a specified index (default is the last item). 
```
Alph = ["a", "z", "c", "d"]  
item = Alph.pop(1)  
print(item)  
```
Output: ["a", "c", "d"] 

***index():*** Returns the index of the first occurrence of a value 
```
Alph = ["a","c", "d"]  
index = Alph.index("c")  
print(index)  
```
Output: 1 

***count():*** Counts the number of occurrences of a value. 
```
count = Alph.count("a")  
print(count)  
```
Output: 1  

***sort():*** Sorts the list in place (ascending by default). 
```
num= [2,1,3]  
num.sort()  
print(numbers)  
```
Output: [1, 2, 3] 

***reverse():*** Reverses the order of the list in place. 
```
Alph = ["a","c", "d"]  
Alph.reverse()  
print(fruits)  
```
Output: ["d", "c", "a"] 

***copy():*** Returns a shallow copy of the list. 
```
Alph = ["d", "c", "a"]  
new_list = Alph.copy()  
print(new_list)  
```
Output: ["d", "c", "a"] 

 

 

 

 

 

 

 

	 

***Tuple:*** An ordered, immutable collection of items. 

Ex: - coordinates = (10, 20)  

 

### 3. Dictionary 

***dict:*** Represents key-value pairs for efficient data retrieval. 

Ex: - person = {"name": "Alice", "age": 30}  


### 4.set: An unordered collection of unique items. 

Ex: - unique_numbers = {1, 2, 3, 4, 4} 

 

### 5. Conditional Statements: 

***if:*** Executes a block of code if the condition is true. 
```
a=10
if a > 5: 
    print("a is greater than 5") 
```
Output: a is greater than 5

***if-else:*** Executes one block if the condition is true and another if false. 
```
if a > 5: 
    print("a is greater than 5") 
else: 
    print("a is not greater than 5") 
```
Output: a is not greater than 5.

***nested if:*** An if statement inside another if statement. 
```
a=10
if a > 5: 
    if a < 15: 
        print("a is between 5 and 15")
    else:
        print("a is 15 or greater")
else:
    print("a is 5 or less") 
 ```
Output: a is between 5 and 15
### 6.Loops: 

***for loop:*** Iterates over a sequence or range. 
```
for i in range(1, 6):
    print(i)
```
Output: 
1
2
3
4
5

***while loop:*** Repeats as long as a condition is true. 
```
count = 0 
while count < 5: 
    print(count) 
    count += 1 
 ```
Output: 
0
1
2
3
4


## Problems
```
s = "[{}()]"
# Initialize an empty stack
stack = []
for char in s:
    # Character is an opening bracket, push it onto the stack
    if char in "({[":
        stack.append(char)
    # If the character is a closing bracket
    elif char in ")}]":
        # Check if the stack is empty or the top of the stack does not match the current closing bracket
        if not stack or {')': '(', '}': '{', ']': '['}[char] != stack.pop():
            print(False)  # if there's a mismatch
            break
else:
    # If we didn't break, check if the stack is empty
    print(not stack)
```
Output: True

```
def is_valid(s):
    # Continuously check for and remove adjacent matching pairs of brackets
    while '()' in s or '{}' in s or '[]' in s:
        # Replace the found pairs with an empty string
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    
    # After all pairs are removed, check if the string is empty
    return s == ''  #all brackets were matched correctly
print(is_valid("[{}()]")) 
```
 Output: True

 

 

 

 

 

 

 