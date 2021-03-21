#!/usr/bin/python
# -*- coding: utf-8 -*-
# cloudstoragecreate.py
# It is an example that handles Cloud Storage buckets on Google Cloud Platform (GCP).
# Create a new Cloud Storage bucket.
# You must provide 1 parameter:
# BUCKET_NAME = Name of the bucket

import sys
from google.cloud import storage
from google.cloud.exceptions import Conflict

def main():

    STORAGE_LOCATION           = 'us-east1'   # Cloud Storage location
  
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 1:
        print('Not enough parameters.\n'\
              'Proper Usage is: python cloudstoragecreate.py <BUCKET_NAME>')
        sys.exit(1)

    bucket_name = args[0]
    print('Bucket name: ' + bucket_name)

    print('Creating bucket ...')
    
    # Instantiate the client.
    client = storage.Client()

    try:
        # Instantiate the bucket.
        bucket = client.bucket(bucket_name)
        # Create the bucket object.
        bucket.create(location=STORAGE_LOCATION)
        print('\nCreated')
    except Conflict:
        print('Error: Bucket already exists!!')
        pass
  
    return
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
