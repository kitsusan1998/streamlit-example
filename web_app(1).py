import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression


def main(model):
    st.title('Loan')

    with st.form("my_form"):

        income = st.number_input('Please input your income')
        load_amount = st.number_input('Please input load amount')
        property_value = st.number_input('Please input your property value')
        open_end_line_of_credit = st.number_input(
            'Please input open-end_line_of_credit')
        co_applicant_credit_score_type = st.radio(
            'Please specific co_applicant_credit_score_type',
            ['1.0', '2.0', '3.0', '8.0', '9.0', '10.0'])
        co_applicant_age_above62 = st.radio('Is co-applicant age above 62?',
                                            [True, False])

        lien_status = st.number_input(
            'Please input tract_one_to_four_family_homes')
        debt_to_income_ratio = st.radio('debt_to_income_ratio',
                                        ['>60%', '36%-<50%'])

        if debt_to_income_ratio == '>60%':
            debt_to_income_ratio_60 = 1
            debt_to_income_ratio_50 = 0
        else:
            debt_to_income_ratio_60 = 0
            debt_to_income_ratio_50 = 1

        co_applicant_credit_score_type_9 = 1 if co_applicant_credit_score_type == '9.0' else 0

        co_applicant_age_above_62 = 1 if co_applicant_age_above62 else 0

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:

            rs_prob = model.predict_proba([[
                debt_to_income_ratio_60,
                income,
                load_amount,
                property_value,
                open_end_line_of_credit,
                debt_to_income_ratio_50,
                co_applicant_credit_score_type_9,
                co_applicant_age_above_62,
                lien_status,
            ]])
            rs = model.predict([[
                debt_to_income_ratio_60,
                income,
                load_amount,
                property_value,
                open_end_line_of_credit,
                debt_to_income_ratio_50,
                co_applicant_credit_score_type_9,
                co_applicant_age_above_62,
                lien_status,
            ]])

            prob = rs_prob[0][1]

            st.markdown('Success probability: {:.2%}'.format(prob))

            if rs[0] == 1:
                st.markdown('Success!')
            else:
                st.markdown('Faild')
                st.markdown(
                    'You may reduce load amount or increase your property value'
                )


if __name__ == '__main__':
    model = joblib.load('log.model')
    main(model)
