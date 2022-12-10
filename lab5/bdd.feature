Feature: Testing a program that solves a biquadrate equation
    Scenario: solution of the biquadrate equation 1
        Given I have the numbers 5, 4, 6
        When I make them the coefficients of the biquadrate equation
        Then I expect it to have the following roots: None

    Scenario: solution of the biquadrate equation 2
        Given I have the numbers 5, 55, 6
        When I make them the coefficients of the biquadrate equation
        Then I expect it to have the following roots: None

    Scenario: solution of the biquadrate equation 3
        Given I have the numbers 5, 455, 6
        When I make them the coefficients of the biquadrate equation
        Then I expect it to have the following roots: None
