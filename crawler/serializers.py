from crawler.models import nba_news
from rest_framework import serializers

class nba_newsSerializer(serializers.ModelSerializer):
    class Meta:
        model = nba_news
        fields = [
            'id','nba_title', 'nba_content', 'nba_url', 'nba_time', 
  
        ] 