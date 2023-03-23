# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fc25kapp.herokuapp.com%2F) | ![screenshot](documentation/testing/html_validation_home.png) | None |
| Run list | None, authentication needed | ![screenshot](documentation/testing/html_validation_run_list.png) | None |
| Run Create | None, authentication needed | ![screenshot](documentation/testing/html_validation_run_create.png) | None |
| Run Edit | None, authentication needed | ![screenshot](documentation/testing/html_validation_run_edit.png) | None |
| Run Delete | None, authentication needed | ![screenshot](documentation/testing/html_validation_run_delete.png) | None |
| Profile | None, authentication needed | ![screenshot](documentation/testing/html_validation_profile.png) | None |
| Profile Create | None, authentication needed | ![screenshot](documentation/testing/html_validation_profile_create.png) | None |
| Profile Update | None, authentication needed | ![screenshot](documentation/testing/html_validation_profile_update.png) | None |
| Profile Delete | None, authentication needed | ![screenshot](documentation/testing/html_validation_profile_delete.png) | None |
| Sign Up | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fc25kapp.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/testing/html_validation_sign_up.png) | None |
| Sign In | [W3C](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fc25kapp.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/testing/html_validation_sign_in.png) | None |
| Sign Out | None, authentication needed | ![screenshot](documentation/testing/html_validation_sign_out.png) | None |
| Leader Tools | None, authentication needed | ![screenshot](documentation/testing/html_validation_leader_tools.png) | None |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fc25kapp.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css) | ![screenshot](documentation/testing/css_validation.png) | No errors in custom CSS, warnings shown relate to bootstrap classes |

### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| settings.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/c25k/main/c25k/settings.py) | ![screenshot](documentation/testing/py_validation_settings.png) | None |
| forms.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/c25k/main/register/forms.py) | ![screenshot](documentation/testing/py_validation_forms.png) | None |
| models.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/c25k/main/register/models.py) | ![screenshot](documentation/testing/py_validation_models.png) | None |
| urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/c25k/main/register/urls.py) | ![screenshot](documentation/testing/py_validation_urls.png) | None |
| views.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/c25k/main/register/views.py) | ![screenshot](documentation/testing/py_validation_views.png) | None |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/browser_compatibility_chrome.png) | Works as expected |
| Firefox Developer | ![screenshot](documentation/testing/browser_compatibility_mozilla.png) | Works as expected |
| Edge | ![screenshot](documentation/testing/browser_compatibility_edge.png) | Works as expected |
| Safari | ![screenshot](documentation/testing/browser_compatibility_safari.PNG) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

### Mobile (DevTools)

| View | Screenshot | Notes |
| --- | --- | --- |
| Home | ![screenshot](documentation/testing/responsive_mobile_devtools_home.png) | Works as expected |
| Run List | ![screenshot](documentation/testing/responsive_mobile_devtools_runlist.png) | Works as expected |
| Add/Edit Form | ![screenshot](documentation/testing/responsive_mobile_devtools_add.png) | Works as expected |
| Delete | ![screenshot](documentation/testing/responsive_mobile_devtools_delete.png) | Works as expected |
| Profile | ![screenshot](documentation/testing/responsive_mobile_devtools_profile.png) | Works as expected |
| Leader Tools | ![screenshot](documentation/testing/responsive_mobile_devtools_leadertools.png) | Works as expected |
| Sign Up | ![screenshot](documentation/testing/responsive_mobile_devtools_signup.png) | Works as expected |
| Sign In | ![screenshot](documentation/testing/responsive_mobile_devtools_signin.png) | Works as expected |
| Sign Out | ![screenshot](documentation/testing/responsive_mobile_devtools_signout.png) | Works as expected |

### Tablet (DevTools)

| View | Screenshot | Notes |
| --- | --- | --- |
| Home | ![screenshot](documentation/testing/responsive_tablet_devtools_home.png) | Works as expected |
| Run List | ![screenshot](documentation/testing/responsive_tablet_devtools_runlist.png) | Works as expected |
| Add/Edit Form | ![screenshot](documentation/testing/responsive_tablet_devtools_add.png) | Works as expected |
| Delete | ![screenshot](documentation/testing/responsive_tablet_devtools_delete.png) | Works as expected |
| Profile | ![screenshot](documentation/testing/responsive_tablet_devtools_profile.png) | Works as expected |
| Leader Tools | ![screenshot](documentation/testing/responsive_tablet_devtools_leadertools.png) | Works as expected |
| Sign Up | ![screenshot](documentation/testing/responsive_tablet_devtools_signup.png) | Works as expected |
| Sign In | ![screenshot](documentation/testing/responsive_tablet_devtools_signin.png) | Works as expected |
| Sign Out | ![screenshot](documentation/testing/responsive_tablet_devtools_signout.png) | Works as expected |

