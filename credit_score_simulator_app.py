import streamlit as st
import matplotlib.pyplot as plt

# Set up page
st.set_page_config(page_title="Credit Score Simulator", page_icon="💳")

st.title("💳 Credit Score Simulator")
st.markdown("Enter your financial details below to simulate your credit score.")

# Input fields
debt = st.number_input("Total Debt (₹)", min_value=0.0, step=1000.0)
income = st.number_input("Monthly Income (₹)", min_value=0.0, step=1000.0)
num_cards = st.slider("Number of Credit Cards", 0, 10, 1)
missed_payments = st.slider("Number of Missed Payments", 0, 10, 0)
utilization = st.slider("Credit Utilization (%)", 0, 100, 30)
credit_age = st.slider("Credit Age (Years)", 0, 30, 5)

# Button to simulate
if st.button("Simulate Credit Score"):
    score = 850
    debt_penalty = (debt / income) * 100 if income > 0 else 0
    missed_penalty = missed_payments * 15
    utilization_penalty = utilization * 0.5
    age_bonus = credit_age * 5
    card_penalty = num_cards * 2

    score -= debt_penalty
    score -= missed_penalty
    score -= utilization_penalty
    score += age_bonus
    score -= card_penalty

    score = max(300, min(850, round(score)))

    st.subheader(f"📊 Your Simulated Credit Score: {score}")

    # Credit score status
    if score >= 750:
        st.success("Status: Excellent ✨")
    elif score >= 700:
        st.info("Status: Good 🙂")
    elif score >= 650:
        st.warning("Status: Fair 😐")
    else:
        st.error("Status: Poor 😟")

    # 💡 Personalized Advice
    st.markdown("### 💡 Personalized Advice:")
    if utilization > 40:
        st.write("- Try to lower your credit utilization to below 30%.")
    if missed_payments > 0:
        st.write("- Avoid missing payments to improve your score.")
    if debt > (income * 0.5):
        st.write("- Consider reducing your total debt.")
    if credit_age < 2:
        st.write("- Keep credit accounts open to build credit history.")
    if num_cards > 5:
        st.write("- Too many credit cards may be seen as risky. Manage wisely.")

    # 📊 Pie Chart of Score Factors
    st.markdown("### 📈 Credit Factor Impact Chart")
    labels = ['Debt Penalty', 'Missed Payments', 'Utilization Penalty', 'Credit Age Bonus', 'Card Penalty']
    values = [debt_penalty, missed_penalty, utilization_penalty, age_bonus, card_penalty]
    colors = ['#ff9999','#ffc000','#8fd9b6','#d395d0','#66b3ff']

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

    # 📁 Downloadable Report
    st.markdown("### 📂 Download Credit Report")
    report = f"""
    Credit Score Simulator Report
    -----------------------------
    Total Debt: ₹{debt}
    Monthly Income: ₹{income}
    Number of Credit Cards: {num_cards}
    Missed Payments: {missed_payments}
    Credit Utilization: {utilization}%
    Credit Age: {credit_age} years

    Simulated Credit Score: {score}

    Tips:
    """

    if utilization > 40:
        report += "- Lower your credit utilization.\n"
    if missed_payments > 0:
        report += "- Avoid missing payments.\n"
    if debt > (income * 0.5):
        report += "- Consider reducing total debt.\n"
    if credit_age < 2:
        report += "- Build credit history over time.\n"
    if num_cards > 5:
        report += "- Manage multiple credit cards wisely.\n"

    st.download_button("Download Report", report, file_name="credit_score_report.txt")
