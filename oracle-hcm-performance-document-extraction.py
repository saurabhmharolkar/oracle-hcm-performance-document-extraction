import requests
import os
import pandas as pd

# ==============================
# Configuration (Update Before Use)
# ==============================

# Oracle UCM SOAP Endpoint
SERVICE_URL = "https://your-instance.oraclecloud.com/idcws/GenericSoapPort"

# Credentials (Use environment variables in real scenarios)
USERNAME = "your_username"
PASSWORD = "your_password"

# Input Excel File
INPUT_FILE = "input.xlsx"

# Output Directory
OUTPUT_DIR = "./downloads"

# ==============================
# Create Output Directory
# ==============================
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================
# Read Input File
# ==============================
df = pd.read_excel(INPUT_FILE)

# ==============================
# Start Session
# ==============================
session = requests.Session()
session.auth = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)

headers = {
    "Content-Type": "text/xml",
    "User-Agent": "http://www.oracle.com/UCM",
    "SOAPAction": "urn:GenericSoap/GenericSoapOperation"
}

# ==============================
# Process Each Record
# ==============================
for index, row in df.iterrows():
    doc_name = row["DM_DOCUMENT_ID"]
    candidate_no = row["CANDIDATE_NUMBER"]
    file_name = row["FILE_NAME"]

    # SOAP Request
    soap_request = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ucm="http://www.oracle.com/UCM">
       <soapenv:Header/>
       <soapenv:Body>
          <ucm:GenericRequest webKey="cs">
             <ucm:Service IdcService="GET_FILE">
                <ucm:Document>
                   <ucm:Field name="RevisionSelectionMethod">Latest</ucm:Field>
                   <ucm:Field name="Rendition">Primary</ucm:Field>
                   <ucm:Field name="dDocName">{doc_name}</ucm:Field>
                </ucm:Document>
             </ucm:Service>
          </ucm:GenericRequest>
       </soapenv:Body>
    </soapenv:Envelope>
    """

    try:
        response = session.post(SERVICE_URL, data=soap_request, headers=headers)

        if response.status_code == 200:
            delimiter = response.content.splitlines()[0]
            sections = response.content.split(delimiter)
            binary = sections[2].split(b"\n")

            # Generate unique file name
            base_file_name = os.path.join(OUTPUT_DIR, f"{candidate_no}_{file_name}")
            output_file_name = base_file_name

            counter = 1
            while os.path.exists(output_file_name):
                output_file_name = os.path.join(
                    OUTPUT_DIR,
                    f"{candidate_no}_{counter}_{file_name}"
                )
                counter += 1

            # Write binary content
            with open(output_file_name, "wb") as file:
                for i in range(5, len(binary)):
                    if i < len(binary) - 2:
                        file.write(binary[i])
                        file.write(b"\n")
                    else:
                        file.write(binary[i][:-1])

            print(f"Saved: {output_file_name}")

        else:
            print(f"Failed for {doc_name}: Status {response.status_code}")

    except Exception as e:
        print(f"Error processing {doc_name}: {str(e)}")