import plotly.express as px
import streamlit as st


def ambiguity_chart(good, ambiguous):

    labels = [
        "Good",
        "Ambiguous"
    ]

    values = [
        good,
        ambiguous
    ]

    fig = px.pie(
        names=labels,
        values=values,
        title="Requirement Quality Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def quality_chart(requirements):

    ids = []

    scores = []

    for req in requirements:

        ids.append(req["id"])

        ambiguous = len(req.get("ambiguity", []))

        score = 100 - ambiguous * 10

        if score < 0:
            score = 0

        scores.append(score)

    fig = px.bar(

        x=ids,

        y=scores,

        labels={
            "x": "Requirement",
            "y": "Quality Score"
        },

        title="Requirement Quality Scores"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )