import typer
import pandas as pd
from .api import fetch_pubmed_ids, fetch_paper_details
from .filters import extract_company_and_authors

app = typer.Typer()

def main():
    typer.run(get_papers_list)

def get_papers_list(query: str, file: str = typer.Option(None, "--file", "-f"), debug: bool = typer.Option(False, "--debug", "-d")):
    ids = fetch_pubmed_ids(query)
    if debug:
        typer.echo(f"Fetched IDs: {ids}")

    if not ids:
        typer.echo("No results found.")
        raise typer.Exit()

    xml_data = fetch_paper_details(ids)
    results = extract_company_and_authors(xml_data)

    if not results:
        typer.echo("No papers with non-academic authors found.")
        raise typer.Exit()

    df = pd.DataFrame(results)
    if file:
        df.to_csv(file, index=False)
        typer.echo(f"Saved results to {file}")
    else:
        typer.echo(df)

if __name__ == "__main__":
    main()
