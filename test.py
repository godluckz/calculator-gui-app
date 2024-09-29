#  "89*2+20%"






import re
 
def evaluate_expression(expression):
    expression_list = [x for x in expression]
    print(expression_list)
    elements = []
    w_val = ""
    for i in expression_list: 
        # print(f"check: {i}")       
        # print(f"w_val: {w_val}")    
        # print(f"pos: {expression_list.index(i)}")
        if i.isnumeric() or i == "%":
            w_val = f"{w_val}{i}"   
            if expression_list.index(i)+1 == len(expression_list):
               elements.append(w_val) #last element
            else:
              continue #check next item first                           
        else:        
           elements.append(w_val)
           elements.append(i)
        w_val = ""                    

    print(elements)
    


    # Initialize the result to the first number
    result = int(elements[0])
    print(f"first number: {result}")
 
    # Apply each operator to the previous result and the current number
    prev_num = result          
    for i in range(1, len(elements), 2):
        print("-----------")
        print("-----------")
        num = None
        w_is_prct = False
        operator = elements[i]
        print(f"operator: {operator}")    
        print(f"prev_num: {prev_num}")    

        try:
            num = elements[i+1]
            if "%" in num:
                w_is_prct = True
                num = num.replace("%","")
            
            if num.isnumeric():
                num = int(num)
                prev_num = num
        except Exception as e:            
            result = None
    
        print(f"num: {num}")        
        if operator and num:
            if w_is_prct:
                percentage_result = (num / 100) * result
                result = result + percentage_result
            elif operator == '+':
                result += num
            elif operator == '-':
                result -= num
            elif operator in ('*','x'):
                result *= num
            elif operator == '/':
                result /= num
    
    return result
 
# Test the function
# expression = "9x3+5+20%"
expression = "89*2+20%+5"
print("The original string is:", expression)
print("The evaluated result is:", evaluate_expression(expression))



# import re

# def evaluate_expression(expression):
#     # Evaluate the initial expression
#     initial_result = (expression)
#     print(initial_result)
    
#     # Find and calculate the percentage of the initial result
#     percentage_match = re.search(r'(\d+)%', expression)
#     print(percentage_match)
#     return
#     if percentage_match:
#         percentage_value = int(percentage_match.group(1))
#         percentage_result = (percentage_value / 100) * initial_result
#         final_result = initial_result + percentage_result
#     else:
#         final_result = initial_result
    
#     return final_result

# # Get the expression from the user
# expression = "89*2+20%"

# # Evaluate the expression
# result = evaluate_expression(expression)

# # Print the result
# print("The result is:", result)