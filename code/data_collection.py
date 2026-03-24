from ucimlrepo import fetch_ucirepo 
import pandas as pd
  
# fetch dataset 
phiusiil_phishing_url_website = fetch_ucirepo(id=967) 
  
# data (as pandas dataframes) 
X = phiusiil_phishing_url_website.data.features 
y = phiusiil_phishing_url_website.data.targets 
  
# metadata 
print(phiusiil_phishing_url_website.metadata) 
  
# variable information
print(phiusiil_phishing_url_website.variables)

# save combined data
df = pd.concat([X, y], axis=1)
df.to_csv('../data/phishing_urls.csv', index=False)
