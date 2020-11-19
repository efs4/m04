# m04
This assignment is based on **h03**.  You may use your work from that assignment as a starting-point for this assignment.

Build a Python program called `aloha_e2.py` that prompts the user for their name and age.

If the user enters `'John'` or `'Jane'` for their name, the program prints-out: `Hello, John.` or `Hello, Jane.`

For any other name, like Ali, the program prints-out: `Aloha e Ali.`

If the user enters a number for their age, the program prints-out their age in two years, as in:
* `Please enter your age: `
* Suppose the user enters 18
* The program prints-out: `In two years you will be 20.`

However, if the user does not enter a number, the program repeatedly prompts them to enter a number: `OOPS! Please enter a number for your age: `
Your program should repeatedly prompt the user to enter a number for their age.

Here are some sample interactions:
### Sample 0
```
Please enter your name: Ty
Aloha e Ty.
Please enter your age: 19
In two years you will be 21.
```

### Sample 1
```
Please enter your name: Jane
Hello, Jane.
Please enter your age: twenty
    OOPS! Please enter a number for your age: twenty-one
    OOPS! Please enter a number for your age: daybreak
    OOPS! Please enter a number for your age: 22
In two years you will be 24.
```

### Sample 2
```
Please enter your name: John
Hello, John.
Please enter your age: 25
In two years you will be 27.
```

