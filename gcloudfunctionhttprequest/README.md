# Google Cloud Function HTTP Request Python example

This folder contains a Google Cloud Function example in Python on Google Cloud Platform (GCP).

It handles a Google Cloud Function that responds to an HTTP request.

## Requirements

* You must have a [Google Cloud Platform (GCP)](http://cloud.google.com/) account.

* The code was written for Python 3.

## Using the code

* Access the Google Cloud console.

* Create a Google Cloud Function:
  * Name: `<CLOUD_FUNCTION_NAME>`
  * Memory allocated: `256 MB`
  * Trigger: `HTTP`
  * URL: `https://<GOOGLE_CLOUD_REGION>-<PROJECT>.cloudfunctions.net/<CLOUD_FUNCTION_NAME>`
  * Source code. You can use 2 options:
    * Inline editor:
      Edit the code of the `main.py` in the browser.
    * ZIP upload:
      Upload a ZIP file containing the `main.py` and `requirements.txt` files.
      * ZIP file: `<ZIP_LOCAL_NAME>`
      * Stage bucket: `<BUCKET_NAME_FOR_STAGGING>`
  * Runtime: `Python 3.7 (Beta)`
  * Function to execute: `http_request`
  * Region: `<GOOGLE_CLOUD_REGION>`
  * Timeout: `60 seconds`

* Save the Google Cloud Function.

  The function is deployed and run.

* Test the function.

  You can test it in 2 ways:
  
  * First way: Test the funcion functionality in the Google Cloud console.

    Go to the `Function details` and select `Testing`.

    Enter the `Triggering event` content:

    ```json
    {
      "message": "Hello Peter!"
    }
    ```

    Click `Test the function`.

    You should see the next message in the Google Cloud `console output`:

    ```bash
    Hello Peter!
    ```

  * Second way: Test the function with a browser.

    Go to the URL: `https://<GOOGLE_CLOUD_REGION>-<PROJECT>.cloudfunctions.net/<CLOUD_FUNCTION_NAME>` using a browser.

    You should see the response:

    ```bash
    Hello World!
    ```
