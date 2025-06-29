# Write a Python program to demonstrate string slicing

text = "PythonProgramming"

print("Original string:", text)

# Basic slicing
print("\nBasic Slicing:")
print(text[0:6])       
print(text[6:]) 
print(text[::2])      

# Negative indexing
print("\nNegative Indexing:")
print(text[-5:])        
print(text[:-3])        

# Step slicing
print("\nStep Slicing:")
print(text[::-1])         
print(text[1:10:2]) 

# Partial slices
print("\nPartial Slices:")
print(text[3:8])          
print(text[::3])      




print()
print("Next Program !........")
print()

# Write a Python program that manipulates and prints strings using various string methods.

# String Methods Examples
message = "  hello World!  "

# Case methods
print("\nCase Methods:")
print("Upper case:", message.upper())         
print("Lower case:", message.lower())        
print("Title case:", message.title())         
print("Capitalized:", message.capitalize())   

# Cleaning methods
print("\nCleaning Methods:")
print("Stripped:", message.strip())           
print("Left stripped:", message.lstrip())     
print("Right stripped:", message.rstrip())    

# Search methods
print("\nSearch Methods:")
print("Position of 'World':", message.find("World"))  
print("Count of 'l':", message.count("l"))    
print("Starts with 'hello':", message.lstrip().startswith("hello")) 

# Transformation methods
print("\nTransformation Methods:")
print("Replace 'World' with 'Python':", message.replace("World", "Python"))
print("Split into words:", message.strip().split())  
print("Joined with dashes:", "-".join(["hello", "world"]))

# Formatting methods
print("\nFormatting Methods:")
print("Centered string:", message.strip().center(20, "*")) 
print("Zero-padded number:", "42".zfill(5))  
