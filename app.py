import streamlit as st

st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations")

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0)

with col2:
    num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Choose an operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

# Calculate button
if st.button("Calculate", type="primary"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"✅ Result: {num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"✅ Result: {num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"✅ Result: {num1} × {num2} = {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"✅ Result: {num1} ÷ {num2} = {result}")
        else:
            st.error("❌ Error: Cannot divide by zero!")
