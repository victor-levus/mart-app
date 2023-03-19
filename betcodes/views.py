from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAdminUser, IsAuthenticated
import logging

from betcodes.models import BetCode, FootballClub, Likes, Post, Comment
from betcodes.serializers import BetCodeSerializer, FootballClubSerializer, LikeSerializer, PostSerializer, CommentSerializer


logger = logging.getLogger(__name__)


class BetCodeViewSet(ModelViewSet):
    queryset = BetCode.objects.all()
    serializer_class = BetCodeSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]     


class PostViewSet(ModelViewSet):
    queryset = Post.objects.prefetch_related('user', 'comments').all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user_id'] = self.request.user
        logger.info('self.kwargs2')
        return context


class ProfilePostViewSet(ModelViewSet):
    queryset = Post.objects.prefetch_related('user', 'comments').all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # logger(self)
        return Post.objects.prefetch_related('user', 'comments').filter(user_id=self.request.user.id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user_id'] = self.request.user
        logger.info('self.kwargs2')
        return context        


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk'], 'user_id': self.request.user}


class LikesViewSet(ModelViewSet):
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Likes.objects.filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk'], 'user_id': self.request.user}



class FootballClubViewSet(ModelViewSet):
    queryset = FootballClub.objects.all()
    serializer_class = FootballClubSerializer
    permission_classes = [IsAdminUser]

