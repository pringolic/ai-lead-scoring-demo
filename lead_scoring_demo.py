import pandas as pd
leads_data = [
    {"Name": "John Miller", "Title": "Director of Toxicology", "Company": "BioTechX", "Funding_Stage": "Series B", "Location": "Boston", "Published_Relevant_Paper": True},
    {"Name": "Mark Johnson", "Title": "Head of Safety Assessment", "Company": "PharmaOne", "Funding_Stage": "Series A", "Location": "Cambridge", "Published_Relevant_Paper": True},
    {"Name": "Sarah Lee", "Title": "Senior Toxicologist", "Company": "LiverGen", "Funding_Stage": "Series B", "Location": "UK", "Published_Relevant_Paper": True},
    {"Name": "David Brown", "Title": "Director of Preclinical Safety", "Company": "OncoLabs", "Funding_Stage": "Series A", "Location": "Boston", "Published_Relevant_Paper": False},
    {"Name": "Emily Davis", "Title": "Research Scientist", "Company": "HealthCore", "Funding_Stage": "Seed", "Location": "UK", "Published_Relevant_Paper": False},
    {"Name": "Anna Smith", "Title": "Junior Scientist", "Company": "SmallLab", "Funding_Stage": "No Funding", "Location": "Texas", "Published_Relevant_Paper": False},
    {"Name": "Michael Chen", "Title": "Director of Drug Safety", "Company": "NeoPharma", "Funding_Stage": "Series B", "Location": "San Francisco", "Published_Relevant_Paper": True},
    {"Name": "Rachel Green", "Title": "Head of Toxicology", "Company": "BioNova", "Funding_Stage": "Series A", "Location": "Basel", "Published_Relevant_Paper": True},
    {"Name": "James Wilson", "Title": "Senior Scientist", "Company": "MedCore", "Funding_Stage": "Seed", "Location": "New York", "Published_Relevant_Paper": False},
    {"Name": "Priya Nair", "Title": "Director of Safety Sciences", "Company": "GenLab", "Funding_Stage": "Series B", "Location": "Cambridge", "Published_Relevant_Paper": True},
    {"Name": "Robert King", "Title": "Principal Scientist", "Company": "CellTech", "Funding_Stage": "Series A", "Location": "UK", "Published_Relevant_Paper": False},
    {"Name": "Laura Martinez", "Title": "Head of Preclinical Research", "Company": "TheraWorks", "Funding_Stage": "Series B", "Location": "Boston", "Published_Relevant_Paper": True},
    {"Name": "Kevin Patel", "Title": "Scientist", "Company": "EarlyBio", "Funding_Stage": "No Funding", "Location": "India", "Published_Relevant_Paper": False},
    {"Name": "Sophia Adams", "Title": "Director of Investigative Toxicology", "Company": "HepatoTech", "Funding_Stage": "Series A", "Location": "San Diego", "Published_Relevant_Paper": True},
    {"Name": "Daniel Moore", "Title": "Research Associate", "Company": "BioStart", "Funding_Stage": "Seed", "Location": "Canada", "Published_Relevant_Paper": False}
]



df = pd.DataFrame(leads_data)

def calculate_propensity_score(row) -> int:
    score = 0

    if "Director" in row["Title"] or "Head" in row["Title"]:
        score += 30

    if row["Funding_Stage"] in ["Series A", "Series B"]:
        score += 20

    if row["Published_Relevant_Paper"]:
        score += 40

    if row["Location"] in ["Boston", "Cambridge", "UK"]:
        score += 10

    return min(score, 100)

df["Propensity_Score"] = df.apply(calculate_propensity_score, axis=1)

df = df.sort_values(by="Propensity_Score", ascending=False)
df["Rank"] = range(1, len(df) + 1)

df = df[
    [
        "Rank",
        "Name",
        "Title",
        "Company",
        "Funding_Stage",
        "Location",
        "Published_Relevant_Paper",
        "Propensity_Score"
    ]
]

print("\n", df.to_string(index=False), "\n")


df.to_csv("lead_scoring_output.csv", index=False)
