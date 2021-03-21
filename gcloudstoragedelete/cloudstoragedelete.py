#!/usr/bin/python
# -*- coding: utf-8 -*-
# cloudstoragedelete.py
# It is an example that handles Cloud Storage buckets on Google Cloud Platform (GCP).
# Delete a Cloud Storage bucket.
# You must provide 1 parameter:
# BUCKET_NAME = Name of the bucket

import sys
from google.cloud import storage
from google.cloud.exceptions import NotFound
from google.cloud.exceptions import Forbidden

def main():

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 1:
        print('Not enough parameters.\n'\
              'Proper Usage is: python cloudstoragedelete.py <BUCKET_NAME>')
        sys.exit(1)

    bucket_name = args[0]
    print('Bucket name: ' + bucket_name)

    print('Deleting bucket ...')
    
    # Instantiate the client.
    client = storage.Client()

    try:
        # Instantiate the bucket.
        bucket = client.bucket(bucket_name)
        # Delete the bucket.
        bucket.delete()
        print('\nDeleted')
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