### Desktop

| View | Screenshot | Notes |
| --- | --- | --- |
| Home | ![screenshot](documentation/testing/responsive_desktop_home.png) | Works as expected |
| Run List | ![screenshot](documentation/testing/responsive_desktop_runlist.png) | Works as expected |
| Add/Edit Form | ![screenshot](documentation/testing/responsive_desktop_add.png) | Works as expected |
| Delete | ![screenshot](documentation/testing/responsive_desktop_delete.png) | Works as expected |
| Profile | ![screenshot](documentation/testing/responsive_desktop_profile.png) | Works as expected |
| Leader Tools | ![screenshot](documentation/testing/responsive_desktop_leadertools.png) | Works as expected |
| Sign Up | ![screenshot](documentation/testing/responsive_desktop_signup.png) | Works as expected |
| Sign In | ![screenshot](documentation/testing/responsive_desktop_signin.png) | Works as expected |
| Sign Out | ![screenshot](documentation/testing/responsive_desktop_signout.png) | Works as expected |

### Other views tested

| View | Screenshot | Notes |
| --- | --- | --- |
| iPhone | ![screenshot](documentation/testing/browser_compatibility_safari.PNG) | Works as expected |
| Samsung Galaxy (Devtools) | ![screenshot](documentation/testing/responsiveness_galaxy_s10.png) | Works as expected |
| iPad mini (Devtools) | ![screenshot](documentation/testing/responsiveness_ipad_mini.png) | Works as expected |
| iPad Pro (Devtools) | ![screenshot](documentation/testing/responsiveness_ipad_pro.png) | Works as expected |
| Kindle Fire (Devtools) | ![screenshot](documentation/testing/responsiveness_kindle_fire.png) | Works as expected |
| HiDPI Screen (Devtools) | ![screenshot](documentation/testing/responsiveness_laptop_HiDPI.png) | Works as expected |
| Nokia 8110 (Devtools) | ![screenshot](documentation/testing/responsiveness_nokia_8110.png) | Interesting that it scales that far! |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](documentation/testing/lighthouse_home_mobile.png) | Warning for bootstrap JS link |
| Home | Desktop | ![screenshot](documentation/testing/lighthouse_home_desktop.png) | Warning for bootstrap CDN links |
| Run List | Mobile | ![screenshot](documentation/testing/lighthouse_runlist_mobile.png) | Warning for out of order headings and poor contrast on green button |
| Run List | Desktop | ![screenshot](documentation/testing/lighthouse_runlist_desktop.png) | Warning for non sequential headings, poor contrast on green button and bootstrap JS link |
| Add / Edit Form | Mobile | ![screenshot](documentation/testing/lighthouse_add_mobile.png) | Warning for bootstrap CDN links,  |
| Add / Edit Form | Desktop | ![screenshot](documentation/testing/lighthouse_add_desktop.png) | Warning for JS link |
| Delete | Mobile | ![screenshot](documentation/testing/lighthouse_delete_mobile.png) | Warning for bootstrap JS link |
| Delete | Desktop | ![screenshot](documentation/testing/lighthouse_delete_desktop.png) | Warning for bootstrap JS link |
| Profile | Mobile | ![screenshot](documentation/testing/lighthouse_profile_mobile.png) | Warning for bootstrap JS link |
| Profile | Desktop | ![screenshot](documentation/testing/lighthouse_profile_desktop.png) | Warning for bootstrap JS link |
| Leader Tools | Mobile | ![screenshot](documentation/testing/lighthouse_leadertools_mobile.png) | Warning for bootstrap JS link |
| Leader Tools | Desktop | ![screenshot](documentation/testing/lighthouse_leadertools_desktop.png) | Warning for bootstrap JS link |
| Sign Up | Mobile | ![screenshot](documentation/testing/lighthouse_signup_mobile.png) | Warning for bootstrap JS link |
| Sign Up | Desktop | ![screenshot](documentation/testing/lighthouse_signup_desktop.png) | Warning for bootstrap JS link |
| Sign In | Mobile | ![screenshot](documentation/testing/lighthouse_signin_mobile.png) | Warning for bootstrap JS link |
| Sign In | Desktop | ![screenshot](documentation/testing/lighthouse_signin_desktop.png) | repeat for any other tested pages/sizes |
| Sign Out | Mobile | ![screenshot](documentation/testing/lighthouse_signout_mobile.png) | Warning for bootstrap JS link |
| Sign Out | Desktop | ![screenshot](documentation/testing/lighthouse_signout_desktop.png) | Warning for bootstrap JS link |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
|1 | Click on Logo | Redirection to Home page | Pass | |
|2 | Click on Home link in navbar | Redirection to Home page | Pass | |
| Run List | | | | |
|3 | Logged out user manually loads the page | Message displayed requiring log in | Pass | ![screenshot](documentation/testing/defensive3.png) |
|4 | Click on Run List link in nav bar | Base page loads for logged in users | Pass | |
|5 | User with leader credentials clicks on link in nav bar | Extra register details only displayed to users with leader group credentials | Pass | |
|6 | User with leader credentials follows profile link from register | Runner profile displayed | Pass | |
|7 | User without leader credentials manually loads profile page | Message displayed requiring leader access | Pass | ![screenshot](documentation/testing/defensive7.png) |
|8 | Logged out user manually loads profile page | Error as no request will be returned from the database | Pass | ![screenshot](documentation/testing/defensive8.png) |
|9 | User with leader credentials clicks the add run button | Add run form displayed | Pass | |
|10 | User without leader credentials manually loads add run page | Message displayed requiring leader access | Pass | ![screenshot](documentation/testing/defensive10.png) |
|11 | Logged out user manually loads the add run page | Message displayed requiring log in | Pass | ![screenshot](documentation/testing/defensive11.png) |
|12 | User with leader credentials clicks the edit run button | Edit run form displayed | Pass | |
|13 | User without leader credentials manually loads edit run page | Message displayed requiring leader access | Pass | ![screenshot](documentation/testing/defensive13.png) |
|14 | Logged out user manually loads the edit run page | Message displayed requiring log in | Pass | ![screenshot](documentation/testing/defensive14.png) |
|15 | User with leader credentials clicks the delete run button | Run deletion confirmation warning displayed | Pass | |
|16 | User without leader credentials manually loads delete run page | Message displayed requiring leader access | Pass | ![screenshot](documentation/testing/defensive16.png) |
|17 | Logged out user manually loads the delete run page | Message displayed requiring log in | Pass | ![screenshot](documentation/testing/defensive17.png) |
| Profile Page | | | | |
|18 | Logged out user manually loads a profile page | Message displayed requiring log in | Pass | ![screenshot](documentation/testing/defensive18.png) |
|19 | Click on link in navbar | User specific profile loads | Pass | |
|20 | Logged in user clicks create profile button | Create profile form loads | Pass | |
|21 | Logged out user clicks create profile button | Message displayed requiring log in | Pass | ![screenshot](documentation/testing/defensive21.png) |
|22 | Logged in user clicks update profile button | Update profile form loads | Pass | |
|23 | Logged in user manually changes URL of update profile form | Error due to user checking in views file | Pass | ![screenshot](documentation/testing/defensive23.png) |
|24 | Logged out user manually accesses profile update form | Message displayed to log in | Pass | ![screenshot](documentation/testing/defensive24.png)  |
|25 | Logged in user clicks delete profile button | Delete profile warning message is displayed | Pass | |
|26 | Logged in user manually changes URL of delete profile form | Delete profile warning message is displayed | Pass | ![screenshot](documentation/testing/defensive26.png) |
|27 | Logged out user manually loads delete profile link | Message displayed to log in | Pass | ![screenshot](documentation/testing/defensive27.png) |
| Leader Tools | | | | |
|28 | User with leader credentials clicks on link | Leader tools page displayed | Pass | |
|29 | User manually loads link | Message displayed requiring leader access | Pass | ![screenshot](documentation/testing/defensive29.png) |
|30 | Logged out user manually loads link  | Message displayed to sign in | Pass | ![screenshot](documentation/testing/defensive30.png) |
| Sign In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Sign Up | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |

## User Story Testing

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature09.png) |
| repeat for all remaining user stories | x |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Bugs

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

For JavaScript and Python applications, it's best to screenshot the errors to include them as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/ccp84/c25k/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/ccp84/c25k/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/ccp84/c25k/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/ccp84/c25k/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/ccp84/c25k/issues/3) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/ccp84/c25k/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/ccp84/c25k/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/ccp84/c25k/issues/5) | Open |

## Unfixed Bugs

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

⚠️⚠️⚠️⚠️⚠️ START OF NOTES (to be deleted) ⚠️⚠️⚠️⚠️⚠️

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

There are no remaining bugs that I am aware of.
