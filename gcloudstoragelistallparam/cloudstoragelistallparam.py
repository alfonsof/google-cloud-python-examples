#!/usr/bin/python
# -*- coding: utf-8 -*-
# cloudstoragelistallparam.py
# It is an example that handles Cloud Storage buckets on Google Cloud Platform (GCP).
# List information about all Cloud Storage buckets and the objects that they contain.
# The user must provide the credentials using the application parameters.
# You must provide 1 parameter:
# CREDENTIALS_FILE_NAME = Path and name of the JSON credential file

import sys
import os
from google.cloud import storage

def main():

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 1:
        print('Not enough parameters.\n'\
              'Proper Usage is: python cloudstoragelistallparam.py <CREDENTIALS_FILE_NAME>')
        sys.exit(1)

    credentials_file = args[0]

    print('Credentials file: ' + credentials_file)

    if not os.path.isfile(credentials_file):
        print("Error: Credentials file does NOT exist!!")
        sys.exit(1)

    print('Listing Cloud Storage buckets and objects ...')
    
    # Instantiate the client.
    # Explicitly use service account credentials by specifying the private key file.
    client = storage.Client.from_service_account_json(credentials_file)

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
