import streamlit as st

st.markdown('<h1 align="center"> How i fooled my schoolmates <h1>' , unsafe_allow_html=True  )
industry = st.text_input("enter filim industry name ")
charecter_name = st.text_input("give any charecter name that you want to play ")
place = st.text_input('enter place name',value='')
show_name = st.text_input("enter any show name you want to perform ")
best_friend = st.text_input("enter friend name ")
teacher_name = st.text_input(" enter teacher name ")
if len(teacher_name) != 0:
    st.markdown('<h2 align="center"> Your story  <h2>' , unsafe_allow_html=True)
    st.write("In second grade, I told everyone that I was leaving school before next semester to move to " , industry ,"to play " , charecter_name ,"from", place ,"on", show_name ,". At first I just told to " , best_friend ," ( My best friend) , but then the whole school found out. I had people coming up to me and asking me for my autograph and my teacher " , teacher_name ,"even asked for a picture with me. When I showed up on the first day of school in third grade, I told everyone that the show was going off the air after the season finished (even though I had no knowledge of when it was ending), and so they wouldn’t need me. AND THE SHOW ENDED AFTER THAT SEASON AND EVERYONE BELIEVED ME UP UNTIL LIKE 6TH GRADE BUT", best_friend ,"NEVER LET ME FORGET ABOUT IT AND I’M SO ANGRY.")






