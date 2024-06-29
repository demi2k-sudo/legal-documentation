import streamlit as st
from dataSources import QueryEngine
from llm import generate_response
from pdf_generator import HtmlToPdf
from template import documentTemplate1
def main():
    
    option = "Upload PDF"
    
    if "engine" not in st.session_state:
        st.session_state.engine = None
    if "dic" not in st.session_state:
        st.session_state.dic = None
    if "sub" not in st.session_state:
        st.session_state.sub = None
    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = None
    if "query" not in st.session_state:
        st.session_state.query = None
    if "response_1" not in st.session_state:
        st.session_state.response_1 = None
    if "response_2" not in st.session_state:
        st.session_state.response_2 = None
    if "response_3" not in st.session_state:
        st.session_state.response_3 = None
    if "response_4" not in st.session_state:
        st.session_state.response_4 = None

    if option == "Google Drive":
        st.subheader("Google Drive Upload")
        link = st.text_input("Enter Google Drive link")
        submit_button = st.button("Submit")
        if submit_button:
            folder_id = link.split("/")[-1]
            st.session_state.engine = QueryEngine("Gdrive", folder_id).get_query_engine()
            st.session_state.uploaded_files = None

    elif option == "Upload PDF":
        st.subheader("File Upload")
        st.session_state.uploaded_files = st.file_uploader("Upload PDF", type="pdf", accept_multiple_files=True)
        upload_button = st.button("Upload")
        if upload_button:
            if st.session_state.uploaded_files:
                names = []
                for i in st.session_state.uploaded_files:
                    bytes_data = i.read()
                    with open(f"data/{i.name}", "wb") as f:
                        f.write(bytes_data)
                    names.append(f"./data/{i.name}")
                st.session_state.engine = QueryEngine("Upload", names).get_query_engine()
                st.success("Files uploaded successfully!")
            else:
                st.warning("No files uploaded")
    
    if st.session_state.engine:
        st.session_state.query = st.text_input("Enter your query")
        submit_button = st.button("Submit Query")
        if submit_button and st.session_state.query:
            st.session_state.response_1 = st.session_state.engine.query(f"""
            User Need: {st.session_state.query}

            Task: Find the document the user needs for his usecase and give an elaborate explanation about the document
            exclude the information about the metadata of the documents and focus on the content
            """)
            # st.write(str(st.session_state.response_1))
            st.session_state.response_2 = st.session_state.engine.query(f"""
            Context: {st.session_state.response_1}
            ------------------------------------------
            Task: Find the Laws that support the context.
            Don't pass the name of the document alone to the query engine but rather provide the elaborate context and possible tweaks to search a wider range of laws.
            If the law doesn't match the exact document try to find if you can fit the law supporting any potential situation of the context.
            You should give me a response at the end of this task
            """)
            # st.write(str(st.session_state.response_2))
            prompt = f"""
            Context: {st.session_state.response_1}
            Supporting Laws: {st.session_state.response_2}
            Task: Draft a legal document with the above contents and leave underscores for the places to be filled by user
            """
            st.session_state.response_3 = generate_response(prompt)
            st.write(str(st.session_state.response_3))
            response_4 = generate_response(f"""
            Frame Questions to ask the user to fill the blanks in the below Document
            Make sure to be elaborate in your questions
            each line of your output must contain a single question

            Document:
            {st.session_state.response_3}
            """)
            st.session_state.response_4 = response_4
            # st.write(response_4)
            questions = response_4.split('\n')
            st.session_state.questions = questions

    if st.session_state.response_4:
        st.subheader("Fill these information : ")
        with st.form(key='template_form'):
            dic = {}
            for i, question in enumerate(st.session_state.questions):
                user_input = st.text_input(f"{question}:", key=f"{question}_input{i}")
                dic[question] = user_input
            sub = st.form_submit_button("Generate PDF")
            if sub:
                st.session_state.dic = dic

    if st.session_state.dic:
        # st.write(st.session_state.dic)
        response_5 = generate_response(f"""
        I have a document with empty spaces and data with the answers to the spaces
        Kindly fill the spaces and return to me the complete document

        Document:
        {st.session_state.response_3}
        Data:
        {st.session_state.dic}
        """)
        # st.write(response_5)
        response_6 = generate_response(f"""
        
        Draft the final document from the previous draft as a html based on the html template given below the draft
        
        Draft: {response_5}
        
        Template: {documentTemplate1}
        """)
        doc = HtmlToPdf(response_6)
        st.write('Click the button below to download your document ')
        st.download_button(label="Download", data=doc, file_name="Document.pdf", mime='application/octet-stream')

if __name__ == "__main__":
    main()
