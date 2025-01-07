Feature: Transfer
    Scenario: A freshly created user has balance equal to "0"
        Given Account with pesel "12312312312" does not exist in registry
        When I create an account using name: "dave", last name: "grohl", pesel: "12312312312"
        Then Account with pesel "12312312312" has "balance" equal to "0"

    Scenario: User receives an incoming transfer
        Given Account with pesel "12312312312" exists in registry
        And Account with pesel "12312312312" has "balance" equal to "0"
        When Account with pesel "12312312312" has an "incoming" transfer for "200"
        Then Account with pesel "12312312312" has "balance" equal to "200"

    Scenario: User sends an outgoing transfer
        Given Account with pesel "12312312312" exists in registry
        And Account with pesel "12312312312" has "balance" equal to "200"
        When Account with pesel "12312312312" has an "outgoing" transfer for "100"
        Then Account with pesel "12312312312" has "balance" equal to "100"

    Scenario: User sends an express transfer
        Given Account with pesel "12312312312" exists in registry
        And Account with pesel "12312312312" has "balance" equal to "100"
        When Account with pesel "12312312312" has an "express" transfer for "50"
        Then Account with pesel "12312312312" has "balance" equal to "49"

    Scenario: User gets removed, so he doesn't interrupt further tests
        Given Account with pesel "12312312312" exists in registry
        When I delete account with pesel: "12312312312"
        And Account with pesel "12312312312" does not exist in registry

    # Scenario: User can't send an outgoing transfer an unexisting user
    #     Given Account with pesel "12312312312" exists in registry
    #     And Account with pesel: "12312312312" has "balance" equal to "100"
    #     And Account with pesel "12345678912" exists in registry
    #     When I delete account with pesel: "89092909876"
    #     And Account with pesel "12312312312" sends an outgoing transfer to account with pesel "89092909876"
    #     Then Account with pesel: "12312312312" has "balance" equal to "100"

    # Scenario: User is able to get an incoming transfer
    #     Given A new or already existing account with name: "dave", last name: "grohl", pesel: "12312312312" has balance equal "0"
    #     When 
    #     And Account with pesel "12312312312" is given an incoming transfer
    #     Then Account with pesel "12312312312" has 
        
