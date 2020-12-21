Feature:
  ---------------
  Introduction
  ---------------
  API Under Test is https://www.metaweather.com/api/
  MetaWeather is an automated weather data aggregator that takes the weather predictions from various forecasters
  and calculates the most likely outcome.
  MetaWeather provides an API that delivers JSON over HTTPS for access to the weather data.
  ----------------------
  LocationSearch.feature
  -----------------------
  This feature intends to verify the Location Search API which helps user in search for the details of specific location,
    Either,
          - by inputting the location name
            for example, /api/location/search/?query=london
    or,
          - by putting latitude and longitude information
            for example, /api/location/search/?lattlong=36.96,-122.02

  The response includes following fields:
    Field	       |  Type	                 |      Description
   title	       | String		             |  Name of the location
   location_type   | string	                 | (City|Region / State / Province|Country|Continent)
   latt_long	   | floats, comma separate |
   woeid	       | integer		         |  Where On Earth ID
   distance	       | integer 	             |  Only returned on a lattlong search (in meters)


  Scenario Outline: When User Searches with a city name, details for that particular city are presented.
    Given User Searches for a location
    When  <location> is passed to the API end point for location search
    Then  Title: <location>, Location Type: <location_type>, Where On Earth: <woeid>, latitude-longitude: <latt_long> are returned for that location.
    Examples:
    | location  | location_type | woeid    | latt_long           |
    | London    |  city         | 44418    | 51.506321,-0.12714  |
    | Berlin    |  city         | 638242   | 52.516071,13.376980 |
    | Mumbai    |  city         | 12586539 | 19.076191,72.875877 |


  Scenario: When User Passed Partial city name, the API returns all the locations with partially matching names.
    Given User Searches for a location
    When Partial text text is passed for the <location>
    Then API returns all the locations with titles partially matching with the partial <location> text


  Scenario Outline: When User searches with Latitude and Longitudes, the API responds with all the near by locations.
    Given User has Latitude and Longitude information
    When User calls the API with Latitude and Longitude details <latt_long>
    Then API returns the following details of all the locations near by <latt_long>: distance, title, location_type, woeid, latt_long
     Examples:
    | latt_long           |
    | 36.96,-122.02       |
    | 19.076191,72.875877 |
