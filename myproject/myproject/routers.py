from rest_framework import routers
from article.viewsets import ArticleViewSet
from leads.viewsets import LeadViewSet

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'leads', LeadViewSet)
