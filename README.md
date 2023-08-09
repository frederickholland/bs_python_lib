# Profile

## BSProfile
- id `str`
- handle `str`
- email `str`
- dob `datetime`
- current `str`
- image `str`
- name [`BSProfileName`](#bsprofilename)
- location [`BSProfileLocation`](#bsprofilelocation)

## BSProfileName
- firstname `str`
- lastname `str`

## BSProfileLocation
- postcode `int`

---

# Venue

## BSVenue
- id `str`
- name `str`
- description `str`
- online `bool`
- order_method `str`
- trending `bool`
- admin `str`
- pid `str`
- address [`BSVenueAddress`](#bsvenueaddress)
- media [`BSVenueMedia`](#bsvenuemedia)

## BSVenueAddress
- street `str`
- suburb `str`
- state `str`
- postcode `int`
- coords [`BSVenueGeopoint`](#bsvenuegeopoint)

## BSVenueMedia
- primary `str`
- additional `[str]`

## BSVenueGeopoint
- latitude `float`
- longitude `float`

# Order

## BSOrder
- id `str`
- order_pid `str`
- reference `str`
- total `int`
- created_time `datetime`
- completed_time `datetime`
- profile [`BSProfile`](#bsprofile)
- venue [`BSVenue`](#bsvenue)