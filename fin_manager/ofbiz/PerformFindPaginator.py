from django.core.paginator import Paginator
from . import services
import requests
import json
from django.utils.functional import cached_property

class PerformFindPaginator(Paginator):
    def __init__(self, object_name, input_fields, per_page, orphans=0,
            allow_empty_first_page=True):
        self.object_name = object_name
        self.input_fields = input_fields
        self.count = 0
        object_list = []
        super(PerformFindPaginator, self).__init__(object_list, per_page,
                orphans, allow_empty_first_page)

    def page(self, request, number):
        viewIndex = int(number) - 1
        postData={'entityName':self.object_name,'inputFields':self.input_fields,'viewIndex':viewIndex,'viewSize':self.per_page}
        jsonData = services.callOfbizService(request,'performFindList',postData)
        self.object_list = jsonData['list']
        self.count = int(jsonData['listSize'])
        #print(self.count)
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        if top + self.orphans >= self.count:
            top = self.count
        #print(self.object_list)
        #print(number)
        return self._get_page(self.object_list, number, self)
