**1. In command line, change directory to the "dash_app" folder and run: docker-compose up --build** <br/>

**2. Go to http://localhost:8050** <br/>
* Scatter plot
   * title submission text that was converted to a vector using the doc2vec and then reduced to 2 dimensions using t-SNE
   * hover over points to see coordinates and corresponding submission title
   * see dash_app_plot.ipynb for how coordinates were calculated
* Two logistic models
  * can move sliders/toggle to select different inputs and see how prediction will change
  * see EDA_PreprocessText_Model.ipynb for how model was created

<p align = "center">(should look something like this)</p>
</br>

<img src="https://github.com/janellashu/Project-stat418-tools-in-datascience/blob/master/figures/dash_app_preview.png" alt="drawing" width="800"/>
