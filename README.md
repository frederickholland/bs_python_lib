# Profile

## BSProfile {#bsprofile}
- id `str`
- handle `str`
- email `str`
- dob `datetime`
- current `str`
- image `str`
- name [`BSProfileName`](#bsprofilename)
- location []`BSProfileLocation`](#bsprofilelocation)

## BSProfileName {#bsprofilename}
- firstname `str`
- lastname `str`

## BSProfileLocation {#bsprofilelocation}
- postcode `int`

# Venue

## BSVenue {#bsvenue}
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

## BSVenueAddress {#bsvenueaddress}
- street `str`
- suburb `str`
- state `str`
- postcode `int`
- coords `BSVenueGeopoint`

## BSVenueMedia {#bsvenuemedia}
- primary `str`
- additional `[str]`

## BSVenueGeopoint {#bsvenuegeopoint}
- latitude `latitude`
- longitude `longitude`

# Order

## BSOrder {#bsorder}
- id `str`
- order_pid `str`
- reference `str`
- total `int`
- created_time `datetime`
- completed_time `datetime`
- profile `BSProfile`
- venue `BSVenue`
