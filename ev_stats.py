import pandas as pd

url = 'https://raw.githubusercontent.com/Dekanas/Streamlit/main/exported.csv'

data = pd.read_csv(url)

import seaborn as sns
import matplotlib.pyplot as plt

data_lower_price = data.loc[data['price in eur'] < 50000]
data_higher_price = data.loc[data['price in eur'] > 50000]
plot_order_lower = data_lower_price.sort_values(by='average score', ascending=False)
plot_order_higher = data_higher_price.sort_values(by='average score', ascending=False)

import streamlit as st

st.title("EV")
## !!! date options
## !!! product options          
product = st.sidebar.selectbox(
            "Select a Product group",
            [
              '<50000',
              '>50000'
            ])
if product == '<50000':
  sns.set_theme(style="whitegrid")
  f, ax = plt.subplots(figsize=(10, 15))

  sns.set_color_codes("pastel")
  sns.barplot(x="average score", y="Car full name", data=plot_order_lower,
              label="average score", color="b")


  ax.legend(ncol=2, loc="lower right", frameon=True)
  ax.set(xlim=(0, 100), ylabel="",
        xlabel="Electric cars by average score")
  sns.despine(left=True, bottom=True)
  st.pyplot(f)
else:
  sns.set_theme(style="whitegrid")
  f, ax = plt.subplots(figsize=(10, 15))

  sns.set_color_codes("pastel")
  sns.barplot(x="average score", y="Car full name", data=plot_order_higher,
              label="average score", color="b")


  ax.legend(ncol=2, loc="lower right", frameon=True)
  ax.set(xlim=(0, 100), ylabel="",
        xlabel="Electric cars by average score")
  sns.despine(left=True, bottom=True)
  st.pyplot(f)

st.write(plot_order_lower)
st.write(plot_order_higher)
