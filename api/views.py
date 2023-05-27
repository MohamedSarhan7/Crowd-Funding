# from rest_framework.decorators import api_view,authentication_classes,permission_classes
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound,APIException
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q


from .models import *
from .serializers import *



class Home(APIView):    
    """
    ######################  Home Page #####################################
    
    1- A slider to show the highest five rated running projects to encourage
        users to donate
    2- List of the latest 5 projects
    3- List of latest 5 featured projects (which are selected by the admin)
    4- A list of the categories. User can open each category to view its
        projects
    5- Search bar that enables users to search projects by title or tag
    """
    
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request):
        '''
        By default, the result is sorted ascending (the lowest value first),
        to change the direction to descending (the highest value first),
        use the minus sign (NOT), - in front of the field average_rating:
        '''
        # the highest five rated
        slider=Project.objects.filter(is_available=True).order_by('-average_rating')[0:5]
        serializer_slider=HomeSerializer(slider,many=True)
        
        # List of the latest 5 projects
        latest=Project.objects.filter(is_available=True).order_by('-created_at')[0:5]
        serializer_latest=HomeSerializer(latest,many=True)
        
        # List of latest 5 featured projects (which are selected by the admin)
        featured=Project.objects.filter(is_featured=True)[0:5]
        serializer_featured=HomeSerializer(featured,many=True)
        
        # A list of the categories
        categories=Category.objects.all()
        serializer_category=CategorySerializer(categories,many=True)
        
        
        return Response(
            {
                "slider":serializer_slider.data,
                "latest":serializer_latest.data,
                "featured":serializer_featured.data,
                "categories":serializer_category.data,
                }
            )
        
class Search(APIView):
    def get(self,request):
        #  5- Search bar that enables users to search projects by title or tag
        value=self.request.query_params.get('value')
        if not value:
            return Response({"error":"pleasr provide a title or tag for search value"},status=status.HTTP_400_BAD_REQUEST)    
                
        search=Project.objects.filter(Q(tags__name__icontains=value)|Q(title__icontains=value)).distinct().order_by('-average_rating')
        serializer_search=HomeSerializer(search,many=True)
            
        return Response(
                {
                    "search":serializer_search.data,
                    }
                )
        
        
        
class CategoryList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request):
        #  get all categories for create project form         
        categories=Category.objects.all()
        serializer_categories=CategorySerializer(categories,many=True)
            
        return Response(
                {
                    "categories":serializer_categories.data,
                    }
                )
        
class TagList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,request):
        #  get all tags for create project form         
        tags=Tag.objects.all()
        serializer_tags=TagSerializer(tags,many=True)
            
        return Response(
                {
                    "tags":serializer_tags.data,
                    }
                )

class ProjectList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        
        # set user in request data from token 
        request.data['user']=request.user.id
        # creation serializer
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project=serializer.save()
        # view serializer
        project=HomeSerializer(project)
        return Response(project.data,status=status.HTTP_201_CREATED)
    
class ProjectDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,id):
        try:
            project=get_object_or_404(Project,id=id)
            project=HomeSerializer(project)
            return Response(project.data,status=status.HTTP_201_CREATED)
        except Http404:
            return Response({'message':'project not found'},status=status.HTTP_404_NOT_FOUND)

    
