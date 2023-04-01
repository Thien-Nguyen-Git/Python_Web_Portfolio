import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Thien Nguyen")
    content = """
    Hi, I am Thien! I am a Software Developer. 
    Lorem ipsum dolor sit amet. Est atque nobis qui aperiam sapiente hic galisum nihil vel deserunt facere. 
    Id labore dignissimos ut consequuntur officiis rem quia quos At beatae Quis quo itaque laudantium. 
    Et totam nihil 33 blanditiis pariatur non nemo amet non sequi quia qui saepe nihil in consequatur voluptates. 
    Cum molestiae dolores vel reiciendis earum cum quos quia. 
    Et veritatis placeat et repudiandae incidunt et omnis quae id dolor molestiae qui perferendis galisum. 
    Id voluptatum atque eum voluptatem explicabo sed excepturi autem sed voluptas assumenda? 
    Est quas magnam aut fugit sunt a voluptas esse. 
    Et dolor internos ab magni rerum aut rerum dolorem sit tempore commodi et sunt vitae eum corrupti iste aut saepe omnis. 
    Cum nisi quia eos perspiciatis voluptate eum debitis voluptas ut voluptatibus necessitatibus id vero maiores aut illum quia et rerum laboriosam. 
    Cum accusamus nisi a eveniet repellendus ut enim laborum ut doloremque laudantium.
    """
    st.info(content)