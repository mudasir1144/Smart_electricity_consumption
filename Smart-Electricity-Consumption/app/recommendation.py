"""
recommendation.py

This module contains the rule-based recommendation engine
for the Smart Electricity Consumption Prediction System.
"""


def get_recommendations(
    ac_hours,
    lighting_hours,
    washing_machine_hours,
    solar_panels,
    work_from_home
):
    """
    Generates personalized energy-saving recommendations.

    Parameters:
        ac_hours (float)
        lighting_hours (float)
        washing_machine_hours (float)
        solar_panels (str)
        work_from_home (str)

    Returns:
        recommendations (list)
        estimated_savings (int)
    """

    recommendations = []

    estimated_savings = 0

    # Rule 1
    if ac_hours > 8:
        recommendations.append(
            "❄️ Reduce AC usage by 1–2 hours during hot afternoons."
        )
        estimated_savings += 800

    # Rule 2
    if lighting_hours > 8:
        recommendations.append(
            "💡 Replace conventional bulbs with LED lighting."
        )
        estimated_savings += 400

    # Rule 3
    if washing_machine_hours > 1.5:
        recommendations.append(
            "🧺 Operate the washing machine during off-peak hours."
        )
        estimated_savings += 300

    # Rule 4
    if solar_panels == "No":
        recommendations.append(
            "☀️ Installing solar panels can significantly reduce electricity costs."
        )
        estimated_savings += 2500

    # Rule 5
    if work_from_home == "Yes":
        recommendations.append(
            "💻 Turn off idle electronics while working from home."
        )
        estimated_savings += 200

    # If no recommendation is needed
    if len(recommendations) == 0:
        recommendations.append(
            "🎉 Excellent! Your household is already energy efficient."
        )

    return recommendations, estimated_savings