#!/usr/bin/python
# -*- coding: utf-8 -*-
# cloudstoragedeleteobject.py
# It is an example that handles Cloud Storage buckets on Google Cloud Platform (GCP).
# Delete an object in a Cloud Storage bucket.
# You must provide 1 parameter:
# BUCKET_NAME = Name of the bucket
# OBJECT_NAME = Name of the object in the bucket

import sys
from google.cloud import storage
from google.cloud.exceptions import NotFound
from google.cloud.exceptions import Forbidden

def main():

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 2:
        print('Not enough parameters.\n'\
              'Proper Usage is: python cloudstoragedeleteobject.py '\
              '<BUCKET_NAME> <OBJECT_NAME>')
        sys.exit(1)

    bucket_name = args[0]
    blob_name = args[1]
    print('Bucket name: ' + bucket_name)
    print('Object name: ' + blob_name)

    print('Deleting object in the bucket ...')
    
    # Instantiate the client.
    client = storage.Client()

    try:
        # Instantiate the bucket.
        bucket = client.bucket(bucket_name)
        # Instantiate the object.
        blob = bucket.blob(blob_name)
        # Delete the object.
        blob.delete()
        print('\nDeleted')
    except NotFound:
        print('Error: Bucket/Object does NOT exists!!')
        pass
    except Forbidden:
        print('Error: Forbidden, you do not have access to it!!')
        pass
  
    return
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
