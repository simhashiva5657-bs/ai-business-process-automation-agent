import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="AI Business Agent",
    page_icon="🤖",
    layout="centered",
)


st.title("🤖 AI Business Process Automation Agent")
st.write("Automate employee equipment requests.")


employee_id = st.text_input(
    "Employee ID",
    placeholder="EMP001",
)

item = st.selectbox(
    "Equipment",
    ["laptop", "monitor", "keyboard", "mouse"],
)


if st.button("Create Equipment Request", type="primary"):

    if not employee_id:
        st.error("Please enter an Employee ID.")

    else:
        try:
            response = requests.post(
                f"{API_URL}/equipment-request",
                params={
                    "employee_id": employee_id,
                    "item": item,
                },
                timeout=30,
            )

            result = response.json()

            if result.get("status") == "SUCCESS":

                st.success("Equipment request created successfully!")

                st.subheader("Employee")
                st.json(result["employee"])

                st.subheader("Inventory")
                st.json(result["inventory"])

                st.subheader("Request")
                st.json(result["request"])

                st.subheader("IT Notification")
                st.json(result["notification"])

            else:
                st.error(result.get("message", "Request failed."))

        except requests.RequestException as exc:
            st.error(f"Unable to connect to FastAPI: {exc}")