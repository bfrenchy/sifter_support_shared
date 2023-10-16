"""
This module provides tools for uploading vectored data to Pinecone.

Because these functions are likely to be used at the beginning
of the process, and not operationally, we are importing the
accessed libraries within the functions.

This will likely lead to slower work but improved readability and modularity.
"""
import os


def load_document(file):
    import os
    name, extension = os.path.splitext(file)
    try:
        if extension == '.pdf':
            try:
                from langchain.document_loaders import PyPDFLoader
                print(f"Loading {file}...")
                loader = PyPDFLoader(file)
            except Exception:
                print(f"Could not load {file}. Check the path!")
        elif extension == '.docx':
            try:
                from langchain.document_loaders import Docx2txtLoader
                print(f"Loading {file}...")
                loader = Docx2txtLoader(file)
            except Exception:
                print(f"Could not load {file}. Check the path!")
        # Add some more supported doc types such as .csv, .xlsx, databases...
        else:
            print(f"Document format {extension} is not supported!")

        data = loader.load()
        return data
    except Exception as e:
        print(f"Something went wrong: {str(e)}")
        return


def chunk_data(data, chunk_size=256, chunk_overlap=20):
    """
    Splits text data from loaded files into chunks to be embedded.
    """
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                   chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_documents(data)
    return chunks


def print_embedding_cost(texts):
    """
    If only one document needs to be uploaded (e.g. it has been combined),
    calculates the embedding cost before any embedding is done.
    """
    import tiktoken
    enc = tiktoken.encoding_for_model('text-embedding-ada-002')
    total_tokens = sum([len(enc.encode(page.page_content)) for page in texts])
    cost = total_tokens / 1000 * 0.004
    print(f"Total tokens: {total_tokens}")
    print(f"Embedding cost for {texts} in USD: ${cost}")
    return cost


def insert_or_fetch_embeddings(index_name, chunks=False):
    import pinecone
    from langchain.vectorstores import Pinecone
    from langchain.embeddings.openai import OpenAIEmbeddings

    embeddings = OpenAIEmbeddings()

    pinecone.init(api_key=os.environ.get('PINECONE_API_KEY'),
                  environment=os.environ.get('PINECONE_ENV'))

    if index_name in pinecone.list_indexes():
        print(f"Index '{index_name}' already exists: Loading embeddings...")
        vector_store = Pinecone.from_existing_index(index_name, embeddings)
        print("Done")
    else:
        print(f"Creating index '{index_name}' and embeddings...")
        pinecone.create_index(index_name, dimension=1536, metric='cosine')
        vector_store = Pinecone.from_documents(chunks,
                                               embeddings,
                                               index_name=index_name)
        print(f"Documents embedded to {index_name} index!")

    return vector_store
