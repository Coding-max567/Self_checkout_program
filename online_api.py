from datetime import datetime, timedelta

# Function to display the available categories to the user
def display_categories(categories):
    print("\nAvailable categories:")
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category}")

# Function to display the available items within a selected category
def display_items(items):
    print("\nAvailable items:")
    for idx, item in enumerate(items, 1):
        print(f"{idx}. {item}")

# Main function that handles the self-checkout process
def checkout_system():
    # Dictionary containing categories and their respective items
    categories = {
        'Appliances': ['Toaster', 'Blender', 'Microwave', 'Coffee Maker'],
        'Electronics': ['Laptop', 'Smartphone', 'Headphones', 'Camera'],
        'Furniture': ['Chair', 'Table', 'Sofa', 'Bed']
    }
    
    # List to store the items selected by the user for purchase
    cart = []
    
    print("Welcome to the self-checkout system!")

    # Loop to allow the user to browse categories and select items
    while True:
        # Display available categories
        display_categories(categories)
        # Prompt the user to choose a category or finish shopping
        category_choice = input("\nEnter the number of the category you want to explore (or type 'done' to finish): ")
        
        # Check if the user is done with shopping
        if category_choice.lower() == 'done':
            break
        
        # Validate the user's category choice
        if not category_choice.isdigit() or int(category_choice) not in range(1, len(categories) + 1):
            print("Invalid choice. Please select a valid category number.")
            continue
        
        # Get the selected category name based on user input
        category_name = list(categories.keys())[int(category_choice) - 1]
        # Retrieve the items in the selected category
        items = categories[category_name]
        
        print(f"\nYou selected: {category_name}")
        # Display items available in the selected category
        display_items(items)
        
        # Loop to allow the user to select items from the chosen category
        while True:
            # Prompt the user to choose an item or finish the category selection
            item_choice = input("\nEnter the number of the item to add to cart (or type 'finish' to move to the next category): ")
            
            # Check if the user is done with the current category
            if item_choice.lower() == 'finish':
                break
            
            # Validate the user's item choice
            if not item_choice.isdigit() or int(item_choice) not in range(1, len(items) + 1):
                print("Invalid choice. Please select a valid item number.")
                continue
            
            # Get the selected item name based on user input
            item_name = items[int(item_choice) - 1]
            # Add the selected item to the cart
            cart.append(item_name)
            print(f"Added {item_name} to cart.")
    
    # Check if the cart is empty and inform the user
    if len(cart) == 0:
        print("Your cart is empty. No items to checkout.")
        return
    
    # Record the current date as the purchase date
    purchase_date = datetime.now().strftime('%Y-%m-%d')
    
    # Assume a shipping time of 5 days
    shipping_time = 5  # in days
    # Calculate the expected arrival date based on the shipping time
    arrival_date = (datetime.now() + timedelta(days=shipping_time)).strftime('%Y-%m-%d')
    
    # Display the checkout summary to the user
    print("\n--- Checkout Summary ---")
    print(f"Date of Purchase: {purchase_date}")
    print("Items Purchased:")
    for idx, item in enumerate(cart, 1):
        print(f"{idx}. {item}")
    
    # Inform the user of the expected arrival date
    print(f"Expected Arrival Date: {arrival_date}")
    print("\nThank you for your purchase!")

# Run the checkout system
checkout_system()



