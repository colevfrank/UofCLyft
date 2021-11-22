from util import soda_data
from util import socrata_api_requests



rides = soda_data.SodaData("TNP Rides",
                            "huhh",
                            'm6dm-c72p',
                            ['trip_id', 'trip_start_timestamp', 
                            'trip_end_timestamp','trip_seconds',
                            'pickup_community_area'],
                            where=["pickup_community_area==41"],
                            limit=10000)


rides_respo = socrata_api_requests.SocrataAPIClient(rides.request_url)

df = rides_respo.data_df
