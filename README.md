# Shopping cart

It is a partial implementation of a shopping till system, which you might find at a supermarket.
This implementation was done by a Junior developer, you as a Senior Software Engineer have been requested to refactor this project.
You may make any technical decisions you would like, but must not change the given abstract class (abc.ShoppingCart) which is used by the shopping till hardware and cannot be easily updated.
Please treat this code as an element of a larger production system. The code is being refactored to ensure reliability and testability.

Tasks requested:
- Make the receipt print items in the order that they were added
- Add a 'Total' line to the receipt. This should be the full price we should charge the customer
- Be able to fetch product prices from an external source (json file, database ...)
- Be able to display the product prices in different currencies (not only Euro).
- Update the test suite to extend coverage and limit the number of tests which need changing when changes are introduced
- Any other changes which improve the reliability of this code in production

If you do not have enough information, make any assumptions you would like and note them down with TODO comments. Feel free to make comments that highlight completion of the tasks listed above.

Please budget 3 hours to complete, and your code should be production ready, clean and tested! Please ensure the code is version controlled also, and make sure to make several commits with sensile commit messages while working on this. When submitting please either:
- Provide a Github/GitLab/etc. link that we can view and clone your work; or
- Use git-bundle (https://git-scm.com/docs/git-bundle) to create a bundle file and send this to us.

## Moyo's comments

Assumptions:
- The directive to not change the abstract class (abc.ShoppingCart) concerns the class name and not the declared abstract methods in the class. Meaning, additional methods can be added.
- The print_receipt method, when called, represents the last step of shopping cart, basically means check out to payment.

What was done:
- Renamed the abc.py file to base.py because  abc.py is the name of the standard library module that is essential for the Python interpreter internals hence an improper shadowing occurs
- Used a yaml file to store prices because of its easy readability. A proper assessment should be conducted for production purposes. 
- Added new abstract methods: remove_item and empty_cart; because it logically makes sense. You should be able to add, remove and empty your cart. 
- Added cart_data dictionary to collect cart data upon printing receipt. This can be added to the session data in the wider system
- Added a logger to capture logs for debugging. This might already exist in the wider system
- Used a config test file to cater for repeated instantiation of cart
- Moved file paths to config. It is better for code maintenance
- Defined list of acceptable currencies in config because this is generally static information which can be updated as required.
- Added a requirements.txt file though this would probably already exist in the wider system
- Pushing all changes a single commit to enable the examiners see the changes against the original code easily.
- Code formatted locally with isort (for structuring imports) and black (for general code structure). These can be added to the pipeline in production to ensure code merged to prod branch is of top format.