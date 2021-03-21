#!/usr/bin/python
# -*- coding: utf-8 -*-
# cloudstoragemove.py
# It is an example that handles Cloud Storage buckets on Google Cloud Platform (GCP).
# Move an object from a Google Storage bucket to another Google Storage bucket.
# You must provide 3 parameters:
# SOURCE_BUCKET      = Source bucket name
# SOURCE_OBJECT      = Source object name
# DESTINATION_BUCKET = Destination bucket name

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
              'Proper Usage is: python cloudstoragemove.py '\
              '<SOURCE_BUCKET> <SOURCE_OBJECT> <DESTINATION_BUCKET>')
        sys.exit(1)

    source_bucket_name = args[0]
    source_blob_name = args[1]
    destination_bucket_name = args[2]
    destination_blob_name = source_blob_name

    print('From - bucket: ' + source_bucket_name)
    print('From - object: ' + source_blob_name)
    print('To   - bucket: ' + destination_bucket_name)
    print('To   - object: ' + destination_blob_name)

    print('Moving object ...')
    
    # Instantiate the client.
    client = storage.Client()

    try:
        # Get the source bucket.
        source_bucket = client.get_bucket(source_bucket_name)
        # Instantiate the source object.
        source_blob = source_bucket.blob(source_blob_name)
        # Get the destination bucket.
        destination_bucket = client.get_bucket(destination_bucket_name)
        # Copies a blob from one bucket to another one.
        source_bucket.copy_blob(source_blob, destination_bucket, destination_blob_name)
        # Delete the source object.
        source_blob.delete()
        print('\nMoved')
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
