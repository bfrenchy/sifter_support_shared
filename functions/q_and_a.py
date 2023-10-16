from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from config.llm_config import llm_model, search_type, chain_type
from config.llm_config import temperature, k


def ask_and_get_answer(vector_store, q, filter_args=None,
                       model=llm_model, k=k, temperature=temperature,
                       search_type=search_type, chain_type=chain_type):
    """
    Allows the user to ask a contextual question and get an answer back.

    -- Parameters --
    * vector_store: the Pinecone vector embeddings, called
                  by insert_or_fetch_embeddings()
    * q: the question being asked
    * filter_args: a bit trickier. This is flexible to any metadata arguments,
            but require a knowledge of the metadata fields in question.
            This must also be in json format, so as an example:
            We want to filter by Garmin product name.
            1) Set the variable: filter = {'product_name': {'$eq': product}}
            2) call the variable: filter_args=filter
            `filter_args={'product_name': {'$eq': product_name}}`

            Or if we want to filter by multiple metadata fields:
            1) filter = {'product_name': {'$eq': product},
                        'product_id': {'$eq': product_id}}
            2) call the variable: filter_args=filter

                In general, it's recommended to clarify the arg outside.
    * k: Uses the k most similar in the similarity search. Defaults to 5.
    * model: the LLM model being used. Default set in config/llm_config.
    * temperature: the LLM temperature, default set in config/llm_config.
    * search_type: default set in config/llm_config, finding commonalities.
    * chain_type: default set in config/llm_config, which is all of the text.
    """
    llm = ChatOpenAI(model=model, temperature=temperature)
    if filter_args is not None:
        retriever = vector_store.as_retriever(
            search_type=search_type,
            search_kwargs={'k': k,
                           'filter': filter_args})
    else:
        retriever = vector_store.as_retriever(
            search_type=search_type,
            search_kwargs={'k': k})

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type=chain_type,  # stuff is the default and uses all of the text
        retriever=retriever)
    answer = chain.run(q)
    return answer


def ask_with_memory(vector_store, q, filter_args=None,
                    chat_history=[], model=llm_model,
                    k=k, temperature=temperature,
                    search_type=search_type):
    """
    Allows the user to ask contexual questions with in-conversation memory.

    -- Parameters --
    * vector_store: the Pinecone vector embeddings, called
                  by insert_or_fetch_embeddings()
    * q: the question being asked
    * chat_history: a list for the chats. Defaults as an empty list.
    * filter_args: a bit trickier. This is flexible to any metadata arguments,
            but require a knowledge of the metadata fields in question.
            This must also be in json format, so as an example:
            We want to filter by Garmin product name.
            1) Set the variable: filter = {'product_name': {'$eq': product}}
            2) call the variable: filter_args=filter
            `filter_args={'product_name': {'$eq': product_name}}`

            Or if we want to filter by multiple metadata fields:
            1) filter = {'product_name': {'$eq': product},
                        'product_id': {'$eq': product_id}}
            2) call the variable: filter_args=filter
    * k: Uses the k most similar in the similarity search. Defaults to 5.
    * model: the LLM model being used. Default set in config/llm_config.
    * temperature: the LLM temperature, default set in config/llm_config.
    * search_type: default set in config/llm_config, finding commonalities.

    """
    llm = ChatOpenAI(temperature=temperature, model=model)

    if filter_args is not None:
        retriever = vector_store.as_retriever(
            search_type=search_type,
            search_kwargs={'k': k,
                           'filter': filter_args})
    else:
        retriever = vector_store.as_retriever(
            search_type=search_type,
            search_kwargs={'k': k})

    crc = ConversationalRetrievalChain.from_llm(llm, retriever)
    result = crc({'question': q, 'chat_history': chat_history})
    chat_history.append((q, result['answer']))

    return result, chat_history
