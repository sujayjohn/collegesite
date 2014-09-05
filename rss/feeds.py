from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from rss.models import *

class TEB(Feed):
	title="Notices for college"
	link="/news/"
	description="Updates on the college Today's Engagement notice board."
	def items(self):
		return teb_board.objects.filter(approved=True).filter(pub_date__lte=timezone.now()).order_by('pub_date')[:10]
	def item_title(self,item):
		return item.heading
	def item_description(self,item):
		return item.description[:30]+' ...'
	def item_link(self,item):
		return reverse('notice',args=[item.id])
