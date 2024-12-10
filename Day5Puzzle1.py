import re
import math

#with open("Day5Puzzle1_Input_Sample.txt", "r") as file:
with open("Day5Puzzle1_Input.txt", "r") as file:    
    inputData = file.read()

splittedInputData = inputData.split('\n\n')
page_ordering_rules = splittedInputData[0].split('\n')
page_numbers_of_update = splittedInputData[1].split('\n')
#print(f"page_ordering_rules: {page_ordering_rules}")
#print(f"page_numbers_of_update: {page_numbers_of_update}")

sum_of_middle_page_numbers_of_correct_updates = 0

for page_number_of_update in page_numbers_of_update:
    page_numbers = page_number_of_update.split(',')
    #print(f"page_number_of_update: {page_number_of_update}")
    
    rule_passed = True

    for page_ordering_rule in page_ordering_rules:
        rule_parts = page_ordering_rule.split('|')
        rule_first_page = rule_parts[0]
        rule_second_page = rule_parts[1]

        if all(page_number in page_numbers for page_number in rule_parts):
            #print(f"page_number_of_update: {page_number_of_update} contains all rule parts {rule_parts}")

            # check if rule_first_page is followed by rule_second_page
            if page_numbers.index(rule_second_page) > page_numbers.index(rule_first_page):
                #print(f"page_number_of_update: {page_number_of_update} contains all rule parts {rule_parts} and {rule_first_page} is followed by {rule_second_page}")
                pass
            else:
                #print(f"page_number_of_update: {page_number_of_update} contains all rule parts {rule_parts} but {rule_first_page} is NOT followed by {rule_second_page}")
                rule_passed = False
                continue
        else:
            #print(f"page_number_of_update: {page_number_of_update} does NOT contain all rule parts {rule_parts}")
            continue

    if rule_passed:
        middle_page_number = page_numbers[len(page_numbers) // 2]
        sum_of_middle_page_numbers_of_correct_updates += int(middle_page_number)
        #print("middle page number of correct update: ", middle_page_number, " update: ", page_numbers)

print("sum of middle page numbers of correct updates: ", sum_of_middle_page_numbers_of_correct_updates)