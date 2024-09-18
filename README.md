<!-- @format -->

# Simple Calculator with Streamlit

This is a simple calculator built using Streamlit. The calculator allows the user to perform basic mathematical operations such as addition, subtraction, multiplication, and division.

## Project Description

This project is a web-based calculator that takes two numbers and performs the following operations:

- Addition
- Subtraction
- Multiplication
- Division (with validation to prevent division by zero)

### Features:

1. Input two numbers.
2. Select the type of mathematical operation.
3. Get the result instantly by clicking the "Calculate" button.

### Note:

When selecting division, if the second number is zero, the operation will be invalid.

## How It Works

The calculator uses Streamlit to provide a web-based interface. The operations are carried out by specific functions in the code such as `plus`, `minus`, `multiplication`, and `division`, with checks to ensure safe operations (like preventing division by zero).

## Installation

1. Clone the repository:
   git clone https://github.com/AliFathi1325/Simple_calculator_Streamlit.git

2. Navigate to the project directory:
   cd Simple_calculator_Streamlit

3. Install the required Python packages:
   pip install -r requirements.txt

4. Run the application:
   streamlit run main.py

The app will open in your web browser automatically.
