'''
Created on Jan 11, 2017

@author: admin
'''
from lettuce import step, before, world
from nose.tools import *
from app.constants import *
from app.utils import *
import requests
import json
import os
from os import path, access, R_OK

@step(u'When I pass page number \'(.*)\'')
def when_i_pass_page_number_group1(step, pageNo):
    world.response = requests.get(BASE_URL + '/api/users?page=' + pageNo);


@step('I search a restaurant \'(.*)\'')
def when_i_search_a_restaurant(step, parameter):
    world.response = requests.get(GOOGLE_API_URL + parameter + KEY)


@step('I should get a \'(.*)\' response')
def then_i_should_get_a_group1_response_group2(step, expected_status_code):
    assert_equals(world.response.status_code, int(expected_status_code))


@step('save the response in file \'(.*)\'')
def and_save_the_response_in_file(step, fileName):
    cwd = os.getcwd()
    newpath = cwd + "/output/"
    if not(path.exists(newpath)):
        os.makedirs(newpath)
    with open(newpath + fileName, 'w') as f:
        json.dump(world.response.json(), f, indent=4, sort_keys=True, separators=(',', ':'))

    world.output_json_path = newpath + fileName
    print "Google map place API output path :: " + world.output_json_path


@step('the following details are returned:')
def and_the_following_user_details(step):
    expected_output_datatable = step.hashes;
    expected_output = expected_output_datatable[0];
    assert_equals(ordered(expected_output['json']), ordered(world.response.text));


@step('validate search response after removing below fields from file \'(.*)\':')
def validate_search_response(step, expectedOutputFile):
    with open(world.output_json_path, 'r') as actual_output_file:
        actual_output = json.load(actual_output_file);

    cwd = os.getcwd()
    newpath = cwd + "/" + expectedOutputFile

    with open(newpath, 'r') as expected_output_file:
        expected_output = json.load(expected_output_file);

    dataTable = step.hashes;
    for jsonObject in dataTable:
        myList = []
        i = 0;
        for key in jsonObject:
            value = jsonObject[key]
            myList.insert(i, value)
            i = i + 1
        actual_output = removeKey(myList[1], myList[0], actual_output)
        expected_output = removeKey(myList[1], myList[0], expected_output)
        #print str(actual_output) + '\n'

    assert_equals(ordered(expected_output), ordered(actual_output));