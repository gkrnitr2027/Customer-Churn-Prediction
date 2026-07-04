import streamlit as st
import pandas as pd
import pickle

# -------------------- Load Model --------------------
with open("customer_churn_model.pkl", "rb") as f:
    model_data = pickle.load(f)

model = model_data["model"]
feature_names = model_data["features_name"]

# -------------------- Load Encoders --------------------
with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")
st.markdown("Enter customer details to predict whether the customer will churn.")

# -------------------- Input Form --------------------
user_input = {}

col1, col2 = st.columns(2)

for i, feature in enumerate(feature_names):

    container = col1 if i % 2 == 0 else col2

    with container:

        # ---------- Categorical Features ----------
        if feature in encoders:

            options = list(encoders[feature].classes_)

            selected = st.selectbox(
                feature,
                options,
                key=feature
            )

            user_input[feature] = encoders[feature].transform([selected])[0]

        # ---------- Numerical Features ----------
        else:

            if feature == "tenure":
                user_input[feature] = st.slider(
                    "Tenure (Months)",
                    min_value=0,
                    max_value=72,
                    value=12
                )

            elif feature == "MonthlyCharges":
                user_input[feature] = st.number_input(
                    "Monthly Charges",
                    min_value=0.0,
                    value=70.0,
                    step=0.1
                )

            elif feature == "TotalCharges":
                user_input[feature] = st.number_input(
                    "Total Charges",
                    min_value=0.0,
                    value=840.0,
                    step=0.1
                )

            else:
                user_input[feature] = st.number_input(
                    feature,
                    value=0.0
                )

# -------------------- Prediction --------------------
if st.button("Predict Churn", use_container_width=True):

    input_df = pd.DataFrame([user_input])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    st.divider()

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is likely to Churn")
    else:
        st.success("✅ Customer is not likely to Churn")

    st.subheader("Prediction Probability")

    st.progress(float(probability[1]))

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "No Churn Probability",
            f"{probability[0]*100:.2f}%"
        )

    with c2:
        st.metric(
            "Churn Probability",
            f"{probability[1]*100:.2f}%"
        )

    st.subheader("Customer Details")

    display_df = pd.DataFrame([user_input])

    # Decode values back to text for display
    for col in encoders:
        if col in display_df.columns:
            display_df[col] = encoders[col].inverse_transform(
                display_df[col].astype(int)
            )

    st.dataframe(display_df, use_container_width=True)