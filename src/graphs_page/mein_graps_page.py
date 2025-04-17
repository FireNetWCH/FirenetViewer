import src.db_function.db_email_function as db_email
from PySide6.QtWidgets import QTableWidgetItem,QVBoxLayout,QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtCharts import QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PySide6.QtWidgets import QVBoxLayout, QWidget,QSizePolicy,QScrollArea
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QDateTime
from matplotlib.figure import Figure
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import numpy as np
from collections import defaultdict
import pandas as pd
import networkx as nx
from pyvis.network import Network
import os
import sys
import logging
import matplotlib as plt
from PySide6.QtCore import Qt
import matplotlib.dates as mdates
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def get_resource_path(relative_path):
    """Zwraca poprawną ścieżkę do zasobów, obsługując tryb onefile"""
    if getattr(sys, 'frozen', False):  
        base_path = sys._MEIPASS  
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def load_stat(parent,connect):
    try:
        # QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
        propaply_onwer = db_email.get_propaply_email_owner_data(connect)
        #print(propaply_onwer)
        parent.ui.nameLabel.setText(propaply_onwer[0][0])
        parent.ui.emailLabel.setText(propaply_onwer[0][1])
        best_sender = db_email.get_best_recipients(connect,propaply_onwer[0][0],propaply_onwer[0][1],1)
        best_recipients = db_email.get_best_recipients(connect,propaply_onwer[0][0],propaply_onwer[0][1],0)
        emails = defaultdict(lambda: [0, 0])
        for email, sender_count, recipients_count in best_sender:
            emails[email][0] += sender_count
            emails[email][1] += recipients_count


        for email, sender_count, recipients_count in best_recipients:
            emails[email][0] += sender_count
            emails[email][1] += recipients_count

        concat_list = [(email, dane[0], dane[1]) for email, dane in emails.items()]

        # table = parent.ui.bestRecipientsTable
        # table.setRowCount(len(concat_list))
        # table.setColumnCount(3)
        


        # for row, (email, count,count_2) in enumerate(concat_list):
        #     table.setItem(row, 0, QTableWidgetItem(email))
        #     table.setItem(row, 1, QTableWidgetItem(str(count_2)))
        #     table.setItem(row, 2, QTableWidgetItem(str(count)))

        # table.resizeColumnsToContents()

        # graph_widget = parent.ui.graphWidget
        # grapg_layout = QVBoxLayout()
        # G = nx.DiGraph()
        # G.add_node(propaply_onwer[0][1])
        # for email, count_sent, count_received in concat_list:
        #     G.add_node(email)
        #     if count_sent > 0:
        #         G.add_edge(propaply_onwer[0][1], email, weight=count_sent)
        #     if count_received > 0:
        #         G.add_edge(email, propaply_onwer[0][1], weight=count_received)

        # pos = nx.spring_layout(G, center=(0, 0), seed=42,k=1.5)
        # edge_labels = nx.get_edge_attributes(G, 'weight')

        # fig, ax = plt.subplots(figsize=(8, 6))
        # nx.draw(G, pos, ax=ax,with_labels=True, node_color='lightblue',node_size=200, arrows=True, font_size=9)
        
        # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
        # canvas = FigureCanvas(fig)
        # grapg_layout.addWidget(canvas)
        # graph_widget.setLayout(grapg_layout)

        #$$$$$$$$$$$$$$$$$$$$$
        
        graph_widget = parent.ui.widget_30
        graph_layout = QVBoxLayout()
        G = nx.DiGraph()
        central_node = propaply_onwer[0][1]
        G.add_node(central_node)

        for email, count_sent, count_received in concat_list:
            G.add_node(email)
            if count_sent > 0:
                G.add_edge(central_node, email, title=f"Wyslano: {count_sent}",label=f"W: {count_sent}")
            if count_received > 0:
                G.add_edge(email, central_node,title=f"Odebrano: {count_received}",label=f"O: {count_received}")

        net = Network(height='100%', width='100%', directed=True, notebook=False,cdn_resources='in_line')
        net.from_nx(G)
        net.set_options("""
    {
    "physics": {
        "barnesHut": {
        "gravitationalConstant": -2500,
        "centralGravity": 0.2,
        "springLength": 200,
        "springConstant": 0.04,
        "damping": 0.09,
        "avoidOverlap": 1
        },
        "stabilization": {
        "enabled": true,
        "iterations": 200
        }
    },
    "layout": {
        "improvedLayout": true
    },
    "edges": {
        "arrows": {
        "to": { "enabled": true }
        },
        "font": {
        "align": "middle"
        },
        "width": 2
    },
    "nodes": {
        "shape": "dot",
        "size": 20
    }
    }
    """)
        html_path = os.path.abspath(get_resource_path("graph.html"))
        html = net.generate_html()  

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        view = QWebEngineView()
        view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # view.reload()
        url = QUrl.fromLocalFile(html_path)
        # url.setQuery(f"t={QDateTime.currentDateTime().toMSecsSinceEpoch()}")

        view.load(url)
        # view.reload()
        
        graph_layout = parent.ui.widget_30.layout()
        if graph_layout is None:
            graph_layout = QVBoxLayout(parent.ui.widget_30)
            parent.ui.widget_30.setLayout(graph_layout)
        for i in reversed(range(graph_layout.count())):
            widget_to_remove = graph_layout.itemAt(i).widget()
            print(widget_to_remove)
            if widget_to_remove:
                widget_to_remove.setParent(None)
                
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(view)
        graph_layout.addWidget(scroll_area)
        

        #QWidget().setLayout(old_layout)
        graph_widget.setLayout(graph_layout)
        #parent.ui.widget_30.setLayout(old_layout)
        #$$$$$$$$$$$$$$$$$$$$$
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
        
        
        ################################
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
        colors = plt.cm.Blues(counts / max(counts)) 
        bars = ax.bar(bin_centers, counts, width=np.diff(bins), align='center',
                    color=colors, edgecolor='black', linewidth=0.5)
        ax.xaxis_date()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        figure.autofmt_xdate(rotation=45)
        ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=5, maxticks=10))
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.set_xlabel("Data", fontsize=12)
        ax.set_ylabel("Liczba wiadomości", fontsize=12)
        ax.set_title("Histogram wiadomości (50 równych przedziałów czasu)", fontsize=14, fontweight='bold')
        ax.tick_params(axis='x', labelsize=10)
        ax.tick_params(axis='y', labelsize=10)
        canvas.draw()
        ########################
        
        all_attachments = db_email.get_all_attachment(connect)
        #at = pd.DataFrame(all_attachments, columns=['id', 'attachment_name','email_id'])
        #len(all_attachments)
        parent.ui.attachmentsCountLabel.setText(str(len(all_attachments)))
        parent.ui.attachmentsCountLabel.setStyleSheet("""color:#102339;
                                                 font-weight: bold;""")
        all_recipients = db_email.get_all_recipients_by_group(connect)
        parent.ui.recipientsCountLabel.setText(str(len(all_recipients)))
        parent.ui.recipientsCountLabel.setStyleSheet("""color:#102339;
                                                 font-weight: bold;""")
        all_email = db_email.get_count_email(connect)
        parent.ui.emailCountLablel.setText(str(all_email[0][0]))
        parent.ui.emailCountLablel.setStyleSheet("""color:#102339;
                                                 font-weight: bold;""")
    except Exception as e:
        logger.error(f":błąd podczas tworzenia statystyk {e}")
        logger.exception("Błąd podczas tworzenia statystyk")
        



