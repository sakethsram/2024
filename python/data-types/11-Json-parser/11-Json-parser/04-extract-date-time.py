import datetime
import elapsed_time_str

# "2018-12-29T10:30:07.119045211Z"
def extract_date_time(str_datetime):
    (new_date, new_time) = str_datetime.split('T')
    print (f"str_datetime :{str_datetime}")
    print (f"new_date :{new_date}")
    print (f"new_time :{new_time}")
    
    yy, mm, dd = new_date.split('-')
    print (f"yy : {yy}, mm :{mm}, dd :{dd}")

    (hh, minu, sec) = new_time.split(':')
    sec, msec = sec.split('.')
    msec = msec.rstrip('Z')
    print (hh, minu, sec, msec)
    
    print(yy, mm, dd, hh, minu, sec, msec)
    t = int(msec)
    print(t)
    return(yy, mm, dd, hh, minu, sec, msec)

def get_elapsed_time_in_str(ptime, ctime):
    d1 = extract_date_time(ptime)
    d2 = extract_date_time(ctime)
    print(f"d1 :{d1}")
    print(f"d2 :{d2}")
    # str_elapsed_time = caliculate_diff(d1, d2)
    # print(str_elapsed_time)
    # return "hello"

    # extract_date_time(str_created_time)
    # retval = aura_date_time.get_docker_date_time_to_elapsed_str(str_created_time)
    # print(retval)
    return

def main():
    ptime = "2018-05-15T10:30:07.119045211Z"
    ctime = "2018-05-30T10:30:07.119045211Z" # 15 Days ago
    ctime = "2018-05-15T12:30:07.119045211Z" # 2 Hours ago
    ctime = "2018-05-15T10:55:07.119045211Z" # 25 Minutes ago
    ctime = "2018-05-15T10:30:27.119045211Z" # 20 Seconds ago

    get_elapsed_time_in_str(ptime, ctime)
    retval = elapsed_time_str.get_elapsed_time_in_str(ptime)
    print(retval)
    
if (__name__ == "__main__"):
    main()

