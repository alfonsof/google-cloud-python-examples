#!/usr/bin/python
# -*- coding: utf-8 -*-
# main.py
# It handles a Google Cloud Function that moves an object when it appears in a Cloud Storage bucket to another Cloud Storage bucket.

from google.cloud import storage
from google.cloud.exceptions import NotFound
from google.cloud.exceptions import Forbidden

def gcs_move(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
            event (dict): Event payload.
            context (google.cloud.functions.Context): Metadata for the event.
    """

    DESTINATION_BUCKET = 'destinationbucket'   # Destination Bucket name

    file = event

    source_bucket_name = file['bucket']
    source_blob_name = file['name']
    destination_bucket_name = DESTINATION_BUCKET
    destination_blob_name = source_blob_name

    print('From - bucket:', source_bucket_name)
    print('From - object:', source_blob_name)
    print('To - bucket:  ', destination_bucket_name)
    print('To - object:  ', destination_blob_name)

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
