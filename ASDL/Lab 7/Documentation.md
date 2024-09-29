# Documentation for Lab 7: Web Application Development

This documentation covers a simple web application that consists of a round trip airline ticket booking form and a basic calculator. The application is built using HTML, CSS, and JavaScript. Below is a detailed explanation of the code, including functionality and structure.

## Overview

The application consists of two main sections:
1. **Round Trip Airline Ticket Booking Form**
2. **Simple Calculator**

Each section has its own form with specific input fields and buttons, enhanced with validation and user interactions via JavaScript.

### 1. HTML Structure

The HTML document starts with a standard `<!DOCTYPE html>` declaration followed by the root `<html>` element. Inside the `<head>` section, we define the document's metadata and include styles and scripts.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lab 7: Web Application Development</title>
```

### 2. CSS Styles

We use CSS to style the body, headings, forms, inputs, buttons, and the calculator layout. This section defines the visual appearance of the application.

```css
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
        background-color: #f4f4f4;
    }
    h1 {
        color: #333;
    }
    form {
        background: #fff;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    input,
    textarea {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
    button {
        padding: 10px 15px;
        margin: 5px;
        border: none;
        border-radius: 4px;
        background-color: #007BFF;
        color: white;
        cursor: pointer;
    }
    button:hover {
        background-color: #0056b3;
    }
    .calculator {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
    }
    .calculator input {
        grid-column: span 4;
    }
</style>
```

### 3. JavaScript Functions

This section contains the JavaScript functions for form validation, user input handling for the calculator, and other interactions. Each function is explained below:

#### 3.1 Validation Functions

1. **`validateFirstName`**: Checks if the first name field is non-empty.
    ```javascript
    function validateFirstName() {
        const firstName = document.myForm.firstName.value;
        return firstName.trim().length > 0;
    }
    ```

2. **`validateLastName`**: Checks if the last name field is non-empty.
    ```javascript
    function validateLastName() {
        const lastName = document.myForm.lastName.value;
        return lastName.trim().length > 0;
    }
    ```

3. **`validateEmail`**: Validates the email format based on a specific regex pattern.
    ```javascript
    function validateEmail() {
        const email = document.myForm.email.value;
        const emailFormat = /^[a-zA-Z]{1,}[0-9a-zA-Z._%+-]*@[a-zA-Z]{1,}(\.[a-zA-Z]{1,}){1,2}$/;
        return emailFormat.test(email);
    }
    ```

4. **`validateCities`**: Ensures that both origin and destination fields are filled and that they are not the same.
    ```javascript
    function validateCities() {
        const origin = document.myForm.origin.value;
        const destination = document.myForm.destination.value;
        return origin.trim().length > 0 && destination.trim().length > 0 && origin !== destination;
    }
    ```

5. **`validateDate`**: Validates that the date format is correct and that the date is in the future.
    ```javascript
    function validateDate(dateString) {
        const dateFormat = /^\d{4}[\-](0?[1-9]|1[012])[\-](0?[1-9]|[12][0-9]|3[01])$/;
        const flag = dateString.match(dateFormat);
        if (!flag) return false;

        const date = new Date(dateString);
        const currentDate = new Date();
        return date.getTime() > currentDate.getTime();
    }
    ```

6. **`validateDates`**: Checks both departure and return dates for validity and ensures the return date is after the departure date.
    ```javascript
    function validateDates() {
        const departureDate = document.myForm.departureDate.value;
        const returnDate = document.myForm.returnDate.value;
        return validateDate(departureDate) && validateDate(returnDate) && (new Date(returnDate) > new Date(departureDate));
    }
    ```

7. **`onSubmitFn`**: The main function that triggers on form submission to run all validations. If any validation fails, it shows an alert.
    ```javascript
    function onSubmitFn() {
        if (!validateFirstName()) {
            alert("First Name is invalid.");
            return false;
        }
        if (!validateLastName()) {
            alert("Last Name is invalid.");
            return false;
        }
        if (!validateEmail()) {
            alert("Email is invalid.");
            return false;
        }
        if (!validateCities()) {
            alert("Origin and Destination cities are invalid or the same.");
            return false;
        }
        if (!validateDates()) {
            alert("Dates are invalid or Departure is not before Return.");
            return false;
        }
        alert("Application received!");
        return true; // Proceed to submission
    }
    ```

8. **`onResetFn`**: Resets the form fields when the reset button is pressed.
    ```javascript
    function onResetFn() {
        document.myForm.reset();
    }
    ```

#### 3.2 Calculator Functions

1. **`appendNumber`**: Adds a number or operator to the current input string, preventing multiple decimal points.
    ```javascript
    function appendNumber(num) {
        if (currentInput.includes('.') && num === '.') return; // Prevent multiple dots
        currentInput += num;
        document.calc.input.value = currentInput;
    }
    ```

2. **`clearInput`**: Clears the current input.
    ```javascript
    function clearInput() {
        currentInput = '';
        document.calc.input.value = '';
    }
    ```

3. **`toggleSign`**: Changes the sign of the current number.
    ```javascript
    function toggleSign() {
        if (currentInput) {
            currentInput = String(-eval(currentInput));
            document.calc.input.value = currentInput;
        }
    }
    ```

4. **`calculate`**: Evaluates the expression in the input field and displays the result.
    ```javascript
    function calculate() {
        if (currentInput) {
            currentInput = String(eval(currentInput));
            document.calc.input.value = currentInput;
        }
    }
    ```

### 4. Form Structure

#### 4.1 Airline Ticket Booking Form

The airline booking form contains various input fields and buttons.

```html
<h1>Round Trip Airline Ticket Booking</h1>
<form name="myForm" onsubmit="return onSubmitFn()" onreset="onResetFn()">
    <input type="text" name="firstName" placeholder="First Name" required>
    <input type="text" name="lastName" placeholder="Last Name" required>
    <input type="email" name="email" placeholder="Email Address" required>
    <input type="text" name="origin" placeholder="Origin City" required>
    <input type="text" name="destination" placeholder="Destination City" required>
    Departure Date: <input type="date" name="departureDate" required>
    Return Date: <input type="date" name="returnDate" required>
    <textarea name="comments" placeholder="General comments"></textarea>
    <button type="submit">Submit</button>
    <button type="reset">Reset</button>
</form>
```

#### 4.2 Simple Calculator

The calculator form allows users to perform basic arithmetic operations.

```html
<h1>Simple Calculator</h1>
<form name="calc">
    <input type="text" name="input" readonly>
    <div class="calculator">
        <button type="button" onclick="appendNumber('7')">7</button>
        <button type="button" onclick="appendNumber('8')">8</button>
        <button type="button" onclick="appendNumber('9')">9</button>
        <button type="button" onclick="appendNumber('/')">/</button>
        <button type="button" onclick="appendNumber('4')">4</button>
        <button type="button" onclick="appendNumber('5')">5</button>
        <button type="button" onclick="appendNumber('6')">6</button>
        <button type="button" onclick="appendNumber('*')">*</button>
        <button type="button" onclick="appendNumber('1')">1</button>
        <button type="button"

 onclick="appendNumber('2')">2</button>
        <button type="button" onclick="appendNumber('3')">3</button>
        <button type="button" onclick="appendNumber('-')">-</button>
        <button type="button" onclick="appendNumber('0')">0</button>
        <button type="button" onclick="appendNumber('.')">.</button>
        <button type="button" onclick="toggleSign()">+/-</button>
        <button type="button" onclick="appendNumber('+')">+</button>
        <button type="button" onclick="calculate()">=</button>
        <button type="button" onclick="clearInput()">C</button>
    </div>
</form>
```

### Complete Code Snippet

Here’s the complete code with all the explanations incorporated:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lab 7: Web Application Development</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
        }

        h1 {
            color: #333;
        }

        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        input,
        textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            padding: 10px 15px;
            margin: 5px;
            border: none;
            border-radius: 4px;
            background-color: #007BFF;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        .calculator {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
        }

        .calculator input {
            grid-column: span 4;
        }
    </style>
    <script>
        function validateFirstName() {
            const firstName = document.myForm.firstName.value;
            return firstName.trim().length > 0;
        }

        function validateLastName() {
            const lastName = document.myForm.lastName.value;
            return lastName.trim().length > 0;
        }

        function validateEmail() {
            const email = document.myForm.email.value;
            const emailFormat = /^[a-zA-Z]{1,}[0-9a-zA-Z._%+-]*@[a-zA-Z]{1,}(\.[a-zA-Z]{1,}){1,2}$/;
            return emailFormat.test(email);
        }

        function validateCities() {
            const origin = document.myForm.origin.value;
            const destination = document.myForm.destination.value;
            return origin.trim().length > 0 && destination.trim().length > 0 && origin !== destination;
        }

        function validateDate(dateString) {
            const dateFormat = /^\d{4}[\-](0?[1-9]|1[012])[\-](0?[1-9]|[12][0-9]|3[01])$/;
            const flag = dateString.match(dateFormat);
            if (!flag) return false;

            const date = new Date(dateString);
            const currentDate = new Date();
            return date.getTime() > currentDate.getTime();
        }

        function validateDates() {
            const departureDate = document.myForm.departureDate.value;
            const returnDate = document.myForm.returnDate.value;
            return validateDate(departureDate) && validateDate(returnDate) && (new Date(returnDate) > new Date(departureDate));
        }

        function onSubmitFn() {
            if (!validateFirstName()) {
                alert("First Name is invalid.");
                return false;
            }
            if (!validateLastName()) {
                alert("Last Name is invalid.");
                return false;
            }
            if (!validateEmail()) {
                alert("Email is invalid.");
                return false;
            }
            if (!validateCities()) {
                alert("Origin and Destination cities are invalid or the same.");
                return false;
            }
            if (!validateDates()) {
                alert("Dates are invalid or Departure is not before Return.");
                return false;
            }
            alert("Application received!");
            return true; // Proceed to submission
        }

        function onResetFn() {
            document.myForm.reset();
        }

        // Calculator functions
        let currentInput = '';

        function appendNumber(num) {
            if (currentInput.includes('.') && num === '.') return; // Prevent multiple dots
            currentInput += num;
            document.calc.input.value = currentInput;
        }

        function clearInput() {
            currentInput = '';
            document.calc.input.value = '';
        }

        function toggleSign() {
            if (currentInput) {
                currentInput = String(-eval(currentInput));
                document.calc.input.value = currentInput;
            }
        }

        function calculate() {
            if (currentInput) {
                currentInput = String(eval(currentInput));
                document.calc.input.value = currentInput;
            }
        }
    </script>
</head>
<body>
    <h1>Round Trip Airline Ticket Booking</h1>
    <form name="myForm" onsubmit="return onSubmitFn()" onreset="onResetFn()">
        <input type="text" name="firstName" placeholder="First Name" required>
        <input type="text" name="lastName" placeholder="Last Name" required>
        <input type="email" name="email" placeholder="Email Address" required>
        <input type="text" name="origin" placeholder="Origin City" required>
        <input type="text" name="destination" placeholder="Destination City" required>
        Departure Date: <input type="date" name="departureDate" required>
        Return Date: <input type="date" name="returnDate" required>
        <textarea name="comments" placeholder="General comments"></textarea>
        <button type="submit">Submit</button>
        <button type="reset">Reset</button>
    </form>

    <h1>Simple Calculator</h1>
    <form name="calc">
        <input type="text" name="input" readonly>
        <div class="calculator">
            <button type="button" onclick="appendNumber('7')">7</button>
            <button type="button" onclick="appendNumber('8')">8</button>
            <button type="button" onclick="appendNumber('9')">9</button>
            <button type="button" onclick="appendNumber('/')">/</button>
            <button type="button" onclick="appendNumber('4')">4</button>
            <button type="button" onclick="appendNumber('5')">5</button>
            <button type="button" onclick="appendNumber('6')">6</button>
            <button type="button" onclick="appendNumber('*')">*</button>
            <button type="button" onclick="appendNumber('1')">1</button>
            <button type="button" onclick="appendNumber('2')">2</button>
            <button type="button" onclick="appendNumber('3')">3</button>
            <button type="button" onclick="appendNumber('-')">-</button>
            <button type="button" onclick="appendNumber('0')">0</button>
            <button type="button" onclick="appendNumber('.')">.</button>
            <button type="button" onclick="toggleSign()">+/-</button>
            <button type="button" onclick="appendNumber('+')">+</button>
            <button type="button" onclick="calculate()">=</button>
            <button type="button" onclick="clearInput()">C</button>
        </div>
    </form>
</body>
</html>
```

### Conclusion

This document provides a detailed overview of the HTML, CSS, and JavaScript code used in the web application. The code includes a functional form for booking airline tickets with necessary validations and a simple calculator capable of performing basic arithmetic operations.