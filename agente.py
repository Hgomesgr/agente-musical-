from groq import Groq
import streamlit as st

st.title('AGENTE DE MUSICA')




client = Groq(api_key = '')

print('----------------------------------------------------')
print()
pergunta = st.text_input('Digite sua pergunta...')
print()
print('----------------------------------------------------')

resposta = client.chat.completions.create(
    model=  'openai/gpt-oss-120b',
    messages=[
    {
        "role":"system",
        'content':"Você é um musicista profissional que gosta de todos estilos de musica mas só fala ingles"
        
    },
    {
    
    "role": "user",
    "content":pergunta 

    }    
    ]
)
st.write(resposta.choices[0].message.content)

