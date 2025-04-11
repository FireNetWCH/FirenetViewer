import src.db_function.db_email_function as db_email
from PySide6.QtWidgets import QTableWidgetItem,QVBoxLayout,QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import datetime
import matplotlib.dates as mdates
import numpy as np

import pandas as pd
def load_stat(parent,connect):
    best_recipients = db_email.get_best_recipients(connect)
    parent.ui.bestRecipientsTable
    table = parent.ui.bestRecipientsTable
    table.setRowCount(len(best_recipients))
    table.setColumnCount(2)
    table.setHorizontalHeaderLabels(["Email", "Liczba wiadomości"])

    for row, (email, count) in enumerate(best_recipients):
        table.setItem(row, 0, QTableWidgetItem(email))
        table.setItem(row, 1, QTableWidgetItem(str(count)))

    table.resizeColumnsToContents()

    group_date = db_email.get_grup_data(connect)
    df = pd.DataFrame(group_date, columns=['date', 'count'])
    date_list = df['date'].tolist()
    count_list = df['count'].tolist()
    #print(group_date)

    # figure = Figure(figsize=(8, 4))
    # canvas = FigureCanvas(figure)
    # layout = QVBoxLayout()
    # layout.addWidget(canvas)
    # parent.ui.timeLineWiget.setLayout(layout)
    # ax = figure.add_subplot(111)
    # ax.bar(date_list, count_list, width=2, color='skyblue')
    # ax.set_xlabel("Data")
    # ax.set_ylabel("Liczba wiadomości")
    # ax.set_title("Histogram wiadomości wg daty")
    # ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # figure.autofmt_xdate()
    # canvas.draw()
    date_nums = mdates.date2num(df['date'])
    counts, bins = np.histogram(date_nums, bins=50)
    bin_centers = 0.5 * (bins[1:] + bins[:-1])
    figure = Figure(figsize=(10, 4))
    figure.clf()
    figure.clear()
    canvas = FigureCanvas(figure)
    old_layout = parent.ui.timeLineWiget.layout()
    if old_layout is not None:

        while old_layout.count():
            item = old_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

 
    QWidget().setLayout(old_layout)
    layout = QVBoxLayout()
    layout.addWidget(canvas)
    parent.ui.timeLineWiget.setLayout(layout)
    ax = figure.add_subplot(111)
    ax.bar(bin_centers, counts, width=np.diff(bins), align='center', color='skyblue', edgecolor='black')
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    figure.autofmt_xdate()
    ax.set_xlabel("Data")
    ax.set_ylabel("Liczba wiadomości")
    ax.set_title("Histogram wiadomości (50 równych przedziałów czasu)")
    canvas.draw()
   
    
    all_attachments = db_email.get_all_attachment(connect)
    #at = pd.DataFrame(all_attachments, columns=['id', 'attachment_name','email_id'])
    #len(all_attachments)
    parent.ui.attachmentsCountLabel.setText(str(len(all_attachments)))
    all_recipients = db_email.get_all_recipients_by_group(connect)
    parent.ui.recipientsCountLabel.setText(str(len(all_recipients)))
    all_email = db_email.get_count_email(connect)
    parent.ui.emailCountLablel.setText(str(all_email[0][0]))
   


