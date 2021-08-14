# Python libraries
from fpdf import FPDF

# Local imports
from daily_counts import plot_daily_count_states, plot_daily_count_countries
from time_series_analysis import plot_countries, plot_states
from helper import get_state_names, get_country_names, Mode

name = 'Juansa'
WIDTH = 210
HEIGHT = 297

def create_report(filename='tutorial.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, f'Hello my name is {name}!')

    # Bar chart - Cases
    states = ['New Hampshire', 'Massachusetts']
    plot_daily_count_states(states, filename='test.png')
    pdf.image('test.png', 5, 30, WIDTH/2-5)
    # Bar chart - Deaths
    plot_daily_count_states(states, mode=Mode.DEATHS, filename='test2.png')
    pdf.image('test2.png', WIDTH/2+5, 30, WIDTH/2-5)

    pdf.add_page()

    # Line Chart - Cases
    plot_states(states, days=7, filename='test3.png')
    pdf.image('test3.png', 5, 110, WIDTH/2-5)
    # Line Chart - Deaths
    plot_daily_count_states(states, mode=Mode.DEATHS, filename='test4.png')
    pdf.image('test4.png', WIDTH/2+5, 110, WIDTH/2-5)

    pdf.output('tuto1.pdf')

if __name__ == '__main__':
    create_report()