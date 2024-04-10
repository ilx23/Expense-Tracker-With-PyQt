# Import necessary modules
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QPushButton, \
    QDialog, QLabel, QLineEdit, QHBoxLayout, QMessageBox, QComboBox, QDateEdit
from PyQt5.QtCore import QDate, Qt


# Dialog window for adding a new expense
class ExpenseWindow(QDialog):
    def __init__(self):
        super().__init__()
        # Set window title
        self.setWindowTitle("Add Expense")

        # Date entry field
        self.date_edit = QDateEdit(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)

        # Category selection dropdown
        self.category_edit = QComboBox()
        self.category_edit.addItems(["Food", "Transportation", "Shopping", "Entertainment", "Others"])
        self.category_edit.setFont(QFont("arial", 9))

        # Amount entry field
        self.amount_entry = QLineEdit()
        self.amount_entry.setFont(QFont("arial", 10))

        # Save button
        self.save_button = QPushButton("Save")
        self.save_button.setFont(QFont("arial", 11))
        self.save_button.clicked.connect(self.save_expense)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.date_edit)
        layout.addWidget(self.category_edit)
        layout.addWidget(self.amount_entry)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    # Method to save expense details
    def save_expense(self):
        date = self.date_edit.date().toString("yyyy-MM-dd")
        category = self.category_edit.currentText()
        amount = self.amount_entry.text()

        # Check if amount is valid
        if amount and amount.isdigit():
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Make sure you have entered a number for your amount")


# Main window of the expense tracker application
class ExpenseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # Initialize UI components
    def initUI(self):
        self.setWindowTitle('Expense Tracker')
        self.setGeometry(100, 100, 600, 400)

        # Title label
        self.app_title = QLabel('Expense Tracker')
        title_font = QFont("nectar bold", 14)
        self.app_title.setFont(title_font)
        self.app_title.setAlignment(Qt.AlignCenter)
        self.app_title.setContentsMargins(0, 0, 0, 10)

        # Expense list widget
        self.expense_list = QListWidget()
        self.setFont(QFont("arial", 11))

        # Buttons for adding, editing, and deleting expenses
        self.add_expense_button = QPushButton('Add Expense')
        self.edit_expense_button = QPushButton('Edit Expense')
        self.delete_expense_button = QPushButton('Delete')

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.app_title)
        layout.addWidget(self.expense_list)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_expense_button)
        button_layout.addWidget(self.edit_expense_button)
        button_layout.addWidget(self.delete_expense_button)
        layout.addLayout(button_layout)

        self.add_expense_button.clicked.connect(self.add_expense)
        self.edit_expense_button.clicked.connect(self.edit_expense)
        self.delete_expense_button.clicked.connect(self.delete_expense)

        self.setLayout(layout)

    # Method to add a new expense
    def add_expense(self):
        dialog = ExpenseWindow()
        if dialog.exec_():
            date = dialog.date_edit.date().toString("yyyy-MM-dd")
            category = dialog.category_edit.currentText()
            amount = dialog.amount_entry.text()
            self.expense_list.addItem(f"{date} - {category} - ${amount}")

    # Method to edit an existing expense
    def edit_expense(self):
        selected_item = self.expense_list.currentItem()
        if selected_item:
            dialog = ExpenseWindow()
            if dialog.exec_():
                date = dialog.date_edit.date().toString("yyyy-MM-dd")
                category = dialog.category_edit.currentText()
                amount = dialog.amount_entry.text()
                selected_item.setText(f"{date} - {category} - ${amount}")
        else:
            QMessageBox.warning(self, "Error", "You haven't selected any item to edit")

    # Method to delete an expense
    def delete_expense(self):
        selected_item = self.expense_list.currentItem()
        if selected_item:
            self.expense_list.takeItem(self.expense_list.row(selected_item))
        else:
            QMessageBox.warning(self, "Error", "You haven't selected any item to delete")


# Entry point of the application
def main():
    app = QApplication(sys.argv)
    ex_tacker = ExpenseTracker()
    ex_tacker.show()
    sys.exit(app.exec_())


# Execute the main function if the script is run directly
if __name__ == '__main__':
    main()
