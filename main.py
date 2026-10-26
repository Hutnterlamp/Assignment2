"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45
COFFEE_COST = 3  

# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    semester_cost_per_credit = annual_cost / SEMESTERS_PER_YEAR / credits
    cs1430_semester_cost = semester_cost_per_credit * CS1430_CREDITS
    return cs1430_semester_cost / CS1430_MEETINGS_PER_SEMESTER




def coffee_cost_per_year(coffee_cost):
    """Give back the annual cost of coffee."""
    coffees_per_year = (SEMESTERS_PER_YEAR * CS1430_MEETINGS_PER_SEMESTER * 3)
    return coffees_per_year * coffee_cost

# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter the annual cost of college: "))
    credits = float(input("Enter the credits this semester: "))# Then ask for the credits this semester.

    while True:
        print("Menu: ")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6. Cost of coffee per class")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            break
        elif choice == "1":
                print(f"Cost per semester: $ {cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
                print(f"Cost per month: $ {cost_per_month(annual_cost):.2f}")
        elif choice == "3":
                print(f"Cost per day: $ {cost_per_day(annual_cost):.2f}")
        elif choice == "4":
                print(f"Cost per credit: $ {cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
                print(f"Cost per class: $ {cost_per_class(annual_cost, credits):.2f}")
        elif choice == "6":
                print(f"Cost of coffee per class: $ {coffee_cost_per_year(COFFEE_COST) / (SEMESTERS_PER_YEAR * CS1430_MEETINGS_PER_SEMESTER):.2f}")
        else:
                print("Invalid choice. Please try again.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
