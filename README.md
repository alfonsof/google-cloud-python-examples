# Python examples on Google Cloud Platform (GCP)

This repo contains Python code examples on Google Cloud Platform (GCP).

These examples show how to use Python 3 and Google Python Client Libraries in order to manage services on Google Cloud Platform. These use Google Cloud Python Client Library or Google API Python Client Library.

Google Python Client Libraries allow Python developers to write software that makes use of Google Cloud services like Compute Engine and Cloud Storage.

Google Python Client Libraries offers two different styles of API:

* Google Cloud Client Library for Python: It is the recommended option for accessing Cloud APIs programmatically, where available. It is an idiomatic, intuitive, and natural way for Python developers to integrate with Google Cloud Platform services, like Cloud Datastore and Cloud Storage.
* Google API Client Library for Python: A number of Google Cloud APIs do not yet have Google Cloud Client Libraries available in Python. If you want to use one of these APIs and there is no Cloud Client Library for Python, you can still use an older version of the client libraries called Google API Client Libraries.

## Quick start

You must have a [Google Cloud Platform (GCP)](http://cloud.google.com/) account.

The code for the samples is contained in individual folders on this repository.

For instructions on running the code, please consult the README in each folder.

This is the list of examples:

**Compute - Compute Engine:**

* [gcloudcomputeengine](/gcloudcomputeengine) - Compute Engine VM instances: Example of how to handle Compute Engine VM instances. It uses the Google API Client Library.

**Storage - Cloud Storage:**

* [gcloudstoragecreate](/gcloudstoragecreate) - Google Cloud Storage Create: Example of how to handle Cloud Storage buckets and create a new Google Storage bucket in a Google Cloud Project. It uses the Google Cloud Client Library.
* [gcloudstoragedelete](/gcloudstoragedelete) - Google Cloud Storage Delete: Example of how to handle Cloud Storage buckets and delete a Google Storage bucket in a Google Cloud Project. It uses the Google Cloud Client Library.
* [gcloudstoragelist](/gcloudstoragelist) - Google Cloud Storage List: Example of how to handle Cloud Storage buckets and list information about the objects in a Cloud Storage bucket in a Google Cloud Project. It uses the Google Cloud Client Library.
* [gcloudstoragelistall](/gcloudstoragelistall) - Google Cloud Storage List All: Example of how to handle Cloud Storage buckets and list information about all Cloud Storage buckets and the objects that they contain in a Google Cloud Project. It uses the Google Cloud Client Library.
* [gcloudstorageupload](/gcloudstorageupload) - Google Cloud Storage Upload: Example of how to handle Cloud Storage buckets and upload a local file to a Cloud Storage bucket in a Google Cloud Project. It uses the Google Cloud Client Library.
* [gcloudstoragedownload](/gcloudstoragedownload) - Google Cloud Storage Download: Example of how to handle Cloud Storage buckets and download an object in a Cloud Storage bucket in a Google Cloud Project to a local file. It uses the Google Cloud Client Library.
* [gcloudstoragecopy](/gcloudstoragecopy) - Google Cloud Storage Copy: Example of how to handle Cloud Storage buckets and copy an object from a Google Storage bucket to another Google Storage bucket in a Google Cloud Project. It uses the Google Cloud Client Library.

## License

This code is released under the MIT License. See LICENSE file.
