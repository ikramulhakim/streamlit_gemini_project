import streamlit as st
from api_calling import note_generate,audio_generate,quiz_generate

from PIL import Image


st.title('Note summary and Quiz Generator')
st.markdown('upload upto 3 images to generat a summary and quizes')

st.divider()


with st.sidebar:
    st.header('controls')

    #images

    images=st.file_uploader('upload images',
                      accept_multiple_files=True, 
                      type=['jpg', 'jpeg', 'png']
                      )
    pil_images=[]
    for img in images:
        pil_images.append(Image.open(img))
    

    if images:
        if len(images) > 3:
            st.warning('Please upload up to 3 images only.')
        else:
            st.subheader('Uploaded Images')

            col=st.columns(len(images))

        

        for i,img in enumerate(images):
            with col[i]:
                st.image(img)

        
     #selectbox

    selected=st.selectbox('select the type of quiz you want to generate',
                  ('Easy','Medium','Hard'),
                  index=None)
    


    pressed=st.button('click to generate summary and quiz',type='primary')



if pressed:
    if not images:
        st.error('Please upload at least one image to generate summary and quiz.')
    if not selected:
        st.error('Please select a quiz type to generate summary and quiz.')


    if images and selected:
        #note

        with st.container(border=True):
            st.subheader('Your note summary')

            with st.spinner('Generating note summary...'):
                generated_note=note_generate(pil_images)
                st.markdown(generated_note)


        #audio

        with st.container(border=True):
            st.subheader('Audio summary')

            with st.spinner('Generating audio summary...'):
                generated_note=generated_note.replace('*','')
                generated_note=generated_note.replace('#','')
                generated_note=generated_note.replace('`','')
                generated_note=generated_note.replace('-','')

                audio_generated=audio_generate(generated_note)
                st.audio(audio_generated)

        #quiz
        with st.container(border=True):
            st.subheader(f'Quiz {selected}')

            with st.spinner('Generating quiz...'):
                quiz_generated=quiz_generate(pil_images,selected)
                st.markdown(quiz_generated)


    