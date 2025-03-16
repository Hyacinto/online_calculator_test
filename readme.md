# Online Calculator Test

This project is designed to test the functionality of an online calculator using automated tests. The tests are written in Python and utilize the Playwright library for browser automation, as well as Pytest for running the tests.

## Project Structure

```
conftest.py
data.csv
push_buttons.py
sound.py
test_calculator.py
transform.py

```

- **conftest.py**: Contains setup and teardown functions for the tests, as well as functions to read test data from `data.csv`.
- **data.csv**: Contains test cases for the calculator in a CSV format.
- **push_buttons.py**: Contains functions to simulate button presses on the calculator.
- **sound.py**: Contains functions to record audio.
- **test_calculator.py**: Contains the test cases for the calculator.
- **transform.py**: Contains functions to perform speech recognition on recorded audio.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd online_calculator_test
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Install Playwright and its dependencies:
    ```sh
    playwright install
    ```

## Running the Tests

To run the tests, use the following command:
```sh
pytest test_calculator.py
```

## Test Data

The test data is stored in `data.csv` in the following format:
```
<params>|<expected_result>
```
For example:
```
1,2,+,3,4,＝|46
7,8,－,5,6,＝|22
```

## Functions

### conftest.py

- `read_test_data()`: Reads test data from `data.csv`.
- `pytest_generate_tests(metafunc)`: Generates test cases for Pytest.
- `setup_teardown()`: Sets up and tears down the browser for each test session.

### push_buttons.py

- `find_button_position(value)`: Finds the position of a button on the calculator.
- `push_button(page, Params)`: Simulates button presses on the calculator.

### sound.py

- `recording_audio()`: Records audio from the system.

### transform.py

- `speech_recognition()`: Performs speech recognition on recorded audio.

### test_calculator.py

- `test_calculator(Params, Result, setup_teardown)`: Tests the calculator with the given parameters and expected result.
- `test_random_and_round(setup_teardown)`: Tests the random number generation and rounding functionality.
- `test_random_statistically(setup_teardown)`: Tests the statistical properties of the random number generation.
- `test_font_size_change(setup_teardown)`: Tests the font size change functionality.
- `test_speech_recognition(setup_teardown)`: Tests the calculator's speech functionality, but it is set to skip due to technical issues and testing principles.
- `test_from_clipboard_to_the_screen(setup_teardown)`: Tests the clipboard paste functionality.
- `test_answer(setup_teardown)`: Tests the answer functionality of the calculator.

