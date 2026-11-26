basic = float(input("Enter basic salary: "))
overtime = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentive: "))

hra = basic * 0.20
da = basic * 0.10
overtime_pay = overtime * 100

gross = basic + hra + da + overtime_pay + incentive
deduction = gross * 0.05
net_salary = gross - deduction

print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net_salary)