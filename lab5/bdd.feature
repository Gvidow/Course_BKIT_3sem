Feature: Testing a program that solves a biquadrate equation
    Scenario: solution of the biquadrate equation
        Given I have the numbers 5, 4, 6
        When I make them the coefficients of the biquadrate equation
        Then I expect it to have the following roots: None
