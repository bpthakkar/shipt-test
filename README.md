# shipt-test

### Assignment 1: Test Case Authoring 
- Refer excel file for test cases
- Docs files for bug reports 

### Assignment 2: SQL Queries 
This is tested on MySQL so if you are testing on different database it may not work (e.g. doesn't work for sqlite)
- Refer query_test.sql file with all the queries

### Assignment 3: API Automation  

##### Questions 

1. If you chose to use a tool or language other than the recommended, briefly explain why.
> Not Applicable 
2. How do you debug a failed test in your test framework?
> I would perform following steps to debug the failure (not in perticular order)
> - Check the locator is not changed
> - Browser console to confirm any java script exception 
> - Application log to check the exception
> - Database query to confirm the data 
> - Refer source code 
3. What do you believe are the most common causes for instability in UI automation?
> locator changes or requirement changes and timeout errors very common issues causes false positives 
> 
4. How do you make your tests consistent and easy to debug?
> User reusable library functions, Parameterization, follow the source directroy structure, Add print/debug log statement 



Follow the instructions to the test

1. Navigate to profile folder shipt-test
2. Activate virtual environment using following command 
```
Bhargavs-MacBook-Pro:shipt-test bhargav$ source venv/bin/activate
```
3. To run the test from command line

```
(venv) Bhargavs-MacBook-Pro:shipt-test bhargav$ pytest
========================================================================================== test session starts ===========================================================================================
platform darwin -- Python 3.7.3, pytest-4.4.1, py-1.8.0, pluggy-0.9.0
rootdir: /Users/bhargav/github_project/tempdir/shipt-test
collected 3 items

test/test_login_api.py ...                                                                                                                                                                         [100%]

======================================================================================== 3 passed in 1.30 seconds ========================================================================================
```

##### Notes

_if you get error about missing package you can run following command to install and require packages_

```
(venv) Bhargavs-MacBook-Pro:shipt-test bhargav$ pip install -r requirements.txt
```

_I used pycharm to create this project. You have might have to update interpreter depending your environment_
