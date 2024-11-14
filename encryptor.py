import random

class Encryptor:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2
        self.__result = self.__perform_operation()

    def __perform_operation(self):
        operation = random.choice(['+', '-', '*', '/'])
        
        if operation == '+':
            result = self.__num1 + self.__num2
        elif operation == '-':
            result = self.__num1 - self.__num2
        elif operation == '*':
            result = self.__num1 * self.__num2
        elif operation == '/':
            if self.__num2 != 0:
                result = self.__num1 / self.__num2
        return result

    def __str__(self):
        return f"результат: {self.__result}"

encryptor = Encryptor(10, 10)

print(encryptor)

