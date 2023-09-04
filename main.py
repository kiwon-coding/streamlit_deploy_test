import streamlit as st
import pandas as pd
import numpy as np
import math
import random

st.write('Hi!')

s = pd.Series([1, 3, 5, np.nan, 6, 8])
st.write(s)