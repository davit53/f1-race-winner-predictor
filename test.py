from pathlib import Path
import pandas as pd
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

    useful_race_results = extract_useful_columns_results_race(session)
    print("\nUseful race result columns:\n", useful_race_results.head(20))
    
    useful_laps_results = extract_useful_columns_laps_race(session)
    print("\nUseful laps columns:\n", useful_laps_results.head(20))


def column_names(session) -> None:
    
    #get the column names of the results and laps dataframes
    
    print("Results columns:\n", session.results.columns)
    print("\nLaps columns:\n", session.laps.columns)
    
#this function extracts useful race result columns for later analysis
def extract_useful_columns_results_race(session):
    useful_columns = [
        "DriverId",
        "FullName",
        "TeamName",
        "GridPosition",
        "Position",
        "Points",
        "Status",
    ]
    return session.results[useful_columns].copy()
    
def extract_useful_columns_laps_race(session):
    
    useful_columns = [
        "Driver",
        "LapNumber",
        "LapTime",
        "Stint",
        "Compound",
    ]
    return session.laps[useful_columns].copy()

    
#fast extraction of cache, saves time and bandwith
def store_cache() -> None:
    
    #store cache in a folder called "cache"
    fastf1.Cache.enable_cache("cache")
    

#if this file is being run directly, call the main function
#otherwise, dont run main() 
if __name__ == "__main__":
    
    #library setup
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    
    #load race
    test_session = fastf1.get_session(2021, "Spanish Grand Prix", "R")
    test_session.load()
    
    #store the file in cache
    store_cache()
    
    main(test_session)
    
    #wait 5 seonds for readability
    # for i in range(5):
    #     print("Waiting... " + str(i + 1) + " seconds...")
    #     time.sleep(1)
    
    #column_names(test_session)
    
    
