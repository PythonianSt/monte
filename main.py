import streamlit as st
import numpy as np
import pandas as pd

# Function to run Monte Carlo simulation
def monte_carlo_dice_rolls(rolls):
    results = []
    for _ in range(rolls):
        result = np.random.randint(1, 7) + np.random.randint(1, 7)  # Two 6-sided dice
        results.append(result)
    return results

# Main Streamlit application
def main():
    st.title("DHV Monte Carlo Dice Roll Simulation")
    
    # Display dice image
    st.image("dice.JPEG", caption="Dice", use_container_width=True)

    # User inputs
    dice1_value = st.number_input("Enter the value for Dice 1 (1-6):", min_value=1, max_value=6, value=1)
    dice2_value = st.number_input("Enter the value for Dice 2 (1-6):", min_value=1, max_value=6, value=1)
    rolls = st.number_input("Enter the number of rolls:", min_value=1, value=1000)

    if st.button("Roll Dice"):
        # Calculate combined number from user input
        combined_input = dice1_value + dice2_value
        
        # Run the Monte Carlo simulation
        results = monte_carlo_dice_rolls(rolls)

        # Calculate probabilities
        results_df = pd.Series(results).value_counts().sort_index()
        probabilities = results_df / rolls

        # Display the results
        st.write(f"### Combined Number from Input: {dice1_value} + {dice2_value} = {combined_input}")
        st.write(f"Total Rolls: {rolls}")
        
        # Display the results in a DataFrame
        result_df = pd.DataFrame({
            'Sum': results_df.index,
            'Count': results_df.values,
            'Probability (%)': (probabilities * 100).values  # Convert to percentage
        })
        
        st.write(result_df)

        # Display predicted combined numbers
        predicted_prob = probabilities.get(combined_input, 0.0) * 100  # Convert to percentage
        st.write(f"### Predicted Probability of Combined Number {combined_input}: {predicted_prob:.2f}%")

        # Plotting the probabilities
        st.bar_chart(result_df.set_index('Sum')['Probability (%)'])

if __name__ == "__main__":
    main()