import streamlit as st

# Define the calculator functions
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division by zero is undefined"
    return a / b

# Title of the Streamlit app
st.title('Simple Calculator')

#
st.write("""
    This is a simple calculator. Follow the steps below:

    1. Enter.
    2. Select the type of mathematical operation you want (addition, subtraction, multiplication or division).
    3. Click the "calculate" button to give the result.

    Note: When selecting division, if the second number is zero, the operation will be invalid.
""")

# Number inputs for user
num1 = st.number_input('Enter the first number', value=1)
num2 = st.number_input('Enter the second number', value=1)

# Operation selection
operation_list = ['Choose', 'Plus', 'Minus', 'Multiplication', 'Division']
operation = st.selectbox('Select the desired operation', operation_list)

# Button to trigger the calculation
if st.button('Calculate'):
    st.markdown("<hr>", unsafe_allow_html=True)

    # Perform the operation based on the user's choice
    if operation == 'Plus':
        result = plus(num1, num2)
        st.success(f'Calculation result: {result}')

    elif operation == 'Minus':
        result = minus(num1, num2)
        st.success(f'Calculation result: {result}')

    elif operation == 'Multiplication':
        result = multiplication(num1, num2)
        st.success(f'Calculation result: {result}')

    elif operation == 'Division':
        result = division(num1, num2)
        if result == "Division by zero is undefined":
            st.error(result)
        else:
            st.success(f'Calculation result: {result}')

    elif operation == 'Choose':
        st.warning('Please select a valid operation')
