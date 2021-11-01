# Google Cloud Storage Copy Python example

This folder contains a Python application example that handles Cloud Storage buckets on Google Cloud Platform (GCP).

Copy an object from a Google Storage bucket to another Google Storage bucket in a Google Cloud Project.

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

  The credentials are taken from `GOOGLE_APPLICATION_CREDENTIALS` environment variable.

  For example:

  ```bash
  GOOGLE_APPLICATION_CREDENTIALS = /path/to/my/key.json
  ```

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

  * Set the GOOGLE_APPLICATION_CREDENTIALS environment variable in your Operating System with the path of your JSON service account key file.

* Run the code.

  You must provide 3 parameters, replace the values of:

  * `<SOURCE_BUCKET>`      by source bucket name.
  * `<SOURCE_OBJECT>`      by source object name.
  * `<DESTINATION_BUCKET>` by destination bucket name.

  Run application:

  ```bash
  python gcloudstoragecopy.py <SOURCE_BUCKET> <SOURCE_OBJECT> <DESTINATION_BUCKET>
  ```

* Test the application.

  The object from the source Google Storage bucket should be copied to the target Google Storage bucket in the Google Cloud Project.
