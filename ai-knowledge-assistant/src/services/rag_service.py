from src.chains.rag_chain import rag_chain


async def ask_question(question):

    return await rag_chain.ainvoke(
        question
    )