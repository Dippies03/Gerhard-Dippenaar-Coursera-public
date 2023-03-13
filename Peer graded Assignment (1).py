#!/usr/bin/env python
# coding: utf-8

# # Gerhard Dippenaar Graded Assignment Notebook

# #### This notebook will serve as evidence of completing the *Tools for Data Science* section of the IBM Data Science Professional Certificate for Gerhard Dippenaar. 

# **These are the 3 most popular data science languages.**
# 
# * Python
# * R
# * SQL

# |Tool name|Category|Open source|
# |:---|:---|:---|
# |MySQL|Data Management|Yes|
# |IMB DB2| Data Managment|No|
# |Tableau|Data Visualization|No|
# |Kibana|Data Visualization|Yes|
# 
# 

# **These coding snippets will demonstrate how to use Python to perform simple arithmetic expressions.** <br>
# * Cell 7 is a program that asks the user to enter two numbers, then asks for the operation, performs it, and prints the results.
# * Cell 8 converts minutes into hours

# In[7]:


# Prompt the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ask the user if they want to multiply or add the numbers
operation = input("Press 'a' to add the numbers. Press 'm' to multiply them.  ")

# Do the operation and print the result
if operation == "m":
    result = num1 * num2
    print(f"The product of {num1} and {num2} is {result}.")
elif operation == "a":
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")
else:
    print("Invalid operation. Please enter 'm' or 'a'.")


# In[8]:


# Prompt the user to enter minutes
minutes = int(input("Enter the number of minutes: "))

# Convert minutes to hours and minutes
hours = minutes // 60
remaining_minutes = minutes % 60

# Print the result
print(f"{minutes} minutes is {hours} hours and {remaining_minutes} minutes.")


# **The objectives of this activity is to:** <br>
# * Create and share a public Jupyter notebook, in any language, in Watson Studio and create markdown cells for peer review.
# * Evaluate and grade final assignments submitted by fellow learners using the given rubric. Provide constructive feedback and offer ideas and suggestions that fellow learners can apply right away.

# Writen by **Gerhard Dippenaar**.

# In[ ]:




