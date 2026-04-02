from pathlib import Path
import time

import fastf1

#main function, we return nothing
def main(session) -> None:


    #print the session information
    print(f"Event: {session.event['EventName']}")
    print(f"Event date: {session.event['EventDate']}")
    print(f"Session: {session.name}")
    
    print("\nResults:\n", session.results.head())
    
    print("\nLaps:\n", session.laps.head())


def column_names(session) -> None:
    
    #get the column names of the results and laps dataframes
    
    print("Results columns:\n", session.results.columns)
    print("\nLaps columns:\n", session.laps.columns)
    
#this function will be used to extract colums from results that will help preduct winners 
def extract_useful_colums_results_race(session) -> None:
    
    #driver id
    print("\nDriver IDs:\n", session.results.get("DriverId"))
    
    #position final
    print("\nPositions:\n", session.results.get("Position"))
    
    #grid position <-- imporatant ??
    print("\nGrid positions:\n", session.results.get("GridPosition"))
    
    #points
    print("\nPoints:\n", session.results.get("Points"))
    
    
    
#fast extraction of cache, saves time and bandwith
def store_cache() -> None:
    
    #store cache in a folder called "cache"
    fastf1.Cache.enable_cache("cache")
    

#if this file is being run directly, call the main function
#otherwise, dont run main() 
if __name__ == "__main__":
    
    #load race
    test_session = fastf1.get_session(2021, "Spanish Grand Prix", "R")
    test_session.load()
    
    #store the file in cache
    store_cache()
    
    main(test_session)
    
    #wait 5 seonds for readability
    for i in range(5):
        print("Waiting... " + str(i + 1) + " seconds...")
        time.sleep(1)
    
    column_names(test_session)
    
    extract_useful_colums_results_race(test_session)