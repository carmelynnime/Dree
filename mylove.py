import streamlit as st
from PIL import Image
import time

# Set the page title and icon
st.set_page_config(
    page_title="Andree, My Heart Belongs to You",
    page_icon=":heart:",
    layout="wide"
)

# Play background music when the app loads
def play_background_music():
    st.audio("audio/love_song.mp3", format="audio/mp3", start_time=0)  # Add your music file path here

# Prompt Message
if 'continue' not in st.session_state:
    st.title("Are you ready to make even more unforgettable memories with me Dreeee?")
    
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes"):
            st.write("Nawa ka??? Dapat laaaanggg!! 😝")
            st.session_state['continue'] = True
    
    with col2:
        if st.button("No"):
            st.write("Sheeeeems! Waka nalipong? Wakay optiooon!!! 😝")
            st.session_state['continue'] = True

# Show Start button after "kidding" message
if 'continue' in st.session_state and 'start' not in st.session_state:
    if st.button("Start"):
        st.session_state['start'] = True

# Play audio and proceed once 'start' button is clicked
if 'start' in st.session_state:
    # Play background music
    play_background_music()

    # Sidebar Navigation
    st.sidebar.title("Navigate our Journey")
    navigation = st.sidebar.radio(
        "Go to",
        ["🌸 Our Beginning", "📷 Polaroid Gallery", "🍽️ Our Foodie Adventures", "👩‍❤️‍👨 Cutie Dates",
         "💌 Love Notes", "💘 How Well Do You Know Us?", "🔗 Forever Bound"]
    )

    # Introduction Page - Our Beginning
    def introduction():
        st.title("🌸 Our Beginning")
        
        header_image = Image.open("photos/ey.JPG")  # Add your header image path here
        st.image(header_image, use_column_width=True)

        st.write("""
        **Dear Dreeeee,**
        
        I’m sorry if I made you wait a little too long. Please, don’t ever doubt your worth or think it has anything to do with why I haven't done much effort yet. I genuinely wanna know you more before I make my decision. Carry on, everything I’m working on now for us and including this site that is created just for you.
        I want you to know how much I truly appreciate you and love you with all my heart. You mean so much to me, and I’m so grateful to have you my most unexpected and biggest plot twist in my life. ❤️
        
        Here's a journey through our relationship. Enjoy reminiscing about our favorite memories and the love we've built. 
        """)

    # Polaroid Gallery
    def polaroid_gallery():
        st.title("📷 Polaroid Gallery")
        
        memories = {
            "🌹 First Glance": ("photos/IMG_9399.JPG", "Seeing this photo of us still makes me blush and smile🥰. Who would have thought that the guy I was only seeing on MyDays would grab my waist during our first meet? It's so surreal, you knaaauuur? HAHAHA. This was the day I first heard your voice, and I was honestly shocked by how it sounded. It was unusual but cute😅. I didn’t expect you to come and spare your precious time just to see me perform at this event. It meant a lot to me, especially since we had only known each other for days. Also, thank you for buying me Sting! HAHAHA, so funny that I got you to do errands on day one. Thank you again for coming Dreeeeee, I appreciate it sauuurr much!"),
            "💫 Magical Skinship": ("photos/IMG_7459.JPG", "The feeling might not be new to you, but it was for me. I don’t easily let other men hold my hand, so I was a bit nervous when you started playing with my hands. I hadn’t held hands with anyone for quite a while and thank you for taking a picture it’s one of my favorites! This was the moment when I started feeling comfortable talking to you. I stopped lying and decided to tell you the truth. Maybe I gave in and decided to trust you. It was hard for me to share, especially knowing you liked me (or ambot AAHAHAH assuming lang AHHAHAH). I didn’t want you to pity me or treat me differently because of my situation. I can stand on my own, and I don’t want to depend on anyone. Despite all the negative thoughts running through my mind, you listened. You sincerely listened and respected me, and you even reminded me that if I wasn’t comfortable sharing, I didn’t have to. You let me take my time. Thank you for making me feel safe enough to trust you. I had fun talking about my life with you, and again, thank you for listening."),
            "✨ Growing Closer": ("photos/IMG_0058.JPeG", "This was the day I purposely pushed you away because I was scared of all the possibilities that could happen if we continued communicating. I was afraid of losing you. I didn’t want to get attached. I was terrified that I’d be building my man for another woman. This was also the time when you first kissed me on the cheek and kept playing with my shoulders while I giggled 😬. Before we went to Il Corso, I remember being so shy during dinner, but my shyness disappeared because you made me so comfortable. Time flew by so fast, and we eventually went to our third unplanned stop, Bay Coffee. I appreciate every time you take the initiative, like ordering food for us, even though you mistakenly ordered the donut😂. But it was still yummy, so it’s fine, cutie boy! I still got shy when you looked at me at this point… hays, my crush HHAHAHA. I love this pic of ours, bc you really go along with my craziness."),
            "💞 Falling in Love": ("photos/IMG_0100.JPG", "We had dinner at Sugbo Mercado before taking this pic. Thanks for the treat I was so full! Anyways, I can’t explain how we look so cute together 😩 AW AHAHHAHA. I still felt shy and awkward during physical contact poses, but thank you for making me comfortable again! This day I felt a bit nervous. Your pace in getting to know each other was too fast for me. It was too fast because I wasn’t used to it. The plan was supposedly just cuddles. I wasn’t supposed to give you our first kiss at QL, GRAAAAAAAAAAAAAAAAAH, but I just couldn’t resist your cuteness when you said, “Pleaseeee.” You kept trying to kiss me, imagine how cute you wereeee!! Until I got carried away and gave in!! We shared our first sweet kiss and I just want you to know you are so gentle and passionate when you kiss. I love the way how you do it."),
        }
        
        selected_memory = st.selectbox("Choose a memory", list(memories.keys()))
        img_path, caption = memories[selected_memory]
        
        # Display the selected image and caption
        st.image(img_path, caption=caption, use_column_width=True)
        
    # Eatwell! Page - Our Foodie Adventures
    def eatwell():
        st.title("🍽️ Our Foodie Adventures")
        
        st.write("**I love seeing you eating, please stay healthy always Dree!!! (Disregard naka rotate liki man ang streamlit TT)**")

        col1, col2 = st.columns(2)
        with col1:
            st.image("photos/IMG_0059.JPG", caption="July 06, 2024")
        with col2:
            st.image("photos/IMG_1170.JPG", caption="July 28, 2024")
        with col1:
            st.image("photos/IMG_1203.JPG", caption="July 28, 2024")
        with col2:
            st.image("photos/IMG_2106.JPG", caption="August 09, 2024")
        with col1:
            st.image("photos/IMG_2346.JPG", caption="August 23, 2024")
        with col2:
            st.image("photos/IMG_2466.JPG", caption="August 23, 2024")
        with col1:
            st.image("photos/IMG_3258.JPG", caption="August 27, 2024")
        with col2:
            st.image("photos/IMG_3431.JPG", caption="September 08, 2024")
        with col1:
            st.image("photos/IMG_3456.JPG", caption="September 09, 2024")
        with col2:
            st.image("photos/IMG_4416.JPG", caption="First delivered food by Andreeee! Appreciate it so much🥰!")
    
    # Cutie Dates Page 
    def cute_date():
        st.title("👩‍❤️‍👨 Cutie Dates")
        
        st.write("**To more dates together with you Dree!!!**")

        header_image = Image.open("photos/IMG_0093.JPG")  # Add your header image path here
        st.image(header_image, caption="First Photobooth!", use_column_width=True)
        header_image = Image.open("photos/IMG_0936.JPG")  
        st.image(header_image, caption="First Trip Together!", use_column_width=True)
        header_image = Image.open("photos/IMG_1615.JPG")  
        st.image(header_image, caption="First at Tops!", use_column_width=True)
        header_image = Image.open("photos/IMG_2438.JPG")  
        st.image(header_image, caption="First Arcade!", use_column_width=True)
        header_image = Image.open("photos/IMG_2493.JPG")  
        st.image(header_image, caption="First Movie Date!", use_column_width=True)
        header_image = Image.open("photos/IMG_3252.JPG")  
        st.image(header_image, caption="First Long Ride!", use_column_width=True)
        header_image = Image.open("photos/IMG_2707.JPG")  
        st.image(header_image, caption="First Ukay Together!", use_column_width=True)
        header_image = Image.open("photos/IMG_3880.JPG")  
        st.image(header_image, caption="First Mass Together!", use_column_width=True)
        header_image = Image.open("photos/IMG_3902.JPG")  
        st.image(header_image, caption="First Jogging!", use_column_width=True)
    
    # Love Notes Page - Hidden Love Messages
    def love_notes():
        st.title("💌 Love Notes for Andree")
        
        st.write("Here are some secret love notes just for you, Dreeeee! Opeeeeen dayooon!")
        
        with st.expander("Click to reveal a love note"):
            st.write("You make my heart so full, Dreeeeeeee. You are so lucky that you have me! AYYYY J0OKEEE ako diay AHAHHAHA I feel so lucky to have you by my side MWAMWAAAA. 😘")
        
        with st.expander("Another secret message"):
            st.write("Thank you for taking care of me, being patient, kind, and making me smile every day. All your efforts are appreciated sauuur muuuch Dreeee!! 💖")
            
        with st.expander("One more note for you"):
            st.write("I can't wait to see what the future holds for us. Yawerrrrdss!! yahaya jud ani niya nako ba!! AHHAHAHAH excited sa future with you!! 🥰")

    # Love Quiz Page - How Well Do You Know Us?
    def quiz():
        st.title("💘 How Well Do You Know Us?")
        
        st.write("Test ta gamay bi!")
        
        q1 = st.radio("Where did we go on our first date?", ["choose", "TCH BBQ", "Sugbo Mercado", "Coffee shop", "Pardo"])
        if q1 == "TCH BBQ":
            st.success("Yatiiiii kahinomdom ohhh! 💕")
        else:
            st.warning("Maooo na dhaaa! Sige kalimti")

        q2 = st.radio("What was my favorite part of you?", ["choose", "Eyes", "Smile", "Voice", "Eyebrows"])
        if q2 == "Smile":
            st.success("Swerte! Pasalamat jud kas imong smile! It f melted my heart. 💖")
        else:
            st.warning("Mao na gapatakataka napud!")

        q3 = st.radio("What's my favorite love language?", ["choose", "Words of affirmation", "Quality Time", "Acts of Service", "Physical Touch"])
        if q3 == "Acts of Service":
            st.success("Ana jud! dapat saktooo!!!")
        else:
            st.warning("Hayyy pa baby pud ta kadyot uii princess treatment ba")

    # Final Page - Forever Bound
    def forever_bound():
        st.title("🔗 Forever Bound")
        
        # Display the video first
        st.video("https://youtu.be/Rq4e3Mv6OX4")

    # Display the message after the video
        st.write("**Hiii Dreeeeeeeeeeeeeeeeeeeeeeee!!!!!!**")
        st.write("""
            I’m literally getting butterflies while making this for you WAAAAAAAAAAAAAHHH AHHAHAHAHA! boang mn diay ko HAHAHAH 😣. Anyway, for the past 4 months I’ve been observing you, I decided to take the risk wholeheartedly now. Even though we’ve been acting like partners for months, I admit I haven’t given my all yet, so you better prepare! Charot! AHHAHAHA. Jokes aside, I appreciate everything you’ve done and proven. You’ve been consistent and true to your words, keeping your promises and standing by what you’ve said. Thank you for being so honest and genuine—I really felt it. Even though we haven’t known each other for long, you trusted me and shared your personal and relationship life without hesitation. I didn’t expect you to share your experiences because no one has ever shared a similar story like yours. I had doubts about continuing with you; I'm afraid that I might just be one of “them,” bc brooooo, I don’t want games or temporary sh*t. I disregarded all my negative thoughts and took the chance to get to know you. I wasn’t ready to be interested in anyone again as I realized that I still have a lot to learn and work on. But despite that, I followed where happiness led me. I tried resisting, but guess what—I still replied to you, and look where it took us.

            Thank you for taking care of me, Dree! You make me want to be babied all the time. My independent alpha self just wants to give in when I’m around you. Special thanks to your sincerity; it made me ready to love and trust a man again <33333. Thank you for letting me experience your love, my love ❤. You bring out all the hidden sides of me. I hope you’ll have long patience for me, especially during times when I’m dumb, dramatic, or when I haven’t shown enough care, and how numb my feelings will be. One thing’s for sure, though—I will always choose you. Please bear with me till the end. I don’t need a man, but for you, I’ll make an exception. Your worth will always be valued, and I will forever be grateful for your existence!! Whatever happens, I hope we continue choosing each other and never break our trust. Let’s work through this together👫. There are innumerable "I love yous" that were left unsaid by me. Thank you for patiently waiting for me, DREEE!! I LOVE YOU TO THE MOON AND BACK, MY BOYFRIEND, ANDREEEEEE!!! 💞
        """)

        st.write("**Let's make a lifetime of memories together 😘😘😘**")

    # Display heart confetti using snow effect
        st.snow()  # Simulates a light confetti effect, which can resemble falling hearts

    # Navigation mapping to functions
    if navigation == "🌸 Our Beginning":
        introduction()
    elif navigation == "📷 Polaroid Gallery":
        polaroid_gallery()
    elif navigation == "🍽️ Our Foodie Adventures":
        eatwell()
    elif navigation == "👩‍❤️‍👨 Cutie Dates":
        cute_date()
    elif navigation == "💌 Love Notes":
        love_notes()
    elif navigation == "💘 How Well Do You Know Us?":
        quiz()
    elif navigation == "🔗 Forever Bound":
        forever_bound()
