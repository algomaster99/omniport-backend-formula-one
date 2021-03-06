from formula_one.models import ContactInformation
from formula_one.serializers.base import ModelSerializer


class ContactInformationSerializer(ModelSerializer):
    """
    Serializer for ContactInformation objects
    """

    class Meta:
        """
        Meta class for ContactInformationSerializer
        """

        model = ContactInformation

        exclude = [
            'datetime_created',
            'datetime_modified',
            'entity_content_type',
            'entity_object_id',
        ]
        read_only_fields = [
            'email_address_verified',
            'institute_webmail_address',
        ]

    def update(self, instance, validated_data):
        """
        Update the fields, setting the invalidating the verified status of the
        email address if updated
        :param instance: the instance being updated
        :param validated_data: the new data for the instance
        :return: the updated instance
        """

        original_email_address = instance.email_address
        new_email_address = validated_data.get('email_address')

        instance = super().update(instance, validated_data)

        if original_email_address != new_email_address:
            instance.email_address_verified = False
            instance.save()

        return instance
