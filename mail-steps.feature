Feature: Compose and send mail

  # Background: 
  #   Given I am on gmail page

 Scenario: Login using valid user email-id on gmail page
  When I login with username "senders mail" and password "password"
  Then I should be on "Home" page

 Scenario: Compose message
  When I click on "Compose"
  Then I should see "Message box"
  Then I enter username "receivers mail" in "Recipients box"
  And I enter "Subject" in "Subject box"
  Then I enter "Message" in "Message body"

 Scenario: Send message
  When I click on "Send"
  Then I see confirmation message
