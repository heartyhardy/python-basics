print("\n")
left = int(input("Enter left operand: "))
right = int(input("Enter right operand: "))
operation = input("Enter Operation: ")

match operation:
  case "+":
    print("\nAddition of {} and {} is: {}".format(left , right, left + right));
  case "-":
    print("\nSubstraction of {} and {} is: {}".format(left , right, left - right));
  case "*":
    print("\nMultiplication of {} and {} is: {}".format(left , right, left * right));
  case "/":
    print("\nDivision of {} and {} is: {}\n".format(left , right, left / right));
