Feature: Testing functionality for the checkout cart

    This includes functionaity for adding to the cart and modifying the order within the cart

    Scenario: The add to cart button exists on the page
        Given I load the website
        When I go to "/w/the-hunger-games-by-suzanne-collins/246187/#edition=5277544&idiq=2904092" page
        Then The Add to Cart Button exists on the page

    Scenario: I can successfully add a book to the cart
        Given I load the website
        When I go to "/w/the-hunger-games-by-suzanne-collins/246187/#edition=5277544&idiq=2904092" page
        When I click add to cart
        Then I see this component "Added to your cart!"

    Scenario: I can succssfully change the quanitity of books I wish to add to my cart
        Given I load the website
        When I go to "/w/the-hunger-games-by-suzanne-collins/246187/#edition=5277544&idiq=2904092" page
        When I change the quanitity of books to "5"
        Then I the quanitity of books becomes "5"

    Scenario: I can add multiple copies of the same book to my cart
        Given I load the website
        When I go to "/w/the-hunger-games-by-suzanne-collins/246187/#edition=5277544&idiq=2904092" page
        When I change the quanitity of books to "5"
        When I click add to cart
        Then I see this component "Added to your cart!"

    Scenario: The view cart button appears after adding to the cart
        Given I load the website
        When I go to "/w/the-hunger-games-by-suzanne-collins/246187/#edition=5277544&idiq=2904092" page
        When I click add to cart
        Then I see a component with className "btn-ViewCart"

    Scenario: The proceed to checkout button appears after adding to the cart
        Given I load the website
        When I go to "/w/the-hunger-games-by-suzanne-collins/246187/#edition=5277544&idiq=2904092" page
        When I click add to cart
        Then I see a component with className "btn-Checkout"

    Scenario: If I view my cart after adding a book, that book will appear
        Given I load the website
        When I go to "/w/the-hunger-games-by-suzanne-collins/246187/#edition=5277544&idiq=2904092" page
        When I click add to cart
        When I click a button with className "btn-ViewCart"
        Then I see this component "The Hunger Games"

    Scenario: If I proceed to checkout after adding a book, the place order button will appear
        Given I load the website
        When I go to "/w/the-hunger-games-by-suzanne-collins/246187/#edition=5277544&idiq=2904092" page
        When I click add to cart
        When I click a button with className "btn-ViewCart"
        Then I see a component with className "PlaceOrder-submitButton"

    Scenario: I can remove a book from my cart
        Given I load the website
        When I go to "/w/the-hunger-games-by-suzanne-collins/246187/#edition=5277544&idiq=2904092" page
        When I click add to cart
        When I click a button with className "btn-ViewCart"
        When I click a button with className "ShoppingCartItem-remove"
        Then I do not see this component "The Hunger Games"