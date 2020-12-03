Feature: Test Search Functionality
    Scenario: Search Box Exists on page
        Given I load the website
        Then I see a component with className "Search-input"

    Scenario: I can type in the search box
        Given I load the website
        When I type "The Hunger Games" in the the search box
        Then The text "The Hunger Games" appears in the search box

    Scenario: I want to find a specific book that I know exists on the site
        Given I load the website
        When I search for "The Hunger Games"
        Then The title "The Hunger Games" by "Suzanne Collins" appears as the first result

    Scenario: I want to find a book series by searching in the author's name
        Given I load the website
        When I search for "Suzanne Collins"
        Then The title "The Hunger Games" by "Suzanne Collins" appears
        Then The title "Catching Fire" by "Suzanne Collins" appears
        Then The title "Mockingjay" by "Suzanne Collins" appears

    Scenario: I want to find a book by searching for a book's ISBN number
        Given I load the website
        When I search for "0439023521"
        Then The title "The Hunger Games" by "Suzanne Collins" appears

    Scenario: I want to find a popular book by searching in the book's genre
        Given I load the website
        When I search for "fiction"
        Then The title "Ender's Game" by "Orson Scott Card" appears

    Scenario: I want to clear out the search field after typing in some text
        Given I load the website
        When I type "The Hunger Games" in the the search box
        When I clear the text field
        Then The search box is empty

    Scenario: I want to be notified that there is no match for a book that doesn't exist
        Given I load the website
        When I search for "bigStringOfGarbageForABookThatDoesNotExist"
        Then The text "We couldn't find a match" appears

