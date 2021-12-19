import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pdfFile = PdfPages("output.pdf")

str0 = "https://api.github.com/repos/bitcoin/bitcoin/stats/commit_activity"
str1 = "https://api.github.com/repos/solana-labs/solana/stats/commit_activity"
for itr in range(2):
    if itr==0:
        response = requests.get(str0)
    else:
        response = requests.get(str1)
    commit_data = response.json()
    xVals = []
    yVals = []

    for s in range(len(commit_data)):
        xVals.append(str(s))
        yVals.append(int(commit_data[s]['total']))

    fig, ax = plt.subplots(figsize=(11, 6))
    la, = ax.plot(xVals, yVals)

    if itr == 0:
        ax.set_title("Bitcoin total commits per week")
    else:
        ax.set_title("Solana total commits per week")

    pdfFile.savefig(fig)

pdfFile.close()