import plotly.graph_objects as go

import pandas as pd



pathout='/Users/alex/AlexBadea_MyPapers/APOE22APOE33APOE44/fa_pics/'
#####
file='/Users/alex/AlexBadea_MyPapers/APOE22APOE33APOE44/APOE22APOE33APOE44VolumesFA062620.xlsx'
df = pd.read_excel(file, sheet_name='APOE22APOE33APOE44FA')

pathout='/Users/alex/AlexBadea_MyPapers/APOE22APOE33APOE44/fa_pics/'
fileind='/Users/alex/AlexBadea_MyPapers/APOE22APOE33APOE44/my_pfa1.xlsx'
dfind=pd.read_excel(fileind)

for col in dfind.columns[8:]:
	if dfind[col][0] < 0.01:
		print(col)
		fig = go.Figure()

		# print(df['Genotype'].isin(['APOE22','APOE33','APOE44']))
		df_short=df[df['Genotype'].isin(['APOE22','APOE33','APOE44'])]


		Genotypes = ['APOE22', 'APOE33', 'APOE44']
		colors = ["red","green","purple"]
		for i in range(3):
			genotype = Genotypes[i]
			color = colors[i]
			fig.add_trace(go.Violin(x=df_short['Genotype'][df_short['Genotype'] == genotype],
									y=df_short[col][df['Genotype'] == genotype], name=genotype,
									box_visible=True, meanline_visible=True,line_color=color))

		fig.update_traces(box_visible=True, meanline_visible=True, points='all', jitter=0.05)
		fig.update_layout(violinmode='group')
		fig.update_layout(
			title=col + "  p = " + str(dfind[col][0]),
		    xaxis_title="Genotype",
		    yaxis_title="FA",
		)
		fig.show()
		fig.write_image(pathout+col+"_fa.png")