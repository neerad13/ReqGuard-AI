import streamlit as st

# ----------------------------
# Session State
# ----------------------------

if "test_cases" not in st.session_state:
    st.session_state.test_cases = {}

if "requirements" not in st.session_state:
    st.session_state.requirements = []

if "srs_text" not in st.session_state:
    st.session_state.srs_text = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "uploaded_filename" not in st.session_state:
    st.session_state.uploaded_filename = ""


# ----------------------------
# Imports
# ----------------------------

from modules.pdf_parser import extract_text_from_pdf
from modules.requirement_extractor import extract_requirements
from modules.ambiguity_detector import detect_ambiguity
from modules.dashboard import display_requirement_card
from modules.metrics import calculate_metrics
from modules.llm import rewrite_requirement
from modules.charts import ambiguity_chart, quality_chart
from modules.report_generator import generate_report
from modules.classifier import classify_requirement
from modules.readability import calculate_readability, get_readability_level
from modules.project_health import generate_project_health
from modules.test_case_generator import generate_test_cases
from modules.traceability import generate_rtm
from modules.duplicate_detector import detect_duplicates
from modules.conflict_detector import detect_conflicts
from modules.ieee_compliance import check_ieee_compliance
from modules.rag_engine import (
    retrieve_relevant_requirements,
    build_rag_context
)

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = "gemini-3.6-flash"


# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="ReqGuard AI",
    page_icon="🛡️",
    layout="wide"
)


# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.title("🛡️ ReqGuard AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📄 Upload SRS",
        "💬 Chat with SRS",
        "🧠 AI Rewrite",
        "📊 Dashboard",
        "📑 Reports",
        "⚙ Settings"
    ]
)


# ----------------------------
# Home Page
# ----------------------------

if page == "🏠 Home":

    st.title("🛡️ ReqGuard AI")

    st.subheader(
        "AI Powered Software Requirements Engineering Assistant"
    )

    st.write("---")

    st.markdown("""
### Welcome 👋

ReqGuard AI analyzes Software Requirement Specification (SRS) documents using:

- Natural Language Processing
- Machine Learning
- Large Language Models (Gemini)

---

### Current Features

✅ Upload SRS PDF

✅ Requirement Extraction

✅ Ambiguity Detection

✅ Requirement Quality Analysis

✅ Requirement Classification

✅ Readability Analysis

✅ AI Requirement Rewriting

✅ Analytics Dashboard

✅ Overall SRS Project Health

✅ PDF Report Generation

✅ AI Test Case Generation

✅ Requirement Traceability Matrix

✅ Duplicate Requirement Detection

✅ Inconsistency / Conflict Detection

✅ IEEE SRS Compliance Checker

✅ Chat with SRS using RAG

---

### Current Version

**Review 2 - Phase 2**
""")

    st.success("System Ready")


# ----------------------------
# Upload SRS Page
# ----------------------------

