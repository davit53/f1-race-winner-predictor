from pathlib import Path
import time

import fastf1

#main function, we return nothing
def main() -> None:
    
    #use cache folder for stroing downloaded data, this will speed up future runs
    fastf1.Cache.enable_cache("cache")

    #get and load the session
    test_session = fastf1.get_session(2021, "Spanish Grand Prix", "R")
    test_session.load()

    #print the session information
    print(f"Event: {test_session.event['EventName']}")
    print(f"Event date: {test_session.event['EventDate']}")
    print(f"Session: {test_session.name}")
    
    print("\nResults:\n", test_session.results.head())
    
    print("\nLaps:\n", test_session.laps.head())


def column_names() -> None:
    
    #get the column names of the results and laps dataframes
    test_session = fastf1.get_session(2021, "Spanish Grand Prix", "R")
    test_session.load()
    
    print("Results columns:\n", test_session.results.columns)
    print("\nLaps columns:\n", test_session.laps.columns)

#if this file is being run directly, call the main function
#otherwise, dont run main() 
if __name__ == "__main__":
    main()
    
    #wait 5 seonds for readability
    for i in range(6):
        print("Waiting... " + str(i) + " seconds...")
        time.sleep(1)
    
    column_names()
    
