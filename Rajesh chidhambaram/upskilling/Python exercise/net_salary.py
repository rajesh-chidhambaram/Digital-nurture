#function
def net_salary(salary,tax_rate):
    tax = salary * tax_rate
    net_salary = salary-tax
    return net_salary

#Example as per instructions
salary = 75000.5
tax_rate = 0.18
net = net_salary(salary,tax_rate)
print(f"Net Salary: {net:.2f}")