elif page == "📄 Upload SRS":

    st.title("📄 Upload Software Requirement Specification")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        save_path = f"uploads/{uploaded_file.name}"

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("PDF Uploaded Successfully")

        # -------------------------------------------------
        # Store uploaded filename
        # -------------------------------------------------

        if (
            st.session_state.uploaded_filename
            != uploaded_file.name
        ):

            st.session_state.uploaded_filename = (
                uploaded_file.name
            )

            st.session_state.chat_history = []
            st.session_state.test_cases = {}


        # ----------------------------
        # PDF Processing
        # ----------------------------

        pdf_text = extract_text_from_pdf(save_path)

        requirements = extract_requirements(pdf_text)

        # Store SRS for other pages
        st.session_state.srs_text = pdf_text
        st.session_state.requirements = requirements


        # ----------------------------
        # Requirement Analysis
        # ----------------------------

        for req in requirements:

            # Detect ambiguity
            req["ambiguity"] = detect_ambiguity(
                req["text"]
            )

            # Classify requirement
            req["type"] = classify_requirement(
                req["text"]
            )

            # Calculate readability
            req["readability"] = calculate_readability(
                req["text"]
            )

            # Get readability level
            req["readability_level"] = get_readability_level(
                req["readability"]
            )


        # Store analyzed requirements
        st.session_state.requirements = requirements


        # ----------------------------
        # Metrics
        # ----------------------------

        metrics = calculate_metrics(requirements)

        st.write("---")

        st.header("📊 Analytics Dashboard")


        # ----------------------------
        # Metrics Cards
        # ----------------------------

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "📄 Requirements",
                metrics["total"]
            )

        with c2:

            st.metric(
                "⚠ Ambiguous",
                metrics["ambiguous"]
            )

        with c3:

            st.metric(
                "✅ Good",
                metrics["good"]
            )

        with c4:

            st.metric(
                "⭐ Avg Score",
                metrics["average"]
            )


        # ----------------------------
        # Charts
        # ----------------------------

        st.write("")

        left, right = st.columns(2)

        with left:

            ambiguity_chart(
                metrics["good"],
                metrics["ambiguous"]
            )

        with right:

            quality_chart(
                requirements
            )


        # ----------------------------
        # PDF Report
        # ----------------------------

        st.write("---")

        if st.button("📄 Generate PDF Report"):

            report = generate_report(
                requirements,
                metrics
            )

            with open(report, "rb") as pdf:

                st.download_button(
                    "⬇ Download Report",
                    pdf,
                    file_name="ReqGuard_Report.pdf",
                    mime="application/pdf"
                )


        # ----------------------------
        # Overall Project Health
        # ----------------------------

        st.write("---")

        st.header("🩺 Overall Project Health")

        if st.button("🔎 Analyze Overall SRS Health"):

            with st.spinner(
                "🤖 AI is analyzing the complete SRS..."
            ):

                health_report = generate_project_health(
                    requirements
                )

            st.success(
                "✅ Project Health Analysis Complete"
            )

            st.info(health_report)


        # ----------------------------
        # Requirement Analysis
        # ----------------------------

        st.write("---")

        st.header("📋 Requirement Analysis")


        # =================================================
        # INDIVIDUAL REQUIREMENTS
        # =================================================

        for req in requirements:

            # ----------------------------
            # Requirement Card
            # ----------------------------

            display_requirement_card(
                req["id"],
                req["text"],
                req["ambiguity"]
            )


            # ----------------------------
            # Requirement Classification
            # ----------------------------

            st.write(
                f"🏷️ **Requirement Type:** "
                f"{req['type']}"
            )


            # ----------------------------
            # Readability
            # ----------------------------

            st.write(
                f"📖 **Readability Score:** "
                f"{req['readability']}/100"
            )

            st.write(
                f"💡 **Readability Level:** "
                f"{req['readability_level']}"
            )


            # ----------------------------
            # AI Rewrite
            # ----------------------------

            if st.button(
                f"✨ Rewrite {req['id']}",
                key=f"rewrite_{req['id']}"
            ):

                with st.spinner(
                    "🤖 Gemini is analyzing..."
                ):

                    rewritten = rewrite_requirement(
                        req["text"]
                    )

                st.success(
                    "🤖 AI Improved Requirement"
                )

                st.info(rewritten)


            # ----------------------------
            # AI Test Case Generation
            # ----------------------------

            st.write("")

            if st.button(
                "🧪 Generate Test Cases",
                key=f"test_{req['id']}"
            ):

                with st.spinner(
                    "🤖 Generating test cases..."
                ):

                    generated_cases = generate_test_cases(
                        req["text"]
                    )

                # Store generated test cases
                st.session_state.test_cases[
                    req["id"]
                ] = generated_cases


            # ----------------------------
            # Display Stored Test Cases
            # ----------------------------

            if req["id"] in st.session_state.test_cases:

                st.success(
                    "🧪 Generated Test Cases"
                )

                st.info(
                    st.session_state.test_cases[
                        req["id"]
                    ]
                )


            # ----------------------------
            # Separator
            # ----------------------------

            st.write("---")


        # =================================================
        # REQUIREMENT TRACEABILITY MATRIX
        # =================================================

        st.header("🔗 Requirement Traceability Matrix")

        st.write(
            "The RTM connects each software requirement "
            "with its corresponding test cases."
        )

        st.write("")

        if st.button("📊 Generate RTM"):

            rtm = generate_rtm(
                requirements,
                st.session_state.test_cases
            )

            st.success(
                "✅ Requirement Traceability Matrix Generated"
            )

            st.dataframe(
                rtm,
                use_container_width=True,
                hide_index=True
            )


        # =================================================
        # DUPLICATE REQUIREMENT DETECTION
        # =================================================

        st.write("---")

        st.header("🔍 Duplicate Requirement Detection")

        st.write(
            "ReqGuard AI compares requirements using "
            "TF-IDF and cosine similarity to identify "
            "potentially duplicate requirements."
        )

        st.write("")

        if st.button("🔎 Detect Duplicate Requirements"):

            with st.spinner(
                "🔍 Comparing requirements..."
            ):

                duplicates = detect_duplicates(
                    requirements
                )


            # ----------------------------
            # Display Results
            # ----------------------------

            if duplicates:

                st.warning(
                    f"⚠️ {len(duplicates)} "
                    "possible duplicate pair(s) detected."
                )

                for duplicate in duplicates:

                    st.error(
                        f"⚠️ **Possible Duplicate**\n\n"
                        f"{duplicate['requirement_1']} ↔ "
                        f"{duplicate['requirement_2']}\n\n"
                        f"Similarity: "
                        f"{duplicate['similarity']}%"
                    )

            else:

                st.success(
                    "✅ No potential duplicate "
                    "requirements detected."
                )


        # =================================================
        # INCONSISTENCY / CONFLICT DETECTION
        # =================================================

        st.write("---")

        st.header("⚔️ Inconsistency / Conflict Detection")

        st.write(
            "ReqGuard AI compares requirements to identify "
            "potentially conflicting constraints and "
            "contradictory statements."
        )

        st.write("")

        if st.button("⚔️ Detect Requirement Conflicts"):

            with st.spinner(
                "⚔️ Analyzing requirements for conflicts..."
            ):

                conflicts = detect_conflicts(
                    requirements
                )


            # ----------------------------
            # Display Results
            # ----------------------------

            if conflicts:

                st.warning(
                    f"⚠️ {len(conflicts)} "
                    "potential conflict(s) detected."
                )

                for conflict in conflicts:

                    st.error(
                        f"⚔️ **Potential Conflict**\n\n"
                        f"{conflict['requirement_1']} ↔ "
                        f"{conflict['requirement_2']}\n\n"
                        f"**Reason:** "
                        f"{conflict['reason']}"
                    )

            else:

                st.success(
                    "✅ No potential requirement "
                    "conflicts detected."
                )


        # =================================================
        # IEEE SRS COMPLIANCE CHECKER
        # =================================================

        st.write("---")

        st.header("📋 IEEE SRS Compliance Checker")

        st.write(
            "ReqGuard AI checks whether important "
            "IEEE-style SRS sections are present "
            "in the uploaded document."
        )

        st.write("")

        if st.button("📋 Check IEEE SRS Compliance"):

            with st.spinner(
                "📋 Checking SRS structure..."
            ):

                compliance = check_ieee_compliance(
                    pdf_text
                )


            # ----------------------------
            # Compliance Score
            # ----------------------------

            st.metric(
                "📊 IEEE-Style Compliance Score",
                f"{compliance['score']}%"
            )

            st.write(
                f"**Compliance Level:** "
                f"{compliance['level']}"
            )

            st.write("")


            # ----------------------------
            # Section Results
            # ----------------------------

            st.subheader(
                "📑 SRS Section Analysis"
            )

            for section, status in compliance[
                "sections"
            ].items():

                if status == "Present":

                    st.success(
                        f"✅ {section} — Present"
                    )

                else:

                    st.warning(
                        f"⚠️ {section} — Missing"
                    )


            st.info(
                "ℹ️ This checker evaluates the presence "
                "of important IEEE-style SRS sections. "
                "It is a structural analysis and does not "
                "represent formal certification."
            )


