# urls.py
from django.urls import path
from . views import MarketDataList, \
                    Top5AirportsPaxByOrigin, \
                    Top5AirportsPaxByDestination, \
                    TopDistanceByMonth, \
                    Top5AirportsFrtByOrigin, \
                    Top5AirportsFrtByDestination, \
                    Top5AirportsMailByOrigin, \
                    Top5AirportsMailByDest, \
                    Top5AirportsDistByOrigin, \
                    Top5AirportsDistByDest, \
                    TopPassengersByMonth, \
                    TopFreightbyAirline, \
                    TopPassengersbyAirline, \
                    TopMailbyAirline, \
                    TopDistbyAirline, \
                    TopAirlinePassByMonth         


urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport"}
        ),
        name="top5paxorigin"),
    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport"}
        ), 
        name="top5paxdestination"),
    path('top5frtorigin/', 
        Top5AirportsFrtByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Origin Airport"}
        ),
        name="top5frtorigin"),
    path('top5frtdestination/',  
        Top5AirportsFrtByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Destination Airport"}
        ), 
        name="top5frtdestination"),
    path('top5mailorigin/', 
        Top5AirportsMailByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Origin Airport"}
        ),
        name="top5mailorigin"),
    path('top5maildest/', 
        Top5AirportsMailByDest.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Destination Airport"}
        ),
        name="top5maildest"),
    path('top5distorigin/', 
        Top5AirportsDistByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Origin Airport"}
        ),
        name="top5distorigin"),
    path('top5distdest/', 
        Top5AirportsDistByDest.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Destination Airport"}
        ),
        name="top5distdest"),
    path('toppassengers_month/',  
        TopPassengersByMonth.as_view(
            extra_context={'title': "Top Passengers by Month"}
        ), 
        name="toppassengers_month"),        
    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month"}
        ), 
        name="topdistance_month"),
    path('topairlinefrt/',  
        TopFreightbyAirline.as_view(
            extra_context={'title': "Top Airline by Freight"}
        ), 
        name="topairlinefrt"),
    path('topairlinepax/',  
        TopPassengersbyAirline.as_view(
            extra_context={'title': "Top Airline by Passengers"}
        ), 
        name="topairlinepax"),
    path('topairlinemail/',  
        TopMailbyAirline.as_view(
            extra_context={'title': "Top Airline by Mail"}
        ), 
        name="topairlinemail"),
    path('topairlinedist/',  
        TopDistbyAirline.as_view(
            extra_context={'title': "Top Airline by Longest Flight Distance"}
        ), 
        name="topairlinedist"),
    path('topairlinepassmonth/<str:airline>',  
        TopAirlinePassByMonth.as_view(
            extra_context={'title': "Ranking of Top 5 Airlines by Passengers Carried"}
        ), 
        name="topairlinepassmonth"),                                        
]