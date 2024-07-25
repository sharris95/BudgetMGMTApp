# budget_management.py

class BudgetCategory:
    def __init__(self, name, allocated_budget):
        self.__name = name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # Getter for category name
    @property
    def name(self):
        return self.__name

    # Setter for category name
    @name.setter
    def name(self, name):
        self.__name = name

    # Getter for allocated budget
    @property
    def allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    @allocated_budget.setter
    def allocated_budget(self, budget):
        if budget < 0:
            raise ValueError("Budget should be a positive number.")
        self.__allocated_budget = budget
        self.__remaining_budget = budget

    # Method to add an expense to the category
    def add_expense(self, amount):
        if amount < 0:
            raise ValueError("Expense amount should be positive.")
        if amount > self.__remaining_budget:
            raise ValueError("Not enough budget remaining.")
        self.__remaining_budget -= amount

    # Method to display the budget category details
    def display_category_summary(self):
        print(f"Category: {self.__name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")

def main():
    # Create instances of BudgetCategory
    food_category = BudgetCategory("Food", 500)
    entertainment_category = BudgetCategory("Entertainment", 300)
    utilities_category = BudgetCategory("Utilities", 200)

    # Add expenses
    food_category.add_expense(100)
    entertainment_category.add_expense(50)
    utilities_category.add_expense(75)

    # Display summaries
    food_category.display_category_summary()
    entertainment_category.display_category_summary()
    utilities_category.display_category_summary()

if __name__ == "__main__":
    main()
