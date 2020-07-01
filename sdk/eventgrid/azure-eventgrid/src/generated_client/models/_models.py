# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class CloudEvent(msrest.serialization.Model):
    """Properties of an event published to an Event Grid topic using the CloudEvent 1.0 Schema.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. An identifier for the event. The combination of id and source must be
     unique for each distinct event.
    :type id: str
    :param source: Required. Identifies the context in which an event happened. The combination of
     id and source must be unique for each distinct event.
    :type source: str
    :param data: Event data specific to the event type.
    :type data: object
    :param type: Required. Type of event related to the originating occurrence.
    :type type: str
    :param time: The time (in UTC) the event was generated, in RFC3339 format.
    :type time: ~datetime.datetime
    :param specversion: Required. The version of the CloudEvents specification which the event
     uses.
    :type specversion: str
    :param dataschema: Identifies the schema that data adheres to.
    :type dataschema: str
    :param datacontenttype: Content type of data value.
    :type datacontenttype: str
    :param subject: This describes the subject of the event in the context of the event producer
     (identified by source).
    :type subject: str
    """

    _validation = {
        'id': {'required': True},
        'source': {'required': True},
        'type': {'required': True},
        'specversion': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'data': {'key': 'data', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'time': {'key': 'time', 'type': 'iso-8601'},
        'specversion': {'key': 'specversion', 'type': 'str'},
        'dataschema': {'key': 'dataschema', 'type': 'str'},
        'datacontenttype': {'key': 'datacontenttype', 'type': 'str'},
        'subject': {'key': 'subject', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CloudEvent, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.source = kwargs['source']
        self.data = kwargs.get('data', None)
        self.type = kwargs['type']
        self.time = kwargs.get('time', None)
        self.specversion = kwargs['specversion']
        self.dataschema = kwargs.get('dataschema', None)
        self.datacontenttype = kwargs.get('datacontenttype', None)
        self.subject = kwargs.get('subject', None)

    def from_dict(self, source):
        """
        Returns an array of CloudEvent objects given a dict of events following the CloudEvent schema.

        :param source: Required. The dict object following the CloudEvent schema.
        :type source: dict

        :rtype: List[~azure.eventgrid.CloudEvent]
        """
        pass


class EventGridEvent(msrest.serialization.Model):
    """Properties of an event published to an Event Grid topic using the EventGrid Schema.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. An unique identifier for the event.
    :type id: str
    :param topic: The resource path of the event source.
    :type topic: str
    :param subject: Required. A resource path relative to the topic path.
    :type subject: str
    :param data: Required. Event data specific to the event type.
    :type data: object
    :param event_type: Required. The type of the event that occurred.
    :type event_type: str
    :param event_time: Required. The time (in UTC) the event was generated.
    :type event_time: ~datetime.datetime
    :ivar metadata_version: The schema version of the event metadata.
    :vartype metadata_version: str
    :param data_version: Required. The schema version of the data object.
    :type data_version: str
    """

    _validation = {
        'id': {'required': True},
        'subject': {'required': True},
        'data': {'required': True},
        'event_type': {'required': True},
        'event_time': {'required': True},
        'metadata_version': {'readonly': True},
        'data_version': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'topic': {'key': 'topic', 'type': 'str'},
        'subject': {'key': 'subject', 'type': 'str'},
        'data': {'key': 'data', 'type': 'object'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'event_time': {'key': 'eventTime', 'type': 'iso-8601'},
        'metadata_version': {'key': 'metadataVersion', 'type': 'str'},
        'data_version': {'key': 'dataVersion', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EventGridEvent, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.topic = kwargs.get('topic', None)
        self.subject = kwargs['subject']
        self.data = kwargs['data']
        self.event_type = kwargs['event_type']
        self.event_time = kwargs['event_time']
        self.metadata_version = None
        self.data_version = kwargs['data_version']
    
    def from_dict(self, source):
        """
        Returns an array of EventGridEvent objects given a dict of events following the EventGridEvent schema.

        :param source: Required. The dict object following the EventGridEvent schema.
        :type source: dict

        :rtype: List[~azure.eventgrid.EventGridEvent]
        """
        pass


class SubscriptionDeletedEventData(msrest.serialization.Model):
    """Schema of the Data property of an EventGridEvent for a Microsoft.EventGrid.SubscriptionDeletedEvent.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar event_subscription_id: The Azure resource ID of the deleted event subscription.
    :vartype event_subscription_id: str
    """

    _validation = {
        'event_subscription_id': {'readonly': True},
    }

    _attribute_map = {
        'event_subscription_id': {'key': 'eventSubscriptionId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SubscriptionDeletedEventData, self).__init__(**kwargs)
        self.event_subscription_id = None


class SubscriptionValidationEventData(msrest.serialization.Model):
    """Schema of the Data property of an EventGridEvent for a Microsoft.EventGrid.SubscriptionValidationEvent.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar validation_code: The validation code sent by Azure Event Grid to validate an event
     subscription. To complete the validation handshake, the subscriber must either respond with
     this validation code as part of the validation response, or perform a GET request on the
     validationUrl (available starting version 2018-05-01-preview).
    :vartype validation_code: str
    :ivar validation_url: The validation URL sent by Azure Event Grid (available starting version
     2018-05-01-preview). To complete the validation handshake, the subscriber must either respond
     with the validationCode as part of the validation response, or perform a GET request on the
     validationUrl (available starting version 2018-05-01-preview).
    :vartype validation_url: str
    """

    _validation = {
        'validation_code': {'readonly': True},
        'validation_url': {'readonly': True},
    }

    _attribute_map = {
        'validation_code': {'key': 'validationCode', 'type': 'str'},
        'validation_url': {'key': 'validationUrl', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SubscriptionValidationEventData, self).__init__(**kwargs)
        self.validation_code = None
        self.validation_url = None


class SubscriptionValidationResponse(msrest.serialization.Model):
    """To complete an event subscription validation handshake, a subscriber can use either the validationCode or the validationUrl received in a SubscriptionValidationEvent. When the validationCode is used, the SubscriptionValidationResponse can be used to build the response.

    :param validation_response: The validation response sent by the subscriber to Azure Event Grid
     to complete the validation of an event subscription.
    :type validation_response: str
    """

    _attribute_map = {
        'validation_response': {'key': 'validationResponse', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SubscriptionValidationResponse, self).__init__(**kwargs)
        self.validation_response = kwargs.get('validation_response', None)
