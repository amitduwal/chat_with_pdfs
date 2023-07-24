
# Chat with Multiple PDFs

This is a Streamlit web application that allows users to chat with a language model about the contents of multiple PDF documents. The application uses various natural language processing techniques to extract text from the uploaded PDFs, split the text into chunks, and then perform conversational retrieval based on user input.

## Getting Started

To run this application, you need to have Python installed on your system. You can follow these steps to get started:

1. Clone the repository to your local machine.
2. Create a virtual environment (optional but recommended).
3. Install the required dependencies using `pip install -r requirements.txt`.

## Running the Application

Once you have set up the environment and installed the dependencies, you can run the application using the following command:

```
streamlit run app.py
```

This will launch the Streamlit app on your local server, and you can access it through your web browser.

## Usage

1. Upload PDF Documents: Use the "Your documents" section in the sidebar to upload one or more PDF documents by clicking on the "Upload your PDFs here and click on 'Process'" button.

2. Ask a Question: In the main section of the app, there is a text input box labeled "Ask a question about your documents." Enter your question related to the contents of the uploaded PDFs and click Enter.

3. View Responses: The application will display a conversation between you and the language model. Your question and the model's response will be alternately displayed in the chat interface.

## How It Works

1. PDF Text Extraction: The uploaded PDF documents are processed to extract the text content from each page using the PyPDF2 library.

2. Text Chunking: The extracted text is split into smaller chunks to improve performance during embedding and retrieval. The CharacterTextSplitter class is used for this purpose.

3. Language Model and Embeddings: The application uses the HuggingFaceInstructEmbeddings class to generate embeddings for the text chunks. The embeddings are then stored using the FAISS library, which allows for efficient similarity search.

4. Conversational Retrieval: The language model (HuggingFaceHub) is used in combination with the vector store to create a ConversationalRetrievalChain. This chain enables the language model to respond contextually to user questions based on the information stored in the vector store.

## Limitations

- The application relies on the Hugging Face ecosystem for language models and embeddings. Changes in the availability or compatibility of these resources may affect the app's functionality.
- The performance of the chat may depend on the size and complexity of the uploaded PDF documents.

## About

This application was created as a demo project to showcase how natural language processing and conversational retrieval can be used in combination with PDF text extraction. It is not intended for production use and is provided as-is without any warranties or support.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

This project was built using various open-source libraries and tools. Special thanks to the creators of Streamlit, Hugging Face, PyPDF2, and FAISS for their contributions to the open-source community.
