Part A

1. 6 9 8
2. FDE
3. 5 0
4. 4 \n 2
5. 1 F \n 2 D \n 3 E
6. 3 , i will add in total till loops break
7. None 0 1 , get will use None as default if key,value not present in dict, else passed default value, or present value
8. {'a': 2, 'b': 1, 'c': 1} as we can see in dict is empty will get filled one by one if exist it will add +1 to prev value else 1 will be set.
9. TODO
10. [1, 9, 25] output will be list of all square of odd numbers based on range and condition

Part B 11. Every function return something even if a function doesn't have return statement then that function return by default is None.

function with only print not return : Use to show the output during execution
def add(a,b):
print(a+b)

function with return : It gives back the value at call site to reuse at later point.
def add(a,b):
return a+b

12. self reference to an instance created by the class, and it is automatically passes internally by python when we call a method but if we don't accept self as parameter at definition it will gives TypeError.

13. because default parameter in functions needs to be on end and default argument is use when there could be a default value if we don't pass anything

14. when we are not sure how many times a loop needs to run and it only stops until a condition changes, for an example retry logic of API connection due to internet issue, for loop runs in a range so in API connection scenerio using foor loop can cause issue of overloop or underloop.

15.

16. Break ends the loop after particula condition fulfill, and continue skip the next statement only

17. whenever data needs meaning we use dictionary as key, value pairs. List is mainly use for keeping the order of collection of items. searching an item is easy in dictionary using key.

18. .get methods doesn't give error if a specific key missing, and d["phone"] raise a KeyError of phone key is missing. for data i created i would use d["phone"] because it will raise error in code to fix.client's might miss "phone" key so i would use get to handle missing information.
