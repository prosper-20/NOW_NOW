from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Post
from .serializers import PostSerializer
from django.contrib.auth.models import User



@api_view(["GET"])
def api_home_view(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def api_detail_view(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)

@api_view(["PUT"])
def api_update_view(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            data = {}
            updated_post = serializer.save()
            data["title"] = updated_post.title
            data["content"] = updated_post.content
            data["slug"] = updated_post.slug
            return Response(data=data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def api_create_view(request):
    user =  User.objects.get(pk=1)
    post = Post(author=user)

    if request.method == "POST":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def api_delete_view(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        data = {}
        operation = post.delete()
        if operation:
            data["Success"] = "Post Delete Successful"
        else:
            data["Failure"] = "Post Delete Failed"
        return Response(data)

