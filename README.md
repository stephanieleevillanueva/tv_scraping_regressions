# tv-scraping-regressions
Web scraping using BeautifulSoup and data analysis using Statsmodels and Scikit.

####Folder structure:
<dl>
  <dt>_py_helpers</dt>
  <dd>contains <b>.py</b> files used in the various <b>.ipynb</b> notebooks.</dd>
  * sidereel.py  
      generates variables ``show_list`` for all TV shows as of July 2015 and ``show_titles`` for all TV show titles as of July 2015 (subset of ``show_list``).
  * tvseriesfinale.py  
      generates variable ``canceled_shows`` for concluded TV shows from 2011-2015 and ``title`` for concluded TV show titles (subset of ``canceled_shows``)
  * wikipedia-state.py  
      generates variable ``show_state`` for shows and their settings (US state) as of July 2015.

<dl>
  <dt>data</dt>
  <dd>contains csv files used in running <b>.ipynb</b> notebooks.</dd> 

