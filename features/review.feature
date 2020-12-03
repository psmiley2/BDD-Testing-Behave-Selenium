Feature: Test Review Functionality
    Scenario: I can find the write a review button on the page
        Given I load the website
        When I go to "/w/the-hunger-games-by-suzanne-collins/246187/#edition=5277544&idiq=2904092" page
        Then I see a component with className "WorkReviews-writeButton"

    Scenario: I can click the write a review button on the page
        Given I load the website
        When I go to "/w/the-hunger-games-by-suzanne-collins/246187/#edition=5277544&idiq=2904092" page
        Then I click Write a Review

    Scenario: I can access the review page
        Given I load the website
        When I go to "/w/the-hunger-games-by-suzanne-collins/246187/review/" page
        Then I see this component "Write a Review"

    Scenario: I can leave a 5-star rating
        Given I load the website
        When I go to "/w/the-hunger-games-by-suzanne-collins/246187/review/" page
        When I click "5" star(s)
        Then The review has "5" star(s)

    Scenario: I can enter a headline for my reivew
        Given I load the website
        When I type "So Great!" in the headline
        Then The text "So Great!" is in the headline

    Scenario: I can enter a review
        Given I load the website
        When I type "I was on the edge of my seat the whole time!" in the review
        Then The text "I was on the edge of my seat the whole time!" is in the review

    Scenario: I can enter a display name
        Given I load the website
        When I type "Hung3erGam3sFan498" in the display name
        Then The text "Hung3erGam3sFan498" is in the display name