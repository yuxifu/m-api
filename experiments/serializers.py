"""
Serializers for experimental features
"""
from rest_framework import serializers
from experiments.models import SimpleEmailMessssage
from django.core.mail import send_mail


class SimpleEmailMessssageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimpleEmailMessssage
        fields = '__all__'

    def create(self, validated_data):
        subject = validated_data['subject']
        message = validated_data['message']
        from_email = validated_data['from_addr']
        recipient_list = validated_data['to_addrs']
        num_sents = send_mail(
            subject,
            message,
            from_email,
            recipient_list.split(",")
        )
        if num_sents == 0:  # failed
            return None
        else:
            return SimpleEmailMessssage(subject, message, from_email, recipient_list)
