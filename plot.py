import analyze
import pygal

data = analyze.analyze_file();

total = data['G'] + data['JH'] + data['ZH']
total_gi = data['GI'] + data['JHI'] + data['ZHI']

pie_chart = pygal.Pie()
pie_chart.title = "Pronounciation of G (in %)"
pie_chart.add('G (Gift)', data['G']/total)
pie_chart.add('J (Giraffe)', data['JH']/total)
pie_chart.add('Z (Genre)', data['ZH']/total)
pie_chart.render_to_file('pie_chart.svg')

pie_chart2 = pygal.Pie()
pie_chart2.title = "Pronounciation of G before I (in %)"
pie_chart2.add('GI (Gift)', data['GI']/total_gi)
pie_chart2.add('JI (Giraffe)', data['JHI']/total_gi)
pie_chart2.add('ZI (Giselle)', data['ZHI']/total_gi)
pie_chart2.render_to_file('pie_chart2.svg')  
