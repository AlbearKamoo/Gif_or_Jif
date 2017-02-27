import analyze
import pygal

data = analyze.analyze_file();

total = data['G'] + data['JH'] + data['ZH']
total_gi = data['GI'] + data['JHI'] + data['ZHI']

pie_chart = pygal.Pie()
pie_chart.title = "Pronounciation of G (in %)"
pie_chart.add('G (Gaze)', data['G']/total)
pie_chart.add('J (Gyro)', data['JH']/total)
pie_chart.add('Z (Genre)', data['ZH']/total)
pie_chart.render_to_file('g_pie.svg')

pie_chart2 = pygal.Pie()
pie_chart2.title = "Pronounciation of G before I (in %)"
pie_chart2.add('GI (Gift)', data['GI']/total_gi)
pie_chart2.add('JI (Giraffe)', data['JHI']/total_gi)
pie_chart2.add('ZI (Giselle)', data['ZHI']/total_gi)
pie_chart2.render_to_file('gi_pie.svg')

bar_chart = pygal.Bar()
bar_chart.title = "Pronounciation of G - Word Count"
bar_chart.add('G (Gaze)', data['G'])
bar_chart.add('J (Gyro)', data['JH'])
bar_chart.add('Z (Genre)', data['ZH'])
bar_chart.render_to_file('g_bar.svg')

bar_chart = pygal.Bar(range=(0, 320), max_scale=10)
bar_chart.title = "Pronounciation of G before I - Word Count"
bar_chart.add('GI (Gift)', data['GI'])
bar_chart.add('JI (Giraffe)', data['JHI'])
bar_chart.add('ZI (Giselle)', data['ZHI'])
bar_chart.render_to_file('gi_bar.svg')