# =================================================
# CHAT WITH SRS PAGE
# =================================================

elif page == "💬 Chat with SRS":

    st.title("💬 Chat with your SRS")

    st.write(
        "Ask questions about your uploaded Software "
        "Requirement Specification."
    )

    st.info(
        "🤖 ReqGuard AI retrieves relevant requirements "
        "from your SRS and uses them as context for Gemini."
    )


    # -------------------------------------------------
    # Check whether an SRS has been uploaded
    # -------------------------------------------------

    if not st.session_state.requirements:

        st.warning(
            "⚠️ Please upload an SRS from the "
            "'📄 Upload SRS' page first."
        )

    else:

        st.success(
            f"📄 SRS loaded — "
            f"{len(st.session_state.requirements)} "
            "requirements available."
        )


        # -------------------------------------------------
        # Display Previous Chat
        # -------------------------------------------------

        for message in st.session_state.chat_history:

            if message["role"] == "user":

                with st.chat_message("user"):

                    st.write(
                        message["content"]
                    )

            else:

                with st.chat_message("assistant"):

                    st.write(
                        message["content"]
                    )


        # -------------------------------------------------
        # Chat Input
        # -------------------------------------------------

        question = st.chat_input(
            "Ask something about your SRS..."
        )


        if question:

            # ----------------------------
            # Display User Question
            # ----------------------------

            with st.chat_message("user"):

                st.write(question)


            # Store user message
            st.session_state.chat_history.append({
                "role": "user",
                "content": question
            })


            # ----------------------------
            # Retrieve Relevant Requirements
            # ----------------------------

            with st.spinner(
                "🔎 Searching your SRS..."
            ):

                relevant_requirements = (
                    retrieve_relevant_requirements(
                        question,
                        st.session_state.requirements,
                        top_k=3
                    )
                )


            # ----------------------------
            # Build Context
            # ----------------------------

            context = build_rag_context(
                relevant_requirements
            )


            # ----------------------------
            # Gemini Prompt
            # ----------------------------

            prompt = f"""
You are ReqGuard AI, a Software Requirements
Engineering assistant.

Answer the user's question using ONLY the
retrieved information from the uploaded SRS.

If the answer cannot be found in the retrieved
requirements, clearly say that the information
is not available in the retrieved SRS context.

Do not invent requirements.

User Question:
{question}

Retrieved SRS Context:
{context}

Give a clear and concise answer.

Mention the relevant requirement IDs when possible.
"""


            # ----------------------------
            # Generate Answer
            # ----------------------------

            with st.spinner(
                "🤖 Generating answer..."
            ):

                try:

                    response = client.models.generate_content(
                        model=MODEL_NAME,
                        contents=prompt
                    )

                    answer = response.text

                except Exception as e:

                    answer = (
                        "⚠️ Unable to generate an answer "
                        "at the moment.\n\n"
                        f"Error: {str(e)}"
                    )


            # ----------------------------
            # Display Answer
            # ----------------------------

            with st.chat_message("assistant"):

                st.write(answer)


            # Store assistant response
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": answer
            })


            # -------------------------------------------------
            # Show Retrieved Requirements
            # -------------------------------------------------

            if relevant_requirements:

                with st.expander(
                    "🔎 View Retrieved SRS Context"
                ):

                    for req in relevant_requirements:

                        st.write(
                            f"**{req['id']}** "
                            f"(Similarity: "
                            f"{req['similarity']}%)"
                        )

                        st.write(
                            req["text"]
                        )

                        st.write("---")


        # -------------------------------------------------
        # Clear Chat
        # -------------------------------------------------

        if st.session_state.chat_history:

            if st.button("🗑️ Clear Chat"):

                st.session_state.chat_history = []

                st.rerun()


# ----------------------------
# AI Rewrite Page
# ----------------------------

elif page == "🧠 AI Rewrite":

    st.title("🧠 AI Requirement Rewrite")

    st.info(
        "Upload an SRS from the Upload page "
        "and use the Rewrite button."
    )


# ----------------------------
# Dashboard Page
# ----------------------------

elif page == "📊 Dashboard":

    st.title("📊 Dashboard")

    st.info(
        "Analytics are shown after uploading "
        "an SRS document."
    )


# ----------------------------
# Reports Page
# ----------------------------

elif page == "📑 Reports":

    st.title("📑 Reports")

    st.info(
        "Generate and download the PDF report "
        "from the Upload SRS page."
    )


# ----------------------------
# Settings Page
# ----------------------------

elif page == "⚙ Settings":

    st.title("⚙ Settings")

    st.info(
        "More settings coming soon."
    )