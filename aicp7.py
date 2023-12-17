
charities = ["Charity A", "Charity B", "Charity C"]
charity_totals = [0, 0, 0]


for i, charity in enumerate(charities, start=1):
    print(f"{i}. {charity}")


while True:
    try:
        choice = int(input("Choose a charity (1, 2, or 3): "))
        if 1 <= choice <= 3:
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")


try:
    shopping_bill = float(input("Enter the shopping bill amount: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")


donation = 0.01 * shopping_bill
charity_totals[choice - 1] += donation


def record_donation():
    while True:
        try:
            choice = int(input("Choose a charity (1, 2, or 3, -1 to show totals): "))
            if choice == -1:
                break
            elif 1 <= choice <= 3:
                shopping_bill = float(input("Enter the shopping bill amount: "))
                donation = 0.01 * shopping_bill
                charity_totals[choice - 1] += donation
                print(f"Donation of ${donation} recorded for {charities[choice - 1]}.")
            else:
                print("Invalid choice. Please enter 1, 2, 3, or -1.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_totals():
    sorted_charities = sorted(zip(charities, charity_totals), key=lambda x: x[1], reverse=True)
    grand_total = sum(charity_totals)

    print("\nCharity Totals:")
    for charity, total in sorted_charities:
        print(f"{charity}: ${total}")

    print("\nGRAND TOTAL DONATED TO CHARITY:", grand_total)


record_donation()
record_donation()
show_totals()
