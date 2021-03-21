# Google Cloud Function Cloud Storage Move Python example

This folder contains a Google Cloud Function example in Python on Google Cloud Platform (GCP).

It handles a Google Cloud Function that Moves an object when it appears in a Cloud Storage bucket to another Cloud Storage bucket.

## Requirements

* You must have a [Google Cloud Platform (GCP)](http://cloud.google.com/) account.

* The code was written for:
  
  * Python 3
  * Google API Python Client Library

* Dependencies in Python are managed with pip and expressed in a metadata file called `requirements.txt` shipped alongside your function.

  This `requirements.txt` file must be in the same directory as the `main.py` file that contains your function code.

  The `requirements.txt` file contains one line per library. Each line contains the package name, and optionally, the requested version.

  In order to use the Google Cloud Python Client Library, the file needs to include this dependency:

  ```bash
  google-cloud-storage==1.12.0
  ```

## Using the code

* Access the Google Cloud console.

* Create a Cloud Storage bucket for the source and another Cloud Storage bucket for the target.

* Create a Google Cloud Function:
  * Name: `<CLOUD_FUNCTION_NAME>`
  * Memory allocated: `256 MB`
  * Trigger: `Cloud Storage`
  * Event Type: `Finalise/Create`
  * Bucket: `<BUCKET_NAME>`
  * Source code. You can use 2 options:
    * Inline editor:
      Edit the code of the `main.py` and `requirements.txt` files in the browser.
    * ZIP upload:
      Upload a ZIP file containing the `main.py` and `requirements.txt` files.
      * ZIP file: `<ZIP_LOCAL_NAME>`
      * Stage bucket: `<BUCKET_NAME_FOR_STAGGING>`
  * Runtime: `Python 3.7 (Beta)`
  * Function to execute: `gcs_move`
  * Region: `<GOOGLE_CLOUD_REGION>`
  * Timeout: `60 seconds`

* You can select the destination bucket name changing the value of `DESTINATION_BUCKET` variable in the code.

* Save the Google Cloud Function.

  The function is deployed and run.

* Test the function.

  Copy a file in the source Cloud Storage bucket.

  The object from the source Cloud Storage bucket should be copied to the target Cloud Storage bucket and deleted in the source Cloud Storage bucket.
