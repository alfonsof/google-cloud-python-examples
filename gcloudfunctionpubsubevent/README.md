# Google Cloud Function Pub/Sub Event Python example

This folder contains a Google Cloud Function example in Python on Google Cloud Platform (GCP).

It handles a Google Cloud Function that sends information about a Cloud Pub/Sub event that depends on the input to the function log.

## Requirements

* You must have a [Google Cloud Platform (GCP)](http://cloud.google.com/) account.

* The code was written for Python 3.

## Using the code

* Access the Google Cloud console.

* Create a Google Cloud Function:
  * Name: `<CLOUD_FUNCTION_NAME>`
  * Memory allocated: `256 MB`
  * Trigger: `Cloud Pub/Sub`
  * Topic: `projects/<PROJECT-NAME>/topics/<TOPIC_NAME>`
  * Source code. You can use 2 options:
    * Inline editor:
      Edit the code of the `main.py` in the browser.
    * ZIP upload:
      Upload a ZIP file containing the `main.py` and `requirements.txt` files.
      * ZIP file: `<ZIP_LOCAL_NAME>`
      * Stage bucket: `<BUCKET_NAME_FOR_STAGGING>`
  * Runtime: `Python 3.7 (Beta)`
  * Function to execute: `pusub_event`
  * Region: `<GOOGLE_CLOUD_REGION>`
  * Timeout: `60 seconds`

* Save the Google Cloud Function.

  The function is deployed and run.

* Test the function.

  Go to the `Function details` and select `Testing`.
  
  * First test:

    Enter the `Triggering event` content:

    ```json
    {}
    ```

    Click `Test the function`.

    You should see the next message in the Google Cloud `console output`:

    `OK`

    You should see the next message in the Google Cloud Function log:

    ```bash
    Hello World!
    ```

  * Second test:

    Encoding the text `Peter` to Base64 format using an external tool, you should get `UGV0ZXI=`.

    Enter the `Triggering event` content:

    ```json
    {
      "data": "UGV0ZXI="
    }
    ```

    Click `Test the function`.

    You should see the next message in the Google Cloud `console output`:

    `OK`

    You should see the next message in the Google Cloud Function log:

    ```bash
    Hello Peter!
    ```
