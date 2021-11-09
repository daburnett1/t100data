# Create your views here.
import pdb
from django.db.models.aggregates import Avg
from django.views.generic import ListView
from django.db.models import Max, Sum
from django.views.generic import DetailView
from . models import MarketData
from . models import counter, airlines, airline

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
class AAPassByMonth(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_AA_pass_month.html"
    object_list = []

    def get_queryset(self,**kwargs):

        month_list = []
        
        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_id',
                        'carrier_name',
                        'month') \
                .filter(month__exact=month) \
                .filter(carrier_id__exact='AA') \
                .annotate(total_pax=Sum('passengers')) \
                .order_by('-total_pax')[0:5]
                
            # off by one error for assignment

            month_list.append(queryset)
        # return list
        return month_list
    
class ASPassByMonth(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_AS_pass_month.html"
    object_list = []

    def get_queryset(self,**kwargs):

        month_list = []
        
        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_id',
                        'carrier_name',
                        'month') \
                .filter(month__exact=month) \
                .filter(carrier_id__exact='AS') \
                .annotate(total_pax=Sum('passengers')) \
                .order_by('-total_pax')[0:5]
                
            # off by one error for assignment

            month_list.append(queryset)
        # return list
        return month_list
    
class DLPassByMonth(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_DL_pass_month.html"
    object_list = []

    def get_queryset(self,**kwargs):

        month_list = []
        
        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_id',
                        'carrier_name',
                        'month') \
                .filter(month__exact=month) \
                .filter(carrier_id__exact='DL') \
                .annotate(total_pax=Sum('passengers')) \
                .order_by('-total_pax')[0:5]
                
            # off by one error for assignment

            month_list.append(queryset)
        # return list
        return month_list 
    
class UAPassByMonth(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_UA_pass_month.html"
    object_list = []

    def get_queryset(self,**kwargs):

        month_list = []
        
        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_id',
                        'carrier_name',
                        'month') \
                .filter(month__exact=month) \
                .filter(carrier_id__exact='UA') \
                .annotate(total_pax=Sum('passengers')) \
                .order_by('-total_pax')[0:5]
                
            # off by one error for assignment

            month_list.append(queryset)
        # return list
        return month_list  
    
class WNPassByMonth(ListView):
    context_object_name = "airline_list"
    template_name="rankorder_WN_pass_month.html"
    object_list = []

    def get_queryset(self,**kwargs):

        month_list = []
        
        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_id',
                        'carrier_name',
                        'month') \
                .filter(month__exact=month) \
                .filter(carrier_id__exact='WN') \
                .annotate(total_pax=Sum('passengers')) \
                .order_by('-total_pax')[0:5]
                
            # off by one error for assignment

            month_list.append(queryset)
        # return list
        return month_list   
    
class AVGPassengersToLAX(ListView):
    context_object_name = "airport_list"
    template_name="avg_pass_to_lax.html"
    queryset = MarketData.objects \
        .values('carrier_id','carrier_name', 'dest_iata_code', 'dest_city_name') \
        .filter(dest_iata_code__exact='LAX') \
        .annotate(avg_pax=Avg('passengers')) \
        .order_by('-avg_pax')[0:1]  
        

class AVGPassengersToSFO(ListView):
    context_object_name = "airport_list"
    template_name="avg_pass_to_sfo.html"
    queryset = MarketData.objects \
        .values('carrier_id','carrier_name', 'dest_iata_code', 'dest_city_name') \
        .filter(dest_iata_code__exact='SFO') \
        .annotate(avg_pax=Avg('passengers')) \
        .order_by('-avg_pax')[0:1]


class AVGPassengersToDFW(ListView):
    context_object_name = "airport_list"
    template_name="avg_pass_to_dfw.html"
    queryset = MarketData.objects \
        .values('carrier_id','carrier_name', 'dest_iata_code', 'dest_city_name') \
        .filter(dest_iata_code__exact='DFW') \
        .annotate(avg_pax=Avg('passengers')) \
        .order_by('-avg_pax')[0:1]


class AVGPassengersToATL(ListView):
    context_object_name = "airport_list"
    template_name="avg_pass_to_atl.html"
    queryset = MarketData.objects \
        .values('carrier_id','carrier_name', 'dest_iata_code', 'dest_city_name') \
        .filter(dest_iata_code__exact='ATL') \
        .annotate(avg_pax=Avg('passengers')) \
        .order_by('-avg_pax')[0:1]


class AVGPassengersToORD(ListView):
    context_object_name = "airport_list"
    template_name="avg_pass_to_ord.html"
    queryset = MarketData.objects \
        .values('carrier_id','carrier_name', 'dest_iata_code', 'dest_city_name') \
        .filter(dest_iata_code__exact='ORD') \
        .annotate(avg_pax=Avg('passengers')) \
        .order_by('-avg_pax')[0:1]
        

class AVGFreightFromMIA(ListView):
    context_object_name = "airport_list"
    template_name="avg_frt_from_mia.html"
    queryset = MarketData.objects \
        .values('carrier_id','carrier_name', 'orig_iata_code', 'orig_city_name') \
        .filter(orig_iata_code__exact='MIA') \
        .annotate(avg_frt=Avg('freight')) \
        .order_by('-avg_frt')[0:1]
        
        
class AVGFreightFromMEM(ListView):
    context_object_name = "airport_list"
    template_name="avg_frt_from_mem.html"
    queryset = MarketData.objects \
        .values('carrier_id','carrier_name', 'orig_iata_code', 'orig_city_name') \
        .filter(orig_iata_code__exact='MEM') \
        .annotate(avg_frt=Avg('freight')) \
        .order_by('-avg_frt')[0:1]
        
        
class AVGFreightFromJFK(ListView):
    context_object_name = "airport_list"
    template_name="avg_frt_from_jfk.html"
    queryset = MarketData.objects \
        .values('carrier_id','carrier_name', 'orig_iata_code', 'orig_city_name') \
        .filter(orig_iata_code__exact='JFK') \
        .annotate(avg_frt=Avg('freight')) \
        .order_by('-avg_frt')[0:1]


class AVGFreightFromANC(ListView):
    context_object_name = "airport_list"
    template_name="avg_frt_from_anc.html"
    queryset = MarketData.objects \
        .values('carrier_id','carrier_name', 'orig_iata_code', 'orig_city_name') \
        .filter(orig_iata_code__exact='ANC') \
        .annotate(avg_frt=Avg('freight')) \
        .order_by('-avg_frt')[0:1]


class AVGFreightFromSDF(ListView):
    context_object_name = "airport_list"
    template_name="avg_frt_from_sdf.html"
    queryset = MarketData.objects \
        .values('carrier_id','carrier_name', 'orig_iata_code', 'orig_city_name') \
        .filter(orig_iata_code__exact='SDF') \
        .annotate(avg_frt=Avg('freight')) \
        .order_by('-avg_frt')[0:1]                                                