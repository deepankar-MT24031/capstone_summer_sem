import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QTableWidgetItem
from base_ui import Ui_MainWindow
import json


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initialize table
        # self.setup_table()

        self.setup_default_format()


    def setup_default_format(self):



        def open_json():
            try:
                with open('Default_format.json', 'r') as json_file:
                    data = json.load(json_file)
                print(f"Data extracted  {data}")
                return data
            except Exception as e:
                print(f"An error occurred while extracting data from the JSON file: {e}")
                return None


        def fill_number_of_beds(json_data):
            number_of_beds = json_data["default_Bed_count"]
            list_of_beds = []

            for i in range(1, number_of_beds + 1):
                list_of_beds.append(str(i))  # from 1 till number_of_beds

            self.comboBox.addItems(list_of_beds)

        def fill_number_of_sex_values(json_data):
            number_of_sex_values = json_data["default_Sex_count"]
            list_of_sex_titles = []

            for i in range(1, number_of_sex_values + 1):
                list_of_sex_titles.append(json_data["each_sex_value_names"][f'Sex_{str(i)}_name'])  # from 1 till number_of_beds

            self.comboBox_2.addItems(list_of_sex_titles)

        def fill_table_widget(json_data):

            self.tableWidget.setColumnCount(1)

            number_of_row_headers = json_data["default_table_rows_count"]

            row_header_name_list = [row["row_header_name"] for row in json_data["each_table_row_layout"].values()]

            row_header_description_list = [row["row_header_description"] for row in json_data["each_table_row_layout"].values()]

            self.tableWidget.setRowCount(number_of_row_headers)

            self.tableWidget.setVerticalHeaderLabels(row_header_name_list)



            print(row_header_name_list,row_header_description_list)

        json_data = open_json()
        fill_number_of_beds(json_data)
        fill_number_of_sex_values(json_data)
        fill_table_widget(json_data)

















    #     # Connect button
    #     self.pushButton_2.clicked.connect(self.add_row_header)
    #
    # def setup_table(self):
    #     # Set up table with sample columns
    #     self.tableWidget.setColumnCount(1)
    #     self.tableWidget.setRowCount(0)  # Start with no rows
    #
    #     # Set column headers
    #     headers = ['Value',]
    #     self.tableWidget.setHorizontalHeaderLabels(headers)
    #
    # def add_row_header(self):
    #     # Show input dialog
    #     row_header, ok = QInputDialog.getText(
    #         self,
    #         'Add Row Header',
    #         'Enter row header name:'
    #     )
    #
    #     if ok and row_header:  # If user clicked OK and entered text
    #         # Add new row
    #         current_row = self.tableWidget.rowCount()
    #         self.tableWidget.insertRow(current_row)
    #
    #         # Set row header
    #         self.tableWidget.setVerticalHeaderItem(
    #             current_row,
    #             QTableWidgetItem(row_header)
    #         )
    #
    #         # Initialize empty cells in the new row
    #         for col in range(self.tableWidget.columnCount()):
    #             self.tableWidget.setItem(
    #                 current_row,
    #                 col,
    #                 QTableWidgetItem('')
    #             )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())