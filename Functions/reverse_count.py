class StringOperations:
    
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_string(self):
        return self.input_string[::-1]

    def count_strings(self):
        words = self.input_string.split()
        return len(words)


class CustomString(StringOperations):
    def __init__(self, input_string):
        super().__init__(input_string)

    def reverse_string(self):
        reversed_str = super().reverse_string()
        return f"Reversed String: {reversed_str}"

    def count_strings(self):
        count = super().count_strings()
        return f"Number of Words: {count}"


input_text = "Hey, Good Morning"
custom_str = CustomString(input_text)

reversed_result = custom_str.reverse_string()
print(reversed_result) 
count_result = custom_str.count_strings()
print(count_result)  
