import json
data_JSON = """
{
 "Telangana":"Hyderabad",
 "Maharastra":"Mumbai",
 "Karnataka":"Banglore",
 "Tamilnadu":"Chennai",
 "West Bangal":"Kolkata",
 "UttraPradesh":"Lucknow",
 "Goa":"Panaji"
}
"""
data_dict = json.loads(data_JSON)
