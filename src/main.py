from SmartCalc import RPN

print("\nTEST\n")

rpn = RPN()
print("rpn:", rpn)
print(rpn.calc("1 + 2 / 5"))
print(RPN.form_final_expression("1 + 2 / 5"))
print(RPN.check_expression("1 + 2 / 5()"))
print()
