# pubmed_papers/filters.py
import xml.etree.ElementTree as ET
from typing import List, Dict

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "college", "institute", "school", "hospital", "centre"]
    return not any(word in affiliation.lower() for word in academic_keywords)

def extract_company_and_authors(xml_data: str) -> List[Dict]:
    root = ET.fromstring(xml_data)
    results = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or ""

        non_acad_authors = []
        company_affiliations = []
        email = ""

        for author in article.findall(".//Author"):
            affiliation = author.findtext(".//AffiliationInfo/Affiliation") or ""
            if is_non_academic(affiliation):
                last_name = author.findtext("LastName") or ""
                fore_name = author.findtext("ForeName") or ""
                full_name = f"{fore_name} {last_name}".strip()
                non_acad_authors.append(full_name)
                company_affiliations.append(affiliation)

            if "@" in affiliation and not email:
                email = affiliation.split()[-1]

        if non_acad_authors:
            results.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": ", ".join(non_acad_authors),
                "Company Affiliation(s)": ", ".join(company_affiliations),
                "Corresponding Author Email": email
            })

    return results