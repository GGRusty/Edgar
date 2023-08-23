import pandas as pd
import requests
import xml.etree.ElementTree as ET
import pprint

# this is a good idea and got me on the path of parsing the xml but this is not reliable in the long term as the data is not always in the same place
def parse_xml_from_content(xml_content):
    root = ET.fromstring(xml_content)

    # Helper function to create a pandas Series from the XML data
    def create_series(context_id, end_date):
        data_dict = {}
        for element in root.findall(".//*"):
            context_ref = element.attrib.get("contextRef", None)
            unit_ref = element.attrib.get("unitRef", None)
            tag_name = element.tag.split("}")[-1]  # Remove the namespace part

            if context_ref == context_id and unit_ref and element.text:
                key = f"{tag_name}-{unit_ref}"
                value = element.text  # Assuming the value is an integer
                data_dict[key] = value

        series_name = end_date  # Set the series name as the end date
        return pd.Series(data_dict, name=series_name)

    # Helper function to find the context IDs
    def find_context_ids():
        statements_id = None
        end_date_of_first_context = None
        balance_sheet_id = None

        for context in root.findall(".//{http://www.xbrl.org/2003/instance}context"):
            context_id = context.attrib['id']
            start_date_element = context.find(".//{http://www.xbrl.org/2003/instance}startDate")
            end_date_element = context.find(".//{http://www.xbrl.org/2003/instance}endDate")

            if start_date_element is not None and end_date_element is not None and statements_id is None:
                statements_id = context_id
                end_date_of_first_context = end_date_element.text

        for context in root.findall(".//{http://www.xbrl.org/2003/instance}context"):
            instant_element = context.find(".//{http://www.xbrl.org/2003/instance}instant")
            if instant_element is not None and instant_element.text == end_date_of_first_context:
                balance_sheet_id = context.attrib['id']
                break

        return statements_id, balance_sheet_id, end_date_of_first_context

    statements_id, balance_sheet_id, end_date_of_first_context = find_context_ids()
    if not statements_id or not balance_sheet_id:
        print("Unable to find required context IDs.")
        return None, None
    balance_sheet_series = create_series(balance_sheet_id, end_date_of_first_context)
    statements_series = create_series(statements_id, end_date_of_first_context)

    return balance_sheet_series, statements_series


def get_xbrl_links(cik):
    # Define the URL and headers
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    # Make the request
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Failed to get data. HTTP status code: {response.status_code}")
    # Extract data and filter for 10-K and 10-Q forms
    data = pd.DataFrame(data["filings"]["recent"]) # this is where we need to start after running get company filings for ticker from submission data function
    data10k = data[data["form"] == "10-K"].head(4)
    data10q = data[data["form"] == "10-Q"].head(12)

    # Function to construct the URL
    def construct_url(row):
        base_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/"
        accession_number = row["accessionNumber"].replace("-", "")
        primary_document = row["primaryDocument"].replace(".", "_") + ".xml"
        return base_url + accession_number + "/" + primary_document

    # Construct the URLs for "10-K" and "10-Q" forms
    urls_10k = data10k.apply(construct_url, axis=1).tolist()
    urls_10q = data10q.apply(construct_url, axis=1).tolist()

    return urls_10k, urls_10q


# # Example usage:]
# headers = {"User-Agent": "russ@sunriseanalysis.com"}
# cik = "0000719955"
# url10k, url10q = get_xbrl_links(cik)
# first_10kurl = url10k[0]
# first_10qurl = url10q[0]
# response = requests.get(first_10qurl, headers=headers)
# xml_content = response.content
# balance_sheet_series, statements_series = parse_xml_from_content(xml_content)
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(balance_sheet_series)