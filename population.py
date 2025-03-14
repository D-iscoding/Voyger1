secs_year = 365 * 24 * 60 * 60  # Total seconds in a year
start_pop = 307357870
births = secs_year / 7
deaths = secs_year / 13
immigrations = secs_year / 35
end_pop = start_pop + births - deaths + immigrations

print("Future population in 1 year will be", end_pop)
