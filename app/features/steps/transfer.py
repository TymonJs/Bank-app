from behave import *
import requests
from unittest_assertions import AssertEqual

assert_equal = AssertEqual()
URL = "http://localhost:5000"

@when('Account with pesel "{pesel}" has an "{type}" transfer for "{amount}"')
def receive_transfer(context,pesel,type,amount):
    r = requests.post(URL + f"/api/accounts/{pesel}/transfer",json={"type":type,"amount":int(amount)})
    assert_equal(r.status_code,200)