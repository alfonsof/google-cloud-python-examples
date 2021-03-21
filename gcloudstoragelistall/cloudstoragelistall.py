#!/usr/bin/python
# -*- coding: utf-8 -*-
# cloudstoragelistall.py
# It is an example that handles Cloud Storage buckets on Google Cloud Platform (GCP).
# List information about all Cloud Storage buckets and the objects that they contain.
# The credentials are taken from GOOGLE_APPLICATION_CREDENTIALS environment variable.

import sys
from google.cloud import storage

def main():

    print('Listing Cloud Storage buckets and objects ...')
    
    # Instantiate the client.
    client = storage.Client()

    # List all the buckets.
    buckets = client.list_buckets()
    for bucket in buckets:
        print('* Bucket:', bucket.name)
        # Lists all the blobs in the bucket.
        blobs = bucket.list_blobs()
        for blob in blobs:
            print('  - Object:', blob.name)
            print('            size:', blob.size)
    print('\nListed')
  
    return
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
