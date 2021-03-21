#!/usr/bin/python
# -*- coding: utf-8 -*-
# main.py
# It handles a Google Cloud Funtion that sends information to the log about an object when it appears in a Cloud Storage bucket.

def gcs_event(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
            event (dict): Event payload.
            context (google.cloud.functions.Context): Metadata for the event.
    """

    file = event
    print(f"Bucket:      {file['bucket']}.")
    print(f"Object:      {file['name']}.")
    print(f"Object size: {file['size']}.")