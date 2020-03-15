from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("collect")
# Create your views here.
# logger = logging.getLogger('log')

# 404

import hashlib

def md5(text):
    """md5加密函数"""
    md5 = hashlib.md5()
    if not isinstance(text, bytes):
        text = str(text).encode('utf-8')
    md5.update(text)
    return md5.hexdigest()

def page_not_found(request,exception):
    return render(request, '404.html')
# 500
def page_error(request):
    return render(request, '500.html')

def index(request):
    print(md5(124566))
    return render(request, 'index.html')