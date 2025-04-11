import streamlit as st
import random

# Game Title
st.title("🎮 Number Guessing Game!")

# Session state setup for game variables
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
if "attempts_left" not in st.session_state:
    st.session_state.attempts_left = 10
if "score" not in st.session_state:
    st.session_state.score = 0

# Displaying game instructions
st.markdown(
    """
    **Instructions:**
    - Guess the number between 1 and 100.
    - You have 10 attempts to guess the correct number.
    - Earn 10 points for every correct guess.
    """
)

# Input for user guess
user_guess = st.number_input(
    "Enter your guess:", min_value=1, max_value=100, step=1, key="guess"
)

# Submit button
if st.button("Submit Guess"):
    if st.session_state.attempts_left > 0:
        # Check if guess is correct
        if user_guess == st.session_state.random_number:
            st.success("🎉 Amazing! You guessed it right!")
            st.session_state.score += 10
            st.session_state.random_number = random.randint(1, 100)  # New number
            st.session_state.attempts_left = 10  # Reset attempts
        elif user_guess < st.session_state.random_number:
            st.warning("🔼 Too low! Try a higher number.")
        else:
            st.warning("🔽 Too high! Try a lower number.")
        st.session_state.attempts_left -= 1
    else:
        st.error("Game Over! 🎮 Restarting...")
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.attempts_left = 10  # Reset attempts
        st.session_state.score = 0  # Reset score

# Display the player's progress
st.write(f"🕹️ Attempts left: {st.session_state.attempts_left}")
st.write(f"🌟 Score: {st.session_state.score}")

# Reset game button
if st.button("Restart Game"):
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts_left = 10
    st.session_state.score = 0
    st.success("Game has been restarted!")