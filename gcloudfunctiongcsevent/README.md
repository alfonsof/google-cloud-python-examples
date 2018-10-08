# Google Cloud Function Cloud Storage Event Python example

This folder contains a Google Cloud Function example in Python on Google Cloud Platform (GCP).

It handles a Google Cloud Function that sends information to the function log about an object when it appears in a Cloud Storage bucket.

## Requirements

* You must have a [Google Cloud Platform (GCP)](http://cloud.google.com/) account.

* The code was written for Python 3.

## Using the code

* Access the Google Cloud console.

* Create a Cloud Storage bucket.

* Create a Google Cloud Function:
  * Name: `<CLOUD_FUNCTION_NAME>`
  * Memory allocated: `256 MB`
  * Trigger: `Cloud Storage`
  * Event Type: `Finalise/Create`
  * Bucket: `<BUCKET_NAME>`
  * Source code. You can use 2 options:
    * Inline editor:
      Edit the code of the `main.py` in the browser.
    * ZIP upload:
      Upload a ZIP file containing the `main.py` and `requirements.txt` files.
      * ZIP file: `<ZIP_LOCAL_NAME>`
      * Stage bucket: `<BUCKET_NAME_FOR_STAGGING>`
  * Runtime: `Python 3.7 (Beta)`
  * Function to execute: `gcs_event`
  * Region: `<GOOGLE_CLOUD_REGION>`
  * Timeout: `60 seconds`

* Save the Google Cloud Function.

  The function is deployed and run.

* Test the function.

  Copy a file in the source Cloud Storage bucket.

  You should see the next message in the Google Cloud Function log:

  ```bash
  Bucket: <BUCKET_NAME>
  Object: <OBJECT_NAME>
  Object size: <OBJECT_SIZE>
  ```
