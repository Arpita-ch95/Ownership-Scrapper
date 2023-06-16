import requests
from bs4 import BeautifulSoup
from typing import List, Tuple

from sec import SECSession


def extract_headers(row) -> List[str]:
    headers = []
    for td_element in row.find_all('td'):
        p_elements = td_element.find_all('p')
        if p_elements:
            header_text = ' '.join(p.text.strip() for p in p_elements)
            headers.append(header_text.replace('\xa0', ' '))  # remove non-breaking space
    return headers


def extract_ownership_data(rows) -> List[List[str]]:
    ownership_data = []
    for row in rows[1:]:  # Exclude the header row
        data = [cell.get_text(strip=True) for cell in row.select('td') if 'solid' in cell.get('style', '')]
        ownership_data.append(data)
    return ownership_data


def extract_ownership_info(content) -> Tuple[List[str], List[List[str]]]:
    soup = BeautifulSoup(content, 'html.parser')

    target_heading = None
    for heading in soup.find_all('h2'):
        if heading.find('a', string=lambda t: t and 'Security Ownership of Certain Beneficial Owners and Management' in t):
            target_heading = heading
            break

    if not target_heading:
        raise ValueError("No target heading found")

    ownership_table = target_heading.find_next('table')
    rows = ownership_table.select('tr')

    headers = extract_headers(rows[0])
    ownership_data = extract_ownership_data(rows)

    return headers, ownership_data


if __name__ == '__main__':
    sec = SECSession(**{
        "dateRange": "custom", "category": "custom",
        "startdt": "2023-01-01", "enddt": "2023-06-16",
        "forms": ["DEF 14A"]
    })
    filing_data = sec.get_filing_url(company_name="Apple Inc", company_ticker="AAPL")
    for ticker, filings in filing_data.items():
        for year, filing_url in filings.items():
            try:
                response = sec.get_filing(filing_url)
                response.raise_for_status()  # Raises HTTPError if status code is not 2xx
                print(extract_ownership_info(response.text))
            except requests.exceptions.HTTPError as e:
                print(f"Failed to retrieve filing: {filing_url}. HTTP error: {e}")
            except requests.exceptions.RequestException as e:
                print(f"Error occurred during request: {e}")
            except ValueError as e:
                print(f"ValueError: {e}")
