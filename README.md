# GOOGLE-DRIVE-API-WEB-SCRAPPER-PROJECT

The GOOGLE-DRIVE-API-WEB-SCRAPPER-PROJECT is a Python script designed to extract information from a text file containing book links, utilize Selenium for web scraping and downloading PDF files, process the data, and manage files using JSON and Google Drive through the Google Drive API.

## Objectives

1. **Data Processing and JSON Storage**:
   - **Objective**: Extract information from a text file containing book links, filter and process the data using custom functions (`filter_`, `convertAllToDict`, `convert_to_dict`), and store the structured data in a JSON file (`RudolfSteinerData.json`).

2. **Web Scraping and File Download**:
   - **Objective**: Utilize Selenium for web scraping to interact with a website, specifically downloading PDF files linked in the processed data. The downloaded files are stored in a specified local directory (`download_loc`).

3. **Update Check and JSON Update**:
   - **Objective**: Check if the existing JSON file (`RudolfSteinerData.json`) is up to date by comparing it with the newly processed data. If there are updates, overwrite the existing JSON file with the updated data.

4. **Google Drive Operations (CRUD)**:
   - **Objective**: Integrate the Google Drive API to perform CRUD (Create, Read, Update, Delete) operations on files and folders. 
     - **Create (Upload)**: Implement functionality to upload files to Google Drive using the `upload_item` function.
     - **Read (Download)**: Develop a mechanism to read files from Google Drive, including options to specify the download path using the `read_item` function.
     - **Update/Edit**: Utilize the `update_item` function to modify files on Google Drive, allowing updates of file content, name, and placement in specific folders.
     - **Delete**: Implement the `delete_item` function to delete files from Google Drive, providing flexibility in file removal.

This project aims to seamlessly combine web scraping with Selenium and efficient file management using the Google Drive API, offering a comprehensive solution for organizing and storing downloaded files.


## Files

### `main.py`

The main script orchestrating the project's objectives, coordinating operations from other modules.

### `web_ops.py`

Includes functions related to web operations, such as setting up a Selenium driver and downloading files.

### `file_ops.py`

Provides various file operations, including reading files, filtering data, converting to JSON, and handling filenames.

### `g_drive_ops.py`

Deals with operations related to Google Drive, such as setting up credentials, uploading, reading, updating, and deleting files.

## Setup

### Prerequisites

- Python 3.x
- Additional dependencies mentioned in `requirements.txt`

### Installation

```bash
pip install -r requirements.txt
```

# Usage

Ensure you have set up the required environment variables in the .env file.

Run the following command to execute the main functionality:

```bash
python main.py
```

## Environment Variables

- `firefox_binary`: Path to the Firefox binary.
- `gecko_driver`: Path to the GeckoDriver executable.

## Google Drive Operations

Place your credentials.json in the Credentials folder.
The token.json should also be in the root directory.

### Google Drive Metadata

You can run the get_metadata() function t0 fetch metadata about files and folders in your Google Drive:

```python
from g_drive_ops import get_metadata
get_metadata()
```

## Google Drive CRUD Operations

### Upload a file to Google Drive:

```python
from g_drive_ops import upload_item
upload_item("file_name.txt", "path/to/file.txt", folder_id="optional_folder_id")
```

### Read a file from Google Drive:

```python
from g_drive_ops import read_item
read_item(item, file_download_path="optional_download_path")
```

### Update/Edit a file on Google Drive:

```python
from g_drive_ops import update_item
update_item(item, new_file_path="path/to/new_file.txt", new_file_name="new_file_name", new_folder_name="new_folder_name")
```

### Delete a file from Google Drive:

```python
from g_drive_ops import delete_item
delete_item(item)
```

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to myself for inspiration and guidance.

Libraries used: Selenium, PyWinAuto, google-auth, google-auth-oauthlib, google-auth-httplib2, google-api-python-client, python-dotenv.


