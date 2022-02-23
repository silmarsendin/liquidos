import streamlit as st
#st.title('Aplicativo para Seleção das Proteções Contra Incêndio para Líquidos Igníferos')
#st.write('De acordo com a Instrução Técnica 25/19 do Corpo de Bombeiros do Estado de São Paulo e NBR 17.505.')
from PIL import Image
image1 = Image.open('liq.png')
st.image(image1, caption='')


# Menu lateral
st.sidebar.title('Cenário')
paginaselecionada = st.sidebar.selectbox('Selecione o cenário',['Defina o cenário','Parque de Tanques','Tanques em Edificações','Fracionados','Operações','Cais ou Pier','Destilarias','Refinarias','Postos de Serviços','Plataforma de Carregamento'])
st.sidebar.caption('Aplicativo desenvolvido em Python pelo Professor Silmar Sendin.')
# Fim do Menu Lateral

if paginaselecionada == 'Defina o cenário':
    st.title('Definição de Cenário')
    st.write('Escolha na caixa de seleção a esquerda qual cenário se aplica ao seu caso concreto.')
    definircenario = st.checkbox('Quero saber como definir o cenário com líquidos igníferos.')
    if definircenario:
       # video_file = open('https://youtu.be/e3a02Hl0ddM', 'rb')
        # video_bytes = video_file.read()
      #  st.video(video_bytes)

        st.video('https://youtu.be/e3a02Hl0ddM', format="video/mp4", start_time=0)

