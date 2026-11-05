import streamlit as st

st.set_page_config(page_title="Interview Prep App")
st.title("Interview Prep App")
st.write("Interview ki tayari karo, confident bano!")

questions_data = {
    "Python Developer": [
        "Python kya hai aur isko kyun use karte hain?",
        "List aur Tuple me kya farq hai?",
        "OOP ke 4 pillars konse hain?",
        "Python me function kaise banate hain?",
        "Apne koi Python project batayein jo apne banaya ho?"
    ],
    "Data Entry / Computer Operator": [
        "Apki typing speed kitni hai?",
        "MS Excel me VLOOKUP ka kya kaam hai?",
        "Data Entry me ghalti se kaise bachte hain?",
        "Aap MS Word aur Excel me kitne expert hain?",
        "Agar aapko 1000 entries 1 din me karni hon to kaise karenge?"
    ],
    "Customer Support": [
        "Apna introduction dein.",
        "Agar customer gussa ho to aap kya karenge?",
        "Aap is company me kyun kaam karna chahte hain?",
        "Aap pressure me kaise kaam karte hain?",
        "Apki sab se bari strength kya hai?"
    ]
}

job = st.selectbox("Apni Job Select Karo", list(questions_data.keys()))
st.subheader(job + " - Interview Questions")

score = 0

for i, q in enumerate(questions_data[job]):
    st.write("Q" + str(i+1) + ": " + q)
    answer = st.text_area("Apna Jawab " + str(i+1) + " Yahan Likho", key="ans" + str(i), height=80)
    if answer:
        words = len(answer.split())
        if words > 30:
            st.success("Bohat Acha Jawab! (" + str(words) + " words) - Detailed hai.")
            score = score + 20
        elif words > 10:
            st.warning("Theek hai (" + str(words) + " words) - Thora aur detail add karo.")
            score = score + 10
        else:
            st.error("Jawab bohat chota hai (" + str(words) + " words) - 2-3 lines likho.")
    st.divider()

if st.button("Final Score Dekho"):
    st.subheader("Total Score: " + str(score) + " / 100")
    if score >= 80:
        st.balloons()
        st.success("Excellent! Tum interview ke liye ready ho.")
    elif score >= 50:
        st.warning("Good, lekin thori aur practice karo.")
    else:
        st.error("Practice ki zaroorat hai. Jawab lambay likho.")
    st.write("Tip: Har jawab me Example do. Jese 'Maine university me ye project banaya tha...'")
