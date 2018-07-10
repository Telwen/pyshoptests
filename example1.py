from django.core.serializers import serialize, json
from django.db.models import Q


def live_search(request, ):
    q = request.GET.get("q", "")
    q = q.lower()
    if q:
        qset = (
                Q(sku__icontains=q) |
                Q(name__icontains=q) |
                Q(description__icontains=q)
        )
        results = serialize('json', Product.objects.filter(qset))
    else:
        results = []
    return HttpResponse(json.dumps({"data": results}), content_type='application/json')
