# Checkout_System
## Overview
The Self-Checkout System is a command-line Python application that simulates an online shopping experience. Users can browse different categories of products, select items to add to their cart, and proceed to checkout. The program then displays the date of purchase and calculates the expected delivery date based on a predefined shipping time.

## Features
- Category Browsing: Users can select from various categories such as Appliances, Electronics, and Furniture.
- Item Selection: Users can choose items from the selected category to add to their shopping cart.
- Checkout Process: The system provides a summary of the items purchased, the date of purchase, and the expected arrival date.

## Running the Program
- Open a terminal or command prompt.
- Navigate to the directory where the program is located.
Run the program using the following command:
python checkout_system.py

### Using the Program
- Welcome Screen: After starting the program, you will see a welcome message and a list of available categories.
- Category Selection: Enter the number corresponding to the category you want to explore.
- Example: If you want to explore "Electronics," type 2 and press Enter.
- Item Selection: Once you select a category, a list of items within that category will be displayed. Enter the number corresponding to the item you want to add to your cart.
- Example: If you want to add a "Smartphone" to your cart, type 2 and press Enter.
- Continue Shopping: You can continue browsing other categories or finish your shopping by typing finish when prompted.
- Checkout: Once you are done, the program will display a summary of your purchase, including the date of purchase and the expected delivery date.
- Exit: The program will thank you for your purchase and exit.

### Example Workflow
- Start the program.
- Select the "Electronics" category.
- Add "Smartphone" and "Headphones" to your cart.
- Select "finish" to stop shopping.
- View the checkout summary with the purchase date and expected arrival date.
  
### Code Overview
- display_categories(categories): Displays the available product categories.
- display_items(items): Shows the items available in the selected category.
- checkout_system(): Handles the entire checkout process, from category selection to checkout.
