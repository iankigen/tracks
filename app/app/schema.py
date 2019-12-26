import graphene

from tracks.schema import Query as TracksQuery, Mutation as TrackMutation


class Query(TracksQuery, graphene.ObjectType):
    pass


class Mutation(TrackMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
