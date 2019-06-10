import unittest
from api import api_classes
from datetime import datetime
import json

test_date = datetime.strptime('2019-06-09 23:24:14', '%Y-%m-%d %H:%M:%S')
date_response = '{"day": "09", "month": "06", "year": "2019"}'
date_response_f = '{"day": "09", "month": "June", "year": "2019", "weekday": "Sunday"}'

time_response_n_m_n_f = '{"hour": "11", "minute": "24", "pm": true}'
time_response_n_m_f = '{"hour": "11", "minute": "24", "pm": true, "second": "14"}'
time_response_m_n_f = '{"hour": "23", "minute": "24"}'
time_response_m_f = '{"hour": "23", "minute": "24", "second": "14"}'


class TestDateTimeApi(unittest.TestCase):

    def test_date_api(self):
        req_data = dict()
        request_obj = api_classes.construct_request("date", req_data)
        self.assertEqual(request_obj.full, False, "Should be set to False")

        req_data = {"full":"true"}
        request_obj = api_classes.construct_request("date", req_data)
        self.assertEqual(request_obj.full, True, "Should be set to True")

        req_data = {"full": "false"}
        request_obj = api_classes.construct_request("date", req_data)
        self.assertEqual(request_obj.full, False, "Should be set to False")

        req_data = {"random": "true"}
        request_obj = api_classes.construct_request("date", req_data)
        self.assertEqual(request_obj.full, False, "Should be set to False")

        response_obj = api_classes.construct_response("date", request_obj, test_date)
        self.assertEqual(response_obj.day, "09", "Day Should be set to 09")
        self.assertEqual(response_obj.year, "2019", "Year Should be set to 2019")
        self.assertEqual(response_obj.month_no, "06", "Month no Should be set to 06")
        self.assertEqual(response_obj.month, "June", "Month Should be set to June")
        self.assertEqual(response_obj.weekday, "Sunday", "Weekday Should be set to Sunday")

        request_obj.full = True
        resp_dict = response_obj.to_dict(request_obj)
        self.assertEqual("weekday" in resp_dict, True, "Weekday Should be present in Dict")
        self.assertEqual(resp_dict["weekday"], "Sunday", "Weekday Should be set to Sunday")
        self.assertEqual(resp_dict["day"], "09", "Day Should be set to 09")
        self.assertEqual(resp_dict["month"], "June", "Month Should be set to June")
        self.assertEqual(resp_dict["year"], "2019", "Year Should be set to 2019")

        self.assertEqual(json.dumps(resp_dict), date_response_f, "Should be equal")

        request_obj.full = False
        response_obj = api_classes.construct_response("date", request_obj, test_date)
        resp_dict = response_obj.to_dict(request_obj)
        self.assertEqual("weekday" in resp_dict, False, "Weekday Should not be present in Dict")
        self.assertEqual(resp_dict["month"], "06", "Month Should be set to 06")
        self.assertEqual(json.dumps(resp_dict), date_response, "Should be equal")

    def test_time_api(self):
        req_data = dict()
        request_obj = api_classes.construct_request("time", req_data)
        self.assertEqual(request_obj.full, False, "Should be set to False")
        self.assertEqual(request_obj.military, False, "Should be set to False")

        req_data = {"full":"true"}
        request_obj = api_classes.construct_request("time", req_data)
        self.assertEqual(request_obj.full, True, "Should be set to True")
        self.assertEqual(request_obj.military, False, "Should be set to False")

        req_data = {"full": "false", "military":"true"}
        request_obj = api_classes.construct_request("time", req_data)
        self.assertEqual(request_obj.full, False, "Should be set to False")
        self.assertEqual(request_obj.military, True, "Should be set to True")

        req_data = {"full": "true", "military":"true"}
        request_obj = api_classes.construct_request("time", req_data)
        self.assertEqual(request_obj.full, True, "Should be set to True")
        self.assertEqual(request_obj.military, True, "Should be set to True")

        req_data = {"full": "true", "military":"false"}
        request_obj = api_classes.construct_request("time", req_data)
        self.assertEqual(request_obj.full, True, "Should be set to True")
        self.assertEqual(request_obj.military, False, "Should be set to False")

        response_obj = api_classes.construct_response("time", request_obj, test_date)
        self.assertEqual(response_obj.hour, "11", "Hour Should be set to 11")
        self.assertEqual(response_obj.hour_m, "23", "Hour_M Should be set to 23")
        self.assertEqual(response_obj.minute, "24", "Minute no Should be set to 24")
        self.assertEqual(response_obj.second, "14", "Second Should be set to 14")
        self.assertEqual(response_obj.pm, True, "PM Should be set to True")

        request_obj.full = True
        request_obj.military = True
        resp_dict = response_obj.to_dict(request_obj)
        self.assertEqual("pm" in resp_dict, False, "PM Should not be present in Dict")
        self.assertEqual(resp_dict["hour"], "23", "Hour Should be set to 23")
        self.assertEqual(resp_dict["minute"], "24", "Minute Should be set to 24")
        self.assertEqual(resp_dict["second"], "14", "Second Should be set to 14")
        self.assertEqual(json.dumps(resp_dict), time_response_m_f, "Should be equal")

        request_obj.full = False
        request_obj.military = True
        response_obj = api_classes.construct_response("time", request_obj, test_date)
        resp_dict = response_obj.to_dict(request_obj)
        self.assertEqual("pm" in resp_dict, False, "PM Should not be present in Dict")
        self.assertEqual("second" in resp_dict, False, "Second Should not be present in Dict")
        self.assertEqual(resp_dict["hour"], "23", "Hour Should be set to 23")
        self.assertEqual(resp_dict["minute"], "24", "Minute Should be set to 24")
        self.assertEqual(json.dumps(resp_dict), time_response_m_n_f, "Should be equal")

        request_obj.full = True
        request_obj.military = False
        response_obj = api_classes.construct_response("time", request_obj, test_date)
        resp_dict = response_obj.to_dict(request_obj)
        self.assertEqual("pm" in resp_dict, True, "PM Should be present in Dict")
        self.assertEqual("second" in resp_dict, True, "Second Should be present in Dict")
        self.assertEqual(resp_dict["hour"], "11", "Hour Should be set to 11")
        self.assertEqual(resp_dict["minute"], "24", "Minute Should be set to 24")
        self.assertEqual(resp_dict["second"], "11", "Second Should be set to 11")
        self.assertEqual(resp_dict["pm"], True, "pm Should be set to True")
        self.assertEqual(json.dumps(resp_dict), time_response_n_m_f, "Should be equal")

        request_obj.full = False
        request_obj.military = False
        response_obj = api_classes.construct_response("time", request_obj, test_date)
        resp_dict = response_obj.to_dict(request_obj)
        self.assertEqual("pm" in resp_dict, True, "PM Should be present in Dict")
        self.assertEqual("second" in resp_dict, False, "Second Should not be present in Dict")
        self.assertEqual(resp_dict["hour"], "11", "Hour Should be set to 11")
        self.assertEqual(resp_dict["minute"], "24", "Minute Should be set to 24")
        self.assertEqual(resp_dict["pm"], True, "pm Should be set to True")
        self.assertEqual(json.dumps(resp_dict), time_response_n_m_n_f, "Should be equal")

if __name__ == '__main__':
    unittest.main()