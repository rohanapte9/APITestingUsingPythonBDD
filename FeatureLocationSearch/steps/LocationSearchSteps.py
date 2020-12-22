import sys, os.path
TestData_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/TestData/')
sys.path.append(TestData_dir)
import Latt_long_directory as td_latt_long
from behave import given, when, then
import requests

# ######## Global Section  ###########

# This dictionary maintains any global variables that are required to exchange data between methods.
# Any method can simply add a key-value pair in this dictionary, which can be accessed by the other methods.
# For example,
# Response to any API call can be stored at global_variables['get_response'], so other methods can access it.
global_variables = {}


# ######## Step Definitions  ###########


@given("User Searches for a location")
def step_impl(context):
    # given block is left blank intentionally. If there is any authentication to be done in future, it can be done here.
    pass


@when("{location} is passed to the API end point for location search")
def step_impl(context, location):
    # Hit the API and store the response in global dictionary which can be accessed from any method.
    global_variables['get_response'] = requests.get(
        "https://www.metaweather.com/api/location/search/?query=" + location)


@then('Title: {location}, Location Type: {location_type}, Where On Earth: {woeid},\
 latitude-longitude: {latt_long} are returned for that location.')
def step_impl(context, location, location_type, woeid, latt_long):
    # Verify the Response code is 200
    assert global_variables['get_response'].status_code == 200

    # Store the response in json format
    res = global_variables['get_response'].json()[0]

    # Verify the response returned against corresponding expected values of the parameters.
    assert res['title'].lower() == location.lower(), "Incorrect Location. Expected: " + location + "  Actual: " + res[
        'title']
    assert res['location_type'].lower() == location_type.lower(), "Incorrect Location Type.\
                Expected: " + location_type + "  Actual: " + res['location_type']
    assert str(res['woeid']) == woeid, "Incorrect Where On Earth Id."
    assert res['latt_long'] == latt_long, "Incorrect Lattitude Longitude."


@when("Partial text text is passed for the {location}")
def step_impl(context,location):
    # Hit the API and store the response in global dictionary which can be accessed from any method.
    global_variables['get_response'] = requests.get(
        "https://www.metaweather.com/api/location/search/?query="+location)


@then("API returns all the locations with titles partially matching with the partial text {location}")
def step_impl(context, location):
    # Verify the Response code is 200
    assert global_variables['get_response'].status_code == 200

    # Verify if all the city names listed in the response contains the word "san"
    for res in global_variables['get_response'].json():
        assert location.lower() in res['title'].lower(), "Incorrect Location. No "+location+" in "+res['title']


@given("User has Latitude and Longitude information")
def step_impl(context):
    pass


@when("User calls the API with Latitude and Longitude details {latt_long}")
def step_impl(context,latt_long):
    global_variables['get_response'] = requests.get(
        "https://www.metaweather.com/api/location/search/?lattlong="+latt_long)


@then("API returns the following details of all the locations near by {latt_long}:\
 distance, title, location_type, woeid, latt_long")
def step_impl(context,latt_long):
    # The Test Data file stores the expected response for specific Lat and Long positions
    # If the Data provided for the test should have corresponding entry in Test Data file.

    if latt_long in td_latt_long.ExpectedResponse.keys():
        # Evaluate the Response directory with the one from Test Data to ensure correct details are returned.
        assert td_latt_long.ExpectedResponse[latt_long] == global_variables['get_response'].json(),\
            "Incorrect Details returned for "+latt_long
    else:
        raise "ExpectedData does not contain expected details for "+latt_long
