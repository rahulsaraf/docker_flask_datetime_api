from collections import OrderedDict

class DateRequest:
    def __init__(self, full):
        self.full = full


class TimeRequest:
    def __init__(self, military, full):
        self.military = military
        self.full = full


class DateTimeRequest:
    def __init__(self, date_request, time_request):
        self.date_request = date_request
        self.time_request = time_request


class DateResponse:
    def __init__(self, day, month, month_no, year, weekday):
        self.day = day
        self.month = month
        self.month_no = month_no
        self.year = year
        self.weekday = weekday

    def to_dict(self, date_request):
        data_dict = OrderedDict()
        data_dict["day"] = self.day
        data_dict["month"] = self.month_no
        data_dict["year"] = self.year
        if date_request.full:
            data_dict["month"] = self.month
            data_dict["weekday"] = self.weekday
        return data_dict


class TimeResponse:
    def __init__(self, hour, hour_m, minute, pm, second):
        self.hour = hour
        self.hour_m = hour_m
        self.minute = minute
        self.pm = pm
        self.second = second

    def to_dict(self, time_request):
        data_dict = OrderedDict()
        data_dict["hour"] = self.hour_m
        data_dict["minute"] = self.minute
        if not time_request.military:
            data_dict["hour"] = self.hour
            data_dict["pm"] = self.pm
        if time_request.full:
            data_dict["second"] = self.second
        return data_dict


class DateTimeResponse:
    def __init__(self, date_response, time_response):
        self.date_response = date_response
        self.time_response = time_response

    def to_dict(self, date_time_request):
        data_dict = OrderedDict()
        data_dict["date"] = self.date_response.to_dict(date_time_request.date_request)
        data_dict["time"] = self.time_response.to_dict(date_time_request.time_request)
        return data_dict


def construct_request(req_type, json_data):
    if req_type == "date":
        return construct_date_request(json_data)
    if req_type == "time":
        return construct_time_request(json_data)
    if req_type == "datetime":
        return construct_date_time_request(json_data)
    return None


def construct_date_request(json_data):
    full = False
    if 'full' in json_data:
        full = json_data['full'] == 'true'
    return DateRequest(full)


def construct_time_request(json_data):
    military = False
    full = False
    if 'military' in json_data:
        military = json_data['military'] == 'true'
    if 'full' in json_data:
        full = json_data['full'] == 'true'
    return TimeRequest(military, full)


def construct_date_time_request(json_data):
    date_json_data = dict()
    time_json_data = dict()
    if 'date' in json_data:
        date_json_data = json_data['date']
    if 'time' in json_data:
        time_json_data = json_data['time']
    return DateTimeRequest(construct_date_request(date_json_data), construct_time_request(time_json_data))


def construct_response(resp_type, request, curr_date):
    if resp_type == "date":
        return construct_date_response(curr_date)
    if resp_type == "time":
        return construct_time_response(curr_date)
    if resp_type == "datetime":
        return construct_date_time_response(curr_date)


def construct_date_response(curr_date):
    weekday = curr_date.strftime("%A")
    month_no = curr_date.strftime("%m")
    month_str = curr_date.strftime("%B")
    year = curr_date.strftime("%Y")
    day = curr_date.strftime("%d")
    return DateResponse(day, month_str, month_no, year, weekday)


def construct_time_response(curr_date):
    hour = curr_date.strftime("%I")
    hour_m = curr_date.strftime("%H")
    minute = curr_date.strftime("%M")
    second = curr_date.strftime("%S")
    pm = curr_date.strftime("%p") == "PM"
    return TimeResponse(hour, hour_m, minute, pm, second)


def construct_date_time_response(curr_date):
    return DateTimeResponse(construct_date_response(curr_date), construct_time_response(curr_date))

