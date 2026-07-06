import streamlit as st
import sys
import os

# Make sure the Bank class is loaded from the same directory
sys.path.insert(0, os.path.dirname(__file__))
from main2 import Bank

st.set_page_config(page_title="Bank Management System", page_icon="🏦", layout="centered")

st.title("🏦 Bank Management System")
st.markdown("---")

bank = Bank()

# Sidebar menu
menu = st.sidebar.radio(
    "Choose an option",
    ["Create Account", "Deposit Money", "Withdraw Money", "View Account", "Update Account", "Delete Account"]
)

st.sidebar.markdown("---")
st.sidebar.info("This is a simple banking app built with Streamlit!")

# ─── 1. Create Account ───────────────────────────────────────────────────────
if menu == "Create Account":
    st.header("📝 Create a New Account")

    with st.form("create_form"):
        name  = st.text_input("Full Name")
        age   = st.number_input("Age", min_value=1, max_value=120, step=1)
        email = st.text_input("Email Address")
        pin   = st.text_input("4-Digit PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("Create Account")

    if submitted:
        if name and email and pin:
            success, result = bank.CreateAccount(name, age, email, pin)
            if success:
                st.success("✅ Account created successfully!")
                st.balloons()
                st.subheader("Your Account Details")
                st.write(f"**Name:** {result['name']}")
                st.write(f"**Age:** {result['age']}")
                st.write(f"**Email:** {result['email']}")
                st.write(f"**Account No:** `{result['account_no']}`")
                st.write(f"**Balance:** Rs. {result['balance']}")
                st.warning("⚠️ Please note your Account Number carefully!")
            else:
                st.error(f"❌ {result}")
        else:
            st.warning("Please fill in all the fields.")

# ─── 2. Deposit Money ────────────────────────────────────────────────────────
elif menu == "Deposit Money":
    st.header("💰 Deposit Money")

    with st.form("deposit_form"):
        acc_no = st.text_input("Account Number")
        pin    = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input("Amount to Deposit (Max Rs.10,000)", min_value=1, max_value=10000, step=1)
        submitted = st.form_submit_button("Deposit")

    if submitted:
        if acc_no and pin:
            success, msg = bank.DepositMoney(acc_no, pin, amount)
            if success:
                st.success(f"✅ {msg}")
            else:
                st.error(f"❌ {msg}")
        else:
            st.warning("Please fill in all the fields.")

# ─── 3. Withdraw Money ───────────────────────────────────────────────────────
elif menu == "Withdraw Money":
    st.header("🏧 Withdraw Money")

    with st.form("withdraw_form"):
        acc_no = st.text_input("Account Number")
        pin    = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input("Amount to Withdraw", min_value=1, step=1)
        submitted = st.form_submit_button("Withdraw")

    if submitted:
        if acc_no and pin:
            success, msg = bank.WithdrawMoney(acc_no, pin, amount)
            if success:
                st.success(f"✅ {msg}")
            else:
                st.error(f"❌ {msg}")
        else:
            st.warning("Please fill in all the fields.")

# ─── 4. View Account ─────────────────────────────────────────────────────────
elif menu == "View Account":
    st.header("👁️ View Account Details")

    with st.form("view_form"):
        acc_no     = st.text_input("Account Number")
        pin        = st.text_input("PIN", type="password", max_chars=4)
        show_pin   = st.checkbox("Show PIN in details")
        submitted  = st.form_submit_button("View Details")

    if submitted:
        if acc_no and pin:
            success, result = bank.ViewAccount(acc_no, pin)
            if success:
                st.success("✅ Account found!")
                st.subheader("Account Details")
                st.write(f"**Name:** {result['name']}")
                st.write(f"**Age:** {result['age']}")
                st.write(f"**Email:** {result['email']}")
                st.write(f"**Account No:** `{result['account_no']}`")
                st.write(f"**Balance:** Rs. {result['balance']}")
                if show_pin:
                    st.write(f"**PIN:** {result['pin']}")
                else:
                    st.write("**PIN:** ****")
            else:
                st.error(f"❌ {result}")
        else:
            st.warning("Please fill in all the fields.")

# ─── 5. Update Account ───────────────────────────────────────────────────────
elif menu == "Update Account":
    st.header("✏️ Update Account Details")
    st.info("You can only change: Name, Email, or PIN. Age, Account Number and Balance cannot be changed.")

    with st.form("update_form"):
        acc_no    = st.text_input("Account Number")
        pin       = st.text_input("Current PIN", type="password", max_chars=4)
        field     = st.selectbox("What do you want to change?", ["name", "email", "pin"])
        new_value = st.text_input("New Value")
        submitted = st.form_submit_button("Update")

    if submitted:
        if acc_no and pin and new_value:
            success, msg = bank.UpdateAccount(acc_no, pin, field, new_value)
            if success:
                st.success(f"✅ {msg}")
            else:
                st.error(f"❌ {msg}")
        else:
            st.warning("Please fill in all the fields.")

# ─── 6. Delete Account ───────────────────────────────────────────────────────
elif menu == "Delete Account":
    st.header("🗑️ Delete Account")
    st.error("⚠️ This action is permanent and cannot be undone!")

    with st.form("delete_form"):
        acc_no    = st.text_input("Account Number")
        pin       = st.text_input("PIN", type="password", max_chars=4)
        confirm   = st.checkbox("Yes, I really want to delete my account.")
        submitted = st.form_submit_button("Delete Account")

    if submitted:
        if acc_no and pin:
            if confirm:
                success, msg = bank.DeleteAccount(acc_no, pin)
                if success:
                    st.success(f"✅ {msg}")
                else:
                    st.error(f"❌ {msg}")
            else:
                st.warning("Please check the confirmation box to proceed.")
        else:
            st.warning("Please fill in all the fields.")
