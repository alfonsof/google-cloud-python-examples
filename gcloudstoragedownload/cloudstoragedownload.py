#!/usr/bin/python
# -*- coding: utf-8 -*-
# cloudstoragedownload.py
# It is an example that handles Cloud Storage buckets on Google Cloud Platform (GCP).
# Download an object from a Cloud Storage bucket to a local file.
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
              'Proper Usage is: python cloudstoragedownload.py '\
              '<BUCKET_NAME> <OBJECT_NAME> <LOCAL_FILE_NAME>')
        sys.exit(1)

    bucket_name = args[0]
    blob_name = args[1]
    local_file_name = args[2]

    print('Bucket:     ' + bucket_name)
    print('Object:     ' + blob_name)
    print('Local file: ' + local_file_name)

    print('Downloading an object from a Cloud Storage bucket to a local file ...')
    
    # Instantiate the client.
    client = storage.Client()

    try:
        # Get the bucket.
        bucket = client.get_bucket(bucket_name)
        # Instantiate the object.
        blob = bucket.blob(blob_name)
        # Downloads an object from the bucket.
        blob.download_to_filename(local_file_name)
        print('\nDownloaded')
    except NotFound:
        print('Error: Bucket/Blob does NOT exists!!')
        pass
    except Forbidden:
        print('Error: Forbidden, you do not have access to it!!')
        pass
  
    return
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
