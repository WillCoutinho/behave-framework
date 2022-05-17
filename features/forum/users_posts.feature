
Feature: Forum Posts
  Allow user to create, get, delete and update posts, simulating a Forum website


  Scenario: Create a Post
    Given I have a new post to create
    When I send this post to "posts"
    Then the post data should be returned as response

  Scenario: Get a comment using its own ID
    Given I have an id from a post already created
    And I want to check all comment data from this post
    When I send the comment id to "comments/id"
    Then the comment data should be returned as response

  Scenario: Get comment from a Post ID
    Given I have an id from a post already created
    When I send the post id to "comments?postId"
    Then the comment list should be returned as response