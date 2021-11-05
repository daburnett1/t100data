# Create your views here.
import pdb
from django.views.generic import ListView
from django.db.models import Max, Sum
from django.views.generic import DetailView
from . models import MarketData

class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_pax=Sum('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_destination.html"


# What are the top 5 airports in terms of: Total freight by origin
class Top5AirportsFrtByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_frt=Sum('freight')) \
                        .order_by('-total_frt')[0:5]
    template_name="rankorder_list_freight_origin.html"

# What are the top 5 airports in terms of: Total freight by destination
class Top5AirportsFrtByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_frt=Sum('freight')) \
                                 .order_by('-total_frt')[0:5]
    template_name="rankorder_list_freight_dest.html"

# What are the top 5 airports in terms of: Total mail by origin
class Top5AirportsMailByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="rankorder_list_mail_origin.html"

# What are the top 5 airports in terms of: Total mail by destination
class Top5AirportsMailByDest(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="rankorder_list_mail_dest.html"

# What are the top 5 airports in terms of: Total distance by origin
class Top5AirportsDistByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_dist=Sum('distance')) \
                        .order_by('-total_dist')[0:5]
    template_name="rankorder_list_dist_origin.html"

# What are the top 5 airports in terms of: Total distance by destination
class Top5AirportsDistByDest(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(total_dist=Sum('distance')) \
                        .order_by('-total_dist')[0:5]
    template_name="rankorder_list_dist_dest.html"

# Which airport reported the most passengers by month?
class TopPassengersByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_pass_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_passengers=Max('passengers')) \
                .order_by('-total_passengers')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_distance=Max('distance')) \
                .order_by('-total_distance')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)
            
        # return list
        return month_list

class MarketDataDetail(DetailView):
    model = MarketData

# Which airline reported the most freight carried?
class TopFreightbyAirline(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_list_freight_by_airline.html"
    queryset = MarketData.objects .values('carrier_id','carrier_name') .annotate(total_frt=Sum('freight')) .order_by('-total_frt')[0:1]

# Which airline reported the most passengers carried?    
class TopPassengersbyAirline(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_list_pass_by_airline.html"
    queryset = MarketData.objects .values('carrier_id','carrier_name') .annotate(total_pax=Sum('passengers')) .order_by('-total_pax')[0:1]

# Which airline reported the most mail carried?    
class TopMailbyAirline(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_list_mail_by_airline.html"
    queryset = MarketData.objects .values('carrier_id','carrier_name') .annotate(total_mail=Sum('mail')) .order_by('-total_mail')[0:1]

# Which airline reported the longest flight distance?    
class TopDistbyAirline(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_list_dist_by_airline.html"
    queryset = MarketData.objects .values('carrier_id','carrier_name') .annotate(total_dist=Max('distance')) .order_by('-total_dist')[0:1]

#           * Rank order passengers carried, by month, for these airlines:
#               * AA (American Airlines)
#               * AS (Alaska Airlines)
#               * DL (Delta Airlines)
#               * UA (United Airlines)
#               * WN (Southwest Airlines)
class TopAirlinePassByMonth(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_list_airline_pass_month.html"

    airline = None

    def get_queryset(self):
        airlines = ["AA", "AS", "DL", "UA", "WN"]
        for airline in airlines:

            month_list = []

            # pdb.set_trace()

            # there are six months worth of data
            # not good ultimately as this is a "hard-coded" fore-knowledge of the data
            for month in range(1,7):
                queryset = MarketData.objects \
                    .values('carrier_id',
                            'carrier_name',
                            'month') \
                    .filter(month__exact=month) \
                    .filter(carrier_id__exact=airline) \
                    .annotate(total_pax=Sum('passengers')) \
                    .order_by('-total_pax')[0:5]
                    
                # off by one error for assignment

                month_list.append(queryset)
                    
        # return list
        return month_list            