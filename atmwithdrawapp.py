balance = float(input("Enter your current balance: "))

while balance > 0:
    withdrawal = float(input("Enter the amount to withdraw (or -1 to exit): "))

    # Check if the user wants to exit
    if withdrawal == -1:
        print("Transaction ended.")
        break

    # Check if withdrawal exceeds balance
    if withdrawal > balance:
        print(f"Insufficient funds. Your current balance is: {balance}")
    else:
        balance -= withdrawal
        print(f"Withdrawal successful. Your new balance is: {balance}")

    # Stop if balance reaches zero
    if balance == 0:
        print("Your balance is zero. No more withdrawals can be made.")
        break