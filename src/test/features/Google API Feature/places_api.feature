@google
Feature: Google Places API Web Service

Scenario Outline: Place Search
When I search a restaurant '/maps/api/place/nearbysearch/json?location=<location>&radius=<radius>&type=<type>&keyword=<keyword>&key='
Then I should get a '200' response
And save the response in file '<case>_search.json'
#And validate search response after removing below fields from file 'expectedData/<case>_search.json':
#|parent_key_path|key|
#|results/photos|photo_reference|
#|results|reference|

Examples:
|case				 |location				 |radius|type	   |keyword|
|restaurant in sydney|-33.8670522,151.1957362|200   |restaurant|cruise |