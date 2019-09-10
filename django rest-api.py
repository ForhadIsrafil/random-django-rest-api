thumbnail = models.FileField(upload_to='media', null=True)


# ------------------------------------------------------------
def lfj(request):
    up_file = request.FILES['file']
    destination = open('/Users/Username/' + up_file.name, 'wb+')
    for chunk in up_file.chunks():
        destination.write(chunk)
        destination.close()

    # ------------------------------------------------------------
    def get_queryset(self):
        category = self.request.GET.get('category')
        order = self.request.GET.get('order', 'desc')
        all_faqs = Faq.objects.all()

        if category:
            filter_faqs = all_faqs.filter(category__iexact=category)
        else:
            filter_faqs = all_faqs
        if order == 'desc':
            faqs = filter_faqs.order_by('-priority')
        else:
            faqs = filter_faqs.order_by('priority')

        return faqs

    def get_serializer_context(self):
        return {'request': self.request}


# ------------------------------------------------------------
def validate_company_website(value):
    if not ".io" in value:
        raise ValidationError("Company website url must be valid url")
    else:
        return value


company_website = models.CharField(max_length=255, validators=[validate_company_website])


# ------------------------------------------------------------
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
def Docs(self):
    file_name = settings.PROJECT_DIR + '/triumapp.md'
    handle = open(file_name, 'r', encoding="utf-8")
    content = handle.read()

    response = """
    <html>
        <head>
    <title></title>
    </head>
    <body>
        <xmp>""" + content + """</xmp>
    </body>
    
    </html>
    """
    return HttpResponse(response)
# ------------------------------------------------------------

#-------------------------------------------------------------
fields = [x for x in model._meta.fields if isinstance(x, django.db.models.CharField)]
search_queries = [Q(**{x.name + "__contains" : search_query}) for x in fields]
q_object = Q()
for query in search_queries:
q_object = q_object | query

results = model.objects.filter(q_object)
search_results.append(results)
#-------------------------------------------------------------
