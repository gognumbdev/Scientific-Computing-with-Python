def add_time(start, duration,starting_day=""):
    # 1.Initialization
    # start time
    start_list = start.split(":")
    start_list_second = start_list[1].split(" ")
    start_time = {"hour":start_list[0],"minute":start_list_second[0],"period":start_list_second[1]}
    # duration 
    dur_hour,dur_minute = duration.split(":")
    duration_value ={"hour":dur_hour,"minute":dur_minute}
    starting_day = starting_day.lower()
  
    number_day={
        1:"monday",
        2:"tuesday",
        3:"wednesday",
        4:"thursday",
        5:"friday",
        6:"saturday",
        7:"sunday",
    }

    day_number={
        "monday":1,
        "tuesday":2,
        "wednesday":3,
        "thursday":4,
        "friday":5,
        "saturday":6,
        "sunday":7,
    }
    
    # 2.Calculation
    sum_hour = int(start_time["hour"])+int(duration_value["hour"])
    sum_minute = int(start_time["minute"])+int(duration_value["minute"])
    remain_minute = sum_minute%60
    
    if(sum_minute>=60):
        sum_hour += sum_minute//60

    cal_time = {"sum_hour":sum_hour,"remain_minute":remain_minute}    

    # 3.Process time and date
    pass_period = cal_time["sum_hour"] // 12
    final_hour = cal_time["sum_hour"] % 12
    reamin_minute = cal_time["remain_minute"]
    reamin_minute_str = str( "0"+str(reamin_minute) if reamin_minute<10 else reamin_minute)
    final_hour_str = str( 12 if final_hour == 0 else final_hour)
    final_time = final_hour_str+":"+reamin_minute_str
    number_of_surpass_day = pass_period//2

    if(start_time["period"] == "AM"):
        if (pass_period%2 == 0):
            final_time += " AM"
        else:
            final_time += " PM"
        
        # On what day in 1 week
        if (starting_day):
            if(pass_period==1):
                final_time += ", "+starting_day.capitalize() 
            else:
                surpass_day_in_week = number_of_surpass_day%7 
                day_until_end_week = (7-day_number[starting_day])
                onDay = ""
                if (surpass_day_in_week<=day_until_end_week) :
                    onDay = number_day[surpass_day_in_week+day_number[starting_day]]
                elif (surpass_day_in_week>day_until_end_week) :
                    onDay = number_day[surpass_day_in_week-day_until_end_week]
                final_time += ", "+onDay.capitalize()

        # days later
        if (pass_period>1):
            if(pass_period==2):
                final_time += " (next day)"
            else:
                final_time += " (" + str(number_of_surpass_day) + " days later)"
            
    else :
        number_of_surpass_day += 1 if pass_period%2!=0 else 0
        if (pass_period%2 == 0):
            final_time += " PM"
        else:
            final_time += " AM"
        # On what day in 1 week
        if (starting_day):
            if(pass_period<1):
                final_time += ", "+starting_day.capitalize() 
            else:
                surpass_day_in_week = number_of_surpass_day%7 
                day_until_end_week = 7-day_number[starting_day]
                onDay = ""
                if (surpass_day_in_week<=day_until_end_week) :
                    onDay = number_day[surpass_day_in_week+day_number[starting_day]]
                elif (surpass_day_in_week>day_until_end_week) :
                    onDay = number_day[surpass_day_in_week-day_until_end_week]
                final_time += ", "+onDay.capitalize()
        # days later
        if (pass_period>0):
            if(pass_period==1):
                final_time += " (next day)"
            else:
                final_time += " (" + str(number_of_surpass_day) + " days later)"
    
    # 4.Feedback Result
    return final_time


result = add_time("8:16 PM", "466:02")
print(result)