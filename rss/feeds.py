from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from rss import models
from django.utils import timezone
from college.models import custom_notice

class notice_feed(Feed):
	title="Notices for college"
	#link=reverse("news_home")
	link='/news/'
	description="Updates on the college Today's Engagement notice board."
	def items(self):
		return models.notice.objects.filter(approved=True).filter(pub_date__lte=timezone.now()).order_by('-pub_date','-id')[:10]
	def item_title(self,item):
		return item.title
	def item_description(self,item):
		return item.description[:30]+' ...'
	def item_link(self,item):
		return reverse('notice',args=[item.id])
		
class notification_feed(Feed):
	title="Notifications from college"
	#link=reverse("notification_view")
	link='/notification/'
	description="Notifications from the college"
	def items(self):
		return custom_notice.objects.filter(alive=True).filter(pub_date__lte=timezone.now()).order_by('-pub_date','-id')[:5]
	def item_title(self,item):
		return item.title
	def item_description(self,item):
		return item.description[:30]+' ...'
	def item_link(self,item):
		return reverse('notification_view',args=[item.id])
