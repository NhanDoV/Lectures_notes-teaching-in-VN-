# Load lubridate
library(lubridate)

# Load the other packages
library(anytime)
library(hms)
library(readr)

# Get the current date with today()
today() 

# Get the current datetime including timezone with now()
now()

# ================================= Automatic parsing ==========================================
# The following uses the anytime package
# Automatically parse dates in multiple formats with anydate()
anydate(c("Jun 16, 1915", "18 October 1919")) # "1915-06-16" "1919-10-18"

# Automatically parse datetimes in multiple formats with anytime()
anytime(c("22 Nov 1963 13:30", "September 15 1901 02:15"), tz = "EST") # "1963-11-22 13:30:00 EST" "1901-09-15 02:15:00 EST"

# =================================== Manual parsing ===========================================
# Parse dates in year, month, day format with ymd()
ymd("1759 09 22") # "1759-09-22"

# Parse dates in month, day, year format with mdy()
mdy("05-12-1820") # "1820-05-12"

# Parse dates in day, month, year format with dmy()
dmy("01/09/1835") # "1835-09-01"

# Parse datetimes in ISO format
ymd_hms("1972-06-30 23:59:59") # "1972-06-30 23:59:59 UTC"

# Parse datetimes in a single format with fast_strptime()
fast_strptime("January 1, 1924", "%B %d, %Y") # "1924-01-01 UTC"

# Parsing datetimes in multiple specified formats with parse_date_time()
parse_date_time(c("Jun 16, 1915", "18 October 1919"),
                c("%b %d, %Y", "%d %B %Y")) # Returns "1915-06-16 UTC" "1919-10-18 UTC"

# ================================= Parsing times =======================================
# Parse times without dates
hms(56,12,15) # Returns 15:12:5

# ================= Making dates and datetimes from components ==========================
# Make dates from components with make_date()
make_date(1777, 4, 30) # "1777-04-30"

# Make datetimes from components with make_datetime()
make_datetime(1945, 6, 16, 05, 29, 21, tz = "US/Mountain") # "1945-06-16 05:29:21 MWT"

# ============================= Extracting components ====================================
# Extract the year from a date or datetime with year()
year("1923-12-11") # 1923

# Extract the day of the year from a date or datetime with yday()
yday("1900-10-14") # 287

# Extract the month or month name from a date or datetime with month()
month("1857-03-27", label = TRUE) # Mar

# Extract the day of the week from a date or datetime with wday()
wday("1890-02-17", label = TRUE) # Mon

# ======================================= Time zones =======================================
# Get the current timezone
Sys.timezone() # "Asia/Kuala_Lumpur"

# List all known timezones
OlsonNames() # "Africa/Abidjan" ... "Zulu"

# Specify a datetime that has a location-based timezone
ymd_hms("1915-04-25 12:00:00", tz = "Australia/Eucla") # "1915-04-25 12:00:00 +0845"

# Specify a datetime that has a UTC offset timezone
ymd_hms("1915-04-25 12:00:00 +08:45") 3 "1915-04-25 03:15:00 UTC"

# Use a different timezone for a datetime with with_tz()
with_tz(ymd_hms("1915-04-25 09:00:00", tz = "Asia/Kuala_Lumpur"), "America/Chicago") 
# Returns "1915-04-24 20:00:00 CDT"

# Override the timezone for a datetime with force_tz()
force_tz(ymd_hms("1915-04-25 09:00:00", tz = "Asia/Kuala_Lumpur"), "America/Chicago") 
# Returns "1915-04-25 09:00:00 CDT"

# ==================================== Time intervals ==================================
# Some points in time
start_of_time1 <- ymd("1970-01-01")
end_of_time1 <- ymd("2012-12-21")
start_of_time2 <- ymd("2001-01-01")
end_of_time2 <- ymd("2019-12-12")

# Specify the interval between two datetimes with interval()
intrvl1 <- interval(start_of_time1, end_of_time1) # 1970-01-01 UTC--2012-12-21 UTC

# Determine the length of an interval in seconds with int_length()
int_length(intrvl1) # 1356048000

# Determine the overlap between two intervals with intersect()
intrvl2 <- interval(start_of_time2, end_of_time2)
intersect(intrvl1, intrvl2) # 2001-01-01 UTC--2012-12-21 UTC

# ---------------------------- Periods and durations -----------------------------------
# Define a period in years
years(2) # "2y 0m 0d 0H 0M 0S"

# Define a duration in years
dyears(2) # "63115200s (~2 years)"

# Intervals for a leap year and non-leap year
leap <- interval("2020-01-01", "2021-01-01")
non_leap <- interval("2021-01-01", "2022-01-01")

# Convert an interval to a period with as.period()
as.period(leap) # "1y 0m 0d 0H 0M 0S"
as.period(non_leap) # "1y 0m 0d 0H 0M 0S"

# Convert an interval to a duration with as.duration()
as.duration(leap) # "31622400s (~1 years)"
as.duration(non_leap) # "31536000s (~52.14 weeks)"

# --------------------------------- Date arithmetic -----------------------------------
# Subtract a historical date from today
today() - ymd("2000-02-29") # Time difference of 8291 days

# Start with a day before a timezone change and add a period of one day
ymd("2022-11-06", tz = "America/New_York") + days(1) # "2022-11-07 EST"

# Start with a day before a timezone change and add a duration of one day
ymd("2022-11-06", tz = "America/New_York") + ddays(1) # "2022-11-06 23:00:00 EST"

# --------------------------------- Rounding dates -------------------------------------
# Round dates to the nearest time unit
round_date(ymd("2004-10-04"), "week")

# Round dates to the previous time unit
floor_date(ymd("2004-10-04"), "week")

# Round dates to the next time unit
ceiling_date(ymd("2004-10-04"), "week")