import graphene
from graphene_django.types import DjangoObjectType
from .models import Track


class TrackType(DjangoObjectType):
    class Meta:
        model = Track


class CreateTrack(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        url = graphene.String(required=True)

    track = graphene.Field(TrackType)

    def mutate(self, info, title, description, url):
        track = Track(title=title, description=description, url=url)
        track.save()
        return CreateTrack(track=track)


class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)

    def resolve_tracks(self, info):
        return Track.objects.all()


class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
