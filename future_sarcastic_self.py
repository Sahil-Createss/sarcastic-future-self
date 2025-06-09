import streamlit as st
import random

# Sarcastic replies database
sarcastic_responses = {
   
    'default': [
        "I'm too sarcastic to answer that seriously.",
        "Ask me something interesting, will you?",
        "Future me says: Chill, it’s all going to be something."

    ],
     'success': [
        "Manifesting success like you manifest 6-pack abs — with zero effort.",
        "You’ll succeed... at pressing snooze 7 times daily."
    ],
    'study': [
        "Study plans? Oh, you mean the thing you make just to ignore?",
        "Studying? Please, even your books feel ghosted."
    ],
    'motivation': [
        "Your motivation is on DND — permanently.",
        "You got inspired for 2 minutes. A new record!"
    ],
    'goals': [
        "Goals? More like glorified to-do lists you never open.",
        "Set goals, ignore them, repeat. Success strategy!"
    ],
    'future': [
        "The future is bright. Like a flashbang grenade.",
        "Good news: your future self is still winging it."
    ],
    'coding': [
        "You code like a chef following a recipe on fire.",
        "StackOverflow is your spirit guide, isn’t it?"
    ],
    'life': [
        "Life update: Still buffering...",
        "You’ve figured out life. Just kidding, panic continues."
    ],
    'parents': [
        "They still think you're studying. Cute.",
        "Your parents check your ‘effort’ like it's crypto. Volatile and full of hype."
    ],
    'confidence': [
        "You radiate confidence. Like a leaking tube light.",
        "Fake it till you break it, am I right?"
    ],
    'grades': [
        "Your GPA is emotionally unavailable.",
        "Grades? Let’s call it a creative interpretation of learning."
    ],
    'career': [
        "Career path? More like a maze with no cheese.",
        "You’ll reach your career goals. After 47 detours and 3 breakdowns."
    ],
    'procrastination': [
        "A professional in putting things off — Olympic level.",
        "You delay more than the Indian Railways."
    ],
    'friends': [
        "Friends? You mean those 3 people you reply to after 2 business days?",
        "Still friends with the squad? Legends who haven’t blocked you — yet."
    ],
    'sleep': [
        "You sleep like a baby. Up every 2 hours questioning life.",
        "Your sleep cycle filed a complaint."
    ],
    'money': [
        "Bank balance so low it echoes.",
        "Your money goes faster than your will to try."
    ],
    'luck': [
        "Luck is real. Just not in your ZIP code.",
        "Even your shadow doesn’t stick around for luck."
    ],
    'discipline': [
        "You’ve got the discipline of a broken vending machine.",
        "Motivated today. Lazy tomorrow. Consistently inconsistent."
    ],
    'gym': [
        "Your gains are hiding better than your ex.",
        "You go to the gym in spirit. That counts, right?"
    ],
    'health': [
        "Health is wealth. You’re broke both ways.",
        "You run... emotionally. Physically? Nah."
    ],
    'relationship': [
        "Your dating life is the WiFi signal: weak, unstable, and disappears often.",
        "Love story loading... timeout error."
    ],
    'crush': [
        "Your crush thinks of you... as a classmate. At best.",
        "You and your crush? Like parallel lines."
    ],
    'food': [
        "Eat clean? Bro, you eat like exams are daily.",
        "That diet plan? Gone faster than your last crush."
    ],
    'fashion': [
        "Outfit on point? Maybe in the dark.",
        "Drip so hard... it flooded your common sense."
    ],
    'phone': [
        "You and your phone? True love. Unhealthy but real.",
        "Screen time called — even it’s worried about you."
    ],
    'reality': [
        "Reality check: You still think tomorrow you'll start.",
        "Dream big, nap harder. That’s the mantra."
    ],
    'internet': [
        "Slow net is still faster than your career decisions.",
        "Your WiFi works better than your will to move on."
    ],
    'vibe': [
        "You're vibing... but the vibe is existential dread.",
        "Mood: Doing everything but what you should."
    ],
    'overthinking': [
        "Your brain plays Netflix thrillers 24/7.",
        "You overthink texts that said 'ok'."
    ],
    'motivation_quotes': [
        "Another quote? Nice. That’ll definitely change your life for 30 seconds.",
        "Pinterest quotes aren't personality traits."
    ],
    'default': [
        "Not sure what you're asking, but your future self just rolled their eyes.",
        "You confuse even AI — congrats!"
    ]
}


def get_sarcastic_reply(user_input):
    user_input = user_input.lower()
    for keyword in sarcastic_responses.keys():
        if keyword in user_input:
            return random.choice(sarcastic_responses[keyword])
    return random.choice(sarcastic_responses['default'])

# Streamlit app
st.title("💬 Chat with Your Future Sarcastic Self")

st.write("Ask any question or share your worries, and your sarcastic future self will reply!")

# Text input from user
user_input = st.text_input("You:", "")

if user_input:
    reply = get_sarcastic_reply(user_input)
    st.markdown(f"*Future Sarcastic Self:* {reply}")