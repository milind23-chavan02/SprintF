# We will automate the Login page of FlipKart Account
  # As the number of rows present in EXAMPLE keyword, Feature file will run those number of times
Feature: login flipkart
    Scenario Outline: login data
      Given we navigate to flipkart homepage
      #Then we click on close button
      When we click on the login button
      Then we type in the "<username>" edit box
      And we type in the "<password>" field
      Then we click on the sign in button
      Then type "<searchTEXT>" in search bar
      And Click on search button
      Then Check on Relevance is clickable
      Then Check on popularity is clickable
      Then Check on Price low-high is clickable
      Then Check on Price high-low is clickable
      Then Check on newest first is clickable
      Then we validate for filter text
      Then we select min price
      And open GO links
      And click assured checkbox
      And Click on rating checkbox 4* above and 3* above
      And click on brand option
      And click the image
     # And click on the color option
     # And click on discount

      Examples:
           | username | | password |     | searchTEXT  |
           | 8867181165 | | Bhavika@123 | |  shirts    |








