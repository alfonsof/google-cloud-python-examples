#!/usr/bin/python
# -*- coding: utf-8 -*-
# cloudstorageupload.py
# It is an example that handles Cloud Storage buckets on Google Cloud Platform (GCP).
# Upload a local file to a Google Storage bucket.
# You must provide 3 parameters:
# BUCKET_NAME     = Bucket name
# OBJECT_NAME     = Object name in the bucket
# LOCAL_FILE_NAME = Local file name
 

import sys
import os
from google.cloud import storage
from google.cloud.exceptions import NotFound
from google.cloud.exceptions import Forbidden

def main():

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 3:
        print('Not enough parameters.\n'\
              'Proper Usage is: python cloudstorageupload.py '\
              '<BUCKET_NAME> <OBJECT_NAME> <LOCAL_FILE_NAME>')
        sys.exit(1)

    bucket_name = args[0]
    blob_name = args[1]
    local_file_name = args[2]

    print('Bucket:     ' + bucket_name)
    print('Object:     ' + blob_name)
    print('Local file: ' + local_file_name)

    if not os.path.isfile(local_file_name):
        print("Error: File Not Found!!")
        sys.exit(1)

    print('Uploading an object to Cloud Storage bucket from a file ...')
    
    # Instantiate the client.
    client = storage.Client()

    try:
        # Get the bucket.
        bucket = client.get_bucket(bucket_name)
        # Instantiate the object.
        blob = bucket.blob(blob_name)
        # Uploads a file to the bucket.
        blob.upload_from_filename(local_file_name)
        print('\nUploaded')
    except NotFound:
        print('Error: Bucket does NOT exists!!')
        pass
    except Forbidden:
        print('Error: Forbidden, you do not have access to it!!')
        pass
  
    return
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
