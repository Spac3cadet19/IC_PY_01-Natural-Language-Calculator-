#Natural Language Calculator using NLP sort of
import re

class NaturalLanguageCalculator:
    def __init__(self):
        # Dictionary to convert words to numbers
        self.word_to_num = {
            'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
            'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
            'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
            'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
            'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
            'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
            'eighty': 80, 'ninety': 90, 'hundred': 100
        }
    
    def convert_words_to_numbers(self, text):
        # we are going to replace word numbers with digits
        for word, number in self.word_to_num.items():
            text = text.replace(word, str(number))
        return text
    
    def extract_numbers(self, text):
        # Find all numbers in the text
        text = self.convert_words_to_numbers(text)
        numbers = re.findall(r'-?\d+\.?\d*', text)
        return [float(num) for num in numbers]
    
    def get_operation(self, text):
        # Check which operation the user wants
        text = text.lower()
        
        if any(word in text for word in ['plus', 'add', 'sum']):
            return 'add'
        elif any(word in text for word in ['minus', 'subtract', 'take away']):
            return 'subtract'
        elif any(word in text for word in ['times', 'multiply', 'multiplied by', 'product']):
            return 'multiply'
        elif any(word in text for word in ['divide', 'divided by', 'division']):
            return 'divide'
        elif any(word in text for word in ['power', 'to the power of', 'exponent']):
            return 'power'
        elif any(word in text for word in ['modulo', 'mod', 'remainder']):
            return 'modulo'
        else:
            return None
    
    def calculate(self, num1, num2, operation):
        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2
        elif operation == 'power':
            return num1 ** num2
        elif operation == 'modulo':
            return num1 % num2
    
    def process_input(self, user_input):
        # Get the numbers from the input
        numbers = self.extract_numbers(user_input)
        
        # Check if we have enough numbers
        if len(numbers) < 2:
            return "I need at least two numbers to calculate"
        
        # Get the operation
        operation = self.get_operation(user_input)
        
        if operation is None:
            return "I couldn't understand the operation. Try using words like add, subtract, multiply, or divide"
        
        # Do the calculation
        result = self.calculate(numbers[0], numbers[1], operation)
        
        # Format the result nicely
        if isinstance(result, float) and result == int(result):
            result = int(result)
        
        return f"The answer is {result}"
    
    def run(self):
        print("Natural Language Calculator")
        print("---------------------------")
        print("Type your calculation in plain English")
        print("Examples:")
        print("  - what is five plus three")
        print("  - add 10 and 5")
        print("  - multiply 7 by 8")
        print("  - divide 20 by 4")
        print("Type 'quit' to exit")
        print()
        
        while True:
            user_input = input("Your question: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'stop']:
                print("Goodbye!")
                break
            
            result = self.process_input(user_input)
            print(result)
            print()

# Run the calculator
if __name__ == "__main__":
    calculator = NaturalLanguageCalculator()
    calculator.run()