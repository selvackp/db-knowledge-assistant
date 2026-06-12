import streamlit as st

from src.pdf_loader import extract_text
from src.chunker import chunk_text
from src.embedder import generate_embeddings

from src.memorydb_store import (
    store_chunk,
    document_exists,
    register_document,
    get_documents
)

from src.search import search_documents

st.set_page_config(
    page_title="Database Operations Knowledge Assistant",
    layout="wide"
)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("📚 Knowledge Assistant")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        if document_exists(uploaded_file.name):

            st.warning(
                f"⚠️ {uploaded_file.name} already indexed"
            )

        else:

            with st.spinner(
                "Processing PDF..."
            ):

                text = extract_text(
                    uploaded_file
                )

                st.info(
                    f"Document Size: {len(text):,} characters"
                )

                chunks = chunk_text(
                    text
                )

                st.info(
                    f"Total Chunks: {len(chunks):,}"
                )

                total_chunks = len(
                    chunks
                )

                progress = st.progress(0)

                stored_count = 0

                BATCH_SIZE = 10

                for start in range(
                    0,
                    total_chunks,
                    BATCH_SIZE
                ):

                    batch_chunks = chunks[
                        start:start + BATCH_SIZE
                    ]

                    embeddings = (
                        generate_embeddings(
                            batch_chunks
                        )
                    )

                    for idx, (
                        chunk,
                        embedding
                    ) in enumerate(
                        zip(
                            batch_chunks,
                            embeddings
                        )
                    ):

                        actual_idx = (
                            start + idx
                        )

                        store_chunk(
                            uploaded_file.name,
                            actual_idx,
                            chunk,
                            embedding
                        )

                        stored_count += 1

                    progress.progress(
                        min(
                            (start + BATCH_SIZE)
                            / total_chunks,
                            1.0
                        )
                    )

                register_document(
                    uploaded_file.name
                )

            st.success(
                f"✅ {uploaded_file.name} indexed successfully"
            )

            st.success(
                f"Stored {stored_count:,} chunks"
            )

    st.markdown("---")

    st.subheader(
        "Indexed Documents"
    )

    try:

        docs = get_documents()

        if docs:

            for doc in docs:

                st.write(
                    f"📄 {doc}"
                )

        else:

            st.info(
                "No documents indexed"
            )

    except Exception as e:

        st.error(
            f"Unable to load document list: {e}"
        )

# ==================================================
# MAIN PAGE
# ==================================================

st.title(
    "🗄️ Database Operations Knowledge Assistant"
)

st.write(
    "Search PostgreSQL, MySQL, SQL Server and operational runbooks."
)

question = st.text_input(
    "Ask a Question",
    placeholder="How do I restore PostgreSQL?"
)

if st.button("Search"):

    if not question:

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Searching..."
        ):

            results = (
                search_documents(
                    question
                )
            )

        st.subheader(
            "Results"
        )

        if len(results) <= 1:

            st.warning(
                "No matching documents found."
            )

        else:

            for i in range(
                1,
                len(results),
                2
            ):

                try:

                    fields = (
                        results[i + 1]
                    )

                    document = (
                        fields[1]
                    )

                    chunk = (
                        fields[3]
                    )

                    if isinstance(
                        document,
                        bytes
                    ):
                        document = (
                            document.decode()
                        )

                    if isinstance(
                        chunk,
                        bytes
                    ):
                        chunk = (
                            chunk.decode()
                        )

                    with st.expander(
                        f"📄 {document}",
                        expanded=(i == 1)
                    ):

                        st.write(
                            chunk
                        )

                except Exception as e:

                    st.error(
                        f"Result parsing error: {e}"
                    )