elif paginaselecionada == 'Parque de Tanques':
    st.title('Parque de Tanques')
    st.write('O cenário selecionado é um parque de Tanques e as informações a seguir só se aplicam a este cenário.')

    mostrarclasses = st.checkbox('Quero saber como classificar um líquido ignífero.')
    if mostrarclasses:
        from PIL import Image
        image = Image.open('classes.png')
        st.image(image, caption='Classes dos Líquidos Igníferos')
        st.write('PF = Ponto de Fulgor, PV = Pressão de Vapor, e PE = Ponto de Ebulição')

    classeliq = st.selectbox('Qual a Classe do Líquido Armazenado:',['Classe I','Classe IA','Classe IB','Classe IC','Classe II','Classe IIIA','Classe IIIB'])
    volumetanques = st.number_input("Qual o volume total, em litros, armazenado sem isolamento:")
    if volumetanques < 20001 or classeliq == 'Classe IIIB':
        st.write('Não será necessário os sistemas de espuma e resfriamento')
        st.write('Prever Sistema de Extintor de acordo com a Tabela 1.2 da IT 25/19 SP ou Tabela A.11 da NBR 17.505 - Parte 7.')
    elif volumetanques > 20000 or classeliq != 'Classe IIIB':
        mostrarnbr = st.checkbox('Quero saber como proteger o cenário de acordo com a NBR 17.505.')
        if mostrarnbr:
            st.write('Prever Sistema de Espuma de acordo com o item 8 da NBR 17.505 - Parte 7.')
            st.write('Prever Sistema de Resfriamento de acordo com o item 4.2.2 e item 6 da NBR 17.505 - Parte 7, checar as exceções do item 4.2.1.')
            st.write('Prever Sistema de Contenção de acordo com o item 5.9 da NBR 17.505 - Parte 2.')
        mostrarit25 = st.checkbox('Quero saber como proteger o cenário de acordo com a IT 25/19 de SP.')
        if mostrarit25:
            st.write('Prever Sistema de Espuma de acordo com o item o item 7.2.2.1.1. da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Prever Sistema de Resfriamento de acordo com o item o item 7.4 da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Prever Sistema de Contenção de acordo com o item 2.3.7. da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
        mostrarcurso = st.checkbox('Quero saber mais sobre proteção contra incêndio para líquidos igníferos.')
        if mostrarcurso:
            st.write('Visite: https://www.silmarsendin.com/cursos-on-line-1 ')
#Exigências para Edificações com Tanques.
elif paginaselecionada == 'Tanques em Edificações':
    st.title('Tanques em Edificações')
    st.write('O cenário selecionado é uma Edificação contendo Tanques e as informações a seguir só se aplicam a este cenário.')

    mostrarclasses = st.checkbox('Quero saber como classificar um líquido ignífero.')
    if mostrarclasses:
        from PIL import Image
        image = Image.open('classes.png')
        st.image(image, caption='Classes dos Líquidos Igníferos')
        st.write('PF = Ponto de Fulgor, PV = Pressão de Vapor, e PE = Ponto de Ebulição')

    classeliq = st.selectbox('Qual a Classe do Líquido Armazenado:',['Classe I','Classe IA','Classe IB','Classe IC','Classe II','Classe IIIA','Classe IIIB'])
    volumetanques = st.number_input("Qual o volume total, em litros, armazenado sem isolamento:")
    if volumetanques < 20001 or classeliq == 'Classe IIIB':
        st.write('Não será necessário os sistemas de espuma e resfriamento de acordo com a NBR 17.505 mas pela IT 25/19 deverá ser previsto para IIIB com mais de 20 m3.')
        st.write('Prever Sistema de Extintor de acordo com a Tabela 1.2 da IT 25/19 SP ou Tabela A.11 da NBR 17.505 - Parte 7.')
    elif volumetanques > 20000 or classeliq != 'Classe IIIB':
        mostrarnbr = st.checkbox('Quero saber como proteger o cenário de acordo com a NBR 17.505.')
        if mostrarnbr:
            st.write('Caso haja apenas uma cobertura, sem paredes laterais e e não haja obstruções a dissipação de calor ou a dispersão dos vapores inflamáveis, considerar como Parque de Tanques.')
            st.write('Prever Sistema de Espuma de acordo com o item 8 da NBR 17.505 - Parte 7.')
            st.write('Prever Sistema de Resfriamento de acordo com o item 4.2.2 e item 6 da NBR 17.505 - Parte 7, checar as exceções do item 4.2.1.')
            st.write('Observar o item 7.4. da NBR 17.505 - Parte 2.')
            st.write('Prever Sistema de Contenção de acordo com o item 7.6 da NBR 17.505 - Parte 2.')
            st.write('Observar as demais exigências do item 7 da NBR 17.505 - Parte 2.')
        mostrarit25 = st.checkbox('Quero saber como proteger o cenário de acordo com a IT 25/19 de SP.')
        if mostrarit25:
            st.write('Prever Sistema de Espuma de acordo com o item o item 7.2.2.1.1. da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Prever Sistema de Resfriamento de acordo com o item o item 7.4 da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Prever Sistema de Contenção de acordo com o item 2.3.7. da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
        mostrarcurso = st.checkbox('Quero saber mais sobre proteção contra incêndio para líquidos igníferos.')
        if mostrarcurso:
            st.write('Visite: https://www.silmarsendin.com/cursos-on-line-1 ')

            #Exigências para Fracionados.
elif paginaselecionada == 'Fracionados':
    st.title('Líquidos Fracionados')
    st.write('O cenário selecionado é um armazenamento de líquidos fracionados e as informações a seguir só se aplicam a este cenário.')

    mostrarclasses = st.checkbox('Quero saber como classificar um líquido ignífero.')
    if mostrarclasses:
        from PIL import Image
        image = Image.open('classes.png')
        st.image(image, caption='Classes dos Líquidos Igníferos')
        st.write('PF = Ponto de Fulgor, PV = Pressão de Vapor, e PE = Ponto de Ebulição')

    classeliq = st.selectbox('Qual a Classe do Líquido Armazenado:',['Classe I','Classe IA','Classe IB','Classe IC','Classe II','Classe IIIA','Classe IIIB'])
    volumetanques = st.number_input("Qual o volume total, em litros, armazenado sem isolamento:")
    if volumetanques < 20001 or classeliq == 'Classe IIIB':
        st.write('Não será necessário os sistemas de espuma e resfriamento de acordo com a NBR 17.505 mas pela IT 25/19 deverá ser previsto para IIIB com mais de 20 m3.')
        st.write('Prever Sistema de Extintor de acordo com a Tabela 1.2 da IT 25/19 SP ou Tabela A.11 da NBR 17.505 - Parte 7.')
    elif volumetanques > 20000 or classeliq != 'Classe IIIB':
       
        mostrarit25 = st.checkbox('Quero saber como proteger o cenário de acordo com a IT 25/19 de SP.')
        if mostrarit25:
            st.write('Prever Sistema de Espuma de acordo com a Tabela 4.25 para áreas abertas e 4.27 para áreas fechadas da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Prever Sistema de Resfriamento de acordo com a Tabela 4.26 para áreas abertas e 4.28 para áreas fechadas da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Prever Sistema de Contenção de acordo com o item 4.8 da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            st.write('Caso os volumes armazenados ultrapassem os determinados na Tabela 4.9, prever Sistema de Chuveiros automáticos de acordo com o item 4.20 da Instrução Técnica 25/19 do Corpo de Bombeiros de São Paulo.')
            mostrar49 = st.checkbox('Quero ver a Tabela 4.9.')
            if mostrar49:
                from PIL import Image
                image2 = Image.open('tabela49.png')
                st.image(image2, caption='Tabela 4.9: Quantidades máximas para armazéns de líquidos M-2 sem sistema de chuveiros automáticos')
                

        mostrarcurso = st.checkbox('Quero saber mais sobre proteção contra incêndio para líquidos igníferos.')
        if mostrarcurso:
            st.write('Visite: https://www.silmarsendin.com/cursos-on-line-1 ')