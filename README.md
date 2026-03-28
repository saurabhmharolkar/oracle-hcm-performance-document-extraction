# Oracle HCM Performance Document Extraction Script

## Overview

This repository contains a Python script developed to extract candidate documents from Oracle HCM Cloud using the UCM SOAP API.

The script reads input data from an Excel file and retrieves document binaries from Oracle UCM, saving them locally with structured naming.

This solution demonstrates automation of document extraction for reporting, migration, and audit purposes.

---

## Technology Stack

* Oracle HCM Cloud
* Oracle UCM (Universal Content Management)
* SOAP Web Services
* Python
* Pandas

---

## Objective

The objective of this script is to automate the extraction of candidate or employee documents from Oracle HCM.

The script:

* Reads document metadata from an Excel file
* Calls Oracle UCM SOAP API
* Retrieves binary document data
* Saves files locally

---

## Input File

The script expects an Excel file containing:

* DM_DOCUMENT_ID
* CANDIDATE_NUMBER
* FILE_NAME

---

## Solution Workflow

1. Read Excel input file using Pandas
2. Loop through each record
3. Construct SOAP request dynamically
4. Call Oracle UCM API (GET_FILE service)
5. Extract binary content from response
6. Save file locally with unique naming

---

## Key Features

* Automated document extraction
* Dynamic SOAP request generation
* Handles duplicate file names
* Saves binary files locally
* Supports multiple document formats
* Uses secure authentication (Basic Auth)

---

## Oracle API Used

The script uses Oracle UCM SOAP service:

GET_FILE

to retrieve document binary content.

---

## Repository Structure

```id="h4hz3n"
oracle-hcm-performance-document-extraction
│
├── README.md
└── performance_document_extraction.py
```

---

## Configuration

Update the following before running:

### Service URL

```python
service_url = 'https://your-instance.oraclecloud.com/idcws/GenericSoapPort'
```

### Credentials

```python
username = 'Your Username'
password = 'Your password'
```

### Input File Path

```python
df = pd.read_excel('input.xlsx')
```

### Output Directory

```python
output_path = './downloads/'
```

---

## Security Note

* Do not store real credentials in the script
* Use environment variables or secure vaults in production

---

## Use Cases

* Performance document migration
* Candidate document extraction
* Audit and compliance
* Data archival

---

## Learning Outcomes

This implementation demonstrates:

* Oracle HCM UCM integration
* SOAP API handling in Python
* Binary data processing
* Automation using Python scripts
* File handling and naming logic

---

## Author

Saurabh Mharolkar
Oracle HCM Developer

---

## License

This project is licensed under the MIT License.
