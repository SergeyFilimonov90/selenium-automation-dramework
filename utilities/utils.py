import openpyxl
import softest
import csv
import logging
import datetime
import os
import inspect



class Utils(softest.TestCase):
    file_name = "C:\\Users\\Elgyn\\selenium-python-automation-framework working\\automation.log"
    logger = None

    def assertListItemText(self, list, value):
        for stop in list:
            print("The text is: " + stop.text)
            self.soft_assert(self.assertEqual, stop.text, value)
            if stop.text == value:
                print("test passed")
            else:
                print("test failed")
        self.assert_all()

    @classmethod
    def write_log_to_file(cls, data: str):
        if cls.logger:
            cls.logger.debug(data)

    @classmethod
    def add_start_step(cls, method: str):
        if not cls.logger:
            cls.logger = cls.custom_logger(logLevel=logging.DEBUG)

        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Start name method: {method}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str):
        if not cls.logger:
            cls.logger = cls.custom_logger(logLevel=logging.DEBUG)

        data_to_add = f"End time: {str(datetime.datetime.now())}\n"
        data_to_add += f"End name method: {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)

    @staticmethod
    def custom_logger(logLevel=logging.DEBUG):
        # Set class/method name from where it's called
        logger_name = inspect.stack()[1][3]

        if not Utils.logger:
            logger = logging.getLogger(logger_name)
            logger.setLevel(logLevel)

            # Create file handler
            fh = logging.FileHandler(Utils.file_name, mode='w')

            # Create formatter
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s',
                                          datefmt='%m/%d/%Y %I:%M:%S %p')

            # Add formatter to file handler
            fh.setFormatter(formatter)

            # Add file handler to logger
            logger.addHandler(fh)

            Utils.logger = logger

        return Utils.logger

    def read_data_from_excel(file_path, sheet_name):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            for username, password in zip(row[::2], row[1::2]):
                data.append(username)
                data.append(password)
        return data

    def read_data_from_csv(filename):
        #Create an empty list
        datalist = []
        #Open CSV file
        csvdata = open(filename,"r")
        #Create CSV reader
        reader = csv.reader(csvdata)
        #skip header
        next(reader)
        #Add CSV rows to list
        for rows in reader:
            datalist.append(rows)
        return datalist


