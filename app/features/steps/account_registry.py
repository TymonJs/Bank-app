from behave import *
import requests
from unittest_assertions import AssertEqual
from string import digits
assert_equal = AssertEqual()
URL = "http://localhost:5000"

@when('I create an account using name: "{name}", last name: "{last_name}", pesel: "{pesel}"')
def create_account(context, name, last_name, pesel):
    json_body = { "name": f"{name}",
    "surname": f"{last_name}",
    "pesel": pesel
    }
    create_resp = requests.post(URL + "/api/accounts", json = json_body)
    assert_equal(create_resp.status_code, 201)

@step('Number of accounts in registry equals: "{count}"')
def is_account_count_equal_to(context, count):
    create_resp = requests.get(URL + "/api/accounts/count")
    assert_equal(create_resp.status_code,200)
    assert_equal(int(create_resp.json()["Account count"]),int(count))

@step('Account with pesel "{pesel}" exists in registry')
def check_account_with_pesel_exists(context, pesel):
    create_resp = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(create_resp.status_code,200)
    assert_equal(create_resp.json()["pesel"],pesel)

@step('Account with pesel "{pesel}" does not exist in registry')
def check_account_with_pesel_does_not_exist(context, pesel):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(response.status_code, 404)

@when('I delete account with pesel: "{pesel}"')
def delete_account(context, pesel):
    r = requests.delete(URL + f"/api/accounts/{pesel}")
    assert_equal(r.status_code,200)
    
@when('I update "{field}" of account with pesel: "{pesel}" to "{value}"')
def update_field(context, field, pesel, value):
    if field not in ["name", "surname"]:
        raise ValueError(f"Invalid field: {field}. Must be 'name' or 'surname'.")
    json_body = { f"{field}": f"{value}" }
    response = requests.patch(URL + f"/api/accounts/{pesel}", json = json_body)
    assert_equal(response.status_code, 200)

@step('Account with pesel "{pesel}" has "{field}" equal to "{value}"')
def field_equals_to(context, pesel, field, value):
    r = requests.get(URL + f"/api/accounts/{pesel}")
    to_check = r.json()[field]
    assert_equal(str(to_check),str(value))
    assert_equal(r.status_code,200)
