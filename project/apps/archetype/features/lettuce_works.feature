Feature: Visiting archetype test urls
    In order to ensure that my fork is working
    As a developer
    I visit the test page, and make sure it has the right content.

    Scenario: Visiting a correct url
        Given I access the django url "/archetype-test"
        When I wait 1 second
        Then I should see "12345"
          And I should see "678910"
          And the element with the CSS selector of ".hidden" should not be visible
