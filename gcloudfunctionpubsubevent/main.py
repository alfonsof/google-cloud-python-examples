#!/usr/bin/python
# -*- coding: utf-8 -*-
# main.py
# It handles a Google Cloud Function that sends information about a Cloud Pub/Sub event that depends on the input to the function log.

def pubsub_event(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
        Args:
            event (dict): Event payload.
            context (google.cloud.functions.Context): Metadata for the event.
    """

    import base64

    if 'data' in event:
        name = base64.b64decode(event['data']).decode('utf-8')
    else:
        name = 'World'
    print('Hello {}!'.format(name))
    