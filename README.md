# Selenium Login Test Project

This is a simple automated test project using Selenium WebDriver, Pytest, and Allure for reporting.  
It tests login functionality on the saucedemo.com demo website.

## Project Structure

test_login/
├── pages/
│   └── login_page.py  # Page Object for the login page
├── tests/
│   └── test_login.py  # Contains 10 test cases for login
├── conftest.py        # Pytest fixture to initialize WebDriver
├── requirements.txt   # List of required packages
└── README.md          # Project overview and usage

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/your-repo.git

2. Navigate to the project folder:
   cd "test login"

3. Create a virtual environment (optional but recommended):
   python -m venv venv
   venv\Scripts\activate

4. Install required packages:
   pip install -r requirements.txt

## Run Tests

To run all test cases with verbose output:
   pytest -v tests/test_login.py

To generate Allure report:
1. Run tests with Allure:
   pytest --alluredir=allure-results

2. Generate the report:
   allure serve allure-results

## Test Cases Included

1. Valid login
2. Invalid username
3. Invalid password
4. Empty username
5. Empty password
6. Locked out user
7. Problem user
8. Performance glitch user
9. Username with spaces
10. SQL injection attempt

## Notes

- Make sure your Chrome and ChromeDriver versions match.
- Allure requires Java to be installed and JAVA_HOME set properly.

## Author

This project was created for demonstration and training purposes by Nguyen Linh.

## License

This project is for educational and demo purposes.
