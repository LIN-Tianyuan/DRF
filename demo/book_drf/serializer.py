from rest_framework import serializers
from books.models import BookInfo

# Character serializer
class PeopleInfoSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()


# Custom Serializers
class BookSerializer(serializers.Serializer):
    # Serialize Return Fields
    name = serializers.CharField(max_length=20, min_length=5)
    readcount = serializers.IntegerField(max_value=100)
    pub_date = serializers.DateField()
    commentcount = serializers.IntegerField(default=10)
    # Returns the associated hero id
    # peopleinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # Returns the value of the str method of the associated hero model class
    # peopleinfo_set = serializers.StringRelatedField(read_only=True, many=True)
    # peopleinfo_set = PeopleInfoSerializer(many=True)

    # Single field validation
    def validate_name(self, value):
        if value == 'python':
            raise serializers.ValidationError("The title of the book can't be Python.")
        return value

    # Multiple field validation
    def validate(self, attrs):
        if attrs['readcount'] < attrs['commentcount']:
            raise serializers.ValidationError("Read more than commented.")
        return attrs

    def create(self, validated_data):
        # Save data
        book = BookInfo.objects.create(**validated_data)
        return book

    def update(self, instance, validated_data):
        # Update data
        instance.name = validated_data['name']
        instance.readcount = validated_data['readcount']
        instance.save()
        return instance

class BookModelSerializer(serializers.ModelSerializer):
    # Specify fields explicitly
    readcount = serializers.IntegerField(max_value=100)
    sms_code = serializers.CharField(max_length=6, min_length=6)

    class Meta:
        model=BookInfo  # Specify the model class that generates the field
        # fields=('name', 'readcount', 'pub_date', 'commentcount')    # Specify fields in the model class
        fields = '__all__'   # Specify fields in the model class
        # exclude = ('id',)
        # Add Modify Field Options parameter
        extra_kwargs = {
            'commentcount': {'default': 10},
            'name': {'required': True}
        }