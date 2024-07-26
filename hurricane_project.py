# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def float_damages(damages):
  updated_damages = [
    float(d.strip("BM")) * conversion[d[-1]] if d != "Damages not recorded" else d for d in damages
  ]
  return updated_damages
# test function by updating damages
updated_damages = float_damages(damages)
# 2 
# Create a Table

def hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricanes = {}
  for i in range(len(names)):
    hurricane_info = {
      "Name": names[i],
      "Month": months[i],
      "Year": years[i],
      "Max Sustained Wind": max_sustained_winds[i],
      "Areas Affected": areas_affected[i],
      "Damage": updated_damages[i],
      "Death": deaths[i]
    }
    hurricanes[names[i]] = hurricane_info
  return(hurricanes)
hurricanes = hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricanes)

# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key

def organize_by_year(hurricanes):
    cane_year_lib = {}
    for library in hurricanes:
        current_cane = hurricanes[library]
        current_year = current_cane['Year']
        
        if current_year not in cane_year_lib:
            cane_year_lib[current_year] = []
        
        cane_year_lib[current_year].append(current_cane)
    
    return cane_year_lib

organized_hurricanes = organize_by_year(hurricanes)
#print(organized_hurricanes)

# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in

def area_count(hurricanes):
    area_affected_count = {}
    for library in hurricanes:
        current_cane = hurricanes[library]
        current_affected_areas = current_cane['Areas Affected']
        
        for area in current_affected_areas:
            if area not in area_affected_count:
                area_affected_count[area] = 1
            else:
                area_affected_count[area] += 1
    
    return area_affected_count

area_cane_frequency = area_count(hurricanes)
#print(area_cane_frequency)


# 5 
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
def highest_freq_area(area_cane_frequency):
    highest_count = 0
    most_affected_areas = []
    
    for area, count in area_cane_frequency.items():
        if count > highest_count:
            highest_count = count
            most_affected_areas = [area]
        elif count == highest_count:
            most_affected_areas.append(area)
    
    return most_affected_areas, highest_count
most_affected_areas, highest_count = highest_freq_area(area_cane_frequency)
#print(f"The areas affected by the most hurricanes are {most_affected_areas} with a frequency of {highest_count} hurricanes each.")

# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
def cane_deaths(hurricanes):
    highest_death = 0
    deadliest_cane = None
    for hurricane_info in hurricanes.values():
        current_cane_death = hurricane_info.get('Death', 0)
        current_cane_name = hurricane_info.get('Name', 'Unknown')
        
        if current_cane_death > highest_death:
            highest_death = current_cane_death
            deadliest_cane = current_cane_name
    
    return deadliest_cane, highest_death
deadliest_cane, highest_death = cane_deaths(hurricanes)
#print(f"The deadliest hurricane was {deadliest_cane}, which had {highest_death} deaths.")


# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}

hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

def rate_cane_mortality(hurricanes):
  for hurricane in hurricanes.values():
    current_cane_death = hurricane.get('Death', 0)
    mortality_rating = 0
    
    # Sort mortality_scale items by threshold values in descending order
    for rating, threshold in sorted(mortality_scale.items(), reverse=True):
        if current_cane_death > threshold:
            # Once we find the appropriate rating, break out of the loop
            mortality_rating = rating + 1
            break

    hurricanes_by_mortality[mortality_rating].append(hurricane)
  return hurricanes_by_mortality

cane_mortality = rate_cane_mortality(hurricanes)
#print(cane_mortality)

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost

def find_max_damage(hurricanes):
  damage_max = 0
  for cane_library in hurricanes.values():
    current_cane = cane_library.get('Name')
    current_damage = cane_library.get('Damage', 0)
    if current_damage == "Damages not recorded":
      current_damage = float(0)
    if current_damage > damage_max:
      damage_max = current_damage
      cane_name = current_cane
  return cane_name, damage_max

cane_max_damage = find_max_damage(hurricanes)
print(cane_max_damage)


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def categorize_hurricanes_by_damage(hurricanes, damage_scale):
    cane_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    
    for hurricane in hurricanes.values():
        current_cane_name = hurricane.get('Name')
        current_cane_damage = hurricane.get('Damage', "Damages not recorded")
        
        if current_cane_damage != "Damages not recorded":
            for rating, threshold in sorted(damage_scale.items(), reverse=True):
                if current_cane_damage > threshold:
                    current_rating = rating + 1
                    break
            cane_damage[current_rating].append(hurricane)
        else:
            cane_damage[0].append(hurricane)  # Append to the 0 damage category if not recorded
    
    return cane_damage

hurricanes_by_damage = categorize_hurricanes_by_damage(hurricanes, damage_scale)
print(hurricanes_by_damage)
