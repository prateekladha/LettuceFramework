@user
Feature: Handle storing, retrieving and deleting customer details

Scenario Outline: Retrieve a customers details
When I pass page number '2'
Then I should get a '200' response
And the following details are returned:
| json |
| {"page":"2","per_page":3,"total":12,"total_pages":4,"data":[{"id":4,"first_name":"eve","last_name":"holt","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/marcoramires/128.jpg"},{"id":5,"first_name":"gob","last_name":"bluth","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/stephenmoon/128.jpg"},{"id":6,"first_name":"tracey","last_name":"bluth","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/bigmancho/128.jpg"}]} |


Examples:
|case				 |location				 |radius|type	   |keyword|
|restaurant in sydney|-33.8670522,151.1957362|200   |restaurant|cruise |