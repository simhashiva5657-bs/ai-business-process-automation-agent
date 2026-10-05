import streamlit as st
import requests


API_URL = "http://127.0.0.1:8080"


st.set_page_config(
    page_title="AI Business Agent",
    page_icon="🤖",
    layout="centered",
)


st.title("🤖 AI Business Process Automation Agent")
st.write("Automate employee equipment requests.")


st.divider()


st.subheader("Equipment Request")


employee_id = st.text_input(
    "Employee ID",
    placeholder="EMP001",
)

item = st.selectbox(
    "Equipment",
    ["laptop", "monitor", "keyboard", "mouse"],
)


if st.button("Process Request", type="primary"):

    if not employee_id:
        st.warning("Please enter an employee ID.")

    else:
        with st.spinner("Processing equipment request..."):

            try:
                response = requests.post(
                    f"{API_URL}/equipment-request",
                    params={
                        "employee_id": employee_id,
                        "item": item,
                    },
                    timeout=120,
                )

                if response.status_code == 200:

                    result = response.json()

                    if result.get("status") == "SUCCESS":
                        st.success("Equipment request processed successfully!")

                        st.json(result)

                    else:
                        st.error("Equipment request failed.")
                        st.json(result)

                else:
                    st.error(
                        f"API request failed with status "
                        f"{response.status_code}"
                    )

            except requests.exceptions.RequestException as exc:
                st.error(f"Unable to connect to FastAPI: {exc}")