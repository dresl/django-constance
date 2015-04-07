# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django.utils.translation import get_language_from_request

from feincms.module.page.models import Page

from leonardo.module.web.models import Widget

class SiteMapWidget(Widget):

    class Meta:
        abstract = True
        verbose_name = _("site map")
        verbose_name_plural = _('site maps')

    def render_content(self, options):
        request = options['request']
        lang = get_language_from_request(request)
        page_list = Page.objects.filter(level=0, active=True, language=lang)
        linkmenu_class = models.loading.get_model('page', 'linkmenuwidget')
        utils_list = linkmenu_class.objects.filter(parent__in=page_list)

        return render_to_string(self.template_name, { 
            'widget': self,
            'page_list': page_list,
            'utils_list': utils_list,
            'request': request,
        })