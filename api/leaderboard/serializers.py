from rest_framework import serializers
from leaderboard.models import (
    codeforcesUser,
    codeforcesUserRatingUpdate,
    codechefUser,
    githubUser,
    openlakeContributor,
    LeetcodeUser
)


class Cf_Serializer(serializers.ModelSerializer):
    """
    TODO
    """

    def create(self, validated_data):
        return codeforcesUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `codeforcesUser`
        instance, given the validated data.
        """
        instance.rating = validated_data.get("rating", instance.rating)
        instance.max_rating = validated_data.get(
            "maxRating", instance.max_rating
        )
        instance.last_activity = validated_data.get(
            "lastActivity", instance.last_activity
        )
        instance.save()
        return instance

    class Meta:
        model = codeforcesUser
        fields = [
            "_id",
            "username",
            "rating",
            "avatar",
            "max_rating",
            "last_activity",
        ]


class Cf_RatingUpdate_Serializer(serializers.ModelSerializer):
    class Meta:
        model = codeforcesUserRatingUpdate
        fields = ["rating", "timestamp"]


class Cf_User_Serializer(Cf_Serializer):
    rating_updates = Cf_RatingUpdate_Serializer(many=True)

    class Meta:
        model = codeforcesUser
        fields = [
            "_id",
            "username",
            "rating",
            "avatar",
            "max_rating",
            "last_activity",
            "rating_updates",
        ]


class CC_Serializer(serializers.ModelSerializer):
    """
    TODO
    """

    def create(self, validated_data):
        return codechefUser.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `codechefUser`
    #     instance, given the validated data.
    #     """
    #     instance.rating = validated_data.get("rating", instance.rating)
    #     instance.max_rating = validated_data.get("maxRating",
    #     instance.max_rating)
    #     instance.Global_rank = validated_data.get("globalrank",
    #     instance.Global_rank)
    #     instance.Country_rank = validated_data.get("countryrank",
    #     instance.Country_rank)
    #     instance.save()
    #     return instance

    class Meta:
        model = codechefUser
        fields = [
            "_id",
            "username",
            "rating",
            "max_rating",
            "Global_rank",
            "Country_rank",
            "avatar",
        ]
class LT_Serializer(serializers.ModelSerializer):
    """
    TODO
    """

    def create(self, validated_data):
        return LeetcodeUser.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `codechefUser`
    #     instance, given the validated data.
    #     """
    #     instance.rating = validated_data.get("rating", instance.rating)
    #     instance.max_rating = validated_data.get("maxRating",
    #     instance.max_rating)
    #     instance.Global_rank = validated_data.get("globalrank",
    #     instance.Global_rank)
    #     instance.Country_rank = validated_data.get("countryrank",
    #     instance.Country_rank)
    #     instance.save()
    #     return instance

    class Meta:
        model = LeetcodeUser
        fields='__all__'


class GH_Serializer(serializers.ModelSerializer):
    """
    TODO
    """

    def create(self, validated_data):
        return githubUser.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `GithubUser`
    #     instance, given the validated data.
    #     """
    #     instance.contributions = validated_data.get("contributions",
    #     instance.contributions)
    #     instance.repositories = validated_data.get("repositories",
    #     instance.repositories)
    #     instance.stars = validated_data.get("stars", instance.stars)
    #     instance.save()
    #     return instance

    class Meta:
        model = githubUser
        fields = ["_id", "username", "contributions", "repositories", "stars","avatar",]


class OL_Serializer(serializers.ModelSerializer):
    """
    TODO
    """

    def create(self, validated_data):
        return openlakeContributor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `OpenLake Contributor` instance,
        given the validated data.
        """
        instance.contributions = validated_data.get(
            "contributions", instance.contributions
        )
        instance.save()
        return instance

    class Meta:
        model = openlakeContributor
        fields = ["_id", "username", "contributions"]
        



