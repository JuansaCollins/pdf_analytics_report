# Python libraries
from fpdf import FPDF
from datetime import datetime, timedelta

# Local imports
from daily_counts import plot_daily_count_states, plot_daily_count_countries
from time_series_analysis import plot_countries, plot_states
from create_case_maps import plot_usa_case_map, plot_global_case_map
from helper import get_state_names, get_country_names, Mode

name = 'Juansa'
WIDTH = 210
HEIGHT = 297

def create_title(day, pdf):
    pdf.set_font('Arial', '', 24)
    pdf.ln(60)
    pdf.write(5, 'Covid Analytics Report')
    pdf.ln(10)
    pdf.set_font('Arial', '', 16)
    pdf.write(4, f'{day}')
    pdf.ln(5)

def create_report(day, filename='new_report.pdf'):
    pdf = FPDF()
    
    # First page 
    pdf.add_page()
    pdf.image('./resources/letterhead_cropped.png', 0, 0, WIDTH)
    create_title(day, pdf)

    plot_usa_case_map('./test/usa_cases.png', day=day)
    pdf.image('./test/usa_cases.png', 5, 90, WIDTH-20)

    # Second Page
    pdf.add_page()

    # Bar chart - Cases
    states = ['New Hampshire', 'Massachusetts']
    plot_daily_count_states(states, filename='./test/test.png')
    pdf.image('./test/test.png', 5, 30, WIDTH/2-5)
    # Bar chart - Deaths
    plot_daily_count_states(states, mode=Mode.DEATHS, filename='./test/test2.png')
    pdf.image('./test/test2.png', WIDTH/2+5, 30, WIDTH/2-5)

    pdf.add_page()

    # Line Chart - Cases
    plot_states(states, days=7, filename='./test/test3.png')
    pdf.image('./test/test3.png', 5, 110, WIDTH/2-5)
    # Line Chart - Deaths
    plot_daily_count_states(states, mode=Mode.DEATHS, filename='./test/test4.png')
    pdf.image('./test/test4.png', WIDTH/2+5, 110, WIDTH/2-5)

    pdf.output(filename)

if __name__ == '__main__':
    day = '10/10/20'
    #day = (datetime.today() - timedelta(days=1)).strftime('%md/%d/%y').replace("/0", '/').lstrip('0')

    create_report(day)