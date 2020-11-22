# Installing dependencies
## Code dependencies
In order to download all dependencies, run the following command: `pip install -r requirements.txt`

## Workstation dependencies
In order to work, you will be to have Chrome installed with the last version.

# Make sure the environment is working well
In order to make sure that the environment is working well, please run the following command: `behave test/feature --color --no-skipped --tags=@test-env`
If you have this output, it means that this is working well: 
```
Feature: Make sure that the login feature is working well # test/feature/Login.feature:1

  @test-env
  Scenario: Test login success                     # test/feature/Login.feature:4
    Given The site to test                         # test/feature/steps/Login.py:9 3.031s
    When I fill the login form with the right user # test/feature/steps/Login.py:16 2.563s
    Then I am logged in                            # test/feature/steps/Login.py:23 0.019s

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 1 skipped
3 steps passed, 0 failed, 4 skipped, 0 undefined
Took 0m5.613s
```

If this is not working, please check your Chrome version (Help > About Google Chrome)
Then, find the corresponding version of `chromedriver-binary` here: https://pypi.org/project/chromedriver-binary/#history
Then, modify the version in the `requirements.txt` file and re-execute the first command.

Here, some version:

| Chrome version | Chromedriver in requirements.txt |
|---|---|
| 87.x | chromedriver-binary==87.0.4280.20.0 |
| 86.x | chromedriver-binary==86.0.4240.22.0 |
| 85.x | chromedriver-binary==85.0.4183.87.0 |

# Run all tests
In order to run all tests, please run the following command: `behave test/feature --color`

# Run a particular test
In order to run a particular test, please run add this annotation before the scenario: `@fast`
Example:
```
@fast
Scenario: Test login failure
    Given The site to test
    When I fill the login form with the wrong user
    Then I am not logger in
    And There is an error displayed
```

After that, you can run the following command: `behave test/feature --color --no-skipped --tags=@fast`