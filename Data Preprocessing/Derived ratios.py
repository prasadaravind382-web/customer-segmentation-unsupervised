rfm['CasesPerRecency'] = rfm['Frequency'] / (rfm['Recency'] + 1)

print(rfm.head())
