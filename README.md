# **Profile**

## **BSProfile**
- id `str`
- handle `str`
- email `str`
- dob `datetime`
- current `str`
- image `str`
- name `BSProfileName`
- location `BSProfileLocation`

## **BSProfileName**
- firstname `str`
- lastname `str`

## **BSProfileLocation**
- postcode `int`

# **Venue**

## **BSVenue**
- id `str`
- name `str`
- description `str`
- online `bool`
- order_method `str`
- trending `bool`
- admin `str`
- pid `str`
- address `BSVenueAddress`
- media `BSVenueMedia`

## **BSVenueAddress**
- street `str`
- suburb `str`
- state `str`
- postcode `int`
- coords `BSVenueGeopoint`

## **BSVenueMedia**
- primary `str`
- additional `[str]`

## **BSVenueGeopoint**
- latitude `latitude`
- longitude `longitude`

# **Order**

## **BSOrder**
- id `str`
- order_pid `str`
- reference `str`
- total `int`
- created_time `datetime`
- completed_time `datetime`
- profile `BSProfile`
- venue `BSVenue`
