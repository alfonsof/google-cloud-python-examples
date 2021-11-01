# Google Cloud Storage List All Parameters Python example

This folder contains a Python application example that handles Cloud Storage buckets on Google Cloud Platform (GCP).

List information about all Cloud Storage buckets and the objects that they contain in a Google Cloud Project.

The user must provide the credentials using the application parameters.

## Requirements

* You must have a [Google Cloud Platform (GCP)](http://cloud.google.com/) account.

* You can install and use the Google Cloud SDK.

  The Google Cloud SDK is a set of tools for Google Cloud Platform.
  It contains gcloud, gsutil, and bq, which you can use to access Google Compute Engine, Google Cloud Storage, Google BigQuery,
  and other products and services from the command line. You can run these tools interactively or in your automated scripts.* The code was written for Python 3 and Google Cloud Python Client Library.

* The code was written for:
  
  * Python 3
  * Google API Python Client Library

* Install the Google Cloud Python Client Library.

  Install the latest Google Cloud Python Client Library release via pip:

  ```bash
  pip install google-cloud-storage
  ```

## Using the code

* Configure your Google Cloud access keys.

  The Google Cloud client library for Java allows you to use several authentication schemes.

  The application uses Application Default Credentials through a JSON service account key for authenticating.

  The credentials are taken from the file name provided by application parameters.

  Use the [Google Cloud Platform console](http://cloud.google.com/):

  * Go to the Google Cloud Project.

  * Prepare the credentials:
  
    * Create a Service account.

      For example:

      ```bash
      Name: gcloud-java-examples
      Role: Owner
      Email: gcloud-java-examples@gcloud-java-examples.iam.gserviceaccount.com
      ```

    * Create a key as a JSON file and download it.

    * Add the Service accounts id (Ex.: gcloud-java-examples@gcloud-java-examples.iam.gserviceaccount.com) as a member of the project in the IAM.

* Run the code.

  You must provide 1 parameter, replace the value of:

  * `<CREDENTIALS_FILE_NAME>` by path and name of the JSON credential file.

  Run application:

  ```bash
  python cloudstoragelistallparam.py <CREDENTIALS_FILE_NAME>
  ```

  Example:

  ```bash
  python cloudstoragelistallparam.py ~/.gcloud/gcloud-java-examples.json
  ```

* Test the application.

  You should see the list of buckets and objects stored in each Cloud Storage bucket in the Google Cloud Project.
