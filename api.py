# pubmed_papers/api.py
import requests
from typing import List, Dict

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def fetch_pubmed_ids(query: str, retmax: int = 20) -> List[str]:
    url = f"{BASE_URL}esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": retmax}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    return data["esearchresult"]["idlist"]

def fetch_paper_details(ids: List[str]) -> str:
    url = f"{BASE_URL}efetch.fcgi"
    params = {"db": "pubmed", "id": ",".join(ids), "retmode": "xml"}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.text