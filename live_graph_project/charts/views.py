from django.shortcuts import render

# Create your views here.
def chart_view(request):
    chart_data = {
        'coordinates' : [
            (1,3),
            (2,6),
            (3,2),
            (4,5),
            (5,8),
            (6,7),
            (7,9),
        ]
    }

    return render(request, 'charts/chart.html', {'chart_data' : chart_data})