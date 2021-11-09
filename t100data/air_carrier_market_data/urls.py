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
                    AAPassByMonth, \
                    ASPassByMonth, \
                    DLPassByMonth, \
                    UAPassByMonth, \
                    WNPassByMonth, \
                    AVGPassengersToLAX, \
                    AVGPassengersToSFO, \
                    AVGPassengersToDFW, \
                    AVGPassengersToATL, \
                    AVGPassengersToORD, \
                    AVGFreightFromMIA, \
                    AVGFreightFromMEM, \
                    AVGFreightFromJFK, \
                    AVGFreightFromANC, \
                    AVGFreightFromSDF        


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
    path('AApassmonth/AA',  
        AAPassByMonth.as_view(
            extra_context={'title': "Ranking of American Airlines by Passengers Carried by Month"}
        ), 
        name="AApassmonth"),
    path('ASpassmonth/AS',  
        ASPassByMonth.as_view(
            extra_context={'title': "Ranking of Alaska Airlines by Passengers Carried by Month"}
        ), 
        name="ASpassmonth"),
    path('DLpassmonth/DL',  
        DLPassByMonth.as_view(
            extra_context={'title': "Ranking of Delta Airlines by Passengers Carried by Month"}
        ), 
        name="DLpassmonth"),
    path('UApassmonth/UA',  
        UAPassByMonth.as_view(
            extra_context={'title': "Ranking of United Airlines by Passengers Carried by Month"}
        ), 
        name="UApassmonth"),
    path('WNpassmonth/WN',  
        WNPassByMonth.as_view(
            extra_context={'title': "Ranking of Southwest Airlines by Passengers Carried by Month"}
        ), 
        name="WNpassmonth"),
    path('AVGpasstoLAX/LAX',  
        AVGPassengersToLAX.as_view(
            extra_context={'title': "Average of Passengers Flown Into Los Angeles International Airport"}
        ), 
        name="AVGpasstoLAX"),
    path('AVGpasstoSFO/SFO',  
        AVGPassengersToSFO.as_view(
            extra_context={'title': "Average of Passengers Flown Into San Franciso International Airport"}
        ), 
        name="AVGpasstoSFO"),
    path('AVGpasstoDFW/DFW',  
        AVGPassengersToDFW.as_view(
            extra_context={'title': "Average of Passengers Flown Into Dallas/Fort Worth International Airport"}
        ), 
        name="AVGpasstoDFW"),
    path('AVGpasstoATL/ATL',  
        AVGPassengersToATL.as_view(
            extra_context={'title': "Average of Passengers Flown Into Atlanta International Airport"}
        ), 
        name="AVGpasstoATL"),
    path('AVGpasstoORD/ORD',  
        AVGPassengersToORD.as_view(
            extra_context={'title': "Average of Passengers Flown Into Chicago International Airport"}
        ), 
        name="AVGpasstoORD"),
    path('AVGfrtfromMIA/MIA',  
        AVGFreightFromMIA.as_view(
            extra_context={'title': "Average of Freight Flown Out of Miami International Airport"}
        ), 
        name="AVGfrtfromMIA"),
    path('AVGfrtfromMEM/MEM',  
        AVGFreightFromMEM.as_view(
            extra_context={'title': "Average of Freight Flown Out of Memphis International Airport"}
        ), 
        name="AVGfrtfromMEM"),
    path('AVGfrtfromJFK/JFK',  
        AVGFreightFromJFK.as_view(
            extra_context={'title': "Average of Freight Flown Out of John F. Kennedy International Airport"}
        ), 
        name="AVGfrtfromJFK"),
    path('AVGfrtfromANC/ANC',  
        AVGFreightFromANC.as_view(
            extra_context={'title': "Average of Freight Flown Out of Anchorage International Airport"}
        ), 
        name="AVGfrtfromANC"),
    path('AVGfrtfromSDF/SDF',  
        AVGFreightFromSDF.as_view(
            extra_context={'title': "Average of Freight Flown Out of Louisville International Airport"}
        ), 
        name="AVGfrtfromSDF"),                                                                                            
]