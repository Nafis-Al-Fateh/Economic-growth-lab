import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Economic Growth Lab",
    layout="wide"
)

# Title
st.title("Economic Growth Lab: Solow Growth Model Simulator")

st.markdown("""
**Author:** Nafis Al Fateh  
**Major:** Economics  
**Institution:** Shahjalal University of Science and Technology  

This interactive application demonstrates the dynamics of the Solow Growth Model.
Users can modify key parameters to observe how savings, depreciation,
population growth, and technological progress influence long-run economic growth.
""")

st.markdown("---")

# Model explanation
st.subheader("Model Overview")

st.markdown("""
The Solow Growth Model explains long-run economic growth through capital accumulation,
labor growth, and technological progress. Adjust the parameters in the sidebar
to observe how the economy converges toward a steady-state equilibrium.
""")

# Sidebar parameters
st.sidebar.header("Simulation Parameters")

s = st.sidebar.slider("Savings Rate (s)", 0.01, 0.9, 0.30)
alpha = st.sidebar.slider("Capital Share (α)", 0.10, 0.70, 0.33)
delta = st.sidebar.slider("Depreciation Rate (δ)", 0.01, 0.20, 0.05)
n = st.sidebar.slider("Population Growth (n)", 0.00, 0.05, 0.02)
g = st.sidebar.slider("Technology Growth (g)", 0.00, 0.05, 0.02)

k0 = st.sidebar.slider("Initial Capital", 0.1, 10.0, 1.0)
T = st.sidebar.slider("Simulation Periods", 20, 200, 100)

# Solow simulation
k = np.zeros(T)
y = np.zeros(T)

k[0] = k0

for t in range(T-1):

    y[t] = k[t] ** alpha

    investment = s * y[t]
    break_even = (n + g + delta) * k[t]

    k[t+1] = k[t] + investment - break_even

y[-1] = k[-1] ** alpha

# steady state
k_star = (s / (n + g + delta)) ** (1 / (1 - alpha))
y_star = k_star ** alpha

# Graph + Interpretation Layout
st.subheader("Economic Growth Simulation")

col1, col2 = st.columns([2,1])

# Graph
with col1:

    fig, ax = plt.subplots(figsize=(6,4))

    ax.plot(k, label="Capital per Worker")
    ax.plot(y, label="Output per Worker")

    ax.set_xlabel("Time")
    ax.set_ylabel("Value")

    ax.legend()

    st.pyplot(fig)

# Interpretation
with col2:

    st.subheader("Economic Interpretation")

    if s > 0.4:
        st.write("• A high savings rate leads to stronger capital accumulation and a higher steady-state level of income.")
    elif s < 0.2:
        st.write("• A low savings rate limits investment and slows long-run capital accumulation.")

    if n > 0.03:
        st.write("• High population growth reduces capital per worker, lowering steady-state income.")
    else:
        st.write("• Moderate population growth supports higher capital per worker.")

    if g > 0.03:
        st.write("• Strong technological progress significantly increases long-run economic growth.")
    else:
        st.write("• Limited technological progress restricts long-run productivity improvements.")

    if delta > 0.1:
        st.write("• High depreciation reduces the effective capital stock and slows capital accumulation.")
    else:
        st.write("• Lower depreciation allows capital to accumulate more effectively.")

    st.markdown("---")

    st.write("**Steady-State Results**")

    st.metric("Steady State Capital (k*)", round(k_star,3))
    st.metric("Steady State Output (y*)", round(y_star,3))

st.markdown("---")

st.markdown("""
**Economic Growth Lab**

Developed by **Nafis Al Fateh**  
Economics Major  
Shahjalal University of Science and Technology
""")
