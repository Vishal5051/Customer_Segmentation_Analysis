import streamlit as st
import pickle

# Load the KMeans model
with open("km.pkl", "rb") as pickle_in:
    km = pickle.load(pickle_in)

def customer_segmentation(MonetaryValue, Frequency, Recency):
    MonetaryValue = int(MonetaryValue)
    Frequency = int(Frequency)
    Recency = int(Recency)

    prediction = km.predict([[MonetaryValue, Frequency, Recency]])
    return prediction[0]

def main():
    st.title("Customer Segmentation Analysis")
    html_temp = """
        <div style="background-color: lavander; padding: 10px">
        <h2 style="color: white; text-align: center;">Customer Segmentation Analysis</h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    MonetaryValue = st.text_input("MonetaryValue", "type here")
    Frequency = st.text_input("Frequency", "type here")
    Recency = st.text_input("Recency", "type here")
    result = ""
    if st.button("Predict"):
        result = customer_segmentation(MonetaryValue, Frequency, Recency)
        if result == 0:
            result = "Churned  customer"
        elif result == 1:
            result = "NEw customer"
        elif result == 2:
            result = "Customer at risk "
        else:
            result = "Churned customer"
    st.success("The output is {}".format(result))

if __name__ == '__main__':
    main()
