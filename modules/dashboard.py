import streamlit as st
from modules.quality_score import calculate_quality_score


def display_requirement_card(req_id, requirement, ambiguous_words):

    score = calculate_quality_score(ambiguous_words)

    with st.container(border=True):

        st.markdown(f"## 📌 {req_id}")

        st.markdown("### 📄 Original Requirement")

        st.info(requirement)

        st.markdown("---")

        st.markdown("### ⚠ Ambiguity Analysis")

        if ambiguous_words:

            st.error(
                "Ambiguous Words: " +
                ", ".join(ambiguous_words)
            )

        else:

            st.success(
                "No ambiguity detected."
            )

        st.markdown("---")

        st.markdown("### ⭐ Requirement Quality")

        st.progress(score / 100)

        col1, col2 = st.columns([1, 2])

        with col1:

            st.metric(
                "Score",
                f"{score}/100"
            )

        with col2:

            if score >= 90:

                st.success("🟢 Excellent")

            elif score >= 70:

                st.warning("🟠 Needs Improvement")

            else:

                st.error("🔴 Poor Requirement")

        st.markdown("---")