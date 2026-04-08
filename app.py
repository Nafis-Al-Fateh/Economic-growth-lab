import streamlit as st
import matplotlib.pyplot as plt
from solow_core import simulate_solow
from steady_state import steady_state_k

st.title("Economic Growth Lab - Solow Model")

st.sidebar.header("Model Parameters")

s = st.sidebar.slider("Savings Rate",0.01,0.9,0.3)
alpha = st.sidebar.slider("Capital Share",0.1,0.7,0.33)
delta = st.sidebar.slider("Depreciation",0.01,0.2,0.05)
n = st.sidebar.slider("Population Growth",0.0,0.05,0.02)
g = st.sidebar.slider("Technology Growth",0.0,0.05,0.02)

k0 = st.sidebar.slider("Initial Capital",0.1,10.0,1.0)
T = st.sidebar.slider("Time Periods",20,200,100)

k,y = simulate_solow(s,alpha,delta,n,g,k0,T)

fig,ax = plt.subplots()

ax.plot(k,label="Capital per Worker")
ax.plot(y,label="Output per Worker")

ax.set_xlabel("Time")
ax.set_ylabel("Value")

ax.legend()

st.pyplot(fig)

k_star,y_star = steady_state_k(s,alpha,delta,n,g)

st.subheader("Steady State")

st.write("Steady State Capital:",k_star)
st.write("Steady State Output:",y_star)
