from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)
