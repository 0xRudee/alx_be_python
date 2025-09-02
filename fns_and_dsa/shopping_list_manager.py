import os

shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            os.system('cls')
            item = str(input("What is the item you wish to add: "))
            if (not item.isalpha()) and (not isinstance(item, str)):
              print(f"The item '{item}' isn't a product")
              continue
            shopping_list.append(item)

        elif choice == '2':
            os.system('cls')
            item = str(input("What is the item you wish to remove: "))
            if item not in shopping_list:
              print(f"The item '{item}' isn't in you shopping list")
              continue
            shopping_list.remove(item)

        elif choice == '3':
            os.system('cls')
            for i in range(len(shopping_list)):
              print(shopping_list[i])

        elif choice == '4':
            os.system('cls')
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()