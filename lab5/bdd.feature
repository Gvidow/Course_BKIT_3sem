Feature: Testing a program that solves a biquadrate equation
    Scenario: solution of the biquadrate equation
        Given I have the numbers a = 4, b = 4 and c = 5
        When I make them the coefficients of the biquadrate equation
        Then I expect it to have the following roots: "7, 3, 5"
